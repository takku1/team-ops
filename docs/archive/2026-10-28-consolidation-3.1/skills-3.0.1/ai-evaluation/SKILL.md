---
name: ai-evaluation
description: Design and assess evaluations for AI features, agents, agent teams, prompts, retrieval, and workflow changes using representative cases, independent checks, calibrated grading, and quality/cost regression criteria. Use before consequential AI releases, when comparing configurations, or when testing whether an agent team beats a single agent. Not a replacement for deterministic software tests. Lead playbook.
---

# AI Evaluation

**Role:** lead (team-lead), when evaluating an AI feature or testing whether the agent team beats a single agent. Grading runs in a fresh context, never by the agent that produced the output. **Returns:** the case set and configuration, the graders, results or a plan labeled as a plan, and a decision with its limits.

## Define the claim and the cases

State the task, the users, the cost of failure, the baseline, and the proposed change. Record the model and provider version when exposed, prompts, tools and permissions, retrieval corpus or index, decoding settings, and environment. Hidden provider changes are a reproducibility limit; say so.

Build cases from representative authorized examples, known failures, boundaries, ambiguous or missing inputs, and adversarial trust crossings. Include cases where the right move is to abstain, skip a workflow, ask a question, or not call a tool. Keep development cases apart from the held-out set: tuning on the holdout makes it a development set. Record each case's origin, expected behavior, slice, and sensitive-data handling.

## Choose independent oracles

- **Executable checks first** for correctness, schemas, calculations, permissions, and resulting state. Test the agent's artifact and side effects, not its explanation.
- **Rubrics for subjective quality:** task-specific, with anchored examples. Blind candidate identity, randomize order, and swap positions where order may matter. Calibrate model judges against human labels and inspect disagreements and verbosity bias.
- **Agreement is not truth.** A model judging its own answer is weak evidence, and agreeing judges can share errors. Keep uncertainty and adjudication visible.
- **By system type:** retrieval, whether permitted relevant evidence is found and answers rest on it; tool agents, action correctness, authorization, completion, retries, and side effects; UX, task success and recovery, not only preference.

## Run and decide

1. Predeclare release criteria by consequence: accepted-task rate, severe failures, key slices, latency, cost, human intervention. Thresholds are product decisions.
2. Run baseline and candidate from matched clean states. Keep case-level outcomes, artifacts, configuration, tool traces, tokens and cost, elapsed time, and failures. Count failed and aborted runs; label environment failures but never drop them silently.
3. Repeat stochastic cases as budget allows and report sample size and uncertainty. Reruns of one case are not independent tasks. Zero observed incidents is not zero risk.
4. Inspect regressions and slices even when the aggregate improves. If the data are thin, say so; never promote a rubric walkthrough to a live run or invent confidence.
5. For release, tie offline results to staged exposure, monitoring, and recovery. Version the whole behavioral configuration, track drift, and turn production failures into regression cases while keeping a fresh holdout.

Deliver the case set and split, configuration, graders, actual results (or a labeled plan), the decision with its limits, and regression follow-ups. Never fabricate a run.

Evidence: R16 and R17 (system-wide checks), R18 (multidimensional evaluation), R19 (judge biases), R20 (adversarial cases). None sets a sample count or pass threshold. See the [research register](../../docs/current/research-evidence.md).
