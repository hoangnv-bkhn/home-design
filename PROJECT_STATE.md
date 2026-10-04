# Project state - resume here

Updated: 2026-10-04. **C15 inward court, edge private baths, sheltered terrace and ranch porch/low parapet**. Proposed, unselected; not for construction.

## Current position

Owner dislikes sister cantilever/enclosed exterior, central private baths and dressing screen; prefers sheltered terrace, requests ranch porch/parapet exploration and ceiling-height clarification. D47 records owner directions; D48 records proposals. Counts, suite minimum, separate WC/shower/basin rules, altar backing/empty upper strip and seated-back rule retained.

- [Viewer](outputs/house-concepts.html) / [C15 comparison](docs/concept-study-C15.md)
- [F1](outputs/option-01-F1.svg) / [F2](outputs/option-01-F2.svg) / [Site](outputs/option-01-site.svg) / [Sections and roof](outputs/option-01-section.svg)
- [Slim ranch porch](outputs/option-01-massing.svg) / [Framed ranch porch](outputs/option-02-massing.svg). Both fully shelter shared terrace. Assistant favors slim Option 01; not owner selection.
- Sources: [metre model](data/concepts.json), [template](src/concept-viewer.html), [build](scripts/build_concepts.py), [browser/export](scripts/review_viewer.py).
- Requirements: [brief](docs/brief.md), [family](docs/preferences-and-feng-shui.md), [site](docs/site-investigation.md), [decisions](docs/decisions.md), [issues](docs/open-issues.md), [workflow](docs/agent-workflow.md).

## Review consequences

- Private stacked WC/shower pairs move to former court near A. Court moves inward/grows 4.80 to 6.96 m2. Suite sleeping minimum and ordinary exits retained. Direct suite court windows narrow 1.50 to 0.90 m; supplementary passage glass 1.20 m. Gallery loses direct court glass, receives borrowed light. Daylight/air/sky and drainage unverified.
- Freestanding dressing screens removed; private passage 1.00 m deep, no new dressing storage. Beds shift 0.50 m toward B. Bed sightlines blocked; 72/324 ordinary-entry rays remain visible with all doors open. Opaque 0.80 m suite sliding doors must close for those views; modeled open leaves fit, hardware/occupied privacy acceptance unresolved.
- Sister returns to 14.80 m2, no cantilever/private balcony; larger D/C windows, wardrobe 2.50 to 1.80 m. Grandpa front window widened; glazed timber entrance panels proposed. Same 3.30 m floor rise already existed in C14: its 6.78 m exterior cap caused the taller appearance. C15 common roof 6.60/parapet 6.95 m; actual clear ceilings/build-up unspecified.
- Shared terrace 11.50 m2 fully sheltered in both options. Ranch porch frontage 2.20 to 3.30 m, depth 2.20 unchanged; canopy 3.00x4.00, existing D projection and steps retained. Garden path leads to front steps, not up the side of the raised porch. Levels, supports/drainage and car maneuvers unresolved.
- Equipment screen moves above rear suite roof to avoid new court. Top 8.15 m assumed, hatch/collector retained. Tank loading/noise, framing, solar/horizon, protected maintenance/replacement access, waterproofing/thermal design, outlets/overflow and airport height remain open. Low parapet is not a guard.
- F1 covered 116.16 m2 (-2.16), F2 actual enclosed 108.32 (-4.71), shared terrace 11.50 separately, porch 7.26 separately. Main envelope 10.80x11.40 unchanged. Affordability unassessed; main footprint remains 16.16 above approximate target before porch.

## Artifacts and checks

- Geometry build: 137/137 limited checks. Privacy limitation is explicitly reported, not counted as full privacy approval.
- Chrome review passed: both options/all five views, 88 actual room selections, keyboard/focus/overlays/390 px overflow and model/view metadata. Ten SVG/PNG drawing pairs plus selection capture regenerated. Both exteriors have zero depth-order cycles. Print/PDF untested.
- Visual review covers F1/F2, site, both exteriors, section/roof sheet and selection. Corrected stale F2 projection label, site-title overlap and two-tread site drawing; final glazed entry, wider Grandpa window and suite sliding leaves inspected. Local links and owner-direction consistency checked; git diff whitespace check passed.
- C14 archive verified before edits: 61 files. [C15 archive](revisions/C15/manifest.json) created and independently checksum-verified: **62 files**. Frozen notes record readiness immediately before archival; this active handoff records completion. Archives preserve proposals, not approval. Never overwrite existing snapshots.

## Next action

Review exterior/porch alongside narrower suite windows, door-dependent bathroom privacy, smaller sister wardrobe and roof tank location. Resolve these compromises before fixing layout; then neighbor rights/sky, structural/services/roof basis, actual levels and budget. Next design issue **C16**, or distinct C15 erratum; preserve C15. No interrupted work or stale current exports.

L02-L16, S01-S04, E01/E02, F01 and budget C01 remain open to stated extent. No new construction approval or environmental/legal/engineering certification.

Commands: `python scripts/build_concepts.py`, `python scripts/review_viewer.py`, `python scripts/snapshot_revision.py --verify C15`.
