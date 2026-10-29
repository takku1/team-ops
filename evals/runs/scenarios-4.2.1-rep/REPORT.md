# Scenario run: 4.2.1 vs 4.1.0, two repeats plus held-out cases

Date 2026-10-29. Same configuration as [scenarios-4.2](../scenarios-4.2/REPORT.md). 38 development cases and 7 new held-out cases (`split: holdout`, written after the 4.2.1 descriptions and never used for tuning), two runs per case per arm (180 runs). The baseline's first development run was reused from scenarios-4.2. The candidate package is 4.2.1 as frozen before the README rewrite and the two error-analysis rules (shared host limits, worker background jobs), which are unmeasured. Cost $22.55.

**ACCEPTED** over 90 paired runs: utility delta +0.033, 95% CI [0.000, +0.067]; no severe failures, no environment errors in kept records, oracles all pass.

| Split | Arm | Runs | Target skill loaded | Pass / partial / fail | Mean utility |
|---|---|---|---|---|---|
| dev | 4.1.0 | 76 | 49 (64%) | 56 / 20 / 0 | 0.868 |
| dev | 4.2.1 | 76 | 62 (82%) | 60 / 16 / 0 | 0.895 |
| holdout | 4.1.0 | 14 | 2 (14%) | 9 / 5 / 0 | 0.821 |
| holdout | 4.2.1 | 14 | 8 (57%) | 11 / 3 / 0 | 0.893 |

## Findings

- **Trigger-first descriptions generalize.** On prompts they were never tuned on, loading rose from 2/14 to 8/14 runs, with a matching utility gain. The sample is small (7 cases).
- **Correction to the 4.2 report.** With two repeats, the gap between runs that loaded the skill and runs that did not shrank (4.2.1: 0.90 vs 0.86; 4.1.0: 0.94 vs 0.74). The single-run "23/24 vs ~45%" contrast overstated how much loading alone explains; case difficulty and noise contributed.
- **Run-to-run noise.** 32-34 of 38 development cases gave the same verdict on both repeats; read totals, not per-case flips.
- **Held-out gaps, deliberately not tuned:** `holdout-green-on-third-retry` was partial in all four runs (correctly refused the retry-green but never named who decides the risk acceptance). `holdout-four-agents-one-render-file` never loaded team-lead ("split this across four agents" phrasing). Fixing them would turn these cases into development data; address with fresh held-out cases next cycle.

## Second judge and clustered statistics (added later)

- Scenario-clustered bootstrap: delta +0.033, CI [-0.006, +0.072] (dev +0.026 [-0.013, +0.072]; held-out +0.071 [+0.000, +0.179]). Non-inferior, but improvement not demonstrated; 34 of 45 cases unchanged.
- Codex (GPT family) re-graded all 180 runs: 67% exact agreement with Opus, Cohen kappa 0.38, stricter (59 pass to partial). Under Codex the delta is -0.006 [-0.061, +0.050], failing the 0.05 non-inferiority margin, and the held-out gain reverses. The quality claim is judge-dependent; the routing gain (read from transcripts, judge-free) is not.

## Limitations

Same as scenarios-4.2: single Opus judge without human calibration, the user's global CLAUDE.md loads in both arms, built-in skills compete for routing, held-out rubrics written by the same author as the skills. 27 runs hit the account usage limit and were retried by the harness.
