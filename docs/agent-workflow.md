# Continuing and issuing house revisions

## Load only what the task needs

Begin with `AGENTS.md` and `PROJECT_STATE.md`. The brief, family rules and site evidence contain the design requirements. Use the local `house-revision` skill for actual concept revisions; a text correction or factual answer need not invoke the full drawing/export process.

Repository instruction discovery follows [OpenAI's AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md). The skill is stored under `.agents/skills/house-revision/SKILL.md`, the repository-local location described in [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills). Sources checked 2026-10-01. Start later sessions from the project root. If the skill is not shown in a client, follow its path from AGENTS.md; restart the session if discovery is stale.

## Sources and derivatives

| Artifact | Role / edit policy |
| --- | --- |
| `docs/brief.md`, family rules, site notes | Current owner requirements/evidence; update from new owner input |
| `data/concepts.json` | Authoritative concept geometry and assumptions, explicitly in metres |
| `src/concept-viewer.html` | Viewer source; contains design-dependent drawing details |
| `scripts/build_concepts.py` | Geometry derivation, limited checks, report and HTML generation |
| `scripts/review_viewer.py` | Optional local Chrome review and SVG/PNG export |
| `outputs/` | Rebuildable current deliverables; exclude browser profile from archives |
| `docs/concept-study-Cxx.md` | Revision-specific explanation, tradeoffs and limitations |
| `revisions/<revision>/` | Preserved sources/deliverables and checksums; never edit in place |

## Preserve, revise, review, hand off

1. Read current state and owner's latest requested change. Distinguish a change to requirements from a proposed design response. Update only the relevant requirement records and decision entries.
2. Before overwriting a review baseline, check `revisions/`. If it has not been archived, run the snapshot helper with that revision ID. An existing archive must not be overwritten.
3. For a new reviewable design, use the next free C-number (or a suffix for an erratum). Update the model's revision/date and all presentation/report references affected by the revision. Source edits alone do not select an option for the owner.
4. Modify source geometry and affected viewer logic together. Preserve IDs and explicit units. Reconcile both floors, entry/stair relationship, altar backing/projection, doors, furnishings and service locations.
5. Run the build for geometry/viewer-source changes. It creates reports and HTML; it does not regenerate standalone screenshots/SVGs. Address failures before presenting the new package.
6. When geometry or UI changed, run the existing Chrome review/export and visually inspect relevant floor/section/site images. If browser execution is blocked by the sandbox, use the environment's escalation mechanism; do not disable sandbox protections. If unavailable, state the browser-review gap and mark old exports as stale in state/notes.
7. Write a concise revision comparison: requested change, actual geometry changes, area consequences, requirement effects, unresolved compromises and checks performed. Update entry links, state and issues. Archive the new review package when complete.

Documentation-only work does not require rebuilding house outputs or advancing the design revision. Snapshot creation itself does not imply engineering or owner approval.

## Commands

```powershell
python scripts/snapshot_revision.py --verify C01
python scripts/build_concepts.py
python scripts/review_viewer.py
# At completion of an actual C02 review package:
python scripts/snapshot_revision.py --revision C02 --note "Describe this review baseline"
```

The snapshot helper requires its revision to match `data/concepts.json`, refuses overwrite and records SHA-256 hashes. Extract `snapshot.zip` into a separate directory to inspect the older self-contained package; do not extract over the active workspace. Review reports inside a snapshot retain their original evidential limits.

## Current implementation caveats — read before geometry edits

The prototype is only partly parameterized. Do not assume changing `house.width` or `house.depth` updates every consumer.

- `build_concepts.py` embeds 10 m / 100 m² envelope checks, 0.2 m wall bounds, option rotation, balcony corner samples, altar width logic and report wording. It also assumes a particular site construction from the supplied side lengths.
- `src/concept-viewer.html` contains 10 m rotation centers, room/furniture labels, summaries, site house rectangle, stair treads, altar projection, section geometry, massing, parking/gate/garden positions, and C01 text. Several are not derived from room objects. Change or parameterize all affected values when geometry changes; otherwise a plan, section and massing can disagree.
- `review_viewer.py` assumes option IDs 01/02, views site/F1/F2/section/massing, a BR-01 selection check and Chrome's Windows installation path. Adjust when those interfaces change. It creates a dedicated local browser profile; keep it out of archives and source control.
- The existing 14 geometry checks are limited. They do not validate door connectivity/swings, all furniture overlap, circulation width, site setbacks, statutory areas, stair headroom, vehicle turning, engineering or all changes to geometry.
- SVG and PNG exports are separate snapshots. `concept-preview.png` is an early overview capture, not the authoritative current floor export. Prefer `option-<id>-<view>` outputs and the working HTML.
- Static SVG axonometric is the current massing view. Three.js, structural solvers and BIM have not been installed or implemented. Introduce them only when the task calls for their capabilities.

## Evidence and review notes

For new technical/standards research, record exact designation/edition, authoritative link, access date, relevant scope/clauses and what remains unverified. No construction checks should be inferred from the C01 discussion grid. For feng shui, distinguish the family's rule from research, source quality and the proposed geometric interpretation.

Keep the final response focused on the changed design and review links. End the file handoff with enough information that a new session can resume without reconstructing chat: current revision, selection status, completed checks, pending issue IDs, stale/partial outputs if any, and the next concrete action.
