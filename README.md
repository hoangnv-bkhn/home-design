# Noi Bai house

Open the [C03a viewer](outputs/house-concepts.html) locally; it works offline. C03 moves the house closer to A/B, puts compact dining in the kitchen, adds a TV stand and widens the entrance proposal. Plot/F1/F2 remain rotated 90° clockwise.

- [C03 design comparison](docs/concept-study-C03.md) · [C03a handoff correction](docs/concept-study-C03a.md)
- [Ground floor](outputs/option-01-F1.svg) · [Plot with shared balcony](outputs/option-01-site.svg)
- [Upper floor — shared balcony](outputs/option-01-F2.svg) · [Shared massing](outputs/option-01-massing.svg)
- [Upper floor — sister's corner balcony](outputs/option-02-F2.svg) · [Corner massing](outputs/option-02-massing.svg)
- [Altar/stair sections](outputs/option-01-section.svg)
- [Owner brief](docs/brief.md) · [Site evidence](docs/site-investigation.md) · [Family rules](docs/preferences-and-feng-shui.md)
- [Geometry review](outputs/geometry-review.md) · [Browser review](outputs/viewer-review.md)
- [Decisions](docs/decisions.md) · [Open issues](docs/open-issues.md)

Resume from [PROJECT_STATE.md](PROJECT_STATE.md), [AGENTS.md](AGENTS.md) and [workflow](docs/agent-workflow.md). Road arrival is confirmed; neither C03 balcony/layout is selected. Near-boundary offsets are owner design preferences, not verified permissions.

Edit [metre geometry](data/concepts.json), then regenerate:

```powershell
python scripts/build_concepts.py
python scripts/review_viewer.py
```

Both C03 options share F1. F2 balcony position/access changes per option; room layout remains the same. Top-level SVG/PNG exports show C03a; its layout is unchanged from C03. PNGs are captured from their standalone SVGs.

Preserved local baselines: [C01](revisions/C01/manifest.json), [C02](revisions/C02/manifest.json), [C03](revisions/C03/manifest.json), [C03a](revisions/C03a/manifest.json). Verify with `python scripts/snapshot_revision.py --verify C03a`. Extract archives into separate folders; never overwrite the workspace. Historical C01-only derivatives remain under `outputs/obsolete-C01/`.

Concept only: survey, permissions, daylight/ventilation, occupied circulation, stair headroom, car turning and structural design remain unresolved.
