# Scenario run: 4.2.1 descriptions vs 4.1.0

Date 2026-10-29. Same configuration as [scenarios-4.2](../scenarios-4.2/REPORT.md); the 4.1.0 baseline records and package were reused unchanged; only the candidate (trigger-first descriptions) was rerun on all 38 cases.

**ACCEPTED.** Utility delta +0.026, CI [-0.040, +0.092]; no severe failures; 29 pass / 9 partial; cost $4.86.

Target skill loaded: 32/38 (4.2.0: 24/38). Newly routed: ai-eval-holdout-judge-bias, code-review-keeps-out-of-diff-findings, context-stale-green-after-edit, failure-log-from-stuck-run, lead-verifies-reported-claims, release-low-traffic-side-effects, review-target-excludes-private-file, supply-provenance-not-sbom, trunk-many-short-branches, capacity-ownership-no-double-reserve. Lost: lead-duplicate-check-owner, lead-unrelated-ready-task (both still passed).

Follow-up [scenarios-4.2.2-lead](../scenarios-4.2.2-lead/) restored team-lead trigger terms and reran its 12 cases: loaded 9/12, passed 10/12 (4.2.0: 8/12 loaded, 9/12 passed). Per-case routing varied between runs; one sample per case cannot separate single flips from noise.
