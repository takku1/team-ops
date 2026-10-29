---
name: ai-evaluation
description: "Evaluate AI features, prompts, agents, or agent-team setups and size their cost: representative cases, independent oracles, calibrated judges, cost per accepted task, team vs solo. Not for unit tests."
---

# AI Evaluation and Efficiency

Judge AI behavior independently of whatever produced it: executable oracles first, fresh-context model judges only when needed and authorized.

**Return:** the configuration, cases, observed results (or a plan clearly labeled as a plan), and a decision with its limits. Without a comparative run, any configuration is a proposal.

## 1. Frame the comparison

State the task, users, cost of failure, baseline, and proposed change. Record everything that can change behavior: model and provider version, prompts, tools and permissions, retrieval corpus, decoding settings, environment. Hidden provider changes are a stated reproducibility limit.

## 2. Build cases

- **Start with error analysis:** read 30-50 real traces yourself, note each failure in one line, group the notes into a failure taxonomy, and count. Write cases for the top failures; a model may propose groupings, not replace the reading.
- Then add representative authorized examples, known failures, boundaries, ambiguous inputs, and adversarial trust crossings.
- Include cases where the right move is to abstain, ask, or not call a tool.
- Hold out a set. Once you tune on it, it is development data.
- Record each case's origin, expected behavior, and slice.

## 3. Choose oracles

- **Executable checks first:** correctness, schemas, calculations, permissions, resulting state. Test the artifact and its side effects, not the explanation.
- **Rubrics** only for subjective quality, with anchored examples. Blind candidate identity, randomize and swap order, calibrate model judges against human labels, watch for verbosity bias.
- **Agreement is not truth.** Self-judgment is weak evidence; agreeing judges can share errors.
- **By system:** retrieval, whether permitted relevant evidence was found and used; tool agents, whether actions and side effects were correct and authorized; UX, task success and recovery.

## 4. Count cost honestly

- **Cost per accepted task** = total cost including failed runs ÷ accepted tasks; undefined, not zero, when nothing passes. Include retrieval, retries, review, repair, and integration.
- Keep dollars, human minutes, and elapsed time separate unless the user supplies a conversion. Generation latency is not end-to-end time.
- **Measure the team, never individuals:** accepted changes, lead time, rework, escaped defects, human minutes, waiting time. Read speed together with rework. Lines, commits, and turns are not productivity.

## 5. Run and decide

1. Predeclare criteria by consequence: acceptance rate, severe failures, slices, latency, cost, human intervention.
2. Run baseline and candidate from matched clean states under equal limits, in counterbalanced order. Keep case-level outcomes, traces, cost, and time.
3. Count failed and aborted runs. Label environment failures; never drop them.
4. Report sample size and uncertainty. Reruns of one case are not independent tasks; zero incidents is not zero risk.
5. Inspect slices and regressions even when the aggregate improves. Report trade-offs, not one unqualified winner. A walkthrough is never a run.
6. For release, version the whole configuration, monitor drift, and turn production failures into regression cases.

## Agent and orchestration setups

Start simple: scripts for exact work, models for judgment, one bounded workflow. More samples, reviewers, or agents need a reason (independent failure detection, separable work, a measured gain) and must pay for briefing, transfer, checks, and integration. Never change a user-chosen model without authorization. Comparisons of solo, current, and candidate use equal ceilings and also record spawns, peak concurrency, duplicate checks, runner compute (apart from LLM tokens), lead overhead, rework by issue ID, and stale-evidence incidents.

Evidence: R08, R13, R15-R25, R29, R33, P03; no sample count, threshold, agent count, or model is proven optimal ([register](../../references/research-evidence.md)).
