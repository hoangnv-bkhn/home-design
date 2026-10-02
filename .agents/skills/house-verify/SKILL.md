---
name: house-verify
description: Verify the current house concept design, execute the 48 geometry checks, run the headless browser review, and verify snapshot integrity without altering design geometry. Use for health checks, test runs, and review validation.
---

# House verification and health check

Use this skill to run non-destructive integrity checks on the current design, outputs, and archived review baselines without modifying concept geometry.

In Antigravity, you can invoke this skill as `house-verify` or via the slash command `/house-verify`.

## Scope and Invariants

- Verification is read-only: do not modify `data/concepts.json` or source code during verification.
- Passing build checks (48/48) confirms geometric validity, envelope containment, non-overlap, fixture counts, and arithmetic consistency; it does **not** constitute professional engineering, planning approval, or daylight certification.
- Headless Chrome review validates SVG/PNG rendering, mobile 390 px viewport behavior, and tab consistency.
- Revision snapshot verification ensures archived baselines remain uncorrupted and immutable.

## Step-by-step verification procedure

### 1. Verify archived snapshot integrity

Check that the latest archived revision package (e.g. `C03a`) is intact and that SHA-256 hashes match:

```powershell
python scripts/snapshot_revision.py --verify C03a
```

*Expected result*: `C03a: verified 44 archived files; active workspace not compared.`
If an archive mismatch or missing manifest is reported, do **not** overwrite the archive; investigate `revisions/` immediately.

### 2. Run model derivation and geometry checks

Run the standard-library build script to derive geometry, evaluate the 48 rule checks, and rebuild `outputs/house-concepts.html` and `outputs/geometry-review.md`:

```powershell
python scripts/build_concepts.py
```

*Verification points*:
- Ensure all 48 checks pass (e.g. `Generated C03a viewer/report: 48/48 limited checks pass.`).
- Verify room counts: 5 bedrooms, 4 separate WC/shower compartments (basins only in showers).
- Confirm envelope containment, altar projection buffer, and stair going/riser arithmetic.
- If any check fails, do not proceed to visual review until the discrepancy is understood.

### 3. Run headless browser review and export

Launch the headless Chrome review script to validate viewer tabs, inspect live SVG geometry, test mobile viewport overflow (390 px width), and export current SVG and PNG views:

```powershell
python scripts/review_viewer.py
```

*Verification points*:
- Script exits with: `C03a viewer review passed; 10 SVG and 10 PNG views exported.`
- Confirm that outputs are updated in `outputs/`:
  - `outputs/option-01-F1.svg` & `.png`
  - `outputs/option-01-F2.svg` & `.png` (shared balcony)
  - `outputs/option-02-F2.svg` & `.png` (corner balcony)
  - `outputs/option-01-site.svg` & `.png`
  - `outputs/option-02-site.svg` & `.png`
  - `outputs/option-01-section.svg` & `.png`
  - `outputs/option-01-massing.svg` & `.png`
  - `outputs/option-02-massing.svg` & `.png`
  - `outputs/viewer-review.md`

### 4. Reconcile documentation and open issues

- Check `PROJECT_STATE.md`: verify that the current revision matches `data/concepts.json` (`revision` field) and that active options (Option 01 vs Option 02) remain labeled as unselected comparisons.
- Check `docs/open-issues.md`: verify whether any recently discussed items affect issues L01–L11, S01–S04, E01–E02.
- Confirm that historical outputs in `outputs/obsolete-C01/` remain separated and are not presented as active revision deliverables.

## Output report format

When reporting verification results, summarize:
1. Current active revision ID and date.
2. Build check results (e.g. 48/48 passed).
3. Browser review status (headless Chrome pass, SVG/PNG export count).
4. Snapshot integrity status.
5. Outstanding evidential reservations (unverified site angles/setbacks, daylight/extract, occupied clearances).
