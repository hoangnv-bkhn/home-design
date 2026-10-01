# Concept C01 — generated geometry review

Generated from `data/concepts.json` by `scripts/build_concepts.py`.

**Concept checks only. These do not establish survey accuracy, buildability, legal compliance, door clearances, car turning, headroom or structural adequacy.**

## Assumed site geometry

- Derived model area: 243.78 m². This belongs only to the assumed polygon; it is NOT the registered plot area.
- D segments: 9.000 + 9.000 m.
- Bend offset from its end-to-end chord: 0.813 m.
- Model vertices in metres: [[0, 0], [15, 0], [14.744591778293383, 8.996375194503877], [12.874781551544865, 17.8], [0, 16]]
- House footprint: 100.00 m². Upper-floor envelope: 100.00 m² including stair opening; external balcony: 4.48 m².
- Two-floor envelope sum: 200.00 m²; plus balcony 4.48 m². This is a concept area convention, not a statutory/contract measurement.
- Model land outside ground-floor footprint: 143.78 m²; includes access gaps/parking, not all garden.

## Automated checks

- PASS — F1: unique room IDs
- PASS — F1: no overlap of room zones
- PASS — F1: two WCs and two showers
- PASS — F1: indoor zones within 10 × 10 m envelope
- PASS — F2: unique room IDs
- PASS — F2: no overlap of room zones
- PASS — F2: two WCs and two showers
- PASS — F2: indoor zones within 10 × 10 m envelope
- PASS — Five bedrooms total
- PASS — Altar clear width at least 3.4 m
- PASS — Altar projection excludes upstairs bedrooms and hall zones
- PASS — No upstairs furniture above altar
- PASS — Option 01: house and balcony corners inside assumed plot
- PASS — Option 02: house and balcony corners inside assumed plot

## F1 clear zone schedule

| ID | Space | Dimensions (m) | Area (m²) |
| --- | --- | --- | --- |
| BR-01 | Parents | 3.70 × 3.20 | 11.84 |
| WC-01 | Private WC | 1.05 × 1.50 | 1.58 |
| SH-01 | Private shower | 1.05 × 1.50 | 1.58 |
| EN-01 | Private passage | 2.20 × 1.60 | 3.52 |
| BR-02 | Grandpa | 3.50 × 3.20 | 11.20 |
| HALL-01 | Shared access | 4.80 × 1.10 | 5.28 |
| STAIR-01 | U stair | 2.30 × 4.20 | 9.66 |
| STORE-01 | Stair reserve | 2.30 × 0.80 | 1.84 |
| KIT-01 | Kitchen | 2.40 × 2.70 | 6.48 |
| WC-02 | Shared WC | 2.40 × 1.10 | 2.64 |
| SH-02 | Shared shower | 2.40 × 1.10 | 2.64 |
| LIV-01 | Living + dining for 6 | 4.70 × 3.40 | 15.98 |
| BUF-ACCESS | Quiet access | 1.10 × 2.80 | 3.08 |
| ALT-01 | Altar area | 3.50 × 1.70 | 5.95 |
| ALT-BUFFER | Indoor buffer | 3.50 × 1.00 | 3.50 |

Indoor named zones sum: 86.76 m², including the stair zone. Remaining 13.24 m² covers walls and unassigned junction strips. These are not net lettable areas.

## F2 clear zone schedule

| ID | Space | Dimensions (m) | Area (m²) |
| --- | --- | --- | --- |
| BR-03 | Brother | 3.70 × 3.20 | 11.84 |
| WC-03 | Private WC | 1.05 × 1.50 | 1.58 |
| SH-03 | Private shower | 1.05 × 1.50 | 1.58 |
| EN-03 | Private passage | 2.20 × 1.60 | 3.52 |
| BR-04 | Younger sister | 3.50 × 3.20 | 11.20 |
| HALL-02 | Shared access | 6.00 × 1.10 | 6.60 |
| STAIR-02 | Stair opening | 2.30 × 4.20 | 9.66 |
| STORE-02 | Stair reserve | 2.30 × 0.80 | 1.84 |
| UTIL-02 | Utility / storage | 2.40 × 2.70 | 6.48 |
| WC-04 | Shared WC | 2.40 × 1.10 | 2.64 |
| SH-04 | Shared shower | 2.40 × 1.10 | 2.64 |
| BR-05 | Bedroom 5 | 3.50 × 3.40 | 11.90 |
| HALL-03 | Access | 1.10 × 2.70 | 2.97 |
| HALL-04 | Wet-room access | 1.10 × 2.30 | 2.53 |
| EMPTY-ALT | Empty above altar | 3.50 × 2.80 | 9.80 |
| BAL-01 | Balcony | 1.40 × 3.20 | 4.48 |

Indoor named zones sum: 86.77 m², including the stair zone. Remaining 13.23 m² covers walls and unassigned junction strips. These are not net lettable areas.

## Still requires manual/professional review

- Door swings/sliding hardware, fixture use and furniture circulation; especially the narrow private turning passage.
- Stair access, risers/landings, opening, headroom and guards; diagram is a reservation, not a stair design.
- Car gate/swept path on the narrow road. Car rectangles only show stationary accommodation.
- Setbacks, opening rights, boundary/neighbor heights and actual site area.
- Ventilation, airport acoustics, plumbing shaft dimensions and drainage routes.
- Structural grid: axes are discussion aids, not selected columns or beams.
- Altar extent/ceremony space, exact meaning of the backing buffer, and upstairs empty-zone acceptance.
- Balcony access is through the sister room in both options; confirm whether shared access is desired.
