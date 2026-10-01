"""Generate a portable concept viewer and factual geometry report. Standard library only."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'data/concepts.json').read_text(encoding='utf-8'))
s = data['site']
# Explicit family of assumed geometries, not a reconstructed survey.
c_dx = math.sqrt(s['C'] ** 2 - s['assumed_C_drop'] ** 2)
p = (s['A'], 0)
q = (c_dx, s['B'] + s['assumed_C_drop'])
dx, dy = q[0] - p[0], q[1] - p[1]
chord = math.hypot(dx, dy)
if chord > s['D']:
    raise ValueError('Assumed geometry cannot accommodate the supplied D length')
bend_offset = math.sqrt((s['D']/2) ** 2 - (chord/2) ** 2)
bend = ((p[0]+q[0])/2 + dy/chord*bend_offset,
        (p[1]+q[1])/2 - dx/chord*bend_offset)
polygon = [(0, 0), p, bend, q, (0, s['B'])]
area = abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(polygon, polygon[1:]+polygon[:1])))/2
data['derived'] = {'polygon': polygon, 'site_area': area, 'bend_offset': bend_offset,
                   'D_segments': [math.dist(p,bend), math.dist(bend,q)]}

def overlap(a,b):
    return max(0,min(a[0]+a[2],b[0]+b[2])-max(a[0],b[0])) * max(0,min(a[1]+a[3],b[1]+b[3])-max(a[1],b[1]))

def inside(point):
    x,y=point
    hit=False
    for a,b in zip(polygon,polygon[1:]+polygon[:1]):
        if (a[1]>y)!=(b[1]>y) and x < (b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:
            hit=not hit
    return hit

checks=[]
def check(name, condition):
    checks.append((name, bool(condition)))

for floor in data['floors']:
    rooms=floor['rooms']
    check(f"{floor['id']}: unique room IDs", len({r['id'] for r in rooms}) == len(rooms))
    check(f"{floor['id']}: no overlap of room zones", all(overlap(a['rect'],b['rect']) < 1e-8 for i,a in enumerate(rooms) for b in rooms[i+1:]))
    check(f"{floor['id']}: two WCs and two showers", sum(r['type']=='wc' for r in rooms)==2 and sum(r['type']=='shower' for r in rooms)==2)
    check(f"{floor['id']}: indoor zones within 10 × 10 m envelope", all(r['type']=='balcony' or (r['rect'][0]>=0.2-1e-8 and r['rect'][1]>=0.2-1e-8 and r['rect'][0]+r['rect'][2]<=9.8+1e-8 and r['rect'][1]+r['rect'][3]<=9.8+1e-8) for r in rooms))
check('Five bedrooms total', sum(r['type']=='bed' for f in data['floors'] for r in f['rooms'])==5)
altar=next(r['rect'] for r in data['floors'][0]['rooms'] if r['type']=='altar')
upper=data['floors'][1]
check('Altar clear width at least 3.4 m', altar[2]>=3.4)
check('Altar projection excludes upstairs bedrooms and hall zones', all(overlap(altar,r['rect'])<1e-8 for r in upper['rooms'] if r['type'] in ['bed','hall']))
check('No upstairs furniture above altar', all(overlap(altar,f[1:])<1e-8 for f in upper['furniture']))
for option in data['options']:
    def transform(x,y):
        if option['rotation']==90: x,y=10-y,x
        return x+s['assumed_house_origin'][0], y+s['assumed_house_origin'][1]
    corners=[(0,0),(10,0),(10,10),(0,10),(10,.2),(11.4,.2),(11.4,3.4),(10,3.4)]
    check(f"Option {option['id']}: house and balcony corners inside assumed plot",all(inside(transform(x,y)) for x,y in corners))

lines=['# Concept C01 — generated geometry review', '',
       'Generated from `data/concepts.json` by `scripts/build_concepts.py`.', '',
       '**Concept checks only. These do not establish survey accuracy, buildability, legal compliance, door clearances, car turning, headroom or structural adequacy.**','',
       '## Assumed site geometry','',
       f'- Derived model area: {area:.2f} m². This belongs only to the assumed polygon; it is NOT the registered plot area.',
       f'- D segments: {math.dist(p,bend):.3f} + {math.dist(bend,q):.3f} m.',
       f'- Bend offset from its end-to-end chord: {bend_offset:.3f} m.',
       '- Model vertices in metres: '+json.dumps(polygon),
       '- House footprint: 100.00 m². Upper-floor envelope: 100.00 m² including stair opening; external balcony: 4.48 m².',
       '- Two-floor envelope sum: 200.00 m²; plus balcony 4.48 m². This is a concept area convention, not a statutory/contract measurement.',
       f'- Model land outside ground-floor footprint: {area-100:.2f} m²; includes access gaps/parking, not all garden.', '',
       '## Automated checks','']
lines += [f"- {'PASS' if result else 'FAIL'} — {name}" for name,result in checks]
for floor in data['floors']:
    lines += ['',f"## {floor['id']} clear zone schedule",'', '| ID | Space | Dimensions (m) | Area (m²) |','| --- | --- | --- | --- |']
    for r in floor['rooms']:
        x,y,w,h=r['rect']
        lines.append(f"| {r['id']} | {r['label']} | {w:.2f} × {h:.2f} | {w*h:.2f} |")
    total=sum(r['rect'][2]*r['rect'][3] for r in floor['rooms'] if r['type']!='balcony')
    lines += ['', f'Indoor named zones sum: {total:.2f} m², including the stair zone. Remaining {100-total:.2f} m² covers walls and unassigned junction strips. These are not net lettable areas.']
lines += ['', '## Still requires manual/professional review','',
          '- Door swings/sliding hardware, fixture use and furniture circulation; especially the narrow private turning passage.',
          '- Stair access, risers/landings, opening, headroom and guards; diagram is a reservation, not a stair design.',
          '- Car gate/swept path on the narrow road. Car rectangles only show stationary accommodation.',
          '- Setbacks, opening rights, boundary/neighbor heights and actual site area.',
          '- Ventilation, airport acoustics, plumbing shaft dimensions and drainage routes.',
          '- Structural grid: axes are discussion aids, not selected columns or beams.',
          '- Altar extent/ceremony space, exact meaning of the backing buffer, and upstairs empty-zone acceptance.',
          '- Balcony access is through the sister room in both options; confirm whether shared access is desired.']
out=ROOT/'outputs'
out.mkdir(exist_ok=True)
(out/'geometry-review.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
data['derived']['checks']=[{'name':n,'pass':p} for n,p in checks]
template=(ROOT/'src/concept-viewer.html').read_text(encoding='utf-8')
(out/'house-concepts.html').write_text(template.replace('__PROJECT_DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')),encoding='utf-8')
print(f"Generated outputs/house-concepts.html and outputs/geometry-review.md; {sum(p for _,p in checks)}/{len(checks)} geometry checks pass.")
if not all(p for _,p in checks):
    raise SystemExit('Geometry checks failed; inspect outputs/geometry-review.md')
