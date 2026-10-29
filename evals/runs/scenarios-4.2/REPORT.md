# Scenario corpus run: 4.1.0 vs 4.2.0

Date 2026-10-29. First execution of the 38-scenario corpus. Harness: `scripts/run_scenarios.py`; gate: prompt-optimization `compare` (paired non-inferiority, bootstrap 95% CI, margin 0.05), contract and utility predeclared in `contract.json`.

## Configuration

- Baseline 4.1.0 and candidate 4.2.0 frozen under `packages/` with neutral labels; hashes and label mapping in `manifest.json`.
- Subject `sonnet` (resolved `claude-sonnet-5-5`), judge `opus`, Claude Code 2.1.312, one run per case per arm, shuffled arm order.
- Isolated empty workspaces (fixtures copied where supplied), `--setting-sources project`, `--strict-mcp-config`, case tool scope and turn limit.
- Blind judge saw prompt, rubric, tool trace, changed files, oracle output, and final answer; not the arm. Three cases have executable oracles (`graders/oracle.py`).

## Result

**ACCEPTED.** Utility delta +0.013, CI [-0.040, +0.066]. No severe failures, no environment errors in kept records, oracles 6/6 pass, cost per run unchanged (~$0.13 including judge; total $9.69).

| Arm | Pass | Partial | Fail |
|---|---|---|---|
| 4.1.0 | 27 | 11 | 0 |
| 4.2.0 | 28 | 10 | 0 |

Differences: 3 improved (`capacity-ownership-no-double-reserve`, `context-relevant-and-untrusted`, `efficiency-count-failures-and-rework`), 2 slipped (`lead-prototype-no-policy-bootstrap`, `supply-provenance-not-sbom`). Neither slip loaded the target skill in either arm, so neither traces to 4.2.0 text.

## Main finding: routing

| Arm | Target skill loaded | No skill loaded |
|---|---|---|
| 4.1.0 | 24 runs, 21 pass | 13 runs, 6 pass |
| 4.2.0 | 24 runs, 23 pass | 13 runs, 5 pass |

In 11 cases neither arm loaded the target skill: `ai-eval-holdout-judge-bias`, `capacity-ownership-no-double-reserve`, `context-handoff-diagnosis-is-hypothesis`, `context-stale-green-after-edit`, `failure-log-from-stuck-run`, `implementation-stale-test-pin`, `lead-prototype-no-policy-bootstrap`, `lead-verifies-reported-claims`, `review-target-excludes-private-file`, `supply-provenance-not-sbom`, `supply-reachable-advisory-no-silent-waiver`. Pass rates conditional on loading are associational (case difficulty may confound), but triggering is the largest visible lever.

## Limitations

- One sample per case per arm; 38 development cases used to tune the suite, not a held-out set.
- The user's `~/.claude/CLAUDE.md` loaded in both arms and was visible in at least one judge rationale.
- Built-in skills competed for routing in both arms. Single judge model, not calibrated against human labels.
- Most scenarios describe situations without fixtures; the judge was told to grade decisions, not absent edits.

## Harness defects found and fixed during the run

1. Relative `--plugin-dir` paths silently loaded no plugins (first pilot invalid); now resolved to absolute and runs without both plugins are environment errors.
2. Rate-limited calls report `subtype: success` with `is_error`/HTTP 429; now retried instead of recorded. 33 affected records were removed and rerun.
3. `lead-small-fix-stays-inline` and `implementation-stale-test-pin` had no files to edit; they now ship fixtures and oracles verified to fail on pristine fixtures and pass on a correct fix.
