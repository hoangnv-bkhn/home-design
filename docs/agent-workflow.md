# Continuing and issuing house revisions

## C15 active implementation override

C15 supersedes historical geometry below where changed. Read `data/concepts.json` and [C15 comparison](concept-study-C15.md). Ground/upper bounding envelopes 10.80×11.40; actual upper notched polygon has no sister projection. `cantilever.depth=0` is a retired reservation, not an active slab. `bedroom_cap.thickness=0` retires the separate cap; common roof datum 6.60, `exterior_design.parapet` defines 0.35 m height. Both options have `shade=roof`; porch kinds `ranch`/`framed-ranch` differ only edge/posts.

Private wet y0.20–2.00, passage y2.10–3.10, court[4.10,3.20,2.40,2.90]. Suite direct court windows 0.90 m; additional `court-dressing` windows must not render on outer facades. Historical `court-gallery` face/IDs retained for stability, but assigned rooms now LIV-01/LANDING-02. Court maintenance door is from living, not gallery. No private screens; opaque BR-01/03-BATH sliding doors have explicit open-leaf reservations. Privacy report separates blocked bed rays from 72/324 unblocked ordinary-entry rays; never describe as full open-door privacy.

Roof service screen/tanks relocate above rear suite, hatch/collector retained and access routed around court. Ground porch 3.30×2.20 m/canopy 3.00×4.00; garden path goes to front steps. Site/plan/section step count corrected to two 300 mm treads. Rebuild/export after geometry/template changes; verify/archive with existing scripts. Detailed checks and artifact status are in PROJECT_STATE.md. No new library or renderer.

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


## Current C12 implementation override

C12 supersedes conflicting C11 constants. Envelope **10.90 × 11.40 m**; court **[4.1,0.2,2.4,2.0]**; F1 **119.46**, F2 **111.62 m²** after **7.84 m²** recess [9.3,0,1.6,4.9]. Shared terrace [9.4,0.2,2.1,4.6], **9.66 m²**, horizontal door y4.9. Window F2-WIN-LANDING starts y5.5, leaving 0.60 m return. Main door [10.8,4.9,1.9,v], moved porch/canopy/scooters and front paths. Stable room IDs retained.

Suites [0.2,0.2,3.8,4.0], common doors y4.25; private bath link x4.05. Shared pair occupies former court and opens to side lobby; private pairs sit in former shared bay with screened dressing above. All showers 1.30 × 1.80. Bedroom court windows now **vertical**, x4.05, not horizontal y4.25. Common court door x6.55 comes from ALT-BUFFER; gallery fixed windows use `face: court-gallery`, excluded from exterior facade mapping. Window and route checks follow the new geometry.

Backing x7.90, altar [8,0.2,2.7,3.4], empty upper exclusion [8,0.2,1.2,3.4]. Gallery/linen [6.6,0.2,1.3,3.4], full-width 1.30 m open portal; ground ledge removed. Sofa faces **[0,-1]**, armchair **[-1,0]**, TV on side console; `occupied_seating` holds knee reservations, rendered with route overlay. TV-centering checks use the lateral axis, not a fixed coordinate. Bedroom wall offsets deliberately differ from C11 alignment and are documented engineering work.

Existing SVG massing primitives now carry 3D coordinates, projected overlap and camera-ray depth ordering; zero-cycle metadata is checked in Chrome for both options. This fixes recessed slab/guard painting over foreground windows. No library/new renderer. Roof keeps real notched outline and court aperture; gallery glazing appears in court section. Source changes require build/export and visual checks; final active reports define check counts (**121** geometry, **88** actual room clicks for C12).

C11 57-file archive verified before changes. C12 review archived; next design issue C13 or distinct C12 erratum. Earlier archives immutable. Do not rerun historical revision migrations over active geometry.

## Current C13 implementation override

C13 supersedes changed C12 dimensions. Ground envelope remains **10.90 × 11.40**, court **[4.1,0.2,2.5,2.0]**, stair **[4.1,7.5,2.5,3.7]**. Principal `grid_x=[0.1,4.05,6.65,10.8]`, `grid_y=[0.1,4.25,7.45,11.3]` are architectural references, not beams/columns. Private wet/gallery edge is x6.65; kitchen/spare ends 4.00, Grandpa/sister start 6.70. Secondary altar/terrace edges need framing review.

F2 envelope is a **bounding** 11.50 × 11.40 rectangle. `house.upper_outline` is authoritative for actual notched/projecting exterior; shoelace area 118.79 minus court 5.00 gives enclosed 113.79. `upper_recesses` now holds **[9.3,0,2.2,4.9]** and **[10.9,4.9,0.6,2.55]**, reconciling the bounding rectangle. Do not derive upper area solely from ground area or the former 7.84 m² terrace recess. Ground covered 119.26. `coordination.cantilever` records a D-side 0.60 m enclosed sister projection [10.9,7.45,0.6,3.95]; site and massing use actual polygon, upper sister window x11.40 maps to facade 11.50.

Altar [7.8,0.2,2.9,3.2], exclusion [7.8,0.2,1.2,3.2], backing [7.7,0.1,0.1,3.3], gallery/linen [6.7,0.2,1.0,3.2], portal [6.7,3.45,1.0,h]. Stable `altar_side_screen` source key now has **kind: wall**, solid plaster material and rect [7.8,3.4,1.7,0.1]; renderer exposes `data-altar-side-wall`. No slat renderer. Linen cabinet moves to landing; gallery stays furniture-free. Altar D-window is provisional interpretation, not confirmed opposite-side/A opening.

Only F1 schedule holds the physical stair window: F1-WIN-STAIR, opening[4.8,11.3,1.1,h], sill 1.80 / height 2.40, `spans_floors=['F1','F2']`. `planWindows()` appends its continuation for F2 plan with the same window ID and STAIR-02 room. F2 source schedule/physical facade has no second stair window. Build explicitly allows this cross-storey height only for the stair record; browser counts upper continuation separately and verifies exactly one physical massing opening.

`exterior_design.bedroom_cap` provides source-driven higher roof plate; optional services overlay draws cap outlet/overflow markers. Main roof preserves court hole and actual upper shape; both massings have zero camera-depth cycles in final review. Porch canopy [10.9,4.55,3.00,2.80]; two 300 mm treads replace old 0.90 m reservation. Posts 13.40 at y 4.65 / 7.25 are set 0.50 m behind outer edge; section/site/plan/massing reconcile assumed levels. Section exports 2400 px for the added bedroom-projection diagram.

Counter aisle grows 1.10 m with table/chair shift 0.20 m; private showers 1.40 m, shared 1.30 m. Grandpa/sister ordinary doors [6.95,7.45,0.90,h] and inward leaves align. Build **127 limited checks**; Chrome **88 actual selections** plus current geometry/labels. UTF-8 text matters: PowerShell pipelines into Python stdin may corrupt new non-ASCII literals; use explicit UTF-8 file writes or ASCII Python source with Unicode escapes, then inspect generated labels. C12 **58-file archive** verified first; C13 issued/verified. Next new issue C14 or distinct C13 erratum; earlier archives immutable.

## Current C14 implementation override

C14 supersedes changed C13 literals. Ground **10.80 × 11.40 m**, court/stair clear **2.40 m**, principal x references **0.10/4.05/6.55/10.70**. Private showers **1.30 × 1.80 m**, shared unchanged; stair nominal flights 1.10/center reservation **0.20 m**. Screen **[4.1,3.65,1.3,0.1]** moves nearer wet entries; private routes go around it at y4.15, basin y4.60. Independent bedroom doors retained.

`house.upper_outline` now extends towards **C**, not D: bounding **10.80 × 12.00 m**, actual polygon **117.83**, court excluded enclosure **113.03 m²**. `upper_recesses=[9.2,0,1.6,4.9]` and `[0,11.4,6.55,0.6]`. Sister **[6.6,7.5,4.0,4.3]**; front aligns with F1. `cantilever.rect=[6.55,11.4,4.25,0.6]`, root along **y11.30**. Do not restore x/front cantilever assumptions. Shared terrace **[9.3,0.2,2.5,4.6]**, 11.50 m², 1.00 m projection; same common access.

`boundary_window_candidates` is separate from normal active `window_proposals/windows`. Altar/parents/brother A-side candidates draw dashed pink with explicit conditional metadata; no window permissions/performance inferred. Remove ordinary road-facing altar window. Physical stair windows now live in each floor's schedule, no continuation duplication: lower z1.80–2.60, upper z4.05–5.55; `stair_beam_reservation` z3.00–3.50 illustrative only. Lower guard/fixed glazing unresolved at half landing.

Entry start y4.60, x10.70; porch/steps/canopy/routes shift right 0.30 m. Compact table **0.70 × 0.40 m**, chair **0.60 × 0.75 m**, knee reservation reconciled; 1.10 m arrival retained. Option-owned `porch_design` drives blade/portal thickness/supports and optional short side screen. `exterior_design.roof_services` reserves cold/hot storage, screen, maintenance strip, exposed collector and stair hatch/access route. No equipment sizing/engineering basis. `sister_balcony_alternative` is a replacement study in sections only; no active BAL-02 or private area. Section roof plan derives its equipment positions from JSON.

Build **136 limited checks**; browser **88 actual pointer selections**, same ten exports, conditional windows, independent stair windows/illustrative beam labels, C-side extension, roof services and distinct porch metadata. Both massings zero camera-depth cycles. Final source changes require build/export; no new library/renderer. C13 **59-file archive** verified before changes; C14 review archived/verified. Next design issue **C15** or distinct C14 erratum. Never rerun historical migration scripts over active geometry.
