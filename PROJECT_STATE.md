# Project state — resume here

Updated: 2026-10-02. Phase: C03 owner-feedback comparison.

## Current position

- Current revision **C03a**, corrected C03 review issue; **neither balcony/layout selected**.
- Road-facing arrival and SE house/altar facing remain confirmed. C03 compares shared balcony versus sister's corner balcony, not entrance orientations.
- Latest input: rear beside B, A-side wall about 0.30 m away; TV stand; entrance around 1.90 m; compact kitchen dining, more open living/altar; bedroom balcony conditionally allowed for layering; WC basins unnecessary.
- B allowance 0.10 m is an assistant assumption. Named A/B edges govern; after retained clockwise display A is right, B above, C left.
- [Viewer](outputs/house-concepts.html) · [C03 comparison/limits](docs/concept-study-C03.md) · [C03a handoff correction](docs/concept-study-C03a.md).
- Sources: [geometry](data/concepts.json), [template](src/concept-viewer.html), [build](scripts/build_concepts.py), [browser/export](scripts/review_viewer.py).
- Requirements/evidence: [brief](docs/brief.md), [site](docs/site-investigation.md), [family rules](docs/preferences-and-feng-shui.md); tracking: [decisions](docs/decisions.md), [issues](docs/open-issues.md), [workflow](docs/agent-workflow.md).

## C03 changes and unresolved consequences

- F1 repositions toward A/B with the footprint retained. Compact kitchen dining frees the central zone for open living with a TV stand and wider entry. Five bedrooms / four separate WC-shower pairs remain; basins only in showers.
- B-side door/cantilever removed; upper layer projects toward C. Garden reached via living/front yard, not a new door into B's narrow allowance. Direct kitchen/garden connection remains L07.
- F2 sister/bedroom 5 positions change; brother enlarges toward C. Bedroom 5 rooflight is a candidate. No A/B windows assumed; kitchen daylight/extract and close-boundary performance remain priority unresolved work (L10/S02).
- Balcony 01 is shared from landing; 02 is through sister's bedroom with stronger corner layering and a privacy/shared-access tradeoff (L03). Same F1 and F2 interior room system.
- Altar solid backing/indoor buffer and exact empty upper projection retained. Final family acceptance of ceremony depth/extent remains L04.
- Stair nominal 21-riser / 2.2 m bay / 260 mm going remains an unverified reservation (L06). Entry, TV, dining and sanitary occupied/swing clearances remain L05/L11.
- Parking moves to front/A corner; shared balcony overlaps bay edge overhead. Turning, supports and clear height unresolved, along with structural, services and budget basis.

## Artifacts and checks

- [F1](outputs/option-01-F1.svg) · [Shared F2](outputs/option-01-F2.svg) · [Corner F2](outputs/option-02-F2.svg).
- [Shared plot](outputs/option-01-site.svg) · [Corner plot](outputs/option-02-site.svg) · [Sections](outputs/option-01-section.svg).
- [Shared massing](outputs/option-01-massing.svg) · [Corner massing](outputs/option-02-massing.svg). Ten current SVGs / ten matching PNGs exported.
- Build **48/48 limited checks passed**; [geometry review](outputs/geometry-review.md). Counts, footprints and metadata are not usable circulation, planning or engineering approvals.
- Chrome: both options/all five views, selection, balcony variants, TV/entry, five overlays and 390 px document overflow checked; [viewer review](outputs/viewer-review.md). PNG capture moved to standalone SVG tabs. Print/PDF not tested.
- Visual inspection of F1, both F2 plans, plot/section and massing; plot labels/export behavior corrected and review rerun.
- C02 verified before edits (32 archived files). C01/C02/C03/C03a local review snapshots verified; archives not overwritten. Snapshots preserve evidence, not owner/professional approval or off-device backup.
- Top-level option-01/02 outputs are current C03a; nested obsolete-C01 outputs are historical. No stale current exports or interrupted edits remain.

## Next action

Review occupied kitchen dining and TV/entrance use, then choose the balcony access priority. Resolve kitchen and bedroom 5 daylight/ventilation, near-boundary construction details and garden adjacency before developing doors, stair headroom and cantilever/balcony structure. Relevant issues L02–L11, S01–S04, E01/E02 and deferred budget remain open. Do not re-ask road arrival, floor naming, room counts, stair clarification or basin-in-shower intent.

C03a corrects the roadmap’s stale C01 introduction after C03 was archived; geometry and dimensions are unchanged. C03 archive remains immutable. A new reviewable design after C03a needs C04, preserving the current baseline first.

```powershell
python scripts/snapshot_revision.py --verify C03a
python scripts/build_concepts.py
python scripts/review_viewer.py
```

Read [implementation caveats](docs/agent-workflow.md) before editing geometry. Detailed dimensions live in model/revision notes rather than this handoff.
