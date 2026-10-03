# Project state — resume here

Updated: 2026-10-03. Phase: C05 owner-feedback review.

## Current position

- Current revision **C05**; layout, footprint, compact sanitary dimensions and both balcony alternatives are **proposals, unselected**.
- Road-facing arrival and SE house/altar facing remain confirmed. F1 is ground/entrance floor; F2 upstairs. No room-count or floor-naming clarification needed.
- Latest owner input: horizontal B extent longer than vertical A; left/C kitchen dining with direct garden access; Grandpa door away from entry/TV; test 1.0 m WC / 1.4 m shower widths; repair black room selection and porch/parking/text errors.
- [Viewer](outputs/house-concepts.html) · [C05 comparison and compromises](docs/concept-study-C05.md) · [F1](outputs/option-01-F1.svg) · [Plot](outputs/option-01-site.svg).
- Sources: [geometry](data/concepts.json), [template](src/concept-viewer.html), [build](scripts/build_concepts.py), [browser/export](scripts/review_viewer.py).
- Authority: [brief](docs/brief.md), [site](docs/site-investigation.md), [family rules](docs/preferences-and-feng-shui.md); tracking: [decisions](docs/decisions.md), [issues](docs/open-issues.md), [workflow](docs/agent-workflow.md).
- Skills: [house-revision](.agents/skills/house-revision/SKILL.md), [house-verify](.agents/skills/house-verify/SKILL.md), [standards-research](.agents/skills/standards-research/SKILL.md), [house-snapshot](.agents/skills/house-snapshot/SKILL.md).

## Design response and compromises

- F1 now 9.6 m along A × 12.8 m along B. In the retained clockwise display B is horizontal/top, A vertical/right and C left. Parcel lengths/bearing are unchanged.
- Front depth along A grows by 1.6 m to a model 5.3 m; bent D means it varies across the frontage. Side yard loses 2.0 m width. Gross footprint grows 1.92 m² rather than reducing toward the approximate 100 m² target; acceptance and budget unresolved (L09/L12).
- C-side kitchen dining gains a direct 0.90 m side-yard door/window. It opens under the upper projection; extract, occupied six-seat fit and garden passage remain open (L07/L10).
- Grandpa door moves onto the west bedroom wall from a 1.40 m deep internal passage, away from the main entry and TV wall. Grandpa and sister rooms become longer/narrower; review furniture and acceptance (L05/L08).
- Four separate stacked WC/shower pairs remain, no WC basins; shower trays/basins arranged along compartment depth. Widths 1.00/1.40 m are clear concept studies, not proven minima/comfort or construction dimensions (L05).
- Parents/brother suites keep screened turning routes. Five bedrooms, nominal 21-riser stair, 1.90 m main opening, TV and both balcony variants remain. Shared 7.04 m² versus sister corner 7.52 m²; neither selected (L03/L06/L11).
- Altar 3.4 × 1.5 m with exact empty upper projection retained. **Indoor backing buffer reduces to 0.9 m**: material assistant compromise requiring family review (L04). No change to indoor/solid-wall rule.
- Porch, steps, car bay and three two-wheel spaces are explicit editable rectangles. Ground reservations no longer overlap; vehicle turning, door/step levels, supports and occupied use remain unresolved.
- Selection keeps room fills with an orange dashed outline; dining colour, fallback fill, keyboard/pressed state and furniture pointer handling repaired (V01).

## Review artifacts and checks

- [Shared F2](outputs/option-01-F2.svg) · [Sister F2](outputs/option-02-F2.svg) · [Sections](outputs/option-01-section.svg) · [Shared massing](outputs/option-01-massing.svg) · [Corner massing](outputs/option-02-massing.svg).
- Ten current SVGs/ten matching PNGs and [focused dining capture](outputs/viewer-selection-review.png) regenerated. Top-level outputs are C05; nested obsolete-C01 is historical.
- **58/58 limited build checks passed** (original 48 plus 10 targeted checks); [geometry review](outputs/geometry-review.md). Passing geometry does not prove occupied circulation, permissions or engineering.
- Chrome: both options/all five views, **66 actual room clicks** plus focus/keyboard, balcony details, TV/entry, overlays and 390 px document overflow passed; [browser review](outputs/viewer-review.md).
- Visual inspection of F1, both F2, plot, sections, massing and selected dining. Print/PDF not tested.
- C03a archive verified before editing. Existing C04 archive discovered and verified despite active workspace being C03a; preserved, not adopted as approval. Next free issue is C05 (D27).
- C05 review baseline archived and checksum verified with house-snapshot after final sources/docs/exports. Archives remain local immutable evidence, not owner approval or off-device backup.
- No stale current exports, temporary migration scripts or interrupted edits remain.

## Next action

Review the front/side-yard tradeoff, Grandpa/sister proportions, **0.9 m backing buffer** and compact sanitary/dining use. Then refine door leaves, stair opening/headroom, near-boundary ventilation and professional structure/services. L02–L12, S01–S04, E01/E02 and deferred budget remain open. Direct kitchen/garden adjacency is drawn; use and acceptance remain open.

Do not re-ask settled floor names, room counts, road-facing arrival, stair interpretation, basin intent or approximate parcel inputs. Current editable units are metres. Read workflow caveats before geometry edits. C05 is archived; the next design issue needs C06 (or a distinct suffix for an erratum), preserving the baseline first.

```powershell
python scripts/build_concepts.py
python scripts/review_viewer.py
python scripts/snapshot_revision.py --verify C05
```
