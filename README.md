# Noi Bai house

Open the [C07 viewer](outputs/house-concepts.html) locally; it works offline. The TV is centered on the sofa, guests enter empty arrival space, and main doors open outward onto a deeper porch. Both 108 m² enclosed floors are retained. Grandpa's room is smaller; daylight and balcony options are proposals.

- [C07 changes and tradeoffs](docs/concept-study-C07.md) · [Daylight/envelope evidence](docs/daylight-and-envelope-C07.md)
- [F1](outputs/option-01-F1.svg) · [Plot](outputs/option-01-site.svg) · [Sections including daylight tubes](outputs/option-01-section.svg)
- [Shared F2](outputs/option-01-F2.svg) · [Shared frame massing](outputs/option-01-massing.svg)
- [Shared + private F2](outputs/option-02-F2.svg) · [Additional private layer](outputs/option-02-massing.svg)
- [Geometry review](outputs/geometry-review.md) · [Browser review](outputs/viewer-review.md) · [Selection capture](outputs/viewer-selection-review.png)
- [Brief](docs/brief.md) · [Site](docs/site-investigation.md) · [Family rules](docs/preferences-and-feng-shui.md) · [Decisions](docs/decisions.md) · [Open issues](docs/open-issues.md)

Resume from [PROJECT_STATE.md](PROJECT_STATE.md), [AGENTS.md](AGENTS.md) and [workflow](docs/agent-workflow.md). Usability-first decision making remains required. Local skills: /house-revision, /house-verify, /standards-research and /house-snapshot.

Neither C07 layout nor balcony is selected. Both comparisons retain independent shared balcony access; one adds a shallow private sister step-out. Grandpa loses 3.08 m² (now 10.36 m²) and has a 0.40 m tighter bed side. Parents roof tubes are daylight candidates only, with no view/ventilation; upper tube boxes deduct 0.32 m². No A/B windows or permissions assumed. Footprint/budget, occupied use, daylight/noise/shading, weather, stair headroom, turning and engineering remain open.

Edit [metre geometry](data/concepts.json), then rebuild/export:

```powershell
python scripts/build_concepts.py
python scripts/review_viewer.py
```

Ten SVGs/ten PNGs and focused capture are current C07. **83 limited build checks and Chrome review passed**; 67 actual room clicks. Print/PDF untested.

Local snapshots: [C01](revisions/C01/manifest.json), [C02](revisions/C02/manifest.json), [C03](revisions/C03/manifest.json), [C03a](revisions/C03a/manifest.json), [C04](revisions/C04/manifest.json), [C05](revisions/C05/manifest.json), [C06](revisions/C06/manifest.json), [C07](revisions/C07/manifest.json). Verify with `python scripts/snapshot_revision.py --verify C07`. Extract separately; never overwrite the workspace. Archives preserve proposals, not approval or off-device backup.
