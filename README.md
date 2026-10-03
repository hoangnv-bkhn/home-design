# Noi Bai house

Open the [C05 viewer](outputs/house-concepts.html) locally; it works offline. The house is wider along B and shallower along A, kitchen dining connects directly to the left/C garden, Grandpa's door moves to an inner passage, and compact separate wet rooms are studied. Selection and plot porch/parking errors are repaired.

- [C05 comparison and compromises](docs/concept-study-C05.md)
- [Ground floor](outputs/option-01-F1.svg) · [Plot](outputs/option-01-site.svg)
- [Shared-balcony F2](outputs/option-01-F2.svg) · [Shared massing](outputs/option-01-massing.svg)
- [Sister-balcony F2](outputs/option-02-F2.svg) · [Corner massing](outputs/option-02-massing.svg)
- [Altar/stair sections](outputs/option-01-section.svg) · [Selection review](outputs/viewer-selection-review.png)
- [Brief](docs/brief.md) · [Site](docs/site-investigation.md) · [Family rules](docs/preferences-and-feng-shui.md)
- [Geometry review](outputs/geometry-review.md) · [Browser review](outputs/viewer-review.md)
- [Decisions](docs/decisions.md) · [Open issues](docs/open-issues.md)

Resume from [PROJECT_STATE.md](PROJECT_STATE.md), [AGENTS.md](AGENTS.md) and [workflow](docs/agent-workflow.md). Compatible with Codex and Antigravity; project slash commands include /house-revision, /house-verify, /standards-research and /house-snapshot.

Both C05 options share F1 and F2 interiors; upper balcony position/access changes. Neither layout/footprint nor balcony is selected. **The wider footprint reduces side-yard width and narrows the altar backing buffer to 0.9 m**; review these compromises. WC/shower widths are concept studies, not verified minima. Survey, permissions, occupied circulation, daylight/ventilation, stair headroom, turning and engineering remain unresolved.

Edit [metre geometry](data/concepts.json), then rebuild/export:

```powershell
python scripts/build_concepts.py
python scripts/review_viewer.py
```

Current outputs: ten SVGs, ten matching PNGs and one focused-dining screenshot; all C05. 58 limited geometry checks and Chrome review passed. Print/PDF not tested.

Preserved local baselines: [C01](revisions/C01/manifest.json), [C02](revisions/C02/manifest.json), [C03](revisions/C03/manifest.json), [C03a](revisions/C03a/manifest.json), [C04](revisions/C04/manifest.json) and [C05](revisions/C05/manifest.json). C04 was discovered while the active workspace was C03a; its existence required the next free C05 issue. Verify with `python scripts/snapshot_revision.py --verify C05`. Extract separately; never overwrite the workspace. Historical C01 derivatives remain under outputs/obsolete-C01.
