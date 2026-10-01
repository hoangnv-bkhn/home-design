# Noi Bai house

Start with [the interactive concept viewer](outputs/house-concepts.html). Open the file in a browser; no server or installation is needed.

For a later AI session, start in this project folder and read [PROJECT_STATE.md](PROJECT_STATE.md). [AGENTS.md](AGENTS.md) routes the agent to the project rules, requirements and local revision skill. See [the revision workflow](docs/agent-workflow.md) for archive/rebuild steps and prototype limitations.

Example continuation: “Read PROJECT_STATE.md and use the house-revision skill to develop C02 from my feedback.” C01 is retained in `revisions/C01/`; verify it with `python scripts/snapshot_revision.py --verify C01`.

- [Concept C01 comparison and limitations](docs/concept-study-C01.md)
- [Owner brief](docs/brief.md)
- [Roadmap](HOUSE_BUILDING_PLAN.md)
- [Site evidence](docs/site-investigation.md)
- [Family preferences and feng shui](docs/preferences-and-feng-shui.md)
- [Geometry checks](outputs/geometry-review.md)
- [Browser review](outputs/viewer-review.md)

Editable dimensions and room definitions are in [data/concepts.json](data/concepts.json), explicitly in metres. Generate the viewer and report with:

```powershell
python scripts/build_concepts.py
```

Standalone drawings are available as `outputs/option-01-F1.svg`, `option-01-F2.svg`, `option-02-F1.svg`, and `option-02-F2.svg`, with matching PNGs. These snapshots must be regenerated after changes using the optional local Chrome review/export script.

All drawings are conceptual. The plot is inferred from approximate lengths; room fit, openings, circulation, structure and services still require development and review.
