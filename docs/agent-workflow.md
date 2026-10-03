# Continuing and issuing house revisions

## Load only what the task needs

Begin with `AGENTS.md` and `PROJECT_STATE.md`. The brief, family rules and site evidence contain the design requirements. Use the local `house-revision` skill for actual concept revisions; a text correction or factual answer need not invoke the full drawing/export process.

Repository instruction discovery follows [OpenAI's AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [Google Antigravity's Customization System](https://antigravity.google/docs/skills). Both environments read `AGENTS.md` at the project root as directory rules and discover skills under `.agents/skills/<name>/SKILL.md`.

Available project skills (runbooks and slash commands):
- `.agents/skills/house-revision/SKILL.md` (`/house-revision`): Concept iteration, geometry editing in `data/concepts.json`, viewer and report rebuilds.
- `.agents/skills/house-verify/SKILL.md` (`/house-verify`): Health check (original 48, 58 in C05, 71 in C06, 83 in C07, 89 in C08, headless Chrome and snapshot verification). Read the actual active report; older skill counts describe earlier scope.
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
# C08 is archived; next design issue C09 or a distinct erratum suffix:
python scripts/snapshot_revision.py --verify C08
```

The snapshot helper requires its revision to match `data/concepts.json`, refuses overwrite and records SHA-256 hashes. Extract `snapshot.zip` into a separate directory to inspect the older self-contained package; do not extract over the active workspace. Review reports inside a snapshot retain their original evidential limits.

## Current implementation caveats — read before geometry edits

Current **C08** changes, superseding conflicting C07 literals below:
- Outer envelope 10.5 × 12.0 m, 126.00 m²; `house.courtyard` / COURT-01/02 are aligned 3.4 × 2.0 m clear open court. `derived.gross` subtracts 6.80 m² to report covered area 119.20 m²; `derived.envelope_area` retains 126.00. `outside_f1` excludes the complete outer envelope, with court recorded separately. Court lining/walls remain included; F2 includes stair reservation. Never count COURT-02 as a floor or altar EMPTY-ALT as a void.
- ALT-01/EMPTY-ALT now 3.4 × 3.0 m / 10.20 m²; backing/buffer retained. BR-02/04 now 15.05 m² with rotated bed; header, section and actual furniture orientation coordinated.
- Parents/brother now share corresponding court-facing geometry, BR-05 moves to C. Both stacked sanitary pairs relocated. Preserve primary bedroom doors independent of internal bathroom doors, privacy screen and the two passage portals. Private bath links 0.80 m, ordinary suite doors 0.90 m.
- Main stair branch HALL-MAIN/HALL-06 is 1.00 m; GP-LOBBY/HALL-05 arrival branch 1.20 m. Tiny LINK-01/HALL-03 are junction strips, suppressed labels; not usable routes by themselves.
- `window_proposals` now has `face`, `operable`, room metadata and explicit court segment. Massing excludes courtyard windows from external facade mapping; roof has an even-odd aperture and clipped interior, not a roof over court. Sections show open court plus normal windows.
- Tubes/upper boxes/rooflight removed. Do not restore them or treat empty lists as tested daylight systems. Parents court window is single-sided; no airflow/daylight performance verified.
- Porch/steps/walks move toward D with house width; gates/left car bay remain. Front depth 4.40 m, no turning solver. Balcony front coordinates follow expanded envelope.
- Build has 89 limited checks, including 900 sampled bed-to-compartment rays and screen/finite private-route bands. Browser has 77 actual pointer selections and C08 window/court/area regressions. Screen overlays ignore pointer events. No legal/occupied/environmental/engineering certification.
- C08 archived; next design issue C09/erratum. C07 52-file archive verified before edits. Historical implementation notes below remain for provenance; active geometry/report takes precedence.

### Historical C07 and retained mechanisms

C07 keeps metre geometry and 108 m² aligned envelopes. Both options now retain shared BAL-01; `options[].extra_balconies` adds private BAL-02 only in option 02. C06 was verified before editing and preserved; C07 is archived, next design issue C08 or a distinct erratum suffix. AGENTS.md usability principles remain active.

C07 implementation additions:
- Entry spans LIV-01 and enlarged GP-LOBBY (open arrival hall). Grandpa's F1 rectangle and horizontal door changed; F2 sister stays unchanged. Avoid copying Grandpa F1 geometry onto sister F2.
- Main leaves explicitly use `swing: outward`; porch/steps/gate/walks moved. `porch_waiting_reservation` is outdoors; floor arrival reservation overlaps living/hall and must not be counted as additional area.
- `window_proposals` records room, matching plan segment, sill/height and shade depth. Massing uses this schedule. F2 sister C window removed for storage; brother wardrobe moved off C window wall.
- `coordination.daylight_tubes` records two 0.40 m upper chase boxes over parents' ceiling. Bedroom 5 loses 0.32 m² after boxes; tube output/view/ventilation are not verified. `rooflights` remains a performance candidate.
- `floorData()` appends optional private balcony room/door/route. Build totals shared/private areas separately and checks extra containment/door/finite path. Browser uses actual displayed room IDs (67 interactions), checks optional balcony details and rendered centers/shades/tubes/outward swings.
- Final report has 83 limited checks. They do not establish full occupied use, standards/opening rights, daylight/ventilation, structural cantilevers or car turning. C07 outputs are regenerated; all prior archives immutable.

The older C06 notes below describe retained mechanisms except where superseded above.

- Source coordinates remain +x toward road/SE, +y along B toward C. Clockwise plot/F1/F2 display rotation is separate; B appears above, A right, C left. Never relabel edges or change compass to match casual left/right descriptions.
- Owner wants about 0.30 m at A and rear next to B. B=0.10 m is an **assumption**, not lawful setback. No A/B opening assumed. C02 rear door/projection superseded; C06 keeps direct kitchen exit on C and removes C05 upper C extension.
- `options[].balcony` defines each variant's rectangle, door, access-room ID, note and route. `floorData()` applies these overrides to the base F2 room/door list; the BAL-01 ID remains stable. Build checks/reports each variant and derives `derived.balconies`. F1 is common to both.
- Floor envelopes, gross areas, stair, fixtures, altar width/projection and wet stacking are parameterized. The altar width is local y; its x dimension is depth. Unsupported physical option rotations are rejected.
- KIT-01 / DIN-01 are adjacent open rectangles with a 0.10 m strip. C06 named zones 16.83 m² versus 17.34 m² bay; 0.51 m² junction difference. Do not double-count. Table orientation and six `dining_chairs[].rect` footprints are explicit; avoid renderer-invented chair geometry. Garden opening is on DIN portion of combined bay.
- `F1.tv`/furniture define sofa facing (`seat_facing`), rear line/arrow and centered TV. Main opening 1.90 m. `door_operations` provides inward bedroom/outward main leaves and unresolved sanitary sliding candidates. `clearance_reservations` and route bands specify limited checks; do not infer comfort, full privacy or finished clearances from them.
- F2 rooflight is a candidate above bedroom 5, not proven daylight/ventilation. Kitchen daylight/extract and actual service shafts remain unresolved.
- C06 preserves 0.90 m buffer, 1.0/1.4 m wet widths, 21-riser stair and all IDs. Private compartments rotate: entry axis now v, shared remains h; `door_joins()` handles both. Bedroom IDs identify primary doors, `BR-01-BATH` / `BR-03-BATH` internal bath doors. Private public doors EN-01/03 removed; screens enclose passages on common side. Avoid restoring C05 coordinates.
- Site source has left/C bay, `vehicle_body`, separate `pedestrian_gate`, `vehicle_path` axis and `pedestrian_reservations`. Dashed paths/axis are not swept-path analysis. Section/backing/porch derive from source, but plot text anchors remain revision-specific.
- 71 checks retain original 48/C05 additions plus 13 C06 regressions: direct bedroom connections, removed private public entry, sofa rear/altar, TV/door, conservative leaf bounding boxes, chairs, clearance rectangles, 0.80 m sampled furniture bands, left bay and walking strips. They do not validate full wall/portal route connectivity, all door interactions, occupied movement, standards, daylight, headroom, turning or structure.
- Browser reads active options, exports five views each and tests 66 real room clicks/focus/keyboard, balcony notes/areas, TV/entry, direct suite exits/leaf/sofa metadata and overlays. PNGs use standalone SVG tabs. Focused dining capture records selection. Chrome remains Windows-specific; print/PDF untested.
- Top-level option-01/02 outputs are C07. Nested obsolete-C01/profile caches excluded from archive. All earlier archives including C05 preserved; never overwrite them.
- Static SVG remains the renderer for plans/sections/massing. No new dependency, BIM or engineering solver was added. Volumes, rooflight, openings, guards and facade frame are schematic.

## Evidence and review notes

For new technical/standards research, record exact designation/edition, authoritative link, access date, relevant scope/clauses and what remains unverified. No construction checks should be inferred from the C01 discussion grid. For feng shui, distinguish the family's rule from research, source quality and the proposed geometric interpretation.

Keep the final response focused on the changed design and review links. End the file handoff with enough information that a new session can resume without reconstructing chat: current revision, selection status, completed checks, pending issue IDs, stale/partial outputs if any, and the next concrete action.

## Current C09 implementation override

C09 supersedes conflicting C08 dimensions above. Envelope/court and area convention retained. Stair moves +0.30 m in local x; wet-core outside and stair/Grandpa-sister division share x=6.25. Kitchen/dining and BR-05 widen 0.30 m. BR-02/04 are [6.3, 8.1, 4.0, 3.7]; common bedroom halls are 1.00 m. Grid is a wall-reference overlay, not engineered beams/columns.

Sofa moves +0.80 m in x and −0.05 m in y; TV moves −0.05 m in y. Buffer door is 0.80 m inward, with 0.95 m sofa-back approach and explicit route. New checks validate actual portal adjacency and sampled finite furniture-free access. TV front gap now 1.85 m.

HALL-04 becomes [6.3, 5.8, 4.0, 1.1]; STUDY-02 is [6.3, 3.7, 4.0, 2.0]. UTIL-02 has dry linen cabinet and inward door. Exact EMPTY-ALT retained, occasional cleaning door moved clear of desk. F2 furniture includes occupied chair footprints; renderer must not interpret Bedroom desk as a bed.

Both options now have only shared BAL-01: option01 [10.5, 4.6, 2.0, 3.6], option02 [10.5, 4.2, 1.6, 4.4]. Balcony furniture is option-owned and appended by floorData(); guard/frame inset, occupied bench, entry reservation and seat facing are explicit. Stable BAL-02 is retired from active geometry, preserved in C08. No additional renderer/library.

Final check count is in the generated report (C09 extends the earlier 89 scope and retires three private-balcony checks). Regenerate ten SVG/PNG exports after source changes. C09 archive is a proposal, not acceptance; next design issue C10 or a distinct erratum suffix.

## Current C10 implementation override

C10 supersedes C09 dimensions/interpretations. `house.depth=11.4`, width 10.5; court [0.2, 4.3, 2, 2]. F1 gross 119.70−4=115.70. `house.upper_outline` is notched; `upper_recesses` subtracts 4.05 m² from F2 enclosure to 111.65. Balcony is separately counted in full; its floor/roof still needs construction. Bounding envelopes alone no longer describe F2 enclosure.

`coordination.altar_exclusion` is authoritative 3.40 × 1.20 m strip. ALT-01 remains 3.40 ×3.00 m worship room; EMPTY-ALT equals the smaller exclusion. Renderer projection/section and checks must use the exclusion, not whole ALT-01. `altar_side_screen` and `porch_canopy` are source-driven proposals.

Corner parents/brother and spare/kitchen right edges align x 3.65; wet/stair/Grandpa axis 6.25 retained. Common COURT-HALL-1/2 and KITCHEN-LOBBY/SPARE-LOBBY keep ordinary exits outside kitchen/spare. HALL-01/02 now narrow open junction zones, not standalone corridors; evaluate their union with cross hall. F2 STUDY-02 is forward of exclusion; LANDING-02 and LOGGIA-LINK connect it/linen to shared balcony. Doors, sweeps, windows, furniture, routes and site porch were reconciled.

Massing uses actual upper outline with court roof aperture. Site area label is dynamic. Build checks distinguish worship/projection, window/storage, actual hinged-door anchors, common exits, screen and recess; final count in current report. Browser checks screen and dynamic ground area, then exports all ten views. No new libraries or renderer. C09 archive verified before changes; completed C10 archived. Next design issue C11 or distinct erratum suffix.

## Current C11 implementation override

C11 supersedes conflicting dimensions above. F1 remains 115.70 m²; `upper_outline` recess moves to right former study: [8.7,0,1.8,4.9], 8.82 m²; F2 enclosed convention 106.88 m². Shared terrace [8.8,0.2,2.3,4.6], 10.58 m², has a **horizontal** weather door at y=4.9 from HALL-04. Do not restore the former vertical-door check. Both options share geometry; `shade`, `shade_rect`, `shade_posts` differ. Drain line/overflow remain proposals.

Shared wet rooms y increases 0.30 m; private enclosure depth increases to 2.10 m. `suite_enclosure` draws its perimeter, both EN zones are open and old EN-ACCESS/RETURN partition portals are retired. `private_screens` retains short sightline screen. Stair [3.7,7.5,2.5,3.7], nominal flights 1.10 m, gap 0.30 m. y4.25 and x3.65/6.25 align real wall references, not structure.

STUDY-02 and its furniture/window/door retired; stable history remains archived. UTIL-02 and EMPTY-ALT have no dividing wall, linen cabinet remains; `open_portals` identifies doorless buffer/linen openings. The empty strip remains unfurnished indoors behind terrace wall. F2-WIN-LANDING serves open hall above entrance; its lower fixed light/guard is unverified.

`entrance_design` holds concept levels, three rises, canopy posts and drainage. Floor/site/massing/section reconcile porch and stair dimensions; sections export at 1800 px height. Static SVG renderer retained with open metal guards, optional shade and new facade composition. Geometry report has 114 limited checks; browser 88 actual room selections and ten current exports. C10 56-file archive verified first. C11 archived; next issue C12 or a distinct erratum suffix.
