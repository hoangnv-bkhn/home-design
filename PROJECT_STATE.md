# Project state — resume here

Updated: 2026-10-01. Phase: initial concept comparison.

## Current position

- Current design: **C01**, presented for owner review; **no option selected**.
- Option 01: road-facing arrival. Option 02: the same layout rotated toward the garden, with window adjustments. Assistant preference for 02 is a proposal only.
- Current entry: [concept viewer](outputs/house-concepts.html). Details: [C01 notes](docs/concept-study-C01.md).
- Sources: [geometry](data/concepts.json), [viewer template](src/concept-viewer.html), [build](scripts/build_concepts.py).
- Context: [brief](docs/brief.md), [site](docs/site-investigation.md), [family rules](docs/preferences-and-feng-shui.md), [roadmap](HOUSE_BUILDING_PLAN.md).
- Tracking: [decisions](docs/decisions.md), [open issues](docs/open-issues.md), [revision workflow](docs/agent-workflow.md).
- Handoff setup completed in this session: project instructions, house-revision skill, state/decision/issue records and an archive helper. House geometry was not revised during this setup.

## Existing evidence and checks

- C01 build reported 14/14 limited geometry checks passing; see [report](outputs/geometry-review.md).
- Both options/all five viewer views were exercised in Chrome, room selection and overlays checked, and 390 px layout checked for document overflow; see [viewer report](outputs/viewer-review.md).
- Floor previews were visually inspected and furniture revised to improve bedroom/ balcony access. Door swings, actual clearances, stair headroom and car turning remain unchecked design issues.
- Boundary geometry and 243.78 m² model area are inferred. No measured survey, geotechnical report, confirmed planning limits, adopted structural calculations or construction issue exists.
- C01 is preserved in `revisions/C01/` with a manifest and archive. Use the snapshot verifier before relying on that baseline. A Git repository is now initialized on local branch `master`; it has no commits or remote configured yet. The repository and snapshots remain local history, not an off-device backup.
- Agent setup validation: skill frontmatter/name/description and referenced local workflow files/links checked directly. The bundled skill validator could not run because PyYAML is absent; no dependency was installed. No house geometry or browser rerun was needed for this instructions-only setup.

## Next action

Continue with the owner's requested revision. If asked simply to continue, review issues L01–L05 and propose a focused refinement of the current comparison; keep both orientations available until the owner selects one. Start a new design revision only when geometry/design actually changes.

The most useful owner choices are entrance orientation, whether approximately 16 m² living/dining feels sufficient, balcony access through the sister's room versus shared access, and acceptance of the reserved altar zones. Do not repeat questions about already confirmed bedrooms, boundary lengths, 100 m² footprint, parking, dining or upstairs-empty-space intent.

## Resume commands

```powershell
python scripts/snapshot_revision.py --verify C01
# After changing concept source or renderer:
python scripts/build_concepts.py
# When geometry/UI changes justify browser/export review:
python scripts/review_viewer.py
```

Before using these for a different footprint or revision, read the implementation caveats in `docs/agent-workflow.md`.

## Handoff maintenance

At the end of substantial work update this file with: current revision and selected-option status, relevant artifacts, checks actually run, unresolved issue IDs, concrete next step, and any interrupted edits or stale outputs. Keep detailed dimensions in the brief/model and decisions in their register.
