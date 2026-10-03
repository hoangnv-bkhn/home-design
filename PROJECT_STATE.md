# Project state — resume here

Updated: 2026-10-03. Phase: C06 usability and footprint review.

## Current position

- Current revision **C06**, proposed and unselected. Road arrival, F1/F2 naming, room counts and family rules remain confirmed.
- Latest feedback: independent parents exit, smaller bedrooms/excess spaces and footprint, sofa backs away from altar, explore left parking, and judge actual household usability. Recorded in [brief](docs/brief.md), [family rules](docs/preferences-and-feng-shui.md), [decisions](docs/decisions.md) and [AGENTS.md](AGENTS.md).
- [Viewer](outputs/house-concepts.html) · [C06 comparison and usability](docs/concept-study-C06.md) · [F1](outputs/option-01-F1.svg) · [Plot](outputs/option-01-site.svg).
- Sources: [metre geometry](data/concepts.json), [template](src/concept-viewer.html), [build](scripts/build_concepts.py), [browser/export](scripts/review_viewer.py).
- Authority/tracking: [brief](docs/brief.md), [site](docs/site-investigation.md), [family rules](docs/preferences-and-feng-shui.md), [decisions](docs/decisions.md), [issues](docs/open-issues.md), [workflow](docs/agent-workflow.md).

## Design response and limits

- F1/F2 both **9.0 m A × 12.0 m B = 108.00 m²**; F1 −14.88 m²/12.1%, F2 −22.56 m²/17.3% from C05. Upper C extension removed; road balcony variants retained. Footprint remains 8% above approximate target; budget/acceptance open (L09/L12).
- All five bedrooms shrink. Parents/brother get independent 0.90 m common-access doors and separate internal bath doors. Private pairs rotate/stack; enclosed 1.30 m passages replace long lobbies. Private passage area 7.20 → 3.12 m² per suite (L05/L08/L13).
- Sofa faces +x/front; rear points away from altar. TV clears the 1.90 m doorway. Bedroom/main-entry inward arcs and sanitary sliding candidates drawn; finished operation open (L02/L05/L11).
- Left/C 3.0 × 5.0 m car bay, separate D vehicle/pedestrian gates. Kitchen–garden–porch walks avoid parked vehicles/steps. Assumed car 4.5 × 1.8 m; road turning, gate leaves/levels unresolved (S03/L11).
- Compact six-seat kitchen retains direct C exit, occupied chair rectangles, 1.00 m counter aisle and 0.90 m garden approach. Actual chair/appliance use pending (L07).
- Altar 3.4 × 1.5 m, exact empty F2 projection and **0.90 m indoor buffer** retained; buffer acceptance unresolved. Four separate stacked WC/shower pairs, shower basins, five bedrooms and nominal 21-riser stair preserved (L04/L05/L06).
- Shared balcony 7.04 m² independent; 7.52 m² corner option crosses sister bedroom, with 0.40 m secondary bed side/shortened wardrobe. Neither selected (L03/L08).
- Upper hall/passage zones shrink 6.96 m² but common landing remains generous. Parents daylight/ventilation, fifth-bedroom rooflight, permissions and real services/structure unresolved (L10/S02/S04/E01/E02).

## Review artifacts and checks

- [Shared F2](outputs/option-01-F2.svg) · [Corner F2](outputs/option-02-F2.svg) · [Sections](outputs/option-01-section.svg) · [Shared massing](outputs/option-01-massing.svg) · [Corner massing](outputs/option-02-massing.svg).
- Ten SVGs, ten PNGs and [focused dining capture](outputs/viewer-selection-review.png) regenerated as C06. Nested obsolete-C01 is historical.
- **71/71 limited build checks passed**; [geometry report](outputs/geometry-review.md). Finite 0.80 m sample bands/door bounding boxes check specified collisions, not full usability, legality or engineering.
- Chrome: both options/all five views, 66 actual room clicks plus focus/keyboard, direct bedroom doors, sofa facing, balcony details/overlays and 390 px overflow passed; [browser report](outputs/viewer-review.md).
- Visual inspection: F1, both F2, plot, section, both massings and dining selection. Print/PDF untested. Local link/state checks completed.
- C05 archive verified before editing. C06 final sources/docs/exports archived and checksum verified with house-snapshot; preserves an unapproved proposal. No temporary migration script or stale/interrupted current output remains.

## Next action

Review the 108 m² proposal, smaller bedrooms and shared/corner balcony compromises. Then detail occupied door/chair use, **parents daylight/ventilation**, stair opening/headroom and actual vehicle access before squeezing further. L02–L13, S01–S04, E01/E02 and budget C01 remain open to their stated extent.

Do not re-ask settled room counts, floors, road arrival, stair interpretation, basin intent, sofa rule or parcel inputs. Units remain metres; B/A allowances remain unverified assumptions/preferences. C06 is archived; next design issue needs C07 or a distinct erratum suffix, preserving baseline first.

```powershell
python scripts/build_concepts.py
python scripts/review_viewer.py
python scripts/snapshot_revision.py --verify C06
```
