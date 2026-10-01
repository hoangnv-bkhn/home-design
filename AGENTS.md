# Working instructions for this house project

## Start here

1. Read `PROJECT_STATE.md` for current revision, unresolved choices and the next action.
2. Read `docs/brief.md` and the open issues relevant to the request. For layout work, also read `docs/site-investigation.md` and `docs/preferences-and-feng-shui.md`.
3. For concept revisions, load `.agents/skills/house-revision/SKILL.md`. For implementation details and checks, follow `docs/agent-workflow.md`.

The latest user instruction governs the task. Record new requirements and corrections durably; do not ask again for information already confirmed. Unknown details may remain labeled assumptions during concept work. Ask only when the answer materially changes the requested work.

## Authority and evidence

- Owner requirements: `docs/brief.md`; family rules: `docs/preferences-and-feng-shui.md`; site evidence: `docs/site-investigation.md`.
- Current editable geometry: `data/concepts.json`. Generated HTML, drawings and screenshots are derived outputs, not independent design sources.
- `PROJECT_STATE.md` is a handoff index, not a second room schedule. `docs/decisions.md` records decisions and supersessions; `docs/open-issues.md` tracks unresolved work.
- Distinguish owner-confirmed requirements, owner-reported approximations, model assumptions, proposals and professionally verified facts. A passing script does not change evidence status.
- Neither C01 option is owner-selected. An assistant recommendation is not approval. A snapshot preserves a revision; it does not approve it.

## Design invariants

- F1 is the ground/entrance floor; F2 is upstairs. Preserve the brief's room counts and separate WC/shower compartments unless the owner changes them.
- The current model explicitly uses **metres**, despite the roadmap's earlier millimetre proposal. Preserve declared units or migrate all consumers explicitly. Keep element IDs stable across revisions.
- A/B/C/D are sides, not vertices. The 130-degree bearing follows A toward D's road. It is not necessarily D's bearing or a facade normal. Ignore the sketch's 192 annotation.
- Site angles, bend, model-derived area, 0.8 m offsets, opening rights and structural grid are unverified. Do not turn them into surveyed facts or statutory setbacks.
- Coordinate both floors, altar projection, circulation and wet zones together. The upper altar zone has a floor but stays empty and out of frequent circulation. Indoor space behind the backing wall is the baseline.
- Preserve editable geometry and show material compromises. Do not count a drawn furniture arrangement as proof of usable circulation or a drawn car as proof of turning access.
- Use project-local, offline-friendly tooling where practical. Do not add libraries or a new renderer without a concrete need in the requested revision.

## Revision discipline

- Preserve the existing review baseline before overwriting it. Use `scripts/snapshot_revision.py`; check for an existing snapshot first and never overwrite it.
- Use C02, C03, etc. for a new design comparison issued for review. Documentation/tooling-only changes do not require a new design number. Corrections to an archived issue get a distinct suffix such as C01a.
- Read the workflow's implementation caveats before changing geometry: the current renderer/build/review scripts contain C01-specific literals and 10 m assumptions.
- Rebuild derived outputs after source changes. Regenerate or explicitly mark obsolete exports; do not present stale screenshots as the new revision.
- Validate what changed. Documentation-only work needs link/state consistency checks, not a browser run. Geometry/UI work uses the relevant existing build and browser checks plus visual inspection. Report limitations and checks actually performed.
- Close substantial work by updating `PROJECT_STATE.md`, affected requirement records, decisions/open issues, current revision notes and entry links. Leave a concrete next action and any interrupted work.

## Engineering and research

- For new code/standard applicability claims, consult current authoritative sources and record edition, clause when available, source, access date and applicability. Do not calculate from snippets or drafts.
- Structural/member, foundation and services design require an explicit design basis and appropriate professional review before construction use. Keep preliminary axes and service markers labeled as such.
- Research feng shui as cultural guidance and the family's chosen interpretation. Record source quality and uncertainty; do not introduce new family constraints or claim guaranteed health/financial outcomes.
- Keep permissions governed by the environment and the user's authorization. This file adds no blanket approval to publish, send messages, install globally or perform external mutations.

## Environment

Windows / PowerShell; project root `D:/Code/2026/house_building`. Use UTF-8 explicitly for text. Python build tools use the standard library; browser export uses installed Chrome. Browser execution and writes under `.agents` may require sandbox escalation. Explain the concrete environment restriction if approval is necessary.
