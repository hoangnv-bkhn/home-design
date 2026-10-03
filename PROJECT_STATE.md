# Project state — resume here

Updated: 2026-10-03. **C10 corner suites, compact spare bedroom and recessed loggia**. Proposed, unselected; not for construction.

## Current position

Owner confirms Bedroom5 is spare and may shrink; upper exclusion only needs approximately 1.20 m altar depth, not whole worship room. Requests smaller footprint, kitchen/wet/court/corner-suite study, better exterior layering and timber partition left of altar. Relayout permitted; no design or structural system selected. D37/D38 record requirement/proposal distinction.

- [Viewer](outputs/house-concepts.html) · [C10 comparison](docs/concept-study-C10.md) · [F1](outputs/option-01-F1.svg) · [F2 / 1.20 m projection](outputs/option-01-F2.svg) · [F2 / 0.60 m projection](outputs/option-02-F2.svg) · [Massing](outputs/option-02-massing.svg).
- Editable metre geometry: [data](data/concepts.json), [template](src/concept-viewer.html), [build](scripts/build_concepts.py), [browser/export](scripts/review_viewer.py).
- Requirements/evidence: [brief](docs/brief.md), [family rules](docs/preferences-and-feng-shui.md), [site](docs/site-investigation.md), [decisions](docs/decisions.md), [issues](docs/open-issues.md), [workflow](docs/agent-workflow.md).

## Proposal and material tradeoffs

- Ground **115.70 m²**, down 3.50 from 119.20. Envelope 10.50 m A ×11.40 m B /119.70 minus 4.00 m² court. Reduction 0.60 m along B gains C-side land; front depth along A remains 4.40 m. Still 15.70 m² above approximate target. Model/site offsets remain unverified.
- Upper enclosed convention **111.65 m²**, subtracting 4.05 m² loggia notch; includes stair reservation. Balcony separately 6.50/5.00 m², including its recessed portion. Loggia/canopy still require construction; no cost/slab-area saving claimed. No enclosed room cantilever.
- Parents/brother rear corner **13.60 m²**; spare **12.58 m²** aligns right wall x 3.65 with brother/kitchen. Grandpa/sister 14.80 unchanged. Wet/stair/Grandpa-sister axis 6.25 retained; other offsets remain. Axes are not designed beams/columns.
- Parents/brother ordinary 0.90 m doors reach common 1.30 m court passage/lobby, separate from screened private bath routes. Rotated bed leaves 0.80 m A side, 1.40 m court side, 0.80 m wardrobe-foot gap. Storage clears 1.50 m court windows. Four separate WC/shower pairs, shower basins and no WC basins retained.
- **Court2 ×2 m** between suite and kitchen; common 0.80 m cleaning door, no need to enter parents room. Smaller court is main light/air compromise. Shared wet pair stays stacked beside kitchen/common junction, rather than moving into kitchen. No direct shared-bath court window; extract/duct routes unresolved. No A/B windows.
- Kitchen/dining named 13.42 m² +0.37 open join; excludes 2.20 m² common lobby. Six compact chairs, 0.70 ×1.60 m table, 0.90 m working aisle/garden approach. Chair withdrawal/appliances/occupied comfort unresolved.
- Ground worship 3.40 ×3.00 m retained; altar strip/furniture 1.20 m deep and upper empty floor **4.08 m²**, superseding full 10.20 m² interpretation. Forward study 5.78 m², linen, 1.10 m landing and 1.30 m loggia access. No regular use over excluded strip.
- Timber screen on altar's displayed left/C side: proposed 1.80 m length, 80 mm thickness, 2.20 m height; 1.20 m front entry. Solid backing/indoor 0.90 m buffer remain; 0.95 m sofa-back approach and 0.80 m inward buffer door. Screen density/fixings/heat clearances unresolved. Sofa 2.00 m, TV gap 1.85 m; open arrival 2.10 ×1.90 m.
- Loggia recessed 1.40 m clear; compare 1.20 m outward projection (6.50 m²) and 0.60 m (5.00 m²). **Option02 assistant preference only** for compact exterior. Separate 2.30 ×2.50 m porch canopy. No additional bedroom projection; sister front projection only a discussed later alternative. Guards, supports, thresholds, weather/drainage unverified.

## Artifacts and checks

- [Geometry](outputs/geometry-review.md): **107/107 limited checks**. New checks cover actual door/sweep anchors, unobstructed court-window strips, bedroom/common exit topology, wall alignment, smaller exclusion, screen/front route and upper recess. Not a usability, daylight, code or engineering certification.
- [Chrome review](outputs/viewer-review.md): both options/all five views, **90 actual pointer selections**, keyboard/focus, overlays, dynamic ground area, screen/windows/doors, 390 px overflow. Ten SVGs/PNGs and selection capture regenerated. Print/PDF untested. Browser required environment escalation after sandbox connection resets.
- Visual inspection: final F1/F2, both balconies/massings, site, sections and selection capture. Wardrobe/window conflict and obsolete court-door swing corrected; exports current.
- C09 **55-file archive verified before editing**. C10 final package archived and SHA-256 verified using house-snapshot; archive preserves proposal, not approval. Existing archives immutable.

## Next action

Review smaller court/daylight and compact kitchen first, then spare 12.58 m², timber screen and loggia depth. If court performance is inadequate, return area or relayout rather than retaining savings at the expense of sleeping-room usability. Engineer to establish structural basis across x 3.65/x 6.25 reference lines, court/stair/recess edges and canopy; no member sizes selected.

L02–L16, S01–S04, E01/E02, F01 and budget C01 remain open to stated extent. Do not reopen confirmed spare use, limited altar strip, counts/floors/road/stair/basins/site rules. Next design issue **C11** or distinct erratum suffix. No interrupted geometry work or stale current exports.

Commands: `python scripts/build_concepts.py`, `python scripts/review_viewer.py`, `python scripts/snapshot_revision.py --verify C10`.
