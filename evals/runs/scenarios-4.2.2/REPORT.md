# Scenario run: solo vs 4.1.0 vs 4.2.2

Date 2026-10-29. Targeted run of the 27 cases touching the two edited skills (team-lead, definition of done) plus all 11 held-out cases (6 new, written to re-test the recorded gaps in new wording), two runs per case per arm. **Solo** is the same model, tools, and limits with no suite loaded. Judge Opus; subject Sonnet; configuration otherwise as [scenarios-4.2](../scenarios-4.2/REPORT.md). Cost $18.41 (77 runs hit the usage limit and were retried).

## Correctness and efficiency

| Split | Arm | Runs | Mean utility | Pass/partial/fail | Skill loaded | Median s | Turns | Tool calls | $/run |
|---|---|---|---|---|---|---|---|---|---|
| dev | solo | 32 | 0.766 | 17/15/0 | 0 | 14 | 1.7 | 0.7 | 0.110 |
| dev | 4.1.0 | 32 | 0.828 | 21/11/0 | 15 | 14 | 2.7 | 1.2 | 0.120 |
| dev | 4.2.2 | 32 | 0.844 | 22/10/0 | 22 | 16 | 3.2 | 1.5 | 0.123 |
| holdout | solo | 22 | 0.659 | 11/7/4 | 0 | 11 | 1.7 | 0.7 | 0.102 |
| holdout | 4.1.0 | 22 | 0.705 | 13/5/4 | 4 | 11 | 2.1 | 1.0 | 0.110 |
| holdout | 4.2.2 | 22 | 0.818 | 17/2/3 | 10 | 13 | 2.8 | 1.3 | 0.112 |

Scenario-clustered paired differences (95% bootstrap over cases):

| Comparison | All 27 cases | Held-out 11 |
|---|---|---|
| 4.2.2 - solo | +0.111 [+0.037, +0.185] | +0.159 [+0.068, +0.250] |
| 4.2.2 - 4.1.0 | +0.056 [-0.009, +0.120] | +0.114 [+0.023, +0.227] |
| 4.1.0 - solo | +0.056 [+0.000, +0.120] | +0.045 [+0.000, +0.114] |

Using the suite beats no suite under this judge, at about +2 s median, +1.5 turns, and +12% cost per run. Cost per accepted unit of utility is roughly flat (solo $0.144, 4.2.2 $0.143 per utility point on dev). No severe failures in any arm.

## Targeted rules

- Retry-green risk owner (`holdout-green-on-third-retry`, now dev): 4.2.2 pass/pass; every other arm partial/partial. The fix works where aimed.
- Worker reports done with a build running: 4.1.0 already passes; the new rule adds nothing measurable.
- Heavy builds near the usage limit: 4.2.2 1/2 pass; all arms tend to cap at two concurrent heavy builds instead of serializing.
- Fresh gap re-tests `holdout2-flaky-e2e-release-call` and `holdout2-five-agents-field-rename` failed in every arm and both runs. In 4.2.2 the target skill never loaded: "is the release ready?" and "rename across five agents" still miss the descriptions. Recorded, not tuned.

## Judge robustness (pending)

On [scenarios-4.2.1-rep](../scenarios-4.2.1-rep/REPORT.md), an independent Codex judge (GPT family) agreed with Opus on 67% of verdicts (kappa 0.38), was stricter (59 pass to partial), and erased the 4.2.1-vs-4.1.0 quality difference (-0.006, clustered CI [-0.061, +0.050]). The same re-grade of this run hit the Codex usage limit before grading anything; rerun `python scripts/rejudge.py --run evals/runs/scenarios-4.2.2` to test whether the solo gap survives a second judge. Until then, treat the solo result as Opus-judged only.
