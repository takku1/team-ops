---
name: ai-evaluation
description: "Evaluate AI features, prompts, agents, and agent-team setups, and size their cost: representative cases, independent oracles, calibrated judges, cost per accepted task, team vs solo. Not for deterministic unit tests."
---

# AI Evaluation and Efficiency

Grade behavior independently of its producer, using executable oracles first and fresh-context judges when needed and authorized. Return configuration, cases, observed results (or a plan labeled as a plan), and a decision with limits.

## Cases

State the task, users, cost of failure, baseline, and proposed change. Record model and provider version, prompts, tools and permissions, retrieval corpus, decoding settings, and environment; hidden provider changes are a stated reproducibility limit.

Draw cases from representative authorized examples, known failures, boundaries, ambiguous inputs, and adversarial trust crossings, including cases where the right move is to abstain, ask, or not call a tool. Keep a held-out set: tuning on it makes it a development set. Record each case's origin, expected behavior, and slice.

## Oracles

- **Executable checks first:** correctness, schemas, calculations, permissions, resulting state. Test the artifact and side effects, not the explanation.
- **Rubrics** for subjective quality, with anchored examples. Blind candidate identity, randomize and swap order, calibrate model judges against human labels, and watch verbosity bias.
- **Agreement is not truth.** Self-judgment is weak evidence; agreeing judges can share errors.
- Retrieval: is permitted relevant evidence found and used. Tool agents: action correctness, authorization, side effects. UX: task success and recovery.

## Cost and capacity

- **Cost per accepted task** = total cost including failed runs ÷ accepted tasks; undefined, not zero, when none pass. Count retrieval, retries, review, repair, and integration. Keep dollars, human minutes, and elapsed time separate unless the user gives a conversion. Generation latency is not end-to-end time.
- **Start simple.** Scripts for exact work, models for judgment. One bounded workflow first; more samples, reviewers, or agents need a reason (independent failure detection, separable work, a measured gain). Never change a user-chosen model without authorization.
- **Coordination must earn its cost.** Count briefing, context transfer, checks, and integration. Independent work may parallelize; coupled contracts need explicit ownership. Do not double-count interrupts already included in measured capacity.
- **Measure the team, never individuals:** accepted changes and lead time, rework and escaped defects, cost per accepted task, human minutes, time waiting. Read speed and rework together. Lines of code, commits, and turns are not productivity.

For orchestration comparisons, record spawns and peak concurrency, duplicate expensive checks, runner compute separately from LLM tokens, controller overhead, rework by stable issue ID, and stale-evidence incidents. Compare solo, current workflow, and candidate from matched snapshots and equal total ceilings; report actual spend and acceptance quality. No agent count or saving is presumed optimal.

## Run and decide

1. Predeclare criteria by consequence: accepted rate, severe failures, slices, latency, cost, human intervention.
2. Run baseline and candidate from matched clean states with equal limits; counterbalance order. Keep case-level outcomes, traces, cost, and time. Count failed and aborted runs; label environment failures, never drop them.
3. Report sample size and uncertainty. Reruns of one case are not independent tasks; zero incidents is not zero risk.
4. Inspect slices and regressions even when the aggregate improves. Report trade-offs, not one unqualified winner. Never promote a walkthrough to a run.
5. For release, version the whole configuration, monitor drift, and turn production failures into regression cases.

Without a comparative run, label any configuration a proposal.

Evidence: R18, R19 (judge biases), R16, R17, R20, R13, R15 (perceived speed is not measured time), R21-R25, R08 and P03 (team-level, multidimensional measures). No sample count, threshold, agent count, or model is proven optimal. [Register](../../references/research-evidence.md).
