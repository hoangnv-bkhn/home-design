# Project state — resume here

Updated: 2026-10-03. **C09 buffer access, wall coordination and useful upstairs space**. Proposed, unselected; not for construction.

## Current position

Owner identifies inaccessible altar buffer, misaligned shower/Grandpa walls, excessive empty F2 space and uncertain balcony usefulness. Relayout/dimension changes expressly permitted. No layout, room use, balcony, footprint or structural system selected.

- [Viewer](outputs/house-concepts.html) · [C09 comparison](docs/concept-study-C09.md) · [F1](outputs/option-01-F1.svg) · [Deeper balcony F2](outputs/option-01-F2.svg) · [Shallower F2](outputs/option-02-F2.svg).
- Editable [metre geometry](data/concepts.json), [template](src/concept-viewer.html), [build](scripts/build_concepts.py), [browser/export](scripts/review_viewer.py).
- Requirements/evidence: [brief](docs/brief.md), [family rules](docs/preferences-and-feng-shui.md), [site](docs/site-investigation.md), [decisions D35/D36](docs/decisions.md), [issues](docs/open-issues.md), [workflow](docs/agent-workflow.md).

## Proposal and tradeoffs

- **Buffer:** C08 door existed but sofa blocked approach. Sofa moves 0.80 m toward TV, leaving **0.95 m approach**, **0.80 m inward door**, **0.90 m indoor buffer**. Solid backing stays continuous; occasional cleaning, no storage/through-route. Sofa/TV centered; front-to-stand gap **2.65 → 1.85 m**. Screen size/viewing acceptance unresolved. Open arrival stays 2.30 × 1.90 m.
- **Wall coordination:** 2.20 × 3.70 m stair moves 0.30 m. Wet-core outer wall and stair/Grandpa-sister division share **x=6.25 m** on both floors. Bedroom rectangles and wet pairs stack. Reference axes are not an engineered frame; other offsets remain. Columns, beams, openings, loads and supports unresolved, E01.
- **Rooms:** Grandpa/sister **14.80 m²**, −0.25 each. Rotated 1.40 × 2.00 m bed: entrance-side gap 0.90, wardrobe gap 0.80, foot strip 1.50, head margin 0.50 m. Ordinary 0.85 m doors retained. Common bedroom passages **1.20 → 1.00 m**. Kitchen/dining and bedroom5 **17.76 m²** each, +1.44. Parents/brother **15.64 m²**, direct exits and screened private-bath routes retained.
- **F2:** former 12.80 m² landing becomes **8.00 m² shared study + 4.40 m² / 1.10 m balcony passage + 0.40 m² open junction**. Desk/occupied chair shown; dry linen cabinet at closed end of 3.06 m² utility room. West linen/east occasional-cleaning approach strips 0.90 m. Shared study and balcony seats face toward altar side, backs away. Study use is a proposal, L16.
- **Altar:** 3.4 × 3.0 m / **10.20 m² exact empty F2 floor**, solid backing, SE facing and indoor baseline retained. No routine routes/furniture above it. Floored exclusion, not a void. C08 cultural evidence remains relevant; no new rule.
- **Balcony:** option01 recommended for review, **2.00 × 3.60 m / 7.20 m²**; option02 **1.60 × 4.40 m / 7.04 m²**. Both shared; private step-out removed. Modeled edge insets leave 1.80/1.40 m depth. Occupied bench clears 1.00 m entry reservation; sliding-door candidate. Guard, support, drainage, threshold and full porch weather cover unresolved.
- **Area/site retained:** 10.5 m A × 12.0 m B = 126.00 m² envelope minus 6.80 m² clear court = **119.20 m² covered convention each floor**, including F2 stair reservation/court lining walls. **No footprint/cost saving**, 19.2% above approximate target. Court has no F2 slab/roof. Parents/brother court windows and C stair windows retained; maintenance through parents remains a compromise. Front depth 4.40 m, parking, gates, porch and walks unchanged. Turning/levels/weather, airflow/daylight, opening rights, soil/structure and affordability unverified. No A/B openings.

## Artifacts and checks

- [Geometry](outputs/geometry-review.md): **98/98 limited checks**. Added actual buffer portal and sampled finite approach, wall alignment, stacked bedrooms, upper occupied furniture, linen access, balcony entry/bench and seating orientation. No occupied-comfort, legal, environmental or structural certification.
- [Chrome review](outputs/viewer-review.md): both options/all five views, **78 actual pointer selections**, keyboard/focus, study/bench/buffer-door metadata, retained court/windows/area tests and 390 px overflow. Ten SVGs/ten PNGs and selection capture regenerated. Print/PDF untested.
- Final visual inspection: F1, both F2, both massings, site, sections and selection capture. No stale current exports.
- **C08 54-file archive verified before editing**. Completed C09 package archived and SHA-256 verified using house-snapshot; unselected proposal. Earlier archives immutable.

## Next action

Review the shorter TV distance, 1.00 m common bedroom passage, usefulness of the shared study and deeper shared balcony. Meaningful footprint reduction needs coordinated court/wet-core/stair/altar relayout; furnishing leftover space does not reduce construction area. Then establish structural design basis and balcony/porch weather details with local team.

L02–L16, S01–S04, E01/E02, F01 and budget C01 remain open to their stated extent. Do not re-ask settled counts/floors/road/altar/stair/basin/site/outward-door inputs. C09 archived; next design issue **C10** or distinct erratum suffix. No owner/professional approval implied.

Commands: `python scripts/build_concepts.py`, `python scripts/review_viewer.py`, `python scripts/snapshot_revision.py --verify C09`.

