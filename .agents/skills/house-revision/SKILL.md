---
name: house-revision
description: Revise and compare concepts for this Noi Bai house project, keeping editable geometry, both floors, family requirements, review artifacts and revision state consistent. Use for layout, site, drawing or concept-viewer revisions in this workspace.
---

# House revision

Paths below are relative to the project root, three directories above this skill folder. Work within the owner's current request; a request to compare or revise does not select an option or authorize construction.

## Resume

Read `PROJECT_STATE.md`, `docs/brief.md`, and the relevant entries in `docs/open-issues.md`. For spatial changes also read `docs/site-investigation.md` and `docs/preferences-and-feng-shui.md`. Read `docs/agent-workflow.md` before changing model/rendering code; it lists the C01-specific constants and archive commands.

Use the latest owner instruction over older records. Update those records when requirements change. Keep owner decisions, approximate site inputs, model assumptions and design proposals distinct. Do not re-ask settled questions or silently choose Option 02 because it was previously recommended.

## Revise

- Preserve an existing review baseline with `scripts/snapshot_revision.py` before overwriting it; do not overwrite archived revisions. A snapshot is not approval.
- Edit `data/concepts.json` and affected rendering/generation logic. Outputs are derivatives. Maintain stable IDs and the model's declared metre units.
- The current viewer is not fully parameterized: its plan, site, section, massing, summaries and checks contain geometry literals. Reconcile all affected representations rather than assuming a JSON dimension change updates everything.
- Coordinate F1/F2 together: bedroom and separate WC/shower counts, suite privacy turns, stair/entrance relationship, solid altar backing and indoor buffer, empty upper altar zone, circulation bypass, wet stacking and balcony access.
- Site lengths and the 130-degree bearing are owner-reported inputs; angles, offsets and model area are inferred. Preserve that distinction in diagrams and notes. Ignore the sketch's 192 annotation.
- Show the practical consequences of an option: room areas, furniture/access compromises, parking/garden space and outstanding assumptions. Do not equate overlap checks with usable circulation, legal setbacks, engineering or vehicle turning.

## Review and issue

For model/template changes run `python scripts/build_concepts.py`. For geometry/UI changes use `python scripts/review_viewer.py` when available and inspect relevant exported drawings. Follow environment permissions if Chrome requires escalation. When browser review cannot run, report the gap and identify stale exports; do not invent a pass.

Documentation-only changes need consistency checks, not a fresh browser run. New engineering or standards claims need applicable authoritative evidence and an explicit design basis. Keep discussion axes/service markers preliminary; apply the existing research and professional-review rules in AGENTS.md.

For a reviewable design change, advance the revision, update presentation/report labels and write `docs/concept-study-<revision>.md`. Update the affected brief/decision/issue records, entry links and `PROJECT_STATE.md`. Archive the completed review baseline and verify its checksums. The handoff should identify current revision, owner selection status, completed checks, unresolved issue IDs and the next action.

## Delivery

Link the working viewer and revision comparison. Explain the changed behavior/layout, main tradeoff and checks actually performed. Keep instructions and state concise enough that the next session can resume from files without chat history.
