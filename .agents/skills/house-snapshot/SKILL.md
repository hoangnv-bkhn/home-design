---
name: house-snapshot
description: Safely archive, verify, and freeze concept design review baselines using snapshot_revision.py. Use when issuing a new revision for review (e.g. C04) or verifying existing revision packages.
---

# House Revision Snapshot & Archival

Use this skill when preparing, archiving, or verifying an immutable review baseline for this house project.

In Antigravity, you can invoke this skill as `house-snapshot` or via the slash command `/house-snapshot`.

## Revision Discipline & Invariants (from `AGENTS.md`)

- **Never overwrite an existing archive**: Each revision folder under `revisions/<rev>/` is immutable once created. If an erratum is needed for an archived package, issue a distinct suffixed ID (e.g., `C01a`, `C03a`).
- **Match declared data revision**: The `--revision` argument passed to `scripts/snapshot_revision.py` must strictly match the `"revision"` key in `data/concepts.json`.
- **Snapshot is not approval**: Archiving preserves a reproducible evidence snapshot with SHA-256 checksums; it does **not** signify client approval or professional engineering sign-off.
- **Top-level deliverables only**: The snapshot tool packages current `outputs/` deliverables (`.html`, `.svg`, `.png`, `.md`), model sources, scripts, docs, and skills. It automatically excludes browser profiles, temporary caches, and nested historical folders (such as `outputs/obsolete-C01/`).

## Step-by-Step Procedure

### 1. Pre-Snapshot Verification

Before taking a snapshot, ensure the active workspace is clean, tests pass, and all deliverables are up to date:

```powershell
# 1. Build geometry and run checks (must pass 48/48)
python scripts/build_concepts.py

# 2. Run browser review and SVG/PNG generation
python scripts/review_viewer.py

# 3. Check git status to ensure working tree reflects intended changes
git status
```

Verify that required artifacts exist:
- `outputs/house-concepts.html`
- `outputs/geometry-review.md`
- `docs/concept-study-<revision>.md`

### 2. Verify Destination is Available

Confirm that `revisions/<revision>/` does NOT already exist:

```powershell
Test-Path revisions/<revision>
```

If it exists, you must increment the revision (e.g., `C04`) in `data/concepts.json` and all affected documentation, or use a distinct suffix (e.g., `C03b`) if issuing an erratum.

### 3. Create the Snapshot Archive

Execute the snapshot script with a descriptive note explaining the review baseline:

```powershell
python scripts/snapshot_revision.py --revision <revision> --note "Brief description of review package"
```

The script will:
1. Validate the active revision against `data/concepts.json`.
2. Collect sources, docs, skills, and current deliverables.
3. Compute SHA-256 digests for each file.
4. Stage into a temporary folder, generate `snapshot.zip` and `manifest.json`, and commit the directory.

### 4. Verify Archive Integrity

Immediately verify that the newly created archive matches its manifest checksums:

```powershell
python scripts/snapshot_revision.py --verify <revision>
```

### 5. Update Project State and Entry Points

Update `PROJECT_STATE.md`:
- Record the newly archived baseline under "Artifacts and checks".
- Note verification status.
- Document next actions for client feedback or technical resolution.
