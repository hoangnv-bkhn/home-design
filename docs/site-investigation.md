# Site evidence and open geometry — Noi Bai

Updated: 2026-10-03.

## Evidence

Owner identifies the central parcel enclosed by sides A, B, C and D in the original `plot_dimensions.jpg`, inspected during initial briefing despite an attachment error. That image is absent from the current working copy. The recorded dimensions below remain owner-reported approximations; no new image/survey evidence was inferred for C07.

The photograph shows a roughly four-sided parcel with a bend along D. A, B and C label the other sides; they are side labels, not vertex names. The plot must not be treated as a mathematical square. A road runs alongside D and is reported by the owner to be approximately 3–4 m wide. The sketch also shows a nearby road junction; access rights along any additional edge are not established.

| Item | Evidence/status |
| --- | --- |
| Location | Owner: Noi Bai, Hanoi, near airport; exact parcel address unknown |
| A | Owner confirmed approximately 15 m side length |
| B | Owner confirmed approximately 16 m side length |
| C | Owner confirmed approximately 13 m side length |
| D | Owner confirmed approximately 18 m total length along both bent segments, not the end-to-end distance |
| D bend | Visible in photograph; owner authorizes a sketch-based assumption; segment lengths and bend position/angle are unmeasured |
| Road | Owner: approximately 3–4 m wide next to D; surveyed width, legal boundary and access geometry pending |
| Direction | Owner confirms 130° SE as the direction along A toward the road beside D (from the A/B junction toward the A/D junction). Adopt for concept orientation; measurement method and magnetic/true north remain unspecified |
| Central annotation | Appears to read “182” over “192”; owner explicitly says to ignore 192. Neither annotation is a geometric input; no area inferred |
| Nearby annotations | “168” and “169” visible; meanings not established |
| Beyond A | Owner: neighbor's wall/house |
| Beyond B | Owner: neighbor's garden |
| Beyond C | Owner: neighbor's wall/house |
| Preferred house position | Owner now wants rear beside B and about 0.30 m at A. C03 models a 0.10 m B allowance; exact B distance, boundary-wall construction and permissions remain unverified |

Site-planning brief: one car plus scooters/bicycles, garden/front yard preferred. Approximately 100 m² footprint near A–B, flexible exact area/proportions and upper cantilever studies. Latest feedback retains B>A, asks smaller footprint and explores left/C parking. C06 proposes 108.00 m² F1/F2; unselected. The house does not occupy the entire plot. Outdoor area model-derived until survey; 192 excluded.

For concept studies, account for the neighboring walls/houses at A and C. The garden beyond B is the currently reported condition, not a guarantee of permanent openness or a right to place boundary windows. Exact offsets, openings and neighboring building heights remain to be established.

## Geometry rules for the next step

Lengths use metres (m); area uses square metres (m²). The owner confirmed the boundary units and D's total length on 2026-10-01. Four approximate edge lengths, especially with one bent side, do not uniquely define the parcel. The owner authorizes an approximate bend for concept work; no registered area is being imposed.

Use the photograph for topology and a provisional bend only. It is a photographed drawing with perspective distortion and unknown original scale; pixel proportions cannot establish exact angles, area or setbacks. Do not silently distort dimensions to make an assumed area fit.

The concept model provides a provisional polygon in [the data source](../data/concepts.json), derived by [the build script](../scripts/build_concepts.py). It assumes perpendicular A/B, a 1.8 m drop along C and two 9 m segments for D. Its computed area is approximately 243.78 m², for this model only. See [the geometry review](../outputs/geometry-review.md) for coordinates and assumptions. No surveyed boundary or registered area has been adopted.

C06 retains that polygon and F1/F2 origin **(0.10, 0.30)**. Approximately 0.30 m at A is owner preference; 0.10 m at B is assistant allowance for “right next to B.” Neither fixes a surveyed envelope, legal setback, construction access or drainage/eaves rights.

C02 rear/B projection/garden door remain superseded. C06 also removes C05's **0.8 m C-side envelope extension**, aligning both floors. Both balcony studies still project toward D. No A/B openings assumed. Kitchen/dining retains its direct C-side door/window. Parents daylight/ventilation beneath F2, upper fifth-bedroom rooflight, kitchen extract and shafts remain unresolved.

C06 reduces F1/F2 to **9.0 m A × 12.0 m B**, 108.00 m² each. Model land outside F1 is about **135.78 m²** (C05 120.90 m²), including gaps/access/parking. Front depth along A becomes **5.90 m**, varying across bent D; side-yard width gains 0.80 m versus C05 and upper side gains 1.60 m. Left/C car bay is 3.0 × 5.0 m with assumed 4.5 × 1.8 m body, separate D vehicle gate and pedestrian gate. Proposed 0.90 m C walk/1.00 m front connector link garden to porch; three two-wheel spaces remain on front/A side. Ground containment/non-overlap and limited walking bands pass, but car/door/gate operation, road turning, levels, drainage and supports remain unverified. Gate endpoint coordinates lie on the assumed D geometry approximately, not a surveyed access approval.

Plot/F1/F2 retain the 90° clockwise presentation. This puts B above, A right and C left on the display. Named A/B edges take precedence over casual left/right wording; no boundary side or bearing was relabeled.

Use the owner-confirmed 130° bearing along A toward D for concept orientation. It is not the bearing along D or necessarily the perpendicular facing direction of a future facade. D has two segments; the eventual house facade and gate need not align with either. Measurement method and magnetic/true north are still unverified, so retain this as owner-provided concept data until survey. Do not derive bearings from the camera framing.

## Location-specific investigations

- Obtain parcel location, current planning conditions and a level/boundary survey before fixing the buildable envelope.
- Ask the local design team to check whether airport-related planning or height controls apply at the exact location, including rooftop equipment and construction lifting. No restriction or exemption is established here simply from airport proximity.
- Observe or measure aircraft and road noise at different times, especially where bedrooms might sit. Aircraft noise is an identified environmental concern: [WHO noise guidance](https://www.who.int/tools/compendium-on-health-and-environment/environmental-noise/) and [ICAO aircraft noise](https://www.icao.int/environmental-protection/aircraft-noise). These sources do not establish exposure at this parcel or a Vietnamese compliance limit.
- Project inference: if site noise is significant, compare roof/wall/window acoustic performance together with a ventilation strategy that remains usable when windows are closed. Do not specify glazing solely by pane count or assume the opposite side of the house eliminates overhead aircraft noise.
- Verify road access for deliveries, emergency access, turning, construction storage and any parking maneuver. An approximate road width is not a complete access assessment.
- Record neighbors/open sides, drainage and flood history, utility points, ground conditions and road/site levels.

## Questions to resolve

1. For later survey/directional refinement: how was the confirmed 130° bearing measured, and is it magnetic or true north? This does not block initial concept studies.
2. Later site detailing: what are the heights/offsets of the reported walls/houses at A and C, and the boundary treatment at B's garden? Any access/opening rights remain unverified.
3. Where should the gate/vehicle access be, and is any road widening or building line known?

Boundary units and the meaning of the 130° orientation are resolved; 192 is excluded. Room relationships and a visibly provisional boundary study can progress using the confirmed approximate lengths, owner-provided bearing and an assumed bend. Survey verification remains outstanding.

## C08 current envelope and real-window proposal

C08 retains polygon, origin (0.10,0.30), approximate A/B allowances and 130° evidence. Outer envelope becomes **10.5 m A × 12.0 m B = 126.00 m²** each floor. A **6.80 m² clear open court** is inside it; subtracting it yields **119.20 m² covered footprint / covered-envelope convention**, including court lining walls and upper stair-opening reservation. Land outside the outer envelope is about **117.78 m²**, plus the internal court. Neither quantity is surveyed garden or statutory coverage. B remains longer than A.

Front depth along A drops **5.90 → 4.40 m**, varying across bent D. Porch and steps move 1.50 m toward D; dimensions and 1.15 m waiting strip remain. Garden connectors move clear of the larger house; front pedestrian strip is now 1.00 m nominal. Separate gates, C parking and two-wheel reservations remain stationary proposals; no road turning or new permission established.

Parents/brother open to an **own 3.4 × 2.0 m open-to-sky court**, with no F2 floor/roof across it, beside sleeping rooms and separate from indoor altar buffer. Both stairs and bedroom 5 have C-yard windows. Reflective tubes/boxes and rooflight removed. No A/B boundary opening assumed. Court sky/airflow, neighbor heights, noise/privacy, drainage, roof/wall edges and services unresolved. [C08 evidence](altar-and-windows-C08.md), S02/S04/L14/L15/E02. No new survey/image evidence or approved footprint.

## C07 entrance and daylight coordination — historical

C07 retains C06's 9.0 × 12.0 m aligned floors, origin and parcel assumptions. Main entrance/porch/pedestrian gate move 1.00 m toward C. Porch depth grows to 2.20 m for outward leaves; steps move outward. Garden approach/walking strips route around the deeper porch; parked-car reservation unchanged. Neither levels nor maneuvering are verified.

Larger shaded bedroom openings face D or the modeled own C yard; no A/B windows. Brother storage is moved off its window wall. Parents receive only explicit roof-tube candidates, and upper bedroom 5 a diffusing rooflight. These are not environmental-performance or permit approvals. The 0.30 m A gap cannot establish adequate sky access without neighbor heights. See [C07 envelope research](daylight-and-envelope-C07.md); legal full-text retrieval failed, so no distance threshold is adopted from search snippets. Site opening rights/planning/airport controls remain S02.

## C09 retained site basis

C09 retains C08 envelope, open court, origin, front depth and ground parking/porch/walking geometry. Balcony 01 changes to 2.00 m projection × 3.60 m frontage; balcony 02 compares the earlier shared 1.60 × 4.40 m form. No private sister slab remains in the active comparison. Both are inside the assumed parcel model; no permission, support design, turning clearance or full porch weather cover is inferred. Ground/survey/environmental evidence status unchanged.

## C10 current site update

Bounding envelope reduces along B to **10.50 × 11.40 m / 119.70 m²**. Clear court relocates to [0.2,4.3,2.0,2.0] / **4.00 m²**, between corner suites and kitchen. Ground covered convention **115.70 m²**; upper enclosed convention **111.65 m²**, excluding its 4.05 m² front loggia notch. Model land outside rectangle is approximately **124.08 m²**, plus court. Front depth along A remains **4.40 m**; 0.60 m is gained toward C, not D.

Origin, owner-reported edges/bearing, offsets, stationary C-side car bay, scooters and gates retain their evidence status. Porch/entry shift 0.60 m along B; arrival path turns from existing pedestrian gate. Canopy is a new 2.30 × 2.50 m schematic reservation. Both balcony options partly recess into F1 and project 1.20/0.60 m toward D; no enclosed room cantilever. Ground walking paths remain reservations, not swept vehicle/door paths or measured levels.

Parents/brother remain dependent on their own smaller court, now with a common cleaning door. No A/B opening assumed. Window size reduces to 1.50 m and storage is clear of it; daylight/airflow/sky and drainage are unverified. [C10 tradeoffs](concept-study-C10.md) supersede prior current-envelope statements above.
