---
name: ai-evaluation
description: Design and assess evaluations for AI features, agents, prompts, retrieval, and workflow changes using representative cases, independent checks, calibrated grading, and quality/cost regression criteria. Use before consequential AI releases or when comparing configurations. Not a replacement for deterministic software tests.
---

# AI Evaluation

## Define the claim and cases

Specify the task, users, failure consequences, baseline, and proposed change. Record model/provider version when exposed, prompts, tools, permissions, retrieval corpus/index, decoding configuration, and environment. Treat hidden provider changes as a reproducibility limit.

Build cases from representative authorized examples, known failures, boundaries, ambiguous/missing inputs, and adversarial trust crossings. Include negative cases where the agent should abstain, skip a workflow, ask a necessary question, or avoid a tool. Separate development examples from held-out evaluation; do not tune on the holdout and still call it held out. Record case origin, expected behavior, slice, and sensitive-data handling.

## Choose independent oracles

- Prefer executable checks for functional correctness, schemas, exact calculations, permissions, and resulting state. Test an agent's artifact and side effects, not just its explanation.
- For subjective quality, write a task-specific rubric with anchored examples. Blind the candidate identity, randomize order, and compare swapped order where position may matter. Calibrate model judges against human labels; examine disagreements and verbosity/style bias.
- A model judging its own answer is weak evidence. Multiple agreeing judges may share errors. Keep uncertainty and adjudication visible rather than calling agreement ground truth.
- For retrieval, measure whether relevant permitted evidence is retrieved and whether answers are supported by it. For tool agents, assess action correctness, authorization, completion, retries, and side effects. For UX, measure user task success and recovery as well as preference.

## Run and decide

1. Predeclare release criteria by consequence: accepted task rate, severe failures, relevant slices, latency, cost, and required human intervention. Thresholds are product decisions, not research constants.
2. Run baseline and candidate from matched clean states. Retain case-level outcomes, artifacts, configuration, tool trace, tokens/cost, elapsed time, and failures. Count failed/aborted runs; distinguish environment failures without silently dropping them.
3. Repeat stochastic cases as budget permits. Report sample size and uncertainty with justified methods. Cluster correlated cases/reruns appropriately; repeated samples of one case are not new independent tasks. Zero observed incidents is not a zero-risk guarantee.
4. Inspect regressions and slice performance even when aggregate results improve. If data are insufficient, say so; do not invent precise confidence or promote a rubric-only walkthrough to a live run.
5. For release, connect offline results to staged exposure, monitoring, and recovery. Version the complete behavioral configuration. Track drift and add production failures as future regression cases while maintaining a fresh holdout.

## Output and evidence

Deliver the dataset/split description, configuration, graders, actual results (or clearly labeled plan), release decision with limitations, and regression follow-ups. Do not fabricate an evaluation run.

R16/R17 motivate system-wide checks; R18 supports multidimensional evaluation; R19 identifies judge biases; R20 supports adversarial cases. None proves a particular sample count or passing threshold. See the [research register](../../docs/current/research-evidence.md).
