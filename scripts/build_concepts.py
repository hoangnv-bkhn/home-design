"""Build the offline viewer and limited model checks; standard library only."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'data/concepts.json').read_text(encoding='utf-8'))
s = data['site']
c_dx = math.sqrt(s['C'] ** 2 - s['assumed_C_drop'] ** 2)
p = (s['A'], 0)
q = (c_dx, s['B'] + s['assumed_C_drop'])
dx, dy = q[0] - p[0], q[1] - p[1]
chord = math.hypot(dx, dy)
if chord > s['D']:
    raise ValueError('Assumed geometry cannot accommodate D')
bend_offset = math.sqrt((s['D']/2)**2 - (chord/2)**2)
bend = ((p[0]+q[0])/2 + dy/chord*bend_offset,
        (p[1]+q[1])/2 - dx/chord*bend_offset)
polygon = [(0, 0), p, bend, q, (0, s['B'])]
area = abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(polygon,polygon[1:]+polygon[:1])))/2

def overlap(a, b):
    return max(0,min(a[0]+a[2],b[0]+b[2])-max(a[0],b[0])) * max(0,min(a[1]+a[3],b[1]+b[3])-max(a[1],b[1]))

def contains(outer, inner):
    return (inner[0] >= outer[0]-1e-8 and inner[1] >= outer[1]-1e-8
            and inner[0]+inner[2] <= outer[0]+outer[2]+1e-8
            and inner[1]+inner[3] <= outer[1]+outer[3]+1e-8)

def corners(r):
    x,y,w,h = r
    return [(x,y),(x+w,y),(x+w,y+h),(x,y+h)]

def inside(point):
    x,y = point
    hit = False
    for a,b in zip(polygon,polygon[1:]+polygon[:1]):
        if (a[1]>y)!=(b[1]>y) and x < (b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:
            hit = not hit
    return hit

def route_samples(route):
    for a,b in zip(route['points'],route['points'][1:]):
        for i in range(101):
            yield [a[0]+(b[0]-a[0])*i/100, a[1]+(b[1]-a[1])*i/100, 0.001, 0.001]

checks = []
def check(name, condition):
    checks.append((name, bool(condition)))

check('Declared geometry units remain metres', data['units']=='m')
all_ids = [r['id'] for f in data['floors'] for r in f['rooms']]
check('Unique room IDs across floors', len(set(all_ids))==len(all_ids))
for f in data['floors']:
    rooms = f['rooms']
    env = f['envelope']
    t = data['house']['external_wall']
    clear_env = [env[0]+t,env[1]+t,env[2]-2*t,env[3]-2*t]
    check(f"{f['id']}: positive zone dimensions", all(r['rect'][2]>0 and r['rect'][3]>0 for r in rooms))
    check(f"{f['id']}: no overlap of room zones", all(overlap(a['rect'],b['rect'])<1e-8 for i,a in enumerate(rooms) for b in rooms[i+1:]))
    check(f"{f['id']}: two WCs and two separate showers", sum(r['type']=='wc' for r in rooms)==2 and sum(r['type']=='shower' for r in rooms)==2)
    check(f"{f['id']}: indoor zones inside declared floor envelope", all(r['type']=='balcony' or contains(clear_env,r['rect']) for r in rooms))
    fixtures = f.get('fixtures', [])
    by_id = {r['id']:r for r in rooms}
    check(f"{f['id']}: fixtures contained in assigned compartments", all(a['room'] in by_id and contains(by_id[a['room']]['rect'],a['rect']) for a in fixtures))
    check(f"{f['id']}: each shower contains a basin and shower tray", all(all(any(a['room']==r['id'] and a['kind']==kind for a in fixtures) for kind in ['basin','shower']) for r in rooms if r['type']=='shower'))
    check(f"{f['id']}: fixture footprints do not overlap", all(overlap(a['rect'],b['rect'])<1e-8 for i,a in enumerate(fixtures) for b in fixtures[i+1:]))
    check(f"{f['id']}: furniture footprints inside floor envelope", all(contains(clear_env,a[1:]) for a in f['furniture']))

f1,f2 = data['floors']
altar = next(r['rect'] for r in f1['rooms'] if r['id']=='ALT-01')
empty = next(r['rect'] for r in f2['rooms'] if r['id']=='EMPTY-ALT')
altar_width = altar[2 if data['coordination']['altar_width_axis']=='x' else 3]
check('Five bedrooms: F1 two / F2 three', sum(r['type']=='bed' for r in f1['rooms'])==2 and sum(r['type']=='bed' for r in f2['rooms'])==3)
check('Altar width parallel to backing at least 3.4 m', altar_width>=3.4)
check('Upper empty zone equals altar projection', all(abs(a-b)<1e-8 for a,b in zip(altar,empty)))
check('No other upstairs zone overlaps altar projection', all(overlap(altar,r['rect'])<1e-8 for r in f2['rooms'] if r['id']!='EMPTY-ALT'))
check('No upstairs fixtures or furniture above altar', all(overlap(altar,a['rect'])<1e-8 for a in f2.get('fixtures',[])) and all(overlap(altar,a[1:])<1e-8 for a in f2['furniture']))
check('Sampled common route centerlines bypass upper altar zone', all(overlap(altar,p)<1e-8 for r in f2.get('routes',[]) for p in route_samples(r)))
check('Altar and house facing vectors agree', data['house']['facing_vector']==data['coordination']['altar_facing_vector'])
wet1 = sorted(r['rect'] for r in f1['rooms'] if r['type'] in ['wc','shower'])
wet2 = sorted(r['rect'] for r in f2['rooms'] if r['type'] in ['wc','shower'])
check('Wet compartments align floor-to-floor', wet1==wet2)
stair = data['house']['stair']
check('21 stair risers split 10 + 11', stair['risers']==21 and stair['flight_risers']==[10,11])
check('Nominal stair flight widths/gap fit 2.2 m bay', abs(2*stair['flight_width']+stair['central_gap']-stair['rect'][2])<1e-8 and abs(stair['rect'][2]-2.2)<1e-8)
check('Longest tread run + landing fits bay depth', (max(stair['flight_risers'])-1)*stair['going']+stair['landing_depth'] <= stair['rect'][3]+1e-8)
check('Stair reservations align on both floors', all(next(r['rect'] for r in f['rooms'] if r['type']=='stair')==stair['rect'] for f in data['floors']))
balcony = data['options'][0]['balcony']['rect']
by_id = {r['id']:r for r in f2['rooms']}
balconies = {}
for opt in data['options']:
    if opt['rotation']!=0:
        raise ValueError('Explicit floor envelopes use site axes; physical option rotation unsupported')
    b = opt['balcony']
    br, door = b['rect'], b['door']
    access = by_id[b['access_room']]['rect']
    balconies[opt['id']] = {'area':br[2]*br[3], 'access':b['access_room']}
    check(f"Option {opt['id']}: balcony door connects declared access room", door[4]=='v' and abs(door[1]-(access[0]+access[2]+.1))<1e-8 and abs(door[1]-(br[0]-.1))<1e-8 and door[2]>=access[1] and door[2]+door[3]<=access[1]+access[3] and door[2]>=br[1] and door[2]+door[3]<=br[1]+br[3])
    check(f"Option {opt['id']}: balcony does not overlap indoor zones", all(overlap(br,r['rect'])<1e-8 for r in f2['rooms'] if r['type']!='balcony'))
    check(f"Option {opt['id']}: balcony route avoids altar exclusion", all(overlap(altar,p)<1e-8 for p in route_samples({'points':b['route']})))
    origin = s['assumed_house_origin']
    shapes = [f['envelope'] for f in data['floors']] + [br]
    check(f"Option {opt['id']}: floor/balcony corners inside assumed plot", all(inside((x+origin[0],y+origin[1])) for r in shapes for x,y in corners(r)))
check('Both floor rear edges retain proposed B allowance', all(abs(f['envelope'][0]+s['assumed_house_origin'][0]-.1)<1e-8 for f in data['floors']))
check('Both floor A edges retain approximate 0.30 m allowance', all(abs(f['envelope'][1]+s['assumed_house_origin'][1]-.3)<1e-8 for f in data['floors']))
check('No doors/windows face near-boundary A or B', all(all(not (d[0]=='GARDEN' or (d[4]=='v' and d[1]<.2) or (d[4]=='h' and d[2]<.2)) for d in f['doors']) and all(not ((w[3]=='v' and w[0]<.2) or (w[3]=='h' and w[1]<.2)) for w in f['windows']) for f in data['floors']))
check('WC compartments contain no basins', all(not (a['room'].startswith('WC') and a['kind']=='basin') for f in data['floors'] for a in f['fixtures']))
entry = next(d for d in f1['doors'] if d[0]=='ENTRY')
living = next(r['rect'] for r in f1['rooms'] if r['id']=='LIV-01')
check('Proposed 1.90 m entrance adjoins open living', entry[4]=='v' and abs(entry[3]-1.9)<1e-8 and abs(entry[1]-(living[0]+living[2]+.1))<1e-8 and entry[2]>=living[1] and entry[2]+entry[3]<=living[1]+living[3])
check('TV stand and sofa lie within living reservation', contains(living,f1['tv']['stand']) and contains(living,f1['tv']['sofa']) and overlap(f1['tv']['stand'],f1['tv']['sofa'])<1e-8)
kit = next(r['rect'] for r in f1['rooms'] if r['id']=='KIT-01')
din = next(r['rect'] for r in f1['rooms'] if r['id']=='DIN-01')
table = next(a[1:] for a in f1['furniture'] if a[0]=='Dining table')
check('Dining table inside open kitchen/dining bay', abs(kit[0]+kit[2]+.1-din[0])<1e-8 and kit[1]==din[1] and kit[3]==din[3] and contains(din,table))
check('Stationary car bay corners inside assumed plot', all(inside(p) for p in corners(s['car_bay'])))
check('Car bay does not overlap F1 footprint', overlap(s['car_bay'],[*s['assumed_house_origin'],*f1['envelope'][2:]])<1e-8)
check('Clockwise plot/floor view rotation declared 90 degrees', data['presentation']['plan_rotation_clockwise']==90)
check('Horizontal B extent exceeds vertical A extent', data['house']['depth']>data['house']['width'])
site_house=[s['assumed_house_origin'][0],s['assumed_house_origin'][1],*f1['envelope'][2:]]
site_items=[s['car_bay'],s['porch'],s['porch_steps'],*s['scooters']]
check('Porch/steps/two-wheel spaces inside assumed parcel', all(inside(p) for r in site_items for p in corners(r)))
check('Parking, porch, steps and two-wheel reservations do not overlap', all(overlap(a,b)<1e-8 for i,a in enumerate(site_items) for b in site_items[i+1:]))
check('Porch, steps and two-wheel spaces avoid F1 footprint', all(overlap(site_house,r)<1e-8 for r in site_items))
entry_center=[s['assumed_house_origin'][0]+entry[1],s['assumed_house_origin'][1]+entry[2]+entry[3]/2,.001,.001]
check('Porch aligns with 1.90 m entrance opening', abs(s['porch'][0]-(site_house[0]+site_house[2]))<1e-8 and s['porch'][1]<=entry_center[1]-entry[3]/2 and s['porch'][1]+s['porch'][3]>=entry_center[1]+entry[3]/2)
check('Arrival centerline avoids parked vehicles and house interior', all(overlap(p,r)<1e-8 for p in route_samples({'points':s['arrival_path']}) for r in [s['car_bay'],*s['scooters'],[site_house[0],site_house[1],site_house[2]-.002,site_house[3]]]))
gp=next(r['rect'] for r in f1['rooms'] if r['id']=='BR-02')
gp_hall=next(r['rect'] for r in f1['rooms'] if r['id']=='GP-LOBBY')
gp_door=next(d for d in f1['doors'] if d[0]=='BR-02')
check('Grandpa door connects bedroom rear wall to inner passage', gp_door[4]=='v' and abs(gp_door[1]-(gp[0]-.05))<1e-8 and abs(gp_door[1]-(gp_hall[0]+gp_hall[2]+.05))<1e-8 and all(gp_door[2]>=r[1] and gp_door[2]+gp_door[3]<=r[1]+r[3] for r in [gp,gp_hall]))
garden_door=next(d for d in f1['doors'] if d[0]=='KIT-GARDEN')
check('Kitchen dining has direct C-side garden opening', garden_door[4]=='h' and abs(garden_door[2]-(f1['envelope'][3]-data['house']['external_wall']/2))<1e-8 and garden_door[1]>=din[0] and garden_door[1]+garden_door[3]<=din[0]+din[2] and din[1]+din[3]==f1['envelope'][3]-data['house']['external_wall'])
check('WC/shower study widths retain 1.0/1.4 m', all(abs(min(r['rect'][2:])-(1 if r['type']=='wc' else 1.4))<1e-8 for f in data['floors'] for r in f['rooms'] if r['type'] in ['wc','shower']))
def door_joins(door, a, b, wall=.1):
    _,x,y,length,axis=door
    along=1 if axis=='v' else 0
    across=1-along
    start=y if axis=='v' else x
    level=x if axis=='v' else y
    return (all(start>=r[along]-1e-8 and start+length<=r[along]+r[along+2]+1e-8 for r in [a,b])
            and ((abs(level-(a[across]+a[across+2]+wall/2))<1e-8 and abs(level-(b[across]-wall/2))<1e-8)
                 or (abs(level-(b[across]+b[across+2]+wall/2))<1e-8 and abs(level-(a[across]-wall/2))<1e-8)))
sanitary_junctions=[]
for f in data['floors']:
    zones={r['id']:r['rect'] for r in f['rooms']}
    for door in f['doors']:
        if door[0].startswith(('WC-','SH-')):
            sanitary_junctions.append(any(door_joins(door,zones[door[0]],r['rect']) for r in f['rooms'] if r['type']=='hall'))
check('Sanitary entries join a real private/common passage in either orientation', all(sanitary_junctions))

# C06 regressions: topology and finite clearance reservations, with narrow scope.
bed_entries=[('F1','BR-01','HALL-01'),('F1','BR-02','GP-LOBBY'),('F2','BR-03','HALL-05'),('F2','BR-04','HALL-05'),('F2','BR-05','HALL-02')]
check('Every bedroom has a direct common-access door independent of ensuite', all(door_joins(next(a for a in f['doors'] if a[0]==bed),next(r['rect'] for r in f['rooms'] if r['id']==bed),next(r['rect'] for r in f['rooms'] if r['id']==hall)) for fid,bed,hall in bed_entries for f in data['floors'] if f['id']==fid))
check('Private passages have no former public ensuite entry door', all(not any(a[0] in ['EN-01','EN-03'] for a in f['doors']) for f in data['floors']))
seat=f1['tv']['sofa']; facing=f1['tv']['seat_facing']
altar_delta=[altar[i]+altar[i+2]/2-seat[i]-seat[i+2]/2 for i in [0,1]]
check('Sofa rear half-plane excludes altar center', sum(-facing[i]*altar_delta[i] for i in [0,1])<=0)
check('TV stand avoids main entrance approach reservation', overlap(f1['tv']['stand'],[living[0]+living[2]-.95,entry[2],.95,entry[3]])<1e-8)
def sweep_box(op):
    points=[op[k] for k in ['hinge','closed_end','open_end']]
    return [min(p[0] for p in points),min(p[1] for p in points),max(p[0] for p in points)-min(p[0] for p in points),max(p[1] for p in points)-min(p[1] for p in points)]
check('Bedroom/main-entry quarter-circle bounding boxes avoid furniture/fixtures', all(all(overlap(sweep_box(op),a)<1e-8 for a in [*[b[1:] for b in f['furniture']],*[b['rect'] for b in f['fixtures']]]) for f in data['floors'] for op in f['door_operations'] if op['kind']=='hinged'))
check('Six occupied chair reservations stay inside dining and avoid furniture', len(f1['dining_chairs'])==6 and all(contains(din,c['rect']) and all(overlap(c['rect'],a[1:])<1e-8 for a in f1['furniture']) for c in f1['dining_chairs']))
check('Kitchen/garden/living clearance rectangles avoid furniture and occupied chairs', all(all(overlap(c['rect'],a)<1e-8 for a in [*[b[1:] for b in f1['furniture']],*[b['rect'] for b in f1['dining_chairs']]]) for c in f1['clearance_reservations']))
def occupied_route(route,width=.8):
    for p in route_samples(route):
        yield [p[0]-width/2,p[1]-width/2,width,width]
check('0.80 m F1 sample bands avoid furniture, fixtures and occupied dining chairs', all(all(overlap(p,a)<1e-8 for a in [*[b[1:] for b in f1['furniture']],*[b['rect'] for b in f1['fixtures']],*[b['rect'] for b in f1['dining_chairs']]]) for r in f1['routes'] for p in occupied_route(r)))
check('Both balcony 0.80 m sample bands avoid upper furniture and altar', all(all(overlap(p,a)<1e-8 for a in [altar,*[b[1:] for b in f2['furniture']]]) for opt in data['options'] for p in occupied_route({'points':opt['balcony']['route']})))
check('Car bay is left/C of house and has separate pedestrian/vehicle gates', s['car_bay'][1]>=site_house[1]+site_house[3] and s['gate']!=s['pedestrian_gate'])
walks=s['pedestrian_reservations']
check('Walking strips inside parcel and clear of house, parking and steps', all(all(inside(p) for p in corners(r)) and all(overlap(r,a)<1e-8 for a in [site_house,*site_items]) for r in walks))
check('Garden walking centerline clears house and parked vehicles', all(overlap(p,r)<1e-8 for p in route_samples({'points':s['garden_path']}) for r in [site_house,s['car_bay'],*s['scooters']]))
check('Compact F1 gross below 110 m²; F2 envelope aligned', f1['envelope'][2]*f1['envelope'][3]<110 and f1['envelope']==f2['envelope'])

gross = {f['id']:f['envelope'][2]*f['envelope'][3] for f in data['floors']}
bal_area = balcony[2]*balcony[3]
data['derived'] = {'polygon':polygon,'site_area':area,'bend_offset':bend_offset,'D_segments':[math.dist(p,bend),math.dist(bend,q)],'gross':gross,'balcony_area':bal_area,'balconies':balconies,'outside_f1':area-gross['F1'],'checks':[{'name':n,'pass':v} for n,v in checks]}
lines = [f"# Concept {data['revision']} — generated geometry review", '',
         'Generated from editable metre geometry. These limited checks do not establish survey accuracy, statutory compliance, usable circulation, stair safety, structural adequacy or vehicle turning.', '',
         '## Assumed site and area convention', '',
         f'- Model site area {area:.2f} m²; not surveyed/registered area.',
         f'- D segments {math.dist(p,bend):.3f} + {math.dist(bend,q):.3f} m; chord bend offset {bend_offset:.3f} m.',
         '- Model vertices (m): '+json.dumps(polygon),
         f"- F1 gross footprint {gross['F1']:.2f} m²; F2 envelope {gross['F2']:.2f} m² including stair opening and empty altar zone.",
         f"- Gross envelope sum {sum(gross.values()):.2f} m²; balcony {bal_area:.2f} m² separately. This is a concept convention, not statutory/contract measurement.",
         f"- Model land outside F1 {area-gross['F1']:.2f} m², including gaps, access and parking, not all garden.",
         f'- F1/F2 B edge modeled 0.10 m from boundary; A edge 0.30 m. C-side upper extension {data["coordination"]["cantilever"]["depth"]:.2f} m. Owner placement preferences, not lawful setbacks.',
         '', '## Automated checks', '']
lines += [f"- {'PASS' if v else 'FAIL'} — {n}" for n,v in checks]
lines += ['', '## Balcony comparison', '', '| Option | Balcony area (m²) | Access |', '| --- | --- | --- |']
for opt in data['options']:
    lines.append(f"| {opt['id']} — {opt['title']} | {balconies[opt['id']]['area']:.2f} | {opt['balcony']['access_room']} |")
for f in data['floors']:
    lines += ['',f"## {f['id']} clear zone schedule",'','| ID | Space | Dimensions (m) | Area (m²) |','| --- | --- | --- | --- |']
    for r in f['rooms']:
        x,y,w,h=r['rect']
        lines.append(f"| {r['id']} | {r['label']} | {w:.2f} × {h:.2f} | {w*h:.2f} |")
    named=sum(r['rect'][2]*r['rect'][3] for r in f['rooms'] if r['type']!='balcony')
    lines += ['',f"Indoor named zones {named:.2f} m² including stair reservation; {gross[f['id']]-named:.2f} m² remains for walls and unassigned junction/extension strips. Not net lettable area."]
lines += ['', '## Stair arithmetic — reservation only', '',
          f"- Assumed floor rise {data['house']['floor_height']:.2f} m / 21 = {1000*data['house']['floor_height']/21:.1f} mm/riser.",
          '- Flights 10 + 11 risers have 9 + 10 intervening treads; tread runs 2.34 / 2.60 m at 260 mm going.',
          '- 2.60 m longest run + 1.10 m intermediate landing = 3.70 m bay depth. Top/bottom approaches lie in common circulation outside the bay.',
          '- Nominal flights 1.00 + 1.00 m with 0.20 m center gap fill the 2.20 m reservation; wall/rail details may reduce finished widths.',
          '', '## Unresolved review', '',
          '- 21 steps provisionally means risers. Owner confirmed staircase; no lift requested. Architect must resolve actual finished flights, openings, headroom, rails and applicability.',
          '- Bedroom/main-entry inward leaves and sliding sanitary entries are concept studies. Bounding-box and 0.80 m sampled bands are limited collision checks, not occupied usability/compliance certification.',
          f'- Living {living[2]*living[3]:.2f} m²; kitchen/dining open bay {(kit[2]+din[2]+data["house"]["partition"])*kit[3]:.2f} m². Occupied chairs/appliances, suite and garden routes remain unverified.',
          '- Altar 3.4 m width × 1.5 m depth, facing SE, and reduced 5.10 m² upper exclusion need family acceptance.',
          '- C-side envelope extension removed; both road balconies, rooflight, foundations, acoustics, waterproofing and guards need a professional design basis.',
          '- Approximate owner placement is not approval of boundary-wall construction/openings; kitchen extract, fifth-bedroom rooflight/ventilation, survey and car turning unresolved.',
          '- Indoor backing buffer remains 0.9 m; family acceptance unresolved. Smaller bedrooms retain furniture studies; sister corner option uses a narrower secondary bed side.',
          '- Left/C 3.0 × 5.0 m car bay, separate gates, porch and steps are reservations. Clear walking strips do not establish road maneuvers, door-opening envelopes, safe levels or finished door/stair operation.']
out=ROOT/'outputs'
out.mkdir(exist_ok=True)
(out/'geometry-review.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
template=(ROOT/'src/concept-viewer.html').read_text(encoding='utf-8')
(out/'house-concepts.html').write_text(template.replace('__REVISION__',data['revision']).replace('__PROJECT_DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')),encoding='utf-8')
print(f"Generated {data['revision']} viewer/report: {sum(v for _,v in checks)}/{len(checks)} limited checks pass.")
if not all(v for _,v in checks):
    raise SystemExit('Geometry checks failed; inspect outputs/geometry-review.md')
