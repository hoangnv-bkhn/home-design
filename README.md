# Noi Bai house

Open the [C06 viewer](outputs/house-concepts.html) locally; it works offline. The footprint is now **108 m², down 12.1% from C05**. Parents and brother have direct bedroom entrances, all bedrooms are smaller, sofa backs face away from the altar, and left parking preserves a garden/porch walk.

- [C06 comparison and usability review](docs/concept-study-C06.md)
- [Ground floor](outputs/option-01-F1.svg) · [Plot](outputs/option-01-site.svg)
- [Shared-balcony F2](outputs/option-01-F2.svg) · [Shared massing](outputs/option-01-massing.svg)
- [Sister-balcony F2](outputs/option-02-F2.svg) · [Corner massing](outputs/option-02-massing.svg)
- [Altar/stair sections](outputs/option-01-section.svg) · [Selection review](outputs/viewer-selection-review.png)
- [Brief](docs/brief.md) · [Site](docs/site-investigation.md) · [Family rules](docs/preferences-and-feng-shui.md)
- [Geometry review](outputs/geometry-review.md) · [Browser review](outputs/viewer-review.md)
- [Decisions](docs/decisions.md) · [Open issues](docs/open-issues.md)

Resume from [PROJECT_STATE.md](PROJECT_STATE.md), [AGENTS.md](AGENTS.md) and [workflow](docs/agent-workflow.md). AGENTS.md requires household usability in every decision. Compatible with Codex and Antigravity; local skills include /house-revision, /house-verify, /standards-research and /house-snapshot.

Both C06 options share interiors; balcony access changes. Neither layout/footprint nor balcony selected. Footprint remains 8% above target; 0.9 m altar buffer needs family review; corner balcony compromises sister's privacy/furniture. Survey, permissions, occupied use, parents daylight/ventilation, stair headroom, road turning and engineering unresolved.

Edit [metre geometry](data/concepts.json), then rebuild/export:

```powershell
python scripts/build_concepts.py
python scripts/review_viewer.py
```

Ten SVGs, ten matching PNGs and focused dining screenshot are current C06. **71 limited checks and Chrome review passed.** Print/PDF untested.

Local baselines: [C01](revisions/C01/manifest.json), [C02](revisions/C02/manifest.json), [C03](revisions/C03/manifest.json), [C03a](revisions/C03a/manifest.json), [C04](revisions/C04/manifest.json), [C05](revisions/C05/manifest.json), [C06](revisions/C06/manifest.json). Verify with `python scripts/snapshot_revision.py --verify C06`. Extract separately; never overwrite workspace. Historical derivatives remain under outputs/obsolete-C01. Archives preserve proposals, not approval or off-device backup.
