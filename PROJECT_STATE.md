# Project state — resume here

Updated: 2026-10-04. **C11 aligned rooms, open right terrace and composed entrance**. Proposed, unselected; not for construction.

## Current position

Owner requests improved grid/wall alignment, fewer unnecessary partitions, right shared terrace replacing study, proper canopy/porch/steps, better use of buffer/linen space and a substantially improved exterior. Stair may fill available width: 2.20 m is no longer fixed. Other settled room, sanitary, altar, site and circulation rules remain. D39 records directions; D40 records assistant proposals.

- [Viewer](outputs/house-concepts.html) · [C11 reasoning/comparison](docs/concept-study-C11.md) · [F1](outputs/option-01-F1.svg) · [F2](outputs/option-01-F2.svg).
- [Open terrace exterior](outputs/option-01-massing.svg) · [Sheltered exterior](outputs/option-02-massing.svg) · [Sections/entrance](outputs/option-02-section.svg) · [Site](outputs/option-01-site.svg).
- Sources: [metre geometry](data/concepts.json), [template](src/concept-viewer.html), [build](scripts/build_concepts.py), [browser/export](scripts/review_viewer.py).
- Evidence: [brief](docs/brief.md), [family rules](docs/preferences-and-feng-shui.md), [site](docs/site-investigation.md), [decisions](docs/decisions.md), [issues](docs/open-issues.md), [workflow](docs/agent-workflow.md).

## Proposal and tradeoffs

- Shared wet rooms move **0.30 m toward C/displayed left** to match parents/brother wall y4.25. Private enclosure follows same line. All wet compartments remain stacked, separate WC/shower and shower basins retained.
- Stair fills **2.50 × 3.70 m** bay: nominal 1.10 m flights, 0.30 m central gap, 1.10 m landing; 21 risers/260 mm going retained. Wall x3.65 now matches suite/kitchen/spare; x6.25 opposite division retained. Architectural references, not engineered axes or finished clearance certification.
- Internal dressing divider removed; short transverse sightline screen and private perimeter retained. Ordinary bedroom entries remain independent. No storage forced into dressing routes.
- **10.58 m² shared right terrace** replaces study, 2.30 × 4.60 m with 0.60 m outward projection. 1.20 m shared sliding weather-door candidate. Old central recess closes into landing; new landing window above entry. Open metal guards, no full-height terrace side frames.
- Both options share one plan: **01 partial pergola / 02 thin full roof**. Assistant prefers 02 for further development; neither owner-selected. Bench backs away from altar; route and shade posts clear occupied reservation. A-side privacy/permission, guard/low window protection, supports and water management unresolved.
- Ground buffer becomes **doorless 0.90 m quiet alcove**, 0.80 m side portal, 0.95 m sofa-back approach, shallow 0.25 m end display ledge. No seat/through-route. Upper linen alcove loses door and divider to empty strip; closed cabinet retained. Proposed uses need family review. Solid ground backing and **4.08 m² empty indoor upper altar strip** unchanged; routine routes stay outside it.
- Entrance: porch **2.20 × 2.20 m**, canopy **2.45 × 2.80 m**, proposed 2.70 m soffit/0.12 m visual edge and two posts. **Three 150 mm rises**, two 300 mm treads plus porch. Yard −0.45 m is an assumption pending site/flood/road levels. Existing outward leaves/front waiting reservation retained. Drains/gutters preliminary.
- Exterior: pale mineral walls, recessed right terrace, charcoal stair-window surround, timber entry and slim canopy. New landing window improves facade and hall daylight opportunity; no daylight result claimed.
- Ground **115.70 m² unchanged**; upper enclosed convention **106.88 m²** after 8.82 m² recess, includes stair reservation. Terrace and roof remain construction, no cost saving claimed. Still above approximate 100 m² ground target; affordability unassessed.
- Bedrooms/court/kitchen retain C10: parents/brother 13.60 m², Grandpa/sister 14.80, spare 12.58, court 2 × 2 m. Smaller court daylight/airflow and compact six-seat dining remain compromises. No new A/B windows or parking-turning result.

## Artifacts and checks

- [Geometry](outputs/geometry-review.md): **114/114 limited checks**; wet/stair alignment, enclosure removal, terrace access/bench/posts, entry-post bands and rise arithmetic added to retained geometry checks. Not a usability, legal, environmental or engineering certification.
- [Chrome](outputs/viewer-review.md): both options/all five views, **88 actual pointer selections**, keyboard/focus, overlays and 390 px overflow. Ten SVG/PNG exports plus selection capture current; sections export at 1800 px height. Print/PDF untested.
- Visual inspection: final F1/F2, both massings, site, sections and selection capture. Stale study section, entrance details and back-facing terrace-door rendering corrected. Final browser rerun required environment escalation after local debugging connection reset.
- C10 **56-file archive verified before changes**. C11 package: [archive manifest](revisions/C11/manifest.json), SHA-256 verification through snapshot helper. Archives preserve proposals, not approval; earlier archives immutable.

## Next action

Review terrace shade/exterior composition and doorless/open alcoves. Then prioritize smaller-court daylight/airflow and occupied kitchen/ensuite use before fixing layout. Establish site/flood/road levels before selecting porch height; engineer to resolve actual structural grid and terrace/canopy supports. Do not reopen settled counts, spare use, limited altar strip or stair-width flexibility.

L02–L16, S01–S04, E01/E02, F01 and budget C01 remain open to stated extent. Next design issue **C12**, or distinct erratum suffix. No interrupted design work or stale current exports.

Commands: `python scripts/build_concepts.py`, `python scripts/review_viewer.py`, `python scripts/snapshot_revision.py --verify C11`.
