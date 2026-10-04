# Noi Bai house

Open the [C15 viewer](outputs/house-concepts.html) locally; it works offline. Exact layout and porch detail proposed, unselected.

- [C15 changes and tradeoffs](docs/concept-study-C15.md)
- [Ground plan](outputs/option-01-F1.svg) / [Upper plan](outputs/option-01-F2.svg)
- [Slim ranch porch + low parapet](outputs/option-01-massing.svg) / [Framed ranch porch](outputs/option-02-massing.svg)
- [Site](outputs/option-01-site.svg) / [Sections and roof drainage/services](outputs/option-01-section.svg)
- [Geometry review](outputs/geometry-review.md) / [Browser review](outputs/viewer-review.md)
- [Brief](docs/brief.md) / [Site evidence](docs/site-investigation.md) / [Family rules](docs/preferences-and-feng-shui.md) / [Decisions](docs/decisions.md) / [Open issues](docs/open-issues.md)

C15 moves private wet pairs to the former court bay and shifts a larger court inward. It removes dressing screens and the sister cantilever, adds larger D/C windows, shelters the shared terrace and proposes a wider ranch porch under a low parapet roof. The sister never had a different modeled floor rise; the raised exterior cap has been removed. The assistant prefers the slim porch, not owner-selected.

Main tradeoffs: direct suite windows narrow 1.50 to 0.90 m; opaque suite doors must close for some standing-entry privacy; sister wardrobe reduces; roof tanks move above the rear suite. F1 covered 116.16 m2, F2 enclosed 108.32 m2, shared terrace 11.50 m2 and porch 7.26 m2 separately. Affordability and professional design unresolved.

Final check/export/archive status: [PROJECT_STATE.md](PROJECT_STATE.md). Resume using [AGENTS.md](AGENTS.md) and [workflow](docs/agent-workflow.md).

Commands: `python scripts/build_concepts.py`, `python scripts/review_viewer.py`, `python scripts/snapshot_revision.py --verify C15`.

Local snapshots in `revisions/` preserve proposals, not approval or off-device backup. Never overwrite an existing archive.
