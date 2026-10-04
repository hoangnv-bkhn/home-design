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

def inside(point, boundary=None):
    boundary = polygon if boundary is None else boundary
    x,y = point
    hit = False
    for a,b in zip(boundary,boundary[1:]+boundary[:1]):
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
altar_room = altar
altar = data['coordination']['altar_exclusion']
altar_width = altar[2 if data['coordination']['altar_width_axis']=='x' else 3]
check('Five bedrooms: F1 two / F2 three', sum(r['type']=='bed' for r in f1['rooms'])==2 and sum(r['type']=='bed' for r in f2['rooms'])==3)
check('Altar width follows owner 3.20 m study', abs(altar_width-3.2)<1e-8)
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
check('Nominal flights and central reservation fit compact 2.40 m bay', abs(2*stair['flight_width']+stair['central_gap']-stair['rect'][2])<1e-8 and abs(stair['rect'][2]-2.4)<1e-8)
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
    extras = opt.get('extra_balconies', [])
    balconies[opt['id']] = {'area':br[2]*br[3]+sum(e['rect'][2]*e['rect'][3] for e in extras), 'shared_area':br[2]*br[3], 'private_area':sum(e['rect'][2]*e['rect'][3] for e in extras), 'access':b['access_room']}
    check(f"Option {opt['id']}: balcony door connects declared access room", door[4]=='h' and abs(door[2]-(access[1]-.1))<1e-8 and abs(door[2]-(br[1]+br[3]+.1))<1e-8 and all(door[1]>=r[0] and door[1]+door[3]<=r[0]+r[2] for r in [access,br]))
    check(f"Option {opt['id']}: balcony does not overlap indoor zones", all(overlap(br,r['rect'])<1e-8 for r in f2['rooms'] if r['type']!='balcony'))
    check(f"Option {opt['id']}: balcony route avoids altar exclusion", all(overlap(altar,p)<1e-8 for p in route_samples({'points':b['route']})))
    origin = s['assumed_house_origin']
    shapes = [f['envelope'] for f in data['floors']] + [br]
    check(f"Option {opt['id']}: floor/balcony corners inside assumed plot", all(inside((x+origin[0],y+origin[1])) for r in shapes for x,y in corners(r)))
    for extra in extras:
        er, ed = extra['rect'], extra['door']
        ar = by_id[extra['access_room']]['rect']
        check(f"Option {opt['id']}: additional private balcony connects bedroom", ed[4]=='v' and abs(ed[1]-(ar[0]+ar[2]+.1))<1e-8 and abs(ed[1]-(er[0]-.1))<1e-8 and all(ed[2]>=r[1] and ed[2]+ed[3]<=r[1]+r[3] for r in [ar,er]))
        check(f"Option {opt['id']}: additional balcony contained and separate", all(inside((x+origin[0],y+origin[1])) for x,y in corners(er)) and all(overlap(er,r['rect'])<1e-8 for r in f2['rooms'] if r['type']!='balcony') and overlap(er,br)<1e-8)
        check(f"Option {opt['id']}: private balcony 0.80 m band avoids furniture/altar", all(all(overlap([p[0]-.4,p[1]-.4,.8,.8],a)<1e-8 for a in [altar,*[f[1:] for f in f2['furniture']]]) for p in route_samples({'points':extra['route']})))
check('Both floor rear edges retain proposed B allowance', all(abs(f['envelope'][0]+s['assumed_house_origin'][0]-.1)<1e-8 for f in data['floors']))
check('Both floor A edges retain approximate 0.30 m allowance', all(abs(f['envelope'][1]+s['assumed_house_origin'][1]-.3)<1e-8 for f in data['floors']))
check('No doors/windows face near-boundary A or B', all(all(not (d[0]=='GARDEN' or (d[4]=='v' and d[1]<.2) or (d[4]=='h' and d[2]<.2)) for d in f['doors']) and all(not ((w[3]=='v' and w[0]<.2) or (w[3]=='h' and w[1]<.2)) for w in f['windows']) for f in data['floors']))
check('WC compartments contain no basins', all(not (a['room'].startswith('WC') and a['kind']=='basin') for f in data['floors'] for a in f['fixtures']))
entry = next(d for d in f1['doors'] if d[0]=='ENTRY')
living = next(r['rect'] for r in f1['rooms'] if r['id']=='LIV-01')
arrival_hall = next(r['rect'] for r in f1['rooms'] if r['id']=='GP-LOBBY')
check('Proposed 1.90 m entrance spans open living and arrival hall', entry[4]=='v' and abs(entry[3]-1.9)<1e-8 and abs(entry[1]-(living[0]+living[2]+.1))<1e-8 and entry[2]>=living[1] and entry[2]+entry[3]<=arrival_hall[1]+arrival_hall[3] and contains(f1['arrival_reservation'],[entry[1]-.5,entry[2],.4,entry[3]]))
check('TV stand and sofa lie within living reservation', contains(living,f1['tv']['stand']) and contains(living,f1['tv']['sofa']) and overlap(f1['tv']['stand'],f1['tv']['sofa'])<1e-8)
kit = next(r['rect'] for r in f1['rooms'] if r['id']=='KIT-01')
din = next(r['rect'] for r in f1['rooms'] if r['id']=='DIN-01')
table = next(a[1:] for a in f1['furniture'] if a[0]=='Dining table')
check('Dining table inside L-shaped kitchen/dining bay', abs(kit[0]+kit[2]+.1-din[0])<1e-8 and abs(kit[1]+kit[3]-din[1]-din[3])<1e-8 and contains(din,table))
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
check('Grandpa door connects bedroom to open arrival hall', gp_door[4]=='h' and abs(gp_door[2]-(gp[1]-.05))<1e-8 and abs(gp_door[2]-(gp_hall[1]+gp_hall[3]+.05))<1e-8 and all(gp_door[1]>=r[0] and gp_door[1]+gp_door[3]<=r[0]+r[2] for r in [gp,gp_hall]))
garden_door=next(d for d in f1['doors'] if d[0]=='KIT-GARDEN')
check('Kitchen dining has direct C-side garden opening', garden_door[4]=='h' and abs(garden_door[2]-(f1['envelope'][3]-data['house']['external_wall']/2))<1e-8 and garden_door[1]>=din[0] and garden_door[1]+garden_door[3]<=din[0]+din[2] and abs(din[1]+din[3]-f1['envelope'][3]+data['house']['external_wall'])<1e-8)
check('WC 1.00 m and all shower widths 1.30 m in compact study', all(abs(min(r['rect'][2:])-(1 if r['type']=='wc' else 1.3))<1e-8 for f in data['floors'] for r in f['rooms'] if r['type'] in ['wc','shower']))
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
bed_entries=[('F1','BR-01','COURT-HALL-1'),('F1','BR-02','GP-LOBBY'),('F2','BR-03','COURT-HALL-2'),('F2','BR-04','HALL-05'),('F2','BR-05','SPARE-LOBBY')]
check('Every bedroom has a direct common-access door independent of ensuite', all(door_joins(next(a for a in f['doors'] if a[0]==bed),next(r['rect'] for r in f['rooms'] if r['id']==bed),next(r['rect'] for r in f['rooms'] if r['id']==hall)) for fid,bed,hall in bed_entries for f in data['floors'] if f['id']==fid))
check('Private passages have no former public ensuite entry door', all(not any(a[0] in ['EN-01','EN-03'] for a in f['doors']) for f in data['floors']))
seat=f1['tv']['sofa']; facing=f1['tv']['seat_facing']
altar_delta=[altar_room[i]+altar_room[i+2]/2-seat[i]-seat[i+2]/2 for i in [0,1]]
check('Sofa rear half-plane excludes altar center', sum(-facing[i]*altar_delta[i] for i in [0,1])<=0)
check('TV stand avoids main entrance approach reservation', overlap(f1['tv']['stand'],[living[0]+living[2]-.95,entry[2],.95,entry[3]])<1e-8)
def sweep_box(op):
    points=[op[k] for k in ['hinge','closed_end','open_end']]
    return [min(p[0] for p in points),min(p[1] for p in points),max(p[0] for p in points)-min(p[0] for p in points),max(p[1] for p in points)-min(p[1] for p in points)]
check('Bedroom/main-entry quarter-circle bounding boxes avoid furniture/fixtures', all(all(overlap(sweep_box(op),a)<1e-8 for a in [*[b[1:] for b in f['furniture']],*[b['rect'] for b in f['fixtures']]]) for f in data['floors'] for op in f['door_operations'] if op['kind']=='hinged'))
check('Hinged door operation anchors match actual opening segments', all(abs(pt[0 if door[4]=='v' else 1]-door[1 if door[4]=='v' else 2])<1e-8 and door[2 if door[4]=='v' else 1]-1e-8<=pt[1 if door[4]=='v' else 0]<=door[2 if door[4]=='v' else 1]+door[3]+1e-8 for f in data['floors'] for op in f['door_operations'] if op['kind']=='hinged' for door in f['doors'] if door[0]==op['door'] for pt in [op['hinge'],op['closed_end']]))
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
court=data['house']['courtyard']['rect']
court_area=court[2]*court[3]
check('Both floors retain the same open court despite upper projection', all(next(r['rect'] for r in f['rooms'] if r['type']=='courtyard')==court for f in data['floors']))

# C07: relationships changed by this revision, still concept-level geometry only.
seat_lateral=0 if f1['tv']['seat_facing'][1] else 1
check('TV screen and sofa have matching lateral centerlines', abs(f1['tv']['sofa'][seat_lateral]+f1['tv']['sofa'][seat_lateral+2]/2-f1['tv']['stand'][seat_lateral]-f1['tv']['stand'][seat_lateral+2]/2)<1e-8)
check('Empty arrival reservation avoids furniture and seated footprints', all(overlap(f1['arrival_reservation'],a[1:])<1e-8 for a in f1['furniture']))
entry_ops=[op for op in f1['door_operations'] if op['door']=='ENTRY']
check('Two main door leaves explicitly open outward', len(entry_ops)==2 and all(op.get('swing')=='outward' and op['open_end'][0]>op['hinge'][0] for op in entry_ops))
wait=s['porch_waiting_reservation']
porch_with_jamb=[s['porch'][0]-.1,s['porch'][1],s['porch'][2]+.1,s['porch'][3]]
global_sweeps=[[r[0]+s['assumed_house_origin'][0],r[1]+s['assumed_house_origin'][1],*r[2:]] for op in entry_ops for r in [sweep_box(op)]]
check('Outward sweep boxes stay on porch and clear front waiting strip', contains(s['porch'],wait) and wait[2]>=1.15-1e-8 and all(contains(porch_with_jamb,r) and overlap(wait,r)<1e-8 for r in global_sweeps))
check('Both comparisons retain independent shared balcony access', all(opt['balcony']['access_room']=='HALL-04' for opt in data['options']))
tubes=data['coordination']['daylight_tubes']
parents=next(r['rect'] for r in f1['rooms'] if r['id']=='BR-01')
fifth=next(r['rect'] for r in f2['rooms'] if r['id']=='BR-05')
check('Reflective tubes and bedroom-5 rooflight removed', not tubes and not f2['rooflights'])
check('Proposed 2.90 m worship depth contains actual 1.20 m altar exclusion', abs(altar_room[2]-2.9)<1e-8 and contains(altar_room,altar) and abs(altar[2]-1.2)<1e-8)
check('Court has no F2 slab/roof reservation or furniture/services', data['house']['courtyard']['open_to_sky'] and all(all(overlap(court,a)<1e-8 for a in [*[b[1:] for b in f['furniture']],*[b['rect'] for b in f['fixtures']]]) for f in data['floors']) and all(overlap(court,[*p,.01,.01])<1e-8 for p in data['coordination']['stacks']))
def opening_segment(o):
    x,y,l,axis=o
    return [x,y,x+(l if axis=='h' else 0),y+(l if axis=='v' else 0)]
def collinear_overlap(a,b):
    # Entries include ID; window proposals do not.
    ax,ay,al,axis=a; _,bx,by,bl,baxis=b
    return axis==baxis and abs((ay if axis=='h' else ax)-(by if axis=='h' else bx))<1e-8 and min((ax if axis=='h' else ay)+al,(bx if axis=='h' else by)+bl)>max(ax if axis=='h' else ay,bx if axis=='h' else by)+1e-8
check('Window schedule matches plan openings and avoids facade door gaps', all([w['opening'] for w in f['window_proposals']]==f['windows'] and all(w['height']>0 and w['sill']>=0 and (w['sill']+w['height']<data['house']['floor_height'] or (w['room']=='STAIR-01' and w.get('spans_floors')==['F1','F2'] and w['sill']+w['height']<2*data['house']['floor_height'])) and all(not collinear_overlap(w['opening'],door) for door in f['doors']) for w in f['window_proposals']) for f in data['floors']) and all(not collinear_overlap(w,ex['door']) for opt in data['options'] for ex in opt.get('extra_balconies',[]) for w in f2['windows']))
check('Parents and brother operable windows join own open court', all(any(w['room']==rid and w['operable'] and w['face']=='court' and door_joins(['window',*w['opening']],next(r['rect'] for r in f['rooms'] if r['id']==rid),court) for w in f['window_proposals']) for f,rid in [(f1,'BR-01'),(f2,'BR-03')]))
stair_windows=[w for f in data['floors'] for w in f['window_proposals'] if w['room'].startswith('STAIR')]
beam_band=data['coordination']['stair_beam_reservation']
check('Two C-yard stair openings avoid illustrative floor-edge beam band', len(stair_windows)==2 and all(w['operable'] and abs(w['opening'][1]-(data['house']['depth']-.1))<1e-8 and w['opening'][0]>=stair['rect'][0] and w['opening'][0]+w['opening'][2]<=stair['rect'][0]+stair['rect'][2] and ((w['sill']+(data['house']['floor_height'] if w['room']=='STAIR-02' else 0)+w['height'])<=beam_band['bottom'] or w['sill']+(data['house']['floor_height'] if w['room']=='STAIR-02' else 0)>=beam_band['top']) for w in stair_windows))
check('Court cleaning door connects common living approach to court', door_joins(next(a for a in f1['doors'] if a[0]=='COURT-01'),living,court))
check('Bedroom furniture stays within a bedroom and outside courtyard', all(all(any(contains(r['rect'],a[1:]) for r in f['rooms'] if r['type']=='bed') for a in f['furniture'] if a[0] in ['Bed','Double bed','Wardrobe']) for f in data['floors']))
def segment_hits_rect(a,b,r):
    lo,hi=0.,1.
    for axis in [0,1]:
        delta=b[axis]-a[axis]
        if abs(delta)<1e-10:
            if not r[axis]<=a[axis]<=r[axis]+r[axis+2]: return False
        else:
            u,v=(r[axis]-a[axis])/delta,(r[axis]+r[axis+2]-a[axis])/delta
            lo,hi=max(lo,min(u,v)),min(hi,max(u,v))
    return lo<=hi
privacy=[]
entry_privacy=[]
for f,bedid,wcid,shid in [(f1,'BR-01','WC-01','SH-01'),(f2,'BR-03','WC-03','SH-03')]:
    bed=next(a[1:] for a in f['furniture'] if a[0]=='Double bed')
    entry=next(a for a in f['doors'] if a[0]==bedid+'-BATH')
    ordinary=next(a for a in f['doors'] if a[0]==bedid)
    views=[(bed[0]+bed[2]*i/4,bed[1]+bed[3]*j/4) for i in range(5) for j in range(5)]
    entry_views=[(ordinary[1]+ordinary[3]*i/8,ordinary[2]) for i in range(9)]
    for ident in [wcid,shid]:
        door=next(a for a in f['doors'] if a[0]==ident)
        for v in views+entry_views:
            for k in range(9):
                target=(door[1]+door[3]*k/8,door[2])
                t=(entry[1]-v[0])/(target[0]-v[0])
                crossing=v[1]+(target[1]-v[1])*t
                blocked=not entry[2]<=crossing<=entry[2]+entry[3] or any(segment_hits_rect(v,target,r) for r in data['coordination']['private_screens'])
                (privacy if v in views else entry_privacy).append(blocked)
check('Sampled bed views to private doors blocked by offset suite entry wall', all(privacy))
check('Private suite entries have opaque closing-door proposal for standing-entry privacy', all(any(op['door']==bed+'-BATH' and op.get('opaque') for op in f['door_operations']) for f,bed in [(f1,'BR-01'),(f2,'BR-03')]))
check('Open opaque suite leaves fit bedroom wall and avoid furnishings and ordinary door sweeps', all(contains(next(r['rect'] for r in f['rooms'] if r['id']==op['door'].replace('-BATH','')),op['slide_open_rect']) and all(overlap(op['slide_open_rect'],a)<1e-8 for a in [*[b[1:] for b in f['furniture']],*[sweep_box(b) for b in f['door_operations'] if b['kind']=='hinged']]) for f in data['floors'] for op in f['door_operations'] if op.get('opaque')))
check('Private 0.80 m route bands avoid physical return screen', all(all(overlap(p,a)<1e-8 for a in data['coordination']['private_screens']) for f in data['floors'] for r in f['routes'] if 'private' in r['label'] for p in occupied_route(r)))

# C09: check the failed access relationship, not just the existence of a door.
buffer = next(r['rect'] for r in f1['rooms'] if r['id']=='ALT-BUFFER')
bd = next(a for a in f1['doors'] if a[0]=='ALT-BUFFER')
buffer_route = next(r for r in f1['routes'] if r['label']=='Buffer cleaning access')
check('Buffer full-width 1.00 m doorless opening joins living outside solid backing', door_joins(bd,buffer,living) and abs(bd[3]-buffer[2])<1e-8 and bd[3]>=1.0 and 'ALT-BUFFER' in f1['open_portals'] and not any(o['door']=='ALT-BUFFER' for o in f1['door_operations']))
check('Buffer approach has 0.90 m furniture-free width and continuous 0.80 m route', seat[0]-living[0]>=.9-1e-8 and all(all(overlap(p,a[1:])<1e-8 for a in f1['furniture']) and all(overlap(p,r['rect'])<1e-8 for r in f1['rooms'] if r['id'] not in ['LIV-01','GP-LOBBY','ALT-BUFFER']) and overlap(p,data['coordination']['backing_wall'])<1e-8 for p in occupied_route(buffer_route)))
axis=data['coordination']['aligned_wall_axis']
check('Private wet outer wall aligns with living-gallery edge on both floors', all(abs(next(r['rect'][0]+r['rect'][2] for r in f['rooms'] if r['id']==sh)+.1-next(r['rect'][0] for r in f['rooms'] if r['id']==hall))<1e-8 for f,sh,hall in [(f1,'SH-01','LIV-01'),(f2,'SH-03','LANDING-02')]))
sis=next(r['rect'] for r in f2['rooms'] if r['id']=='BR-04')
check('Grandpa-sister front and base walls align; sister extends only towards C', gp[:2]==sis[:2] and abs(gp[2]-sis[2])<1e-8 and abs(sis[3]-gp[3]-data['coordination']['cantilever']['depth'])<1e-8)
check('Upper common and linen access bands avoid furnishings and altar', all(all(overlap(c['rect'],a[1:])<1e-8 for a in f2['furniture']) and overlap(c['rect'],altar)<1e-8 for c in f2['clearance_reservations']) and all(all(overlap(p,a[1:])<1e-8 for a in f2['furniture']) for r in f2['routes'] for p in occupied_route(r)))
check('Doorless linen opening joins common landing', door_joins(next(a for a in f2['doors'] if a[0]=='UTIL-02'),next(r['rect'] for r in f2['rooms'] if r['id']=='UTIL-02'),next(r['rect'] for r in f2['rooms'] if r['id']=='LANDING-02')))
check('Upper furniture and occupied chair footprints do not overlap', all(overlap(a[1:],b[1:])<1e-8 for i,a in enumerate(f2['furniture']) for b in f2['furniture'][i+1:]))
for opt in data['options']:
    b=opt['balcony']
    check(f"Option {opt['id']}: balcony occupied bench and entry fit modeled guard/frame insets", contains(b['usable_rect'],b['occupied']) and contains(b['usable_rect'],b['entry_clearance']) and overlap(b['occupied'],b['entry_clearance'])<1e-8 and all(contains(b['occupied'],a[1:]) for a in b['furniture']))
    check(f"Option {opt['id']}: balcony route clears occupied bench", all(overlap(p,b['occupied'])<1e-8 for p in occupied_route({'points':b['route']})))
seats=[(next(a[1:] for a in f2['furniture'] if a[0]==s['furniture']),s['facing']) for s in f2['seating']]
seats += [(o['balcony']['furniture'][0][1:],o['balcony']['seat_facing']) for o in data['options']]
check('Terrace seated backs face away from altar projection', all(sum(-facing[i]*(altar[i]+altar[i+2]/2-r[i]-r[i+2]/2) for i in [0,1])<=0 for r,facing in seats))

# C10: new topology, separate worship/exclusion extents and upper recesses.
screen=data['coordination']['altar_side_screen']['rect']
check('Spare and ground kitchen wall remain aligned; suites meet owner 3.80 by 4.00 minimum', abs(fifth[0]+fifth[2]-din[0]-din[2])<1e-8 and all(sorted(next(r['rect'][2:] for r in f['rooms'] if r['id']==rid))[0]>=3.8 and sorted(next(r['rect'][2:] for r in f['rooms'] if r['id']==rid))[1]>=4 for f,rid in [(f1,'BR-01'),(f2,'BR-03')]))
check('Spare bedroom remains furnished and has ordinary common entry', door_joins(next(a for a in f2['doors'] if a[0]=='BR-05'),fifth,next(r['rect'] for r in f2['rooms'] if r['id']=='SPARE-LOBBY')))
check('Parents and brother corner sleeping-room walls stack', parents==next(r['rect'] for r in f2['rooms'] if r['id']=='BR-03') and parents[:2]==[.2,.2])
check('Court-facing bedroom windows have a 0.60 m furniture-free interior strip', all(all(overlap(([w['opening'][0]-.65,w['opening'][1],.6,w['opening'][2]] if w['opening'][3]=='v' else [w['opening'][0],w['opening'][1]-.65,w['opening'][2],.6]),a[1:])<1e-8 for a in f['furniture']) for f in data['floors'] for w in f['window_proposals'] if w['face']=='court'))
check('Solid altar side wall leaves 1.20 m front approach and avoids furniture/routes', data['coordination']['altar_side_screen']['kind']=='wall' and abs(altar_room[0]+altar_room[2]-screen[0]-screen[2]-1.2)<1e-8 and all(overlap(screen,a[1:])<1e-8 for a in f1['furniture']) and all(overlap(screen,p)<1e-8 for r in f1['routes'] for p in occupied_route(r)))
check('Study retired; terrace replaces it without entering altar exclusion', not any(r['id']=='STUDY-02' for r in f2['rooms']) and all(overlap(o['balcony']['rect'],altar)<1e-8 for o in data['options']))
check('Shared wet rear wall aligns with corner bedroom wall on both floors', all(abs(next(r['rect'][1] for r in f['rooms'] if r['id']==wet)-.1-next(r['rect'][1]+r['rect'][3] for r in f['rooms'] if r['id']==bed))<1e-8 for f,wet,bed in [(f1,'WC-02','BR-01'),(f2,'WC-04','BR-03')]))
check('Court stair private-wet bay and kitchen/spare share both principal wall lines', abs(stair['rect'][0]-court[0])<1e-8 and abs(stair['rect'][2]-court[2])<1e-8 and abs(stair['rect'][0]-.05-data['coordination']['grid_x'][1])<1e-8 and abs(stair['rect'][0]+stair['rect'][2]+.05-axis)<1e-8 and abs(din[0]+din[2]+.1-stair['rect'][0])<1e-8)
check('Private passage retains outer enclosure with no freestanding screen or obsolete portals', all(not any(d[0].startswith(('EN-ACCESS','EN-RETURN')) for d in f['doors']) and all(r.get('open') for r in f['rooms'] if r['id'].startswith(('EN-ACCESS','EN-0'))) for f in data['floors']) and not data['coordination']['private_screens'])
check('Linen alcove door removed and empty floor stays unfurnished', 'UTIL-02' in f2['open_portals'] and not any(o['door']=='UTIL-02' for o in f2['door_operations']) and all(overlap(altar,a[1:])<1e-8 for a in f2['furniture']))
entrance_design=data['coordination']['entrance_design']
check('Entrance three-rise arithmetic matches proposed yard and porch levels', abs(entrance_design['risers']*entrance_design['riser_height']-entrance_design['porch_level']+entrance_design['yard_level'])<1e-8 and (entrance_design['risers']-1)*entrance_design['tread_depth']<=s['porch_steps'][2])
check('Canopy posts avoid entry sweeps waiting and arrival centerline', all(all(overlap([pt[0]+s['assumed_house_origin'][0]-.04,pt[1]+s['assumed_house_origin'][1]-.04,.08,.08],r)<1e-8 for r in [wait,*global_sweeps,*occupied_route({'points':s['arrival_path']})]) for pt in entrance_design['canopy_posts']))
check('Terrace shade posts fit slab and avoid occupied seat and entry bands', all(contains(o['balcony']['rect'],[pt[0]-.025,pt[1]-.025,.05,.05]) and all(overlap([pt[0]-.025,pt[1]-.025,.05,.05],r)<1e-8 for r in [o['balcony']['occupied'],o['balcony']['entry_clearance'],*occupied_route({'points':o['balcony']['route']})]) for o in data['options'] for pt in o['balcony']['shade_posts']))

check('Upper recess excludes enclosed rooms and indoor furniture', all(overlap(recess,r['rect'])<1e-8 for recess in data['house']['upper_recesses'] for r in f2['rooms'] if r['type']!='balcony') and all(overlap(recess,a[1:])<1e-8 for recess in data['house']['upper_recesses'] for a in f2['furniture']))
# Sample the actual corner-room exit through common zones, with 0.10 m open joints.
check('Corner bedroom exits reach main hall through common space only', all(any(contains([r['rect'][0]-.051,r['rect'][1]-.051,r['rect'][2]+.102,r['rect'][3]+.102],[*pt,0,0]) for r in f['rooms'] if r['type']=='hall') for f in data['floors'] for route in f['routes'] if 'direct exit' in route['label'] for p in occupied_route({'points':[[route['points'][0][0],4.75],*route['points'][1:]]},.8) for pt in corners(p)))

envelope_area = {f['id']:f['envelope'][2]*f['envelope'][3] for f in data['floors']}
# C12: check the owner-requested changes rather than just revised constants.
check('Shared sanitary doors sit laterally outside stair opening alignment', all(d[4]=='h' and d[1]+d[3]<stair['rect'][0] for f in data['floors'] for d in f['doors'] if d[0] in ['WC-02','SH-02','WC-04','SH-04']))
loose_furniture=[a for a in f1['furniture'] if a[0] not in ['Sink','Hob']]
check('F1 furniture footprints are separate except counter-integrated sink and hob', all(overlap(a[1:],b[1:])<1e-8 for i,a in enumerate(loose_furniture) for b in loose_furniture[i+1:]) and all(contains(next(a[1:] for a in f1['furniture'] if a[0]=='Counter'),a[1:]) for a in f1['furniture'] if a[0] in ['Sink','Hob']))
check('Every wooden seat back faces away from altar center', all(sum(-seat['facing'][i]*(altar_room[i]+altar_room[i+2]/2-r[i]-r[i+2]/2) for i in [0,1])<=1e-8 for seat in f1['seating'] for r in [next(a[1:] for a in f1['furniture'] if a[0]==seat['furniture'])]))
check('Wooden seated reservations avoid table TV screen and other furniture', all(contains(living,seat['rect']) and all(overlap(seat['rect'],a[1:])<1e-8 for a in f1['furniture'] if a[0]!=seat['furniture']) and overlap(seat['rect'],screen)<1e-8 for seat in f1['occupied_seating']))
check('Arrival stair altar and gallery routes avoid occupied wooden seats', all(overlap(p,seat['rect'])<1e-8 for r in f1['routes'] if r['label'] in ['Main arrival / stair','Guests to seating','Altar front approach','Buffer cleaning access'] for p in occupied_route(r) for seat in f1['occupied_seating']))
check('Gallery glazing faces court without cutting altar backing', all(door_joins(['window',*w['opening']],court,next(r['rect'] for r in f['rooms'] if r['id']==w['room'])) and abs(w['opening'][0]-data['coordination']['backing_wall'][0])>1 for f in data['floors'] for w in f['window_proposals'] if w['face']=='court-gallery'))
check('Landing window has at least 0.60 m wall return beyond terrace', all(w['opening'][1]-(o['balcony']['rect'][1]+o['balcony']['rect'][3]+.1)>=.6-1e-8 for o in data['options'] for w in f2['window_proposals'] if w['id']=='F2-WIN-LANDING'))
upper_outline=data['house']['upper_outline']
upper_area=abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(upper_outline,upper_outline[1:]+upper_outline[:1])))/2
check('Actual upper polygon agrees with bounding envelope minus all recesses', abs(upper_area-envelope_area['F2']+sum(r[2]*r[3] for r in data['house']['upper_recesses']))<1e-8)
check('Upper indoor room and furniture corners lie inside actual projecting outline', all(all(inside(pt,upper_outline) for pt in corners(r)) for r in [*[r['rect'] for r in f2['rooms'] if r['type']!='balcony'],*[a[1:] for a in f2['furniture']]]))
check('Grandpa door is at stair end of common hall with independent bedroom exit', gp_door[1]>=gp[0] and gp_door[1]+gp_door[3]<=gp[0]+1.2 and gp_door[3]>=.9 and all(overlap(p,a[1:])<1e-8 for a in f1['furniture'] for r in f1['routes'] if r['label']=='Grandpa to shared bathrooms' for p in occupied_route(r)))
cap=data['coordination']['exterior_design']['bedroom_cap']
check('Bedroom roof cap stays off open court and inside assumed parcel', overlap(cap['rect'],court)<1e-8 and all(inside((pt[0]+origin[0],pt[1]+origin[1])) for pt in corners(cap['rect'])))
check('Canopy covers porch and both treads and keeps out of bedroom projection', contains(data['coordination']['porch_canopy'],[s['porch'][0]-origin[0],s['porch'][1]-origin[1],s['porch'][2]+s['porch_steps'][2],s['porch'][3]]) and overlap(data['coordination']['porch_canopy'],data['coordination']['cantilever']['rect'])<1e-8 and abs(s['porch_steps'][2]-(entrance_design['risers']-1)*entrance_design['tread_depth'])<1e-8)
check('Quiet gallery is 1.00 m clear and has no furniture on either floor', abs(buffer[2]-1)<1e-8 and all(overlap(next(r['rect'] for r in f['rooms'] if r['id'] in ['ALT-BUFFER','UTIL-02']),a[1:])<1e-8 for f in data['floors'] for a in f['furniture']))

# C14: conditional boundary candidates are separate from the usable window schedule.
candidates=data['coordination']['boundary_window_candidates']
check('Conditional A-side candidates do not enter ordinary window schedules', all(w['status']=='conditional' and w['face']=='A' and w['opening'][3]=='h' and abs(w['opening'][1]-.1)<1e-8 and not any(a['id']==w['id'] for f in data['floors'] for a in f['window_proposals']) for w in candidates))
alt_side=next(w for w in candidates if w['room']=='ALT-01')
check('Altar side candidate stays beyond actual altar strip, off facing and backing walls', alt_side['opening'][0]>=altar[0]+altar[2] and alt_side['opening'][0]+alt_side['opening'][2]<=altar_room[0]+altar_room[2] and not any(w['room']=='ALT-01' and w['opening'][3]=='v' for w in f1['window_proposals']))
check('Shared terrace projects 1.00 m beyond ground facade with retained common access', all(abs(o['balcony']['rect'][0]+o['balcony']['rect'][2]-data['house']['width']-1)<1e-8 and o['balcony']['access_room']=='HALL-04' for o in data['options']))
rs=data['coordination']['exterior_design']['roof_services']
roof_rects=[rs[k] for k in ['screen_rect','collector_rect','hatch_rect']]
check('Roof equipment/hatch avoid court and altar and stay within actual roof', all(all(inside(p,upper_outline) for p in corners(r)) and overlap(r,court)<1e-8 and overlap(r,altar)<1e-8 for r in roof_rects) and all(overlap(a,b)<1e-8 for i,a in enumerate(roof_rects) for b in roof_rects[i+1:]))
check('Cold/hot tank and maintenance reservations fit ventilated service screen without overlap', all(contains(rs['screen_rect'],rs[k]) for k in ['tank_rect','hot_storage_rect','maintenance_rect']) and rs['maintenance_rect'][3]>=.8 and all(overlap(rs[a],rs[b])<1e-8 for a,b in [('tank_rect','hot_storage_rect'),('tank_rect','maintenance_rect'),('hot_storage_rect','maintenance_rect')]) and max(rs['tank_top'],rs['hot_storage_top'])<rs['screen_top'])
check('Roof access sample stays on actual roof and clears collector court and tanks', all(inside(p[:2],upper_outline) and all(overlap(p,r)<1e-8 for r in [court,rs['tank_rect'],rs['hot_storage_rect'],rs['collector_rect'],altar]) for p in route_samples({'points':rs['access_route']})))
for opt in data['options']:
    pd=opt['porch_design']
    check(f"Option {opt['id']}: porch canopy covers porch/treads and framed supports clear arrival", contains(pd['canopy_rect'],[s['porch'][0]-origin[0],s['porch'][1]-origin[1],s['porch'][2]+s['porch_steps'][2],s['porch'][3]]) and all(all(overlap([pt[0]+origin[0]-pd['post_width']/2,pt[1]+origin[1]-pd['post_width']/2,pd['post_width'],pd['post_width']],r)<1e-8 for r in [wait,*global_sweeps,*occupied_route({'points':s['arrival_path']})]) for pt in pd['posts']))
    if pd.get('side_screen_rect'):
        r=pd['side_screen_rect']; global_r=[r[0]+origin[0],r[1]+origin[1],*r[2:]]
        check('Portal side slats keep garden/arrival walks and door/waiting bands free', contains(pd['canopy_rect'],r) and all(overlap(global_r,a)<1e-8 for a in [wait,*global_sweeps,*occupied_route({'points':s['arrival_path']}),*occupied_route({'points':s['garden_path']})]))
gross = {'F1':envelope_area['F1']-court_area,'F2':upper_area-court_area}
bal_area = balcony[2]*balcony[3]
data['derived'] = {'polygon':polygon,'site_area':area,'bend_offset':bend_offset,'D_segments':[math.dist(p,bend),math.dist(bend,q)],'gross':gross,'envelope_area':envelope_area,'upper_outline_area':upper_area,'courtyard_area':court_area,'balcony_area':bal_area,'balconies':balconies,'outside_f1':area-envelope_area['F1'],'checks':[{'name':n,'pass':v} for n,v in checks]}
lines = [f"# Concept {data['revision']} — generated geometry review", '',
         'Generated from editable metre geometry. These limited checks do not establish survey accuracy, statutory compliance, usable circulation, stair safety, structural adequacy or vehicle turning.', '',
         '## Assumed site and area convention', '',
         f'- Model site area {area:.2f} m²; not surveyed/registered area.',
         f'- D segments {math.dist(p,bend):.3f} + {math.dist(bend,q):.3f} m; chord bend offset {bend_offset:.3f} m.',
         '- Model vertices (m): '+json.dumps(polygon),
         f"- Ground envelope {envelope_area['F1']:.2f} m² minus court {court_area:.2f} m² = F1 covered {gross['F1']:.2f} m². Actual notched/projecting upper polygon {upper_area:.2f} m² minus court = F2 enclosed {gross['F2']:.2f} m². Stair reservation and court lining remain included; F2 bounding rectangle is not its floor area.",
         f"- Covered-envelope sum {sum(gross.values()):.2f} m²; balcony {bal_area:.2f} m² separately. This is a concept convention, not statutory/contract measurement.",
         f"- Model land outside outer envelope {area-envelope_area['F1']:.2f} m², plus {court_area:.2f} m² internal court; gaps/access/parking are not all garden.",
         f'- F1/F2 B edge modeled 0.10 m from boundary; A edge 0.30 m. C-side upper bedroom projection {data["coordination"]["cantilever"]["depth"]:.2f} m. Owner placement preferences, not lawful setbacks.',
         '', '## Automated checks', '']
lines += [f"- {'PASS' if v else 'FAIL'} — {n}" for n,v in checks]
lines += ['', '## Balcony comparison', '', '| Option | Balcony area (m²) | Access |', '| --- | --- | --- |']
for opt in data['options']:
    lines.append(f"| {opt['id']} — {opt['title']} | {balconies[opt['id']]['area']:.2f} (shared {balconies[opt['id']]['shared_area']:.2f} + private {balconies[opt['id']]['private_area']:.2f}) | {opt['balcony']['access_room']} shared |")
for f in data['floors']:
    lines += ['',f"## {f['id']} clear zone schedule",'','| ID | Space | Dimensions (m) | Area (m²) |','| --- | --- | --- | --- |']
    for r in f['rooms']:
        x,y,w,h=r['rect']
        boxes=sum(t['chase_rect'][2]*t['chase_rect'][3] for t in data['coordination']['daylight_tubes'] if t['upper_room']==r['id'])
        area_label=f'{w*h:.2f}' if not boxes else f'{w*h:.2f} rectangle / {w*h-boxes:.2f} after boxes'
        lines.append(f"| {r['id']} | {r['label']} | {w:.2f} × {h:.2f} | {area_label} |")
    named=sum(r['rect'][2]*r['rect'][3] for r in f['rooms'] if r['type'] not in ['balcony','courtyard'])
    lines += ['',f"Indoor named zones {named:.2f} m² including stair reservation; {gross[f['id']]-named:.2f} m² remains for walls and unassigned junction/extension strips. Not net lettable area."]
lines += ['', '## C15 inward court and open exterior study', '',
          f'- Privacy limitation: {sum(not v for v in entry_privacy)}/{len(entry_privacy)} sampled ordinary-bedroom-entry rays can see a sanitary doorway when all doors are open. Opaque suite door must close for those positions; bed rays pass with it open. This is a material compromise, not full privacy approval.',
          '- Parents/brother each 3.80 × 4.00 m, excluding private sanitary areas. Independent ordinary doors retained.',
          '- Court and stair share 2.40 m bay. Private baths move into former A-edge court; court moves inward and grows to 6.96 m². Envelope stays 10.80 × 11.40 m.',
          '- Showers remain 1.30 × 1.80 m with basins; WCs 1.00 × 1.80 m. Dressing screen removed; offset 1.00 m private passage replaces dressing area.',
          '- Grandpa common door moves near stair; solid altar side wall supports TV. Compact wooden set retained with 1.60 m front-to-front TV gap.',
          '- Quiet gallery 1.00 m wide; court glass moves to living/upper landing. Worship 3.20 × 2.90 m; exact upper empty strip retained. Suite direct court windows narrow from 1.50 to 0.90 m; dressing adds supplementary glass.',
          f'- Ground covered {gross["F1"]:.2f} m²; upper {gross["F2"]:.2f} m², no enclosed bedroom projection; sheltered shared terrace 11.50 m² and porch 7.26 m² separately.',
          '- Same upper roof datum at 6.60 m; low parapet top6.95 m, roof services top8.15 m assumed. Tank screen relocated above rear suite; structural support/noise unresolved. Two ranch porch edge/support comparisons.',
          '- Stair, porch/canopy levels and six-seat compact dining retain stated limitations.',
          '- See docs/concept-study-C15.md; exact layout and porch detail remain unselected. Sheltered terrace is owner preference.']
lines += ['', '## Stair arithmetic — reservation only', '',
          f"- Assumed floor rise {data['house']['floor_height']:.2f} m / 21 = {1000*data['house']['floor_height']/21:.1f} mm/riser.",
          '- Flights 10 + 11 risers have 9 + 10 intervening treads; tread runs 2.34 / 2.60 m at 260 mm going.',
          '- 2.60 m longest run + 1.10 m intermediate landing = 3.70 m bay depth. Top/bottom approaches lie in common circulation outside the bay.',
          '- Nominal flights 1.10 + 1.10 m with 0.20 m center reservation fill the 2.40 m bay; wall/rail details may reduce finished widths.',
          '', '## Unresolved review', '',
          '- 21 steps provisionally means risers. Owner confirmed staircase; no lift requested. Architect must resolve actual finished flights, openings, headroom, rails and applicability.',
          '- Bedroom inward/main-entry outward leaves and sliding sanitary entries are concept studies. Bounding-box and 0.80 m sampled bands are limited collision checks, not occupied usability/compliance certification.',
          f'- Living {living[2]*living[3]:.2f} m²; kitchen/dining named L-shaped zones {kit[2]*kit[3]+din[2]*din[3]:.2f} m² plus 0.37 m² open join. Common lobby excluded. Occupied appliances/chair withdrawal remain unverified.',
          '- Altar furniture 1.20 m deep leaves 1.70 m forward worship depth. Upper empty floor 3.20 × 1.20 m; ceremony/heat/privacy arrangement is a proposal, not a feng shui minimum.',
          '- Both terrace-shade variants, porch canopy, court, foundations, acoustics, waterproofing and guards need a professional design basis.',
          '- Approximate owner placement is not approval of boundary-wall construction/openings; court sky/airflow, window acoustics, kitchen extract, survey and car turning unresolved.',
          '- Indoor backing gallery 1.00 m with 0.90 m approach. Ground footprint 116.16 m² and front depth reference along A 4.10 m. Structural load paths and affordability unassessed.',
          '- Left/C 3.0 × 5.0 m car bay, separate gates, porch and steps are reservations. Clear walking strips do not establish road maneuvers, door-opening envelopes, safe levels or finished door/stair operation.']
out=ROOT/'outputs'
out.mkdir(exist_ok=True)
(out/'geometry-review.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
template=(ROOT/'src/concept-viewer.html').read_text(encoding='utf-8')
(out/'house-concepts.html').write_text(template.replace('__REVISION__',data['revision']).replace('__PROJECT_DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')),encoding='utf-8')
print(f"Generated {data['revision']} viewer/report: {sum(v for _,v in checks)}/{len(checks)} limited checks pass.")
if not all(v for _,v in checks):
    raise SystemExit('Geometry checks failed; inspect outputs/geometry-review.md')
