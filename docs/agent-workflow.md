# Continuing and issuing house revisions

## Load only what the task needs

Begin with `AGENTS.md` and `PROJECT_STATE.md`. The brief, family rules and site evidence contain the design requirements. Use the local `house-revision` skill for actual concept revisions; a text correction or factual answer need not invoke the full drawing/export process.

Repository instruction discovery follows [OpenAI's AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [Google Antigravity's Customization System](https://antigravity.google/docs/skills). Both environments read `AGENTS.md` at the project root as directory rules and discover skills under `.agents/skills/<name>/SKILL.md`.

Available project skills (runbooks and slash commands):
- `.agents/skills/house-revision/SKILL.md` (`/house-revision`): Concept iteration, geometry editing in `data/concepts.json`, viewer and report rebuilds.
- `.agents/skills/house-verify/SKILL.md` (`/house-verify`): Non-destructive health check (48 build checks, headless Chrome review, snapshot verification).
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
# At completion of a new C03 review package (refuses an existing archive):
python scripts/snapshot_revision.py --revision C03 --note "Describe this review baseline"
```

The snapshot helper requires its revision to match `data/concepts.json`, refuses overwrite and records SHA-256 hashes. Extract `snapshot.zip` into a separate directory to inspect the older self-contained package; do not extract over the active workspace. Review reports inside a snapshot retain their original evidential limits.

## Current implementation caveats — read before geometry edits

C03 keeps metre geometry, explicit per-floor envelopes and two balcony-access variants. Viewer overview prose and some annotation/facade positions remain revision-specific.

- Source coordinates remain +x toward road/SE, +y along B toward C. Clockwise plot/F1/F2 display rotation is separate; B appears above, A right, C left. Never relabel edges or change compass to match casual left/right descriptions.
- Owner wants about 0.30 m at A and rear next to B. B=0.10 m is a **model assumption**, not owner exact dimension or lawful boundary construction. No A/B door/window is assumed. C02 rear projection/door is superseded by the C-side upper projection and front-yard garden route.
- `options[].balcony` defines each variant's rectangle, door, access-room ID, note and route. `floorData()` applies these overrides to the base F2 room/door list; the BAL-01 ID remains stable. Build checks/reports each variant and derives `derived.balconies`. F1 is common to both.
- Floor envelopes, gross areas, stair, fixtures, altar width/projection and wet stacking are parameterized. The altar width is local y; its x dimension is depth. Unsupported physical option rotations are rejected.
- Compact kitchen/dining is represented by adjacent open KIT-01 / DIN-01 rectangles with a 0.10 m junction strip. Their sum differs from the combined bay by 0.29 m². Do not add their bay area again to room totals.
- `F1.tv` and furniture define the TV stand/sofa proposal. Main entry width is 1.90 m. No leaf/swing, occupied clearance or TV-size recommendation is encoded.
- F2 rooflight is a candidate above bedroom 5, not proven daylight/ventilation. Kitchen daylight/extract and actual service shafts remain unresolved.
- Viewer summaries, section/facade details, review questions, site annotations and some requirement-check values remain C03-specific. Reconcile them with future geometry rather than editing JSON alone.
- The 48 checks are limited to counts, zones/envelopes, fixtures, stacking, altar, nominal stair arithmetic, both balcony access/routes, A/B allowances, entrance and selected furniture/site relationships. They do not validate all doors, use clearances, headroom, setbacks, daylight, turning or structure.
- Browser review reads active options, tests per-option balcony notes/areas plus displayed TV/entry, and exports five views per option. PNGs are captured from their standalone SVGs in separate blank-origin tabs; this avoids viewer scroll/reflow clipping. Chrome path remains Windows-specific. Print/PDF output is not tested.
- Current top-level option-01 and option-02 outputs are C03. Nested `outputs/obsolete-C01/` remains historical and is excluded by snapshot helper, along with browser profiles. C01/C02 verified archives preserve the originals.
- Static SVG remains the renderer for plans/sections/massing. No new dependency, BIM or engineering solver was added. Volumes, rooflight, openings, guards and facade frame are schematic.

## Evidence and review notes

For new technical/standards research, record exact designation/edition, authoritative link, access date, relevant scope/clauses and what remains unverified. No construction checks should be inferred from the C01 discussion grid. For feng shui, distinguish the family's rule from research, source quality and the proposed geometric interpretation.

Keep the final response focused on the changed design and review links. End the file handoff with enough information that a new session can resume without reconstructing chat: current revision, selection status, completed checks, pending issue IDs, stale/partial outputs if any, and the next concrete action.
