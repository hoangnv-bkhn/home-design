# Continuing and issuing house revisions

## Load only what the task needs

Begin with `AGENTS.md` and `PROJECT_STATE.md`. The brief, family rules and site evidence contain the design requirements. Use the local `house-revision` skill for actual concept revisions; a text correction or factual answer need not invoke the full drawing/export process.

Repository instruction discovery follows [OpenAI's AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [Google Antigravity's Customization System](https://antigravity.google/docs/skills). Both environments read `AGENTS.md` at the project root as directory rules and discover skills under `.agents/skills/<name>/SKILL.md`.

Available project skills (runbooks and slash commands):
- `.agents/skills/house-revision/SKILL.md` (`/house-revision`): Concept iteration, geometry editing in `data/concepts.json`, viewer and report rebuilds.
- `.agents/skills/house-verify/SKILL.md` (`/house-verify`): Health check (original 48, 58 in C05, 71 in C06, headless Chrome and snapshot verification). Read the actual active report; older skill counts describe earlier scope.
- `.agents/skills/standards-research/SKILL.md` (`/standards-research`): Vietnamese building codes (QCVN 01, QCVN 06, TCVN 9411) and feng shui cultural research with mandatory citations.
- `.agents/skills/house-snapshot/SKILL.md` (`/house-snapshot`): Archiving and verifying immutable review baselines in `revisions/`.

In Antigravity, subagents can be leveraged via `invoke_subagent` (e.g. `research` subagent for deep code/standards lookups without cluttering main conversation context). Start later sessions from the project root. If a skill is not discovered automatically, follow its path from `AGENTS.md`.

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
# When issuing a new revision, use its matching unused ID (C06 is already archived):
python scripts/snapshot_revision.py --verify C06
```

The snapshot helper requires its revision to match `data/concepts.json`, refuses overwrite and records SHA-256 hashes. Extract `snapshot.zip` into a separate directory to inspect the older self-contained package; do not extract over the active workspace. Review reports inside a snapshot retain their original evidential limits.

## Current implementation caveats — read before geometry edits

C06 keeps metre geometry and two balcony variants; F1/F2 envelopes now align at 9.0 × 12.0 m, without a C extension. Viewer headline and some annotation/facade positions remain revision-specific. C05 verified before C06; all archives preserved. C06 archived; next design review C07 or distinct erratum suffix. Apply AGENTS.md usability-first principles during every decision.

- Source coordinates remain +x toward road/SE, +y along B toward C. Clockwise plot/F1/F2 display rotation is separate; B appears above, A right, C left. Never relabel edges or change compass to match casual left/right descriptions.
- Owner wants about 0.30 m at A and rear next to B. B=0.10 m is an **assumption**, not lawful setback. No A/B opening assumed. C02 rear door/projection superseded; C06 keeps direct kitchen exit on C and removes C05 upper C extension.
- `options[].balcony` defines each variant's rectangle, door, access-room ID, note and route. `floorData()` applies these overrides to the base F2 room/door list; the BAL-01 ID remains stable. Build checks/reports each variant and derives `derived.balconies`. F1 is common to both.
- Floor envelopes, gross areas, stair, fixtures, altar width/projection and wet stacking are parameterized. The altar width is local y; its x dimension is depth. Unsupported physical option rotations are rejected.
- KIT-01 / DIN-01 are adjacent open rectangles with a 0.10 m strip. C06 named zones 16.83 m² versus 17.34 m² bay; 0.51 m² junction difference. Do not double-count. Table orientation and six `dining_chairs[].rect` footprints are explicit; avoid renderer-invented chair geometry. Garden opening is on DIN portion of combined bay.
- `F1.tv`/furniture define sofa facing (`seat_facing`), rear line/arrow and TV. Main opening 1.90 m. `door_operations` provides inward bedroom/main leaves and unresolved sanitary sliding candidates. `clearance_reservations` and route bands specify limited checks; do not infer comfort, full privacy or finished clearances from them.
- F2 rooflight is a candidate above bedroom 5, not proven daylight/ventilation. Kitchen daylight/extract and actual service shafts remain unresolved.
- C06 preserves 0.90 m buffer, 1.0/1.4 m wet widths, 21-riser stair and all IDs. Private compartments rotate: entry axis now v, shared remains h; `door_joins()` handles both. Bedroom IDs identify primary doors, `BR-01-BATH` / `BR-03-BATH` internal bath doors. Private public doors EN-01/03 removed; screens enclose passages on common side. Avoid restoring C05 coordinates.
- Site source has left/C bay, `vehicle_body`, separate `pedestrian_gate`, `vehicle_path` axis and `pedestrian_reservations`. Dashed paths/axis are not swept-path analysis. Section/backing/porch derive from source, but plot text anchors remain revision-specific.
- 71 checks retain original 48/C05 additions plus 13 C06 regressions: direct bedroom connections, removed private public entry, sofa rear/altar, TV/door, conservative leaf bounding boxes, chairs, clearance rectangles, 0.80 m sampled furniture bands, left bay and walking strips. They do not validate full wall/portal route connectivity, all door interactions, occupied movement, standards, daylight, headroom, turning or structure.
- Browser reads active options, exports five views each and tests 66 real room clicks/focus/keyboard, balcony notes/areas, TV/entry, direct suite exits/leaf/sofa metadata and overlays. PNGs use standalone SVG tabs. Focused dining capture records selection. Chrome remains Windows-specific; print/PDF untested.
- Top-level option-01/02 outputs are C06. Nested obsolete-C01/profile caches excluded from archive. All earlier archives including C05 preserved; never overwrite them.
- Static SVG remains the renderer for plans/sections/massing. No new dependency, BIM or engineering solver was added. Volumes, rooflight, openings, guards and facade frame are schematic.

## Evidence and review notes

For new technical/standards research, record exact designation/edition, authoritative link, access date, relevant scope/clauses and what remains unverified. No construction checks should be inferred from the C01 discussion grid. For feng shui, distinguish the family's rule from research, source quality and the proposed geometric interpretation.

Keep the final response focused on the changed design and review links. End the file handoff with enough information that a new session can resume without reconstructing chat: current revision, selection status, completed checks, pending issue IDs, stale/partial outputs if any, and the next concrete action.
