# Project state — resume here

Updated: 2026-10-03. Phase: C07 entrance, living, balcony and daylight review.

## Current position

- Current revision **C07**, proposed and unselected. Owner permits outward main entry and requests centered seating/TV, open arrival, coordinated balcony/exterior and better bedroom daylight. No private-balcony mandate or boundary-window permission added.
- [Viewer](outputs/house-concepts.html) · [C07 comparison](docs/concept-study-C07.md) · [Daylight/envelope evidence](docs/daylight-and-envelope-C07.md) · [F1](outputs/option-01-F1.svg).
- Sources: [metre geometry](data/concepts.json), [template](src/concept-viewer.html), [build](scripts/build_concepts.py), [browser/export](scripts/review_viewer.py).
- Requirements/tracking: [brief](docs/brief.md), [site](docs/site-investigation.md), [family rules](docs/preferences-and-feng-shui.md), [decisions](docs/decisions.md), [issues](docs/open-issues.md), [workflow](docs/agent-workflow.md).

## Design response and material limits

- Aligned F1/F2 **9.0 m A × 12.0 m B = 108.00 m²** retained; 8% above approximate target, affordability unassessed.
- TV centered with 2.20 m sofa; 2.25 m front-to-stand gap. Main entry shifts 1.00 m toward C into **2.30 × 1.90 m empty arrival**, with **1.00 m through hall** outside viewing line. Sofa rear stays away from altar.
- Two 0.95 m main leaves open outward. Porch becomes **2.20 × 2.20 m / 4.84 m²**, +1.54 m² outdoor ground; **1.15 m front waiting strip** outside sweep boxes. Steps, pedestrian gate and garden walks coordinated. Full weather cover, thresholds/levels and concurrent passing unresolved.
- Grandpa trades **3.08 m²**, now **10.36 m²** with 1.40 × 2.00 m bed, 0.40/1.00 m sides and 0.60 m wardrobe-front gap. Normal 0.85 m hall entrance retained. Tighter side/storage/use needs review (L08).
- Both options retain independent **7.04 m² shared BAL-01** as facade/entry frame. Option 02 adds **2.60 m² private BAL-02 / 1.00 m projection**, total **9.64 m²**; no shared bedroom crossing. Finished guard/fins reduce net area/depth; support/cost/shading unresolved (L03/E01).
- Wider shaded bedroom windows toward own yard: Grandpa 2.10 m, brother 2.30 m, sister 2.20 m, nominal 1.65 m height. Brother wardrobe moved off window wall; sister C wall stays for storage. No A/B windows assumed.
- Bedroom 5 has **1.12 m² rooflight candidate**. Two parents daylight tubes have explicit upper 0.40 m chase boxes, total **0.32 m²**, leaving bedroom 5 **12.60 m² after boxes** (12.92 rectangle). Output, roof/beam/slab paths and acoustic/fire detailing unverified; tubes give no view/ventilation. Parents environment remains a material open issue (new L14). Courtyard/yard-facing relocation is a future topology alternative, not implemented.
- Five bedrooms, four separate stacked WC/shower pairs with shower basins, independent suite exits, compact C kitchen/garden door, altar 3.4 × 1.5 m/exact empty upper projection and 0.90 m indoor buffer retained. Stair still 21-riser reservation. Left parking remains stationary study with turning unresolved.

## Artifacts and checks

- [Shared F2](outputs/option-01-F2.svg) · [Shared + private F2](outputs/option-02-F2.svg) · [Shared massing](outputs/option-01-massing.svg) · [Additional private massing](outputs/option-02-massing.svg) · [Sections including tubes](outputs/option-01-section.svg) · [Plot](outputs/option-01-site.svg).
- **83/83 limited build checks passed**; [geometry report](outputs/geometry-review.md). Finite bands/sweep boxes are not occupied usability, daylight, legality or engineering verification.
- Chrome passed both options/all five views; **67 actual pointer clicks**, focus/keyboard, optional BAL-02/areas, rendered sofa/TV centers, outward leaves, tube/shade metadata, controls and 390 px overflow. [Browser report](outputs/viewer-review.md).
- Ten SVGs/ten PNGs and focused selection capture regenerated. Visual inspection: F1, both F2, plot, sections, both massings and selection capture. Print/PDF untested; no stale current outputs or temporary scripts remain.
- DOE primary daylight/fenestration guidance recorded. Vietnamese legal/standard primary full-text retrieval failed; no snippet-derived distances/compliance applied. S02 remains open.
- C06 50-file snapshot verified before editing. Completed C07 package archived and SHA-256 verified using house-snapshot; preserves an unselected proposal. Earlier archives immutable.

## Next action

Review open arrival and Grandpa's 0.40 m side/10.36 m² tradeoff, optional private step-out usefulness, and parents' long-term daylight/view/ventilation strategy. Then detail shade/noise/glazing, occupied doors/weather, balcony support, stair opening/headroom and real road/car access. L02–L14, S01–S04, E01/E02 and budget C01 remain open to their stated extent.

Do not re-ask settled counts/floors/road/sofa/altar/stair/basin/site inputs or outward-door permission. Keep metres, stable IDs and evidence statuses. C07 archived; next design issue C08 or distinct erratum suffix, preserving baseline first.

```powershell
python scripts/build_concepts.py
python scripts/review_viewer.py
python scripts/snapshot_revision.py --verify C07
```
