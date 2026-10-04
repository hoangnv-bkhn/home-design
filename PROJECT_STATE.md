# Project state — resume here

Updated: 2026-10-04. **C14 compact bay, lateral-window candidates and C-side bedroom/roof/porch study**. Proposed, unselected; not for construction.

## Current position

Owner requests stair glazing clear of possible beam, lateral altar windows, 2.40 m bay/reduced depth, more open dressing, A-side bedroom-window study, slightly right entrance, side sister projection/private balcony, 1.00 m shared projection, rooftop water/solar provision and another porch. D45 records directions; D46 records proposals. Counts, suite minimum, separate sanitary/basin rules, solid indoor backing/empty upper altar strip and seated-back rule retained.

- [Viewer](outputs/house-concepts.html) · [C14 comparison](docs/concept-study-C14.md) · [window/roof evidence](docs/windows-roof-C14.md).
- [F1](outputs/option-01-F1.svg) · [F2](outputs/option-01-F2.svg) · [Site](outputs/option-01-site.svg) · [Sections/roof/private balcony comparison](outputs/option-02-section.svg).
- [Blade canopy + pergola](outputs/option-01-massing.svg) · [Portal porch + sheltered terrace](outputs/option-02-massing.svg). Assistant favors portal/shelter + enclosed side extension; owner unselected.
- Sources: [metre model](data/concepts.json), [template](src/concept-viewer.html), [build](scripts/build_concepts.py), [browser/export](scripts/review_viewer.py).
- Requirements/evidence: [brief](docs/brief.md), [family](docs/preferences-and-feng-shui.md), [site](docs/site-investigation.md), [decisions](docs/decisions.md), [issues](docs/open-issues.md), [workflow](docs/agent-workflow.md).

## Review consequences

- Court/stair/private wet bay **2.50 → 2.40 m**; ground depth along A **10.90 → 10.80 m**, B width 11.40 retained. Shared showers were already 1.30 m. Private showers reduce 1.40 → 1.30 m; stair central reservation 0.30 → 0.20 m, nominal flights retained. Actual finished rails/widths/basin/splash use unresolved.
- Short dressing screen moves **0.45 m towards wet doors**, opening bedroom approach; sampled privacy/0.80 m routes pass. Main entry moves **0.30 m right** with porch/leaves/routes; compact 0.70 m tea table/0.60 m chair keep arrival space. Exact furnishings and all-position privacy need review.
- Stair windows now separate, below/above illustrative z3.00–3.50 m floor-edge band. Lower sill low relative to half landing: guard/fixed glazing/vent reach unresolved; no actual beam designed. Road-facing altar window removed; **conditional A-side** altar/parents/brother candidates shown pink and excluded from ordinary schedule. Placement direction settled; A interpretation/rights/sky conditional. Court windows remain primary suite light/ventilation.
- Sister **0.60 m extension moves to own C garden**, front aligns with F1. Shared terrace projection **0.60 → 1.00 m**. Separate section diagram compares 1.00 m private step-out replacing extension; excluded from active plan/areas, door/storage needs development if preferred.
- Roof screen over wet core reserves separate cold/hot storage, exposed collector and stair hatch/maintenance route. Top **8.15 m assumed**; no product/capacity/system selected. Safe access, replacement, roof loads/support, self-shading/solar orientation, drainage and airport height applicability unresolved. Blade/portal porch options use same coverage; portal short side slats clear limited garden/arrival bands.
- F1 covered **118.32 m² (−0.94)**; actual F2 enclosed **113.03 (−0.76)**; shared terrace **11.50 (+1.84)** separately. F2 10.80 × 12.00 bounding rectangle is not area. Model front reference **4.10 m**. Ground still exceeds approximate target by 18.32 m²; affordability unassessed.

## Artifacts and checks

- [Geometry](outputs/geometry-review.md): **136/136 limited checks**; no architectural/legal/environmental/engineering certification.
- [Chrome](outputs/viewer-review.md): both options/all five views, **88 actual pointer selections**, keyboard/focus/overlays/390 px overflow, conditional-window/stair/beam/roof/porch metadata. Ten SVG/PNG exports and selection image current; both exteriors zero depth-order cycles. Print/PDF untested.
- Final visual review covers F1/F2, both exteriors, site, sections and selection. Roof service diagram uses source positions; collector/porch/stair labels corrected before final export. No new library/renderer.
- **C13 archive: 59 files verified before changes**, immutable. [C14 review archive](revisions/C14/manifest.json) issued and checksum-verified: **61 files**. Its frozen handoff records the pre-archive close-out step; this active handoff records completion. Archives preserve proposals, not approval.

## Next action

Review compact shower/dressing/entry furniture and the portal/shelter/C-side volume together. Then resolve neighbor rights/sky and actual stair framing/low-sill protection, rooftop equipment/support/access/solar conditions, measured levels and budget before fixing layout. Next new design issue **C15**, or distinct C14 erratum; preserve C14 before further design changes.

L02–L16, S01–S04, E01/E02, F01 and budget C01 remain open to stated extent. No repeat briefing needed for settled counts/suite minimum/spare use/altar strip/stair flexibility. No interrupted design work or stale current exports.

Commands: `python scripts/build_concepts.py`, `python scripts/review_viewer.py`, `python scripts/snapshot_revision.py --verify C14`.
