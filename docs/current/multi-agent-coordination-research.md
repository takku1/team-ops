# Multi-agent coordination: suite audit and proposed experiment

Date: 2026-10-28. Research and design proposal; no orchestration changes implemented.

## Recommendation

Use an event-driven controller, a shared task/evidence board, one implementation owner per coupled change, and a controlled build runner. Activate isolated investigators and independent reviewers only when their contribution justifies their context and coordination cost. Represent dependencies explicitly; route messages selectively.

This is a sparse, centrally governed graph with shared artifacts. The useful analogy is a scheduler and build system. Quantum computing is not required by any of the mechanisms proposed here.

Distinguish two graphs:

- Task graph: prerequisites, affected artifacts, checks, and acceptance. A dependency DAG within each attempt; rework creates a new versioned attempt rather than silently resetting completed work.
- Communication graph: who receives which event or evidence pointer. Sparse, with temporary direct edges for a specific dependency question. It need not mirror the task graph.

## What the current suite actually says

Inspected the core orchestration, implementation, context, review, verification, work breakdown, and evaluation skills; all five agent definitions; delegation/check references across both plugins; README, STATUS, research register, relevant eval prompts and historical field report.

The current README identifies version 3.1.0. `team-lead` already makes the main session the controller, defaults phases to inline, prohibits recursive spawning, requires scoped briefs, and specifies one writer per path. `plan-work-breakdown` records dependencies and says planning does not dispatch agents. Agent descriptions make spawning optional. These are useful foundations.

The reported six-agent run is not explained by these defaults alone. Its transcript, installed plugin version, user authorization, and dispatch decisions were not available. Historical reports describe older versions; they cannot establish the cause of this run. Six agents over an entire run is also different from six concurrent writers.

Specific gaps:

| Location | Existing behavior | Potential cost or ambiguity |
|---|---|---|
| `team-lead`, phase selection and acceptance | Inline review reruns checks; lead reruns deciding checks or routes to verify | No assignment identifying which execution constitutes final verification |
| `build-implementation-loop`, change and verify | Implementer runs required checks | Appropriate local feedback, but potentially followed by duplicate full suites |
| `build-code-review`, step 3 | Reviewer reruns cheap reported checks | No shared execution identity or distinction between a new independent test and identical repetition |
| `build-definition-of-done`, accept work | Explicitly rerun acceptance and required checks | Can repeat implementation, review, and lead work |
| `ai-context-management`, handoffs | Cited summaries and fixed reports | No shared task revision, artifact identity, or event acknowledgement |
| `team-lead`, briefs and stop rule | Per-task budget; two rounds without new evidence | No mandatory run-wide spend ceiling, spawn admission test, or structured evidence-change record |
| Agent definitions and integration guidance | Separate scratch/build lanes; isolated worktrees | Protects processes but can duplicate cold builds, caches, and environment setup |

These are plausible mechanisms, not observed attribution of the user's run. Independent verification remains valuable; reducing duplicates must preserve it.

## Research and what it supports

1. **Towards a Science of Scaling Agent Systems**, Kim et al., arXiv preprint, revised April 2026. [Paper](https://arxiv.org/abs/2512.08296v3), [full text](https://arxiv.org/html/2512.08296v3). Controlled comparison of 260 configurations across six benchmarks, five architectures, and three model families. Architecture benefits depend strongly on task structure; tool-heavy work incurs overhead and centralized verification can limit error propagation. Its predictive fit is moderate and large collectives remain an open question. Supports task-aware selection, not a universal optimal team size.

2. **Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems (AgentPrune)**, Zhang et al. [Paper](https://arxiv.org/abs/2410.02506), [full text](https://arxiv.org/html/2410.02506v1). Prunes spatial and temporal communication edges. Reports 28.1–72.8% token reductions when integrated into tested frameworks. This is evidence that redundant messages and rounds can be removed in those experiments, not a savings forecast for this suite or proof that manual pruning reproduces learned pruning.

3. **G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks**, Zhang et al., ICML 2025. [Proceedings](https://proceedings.mlr.press/v267/zhang25cu.html). Learns task-dependent communication graphs; experiments span six benchmarks, including HumanEval. Direct academic precedent for the graph intuition. Short code benchmarks do not establish repository-scale performance, and training a graph model is not justified for this suite before simpler routing is evaluated.

4. **Why Do Multi-Agent LLM Systems Fail? (MAST)**, Cemri et al., arXiv v3, October 2025. [Paper](https://arxiv.org/abs/2503.13657v3), [full text](https://arxiv.org/html/2503.13657v3). Dataset includes 1,600+ annotated traces across seven frameworks; taxonomy development uses 150 expert-guided traces. Fourteen failure modes include repeated steps, lost history, unrecognized termination conditions, ignored inputs, and incomplete verification. Supports explicit state, completion conditions, and failure-oriented evaluation. It does not validate this proposed controller.

5. **Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture**, Han and Zhang, 2025 preprint. [Paper](https://arxiv.org/abs/2507.01701). Shared workspace and state-dependent agent selection evaluated on knowledge, reasoning, and math tasks. Supports a shared-board research direction. Its all-information-sharing formulation is not a reason to inject the entire board into every agent's prompt.

6. **Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead**, Yu et al., March 2026 position paper. [Paper](https://arxiv.org/abs/2603.10062). Identifies consistency and access-control gaps in shared/distributed agent memory. Architectural framing, not empirical proof of a speedup. Relevant to stale evidence and versioned state.

7. **How we built our multi-agent research system**, Anthropic, June 2025 practitioner report. [Article](https://www.anthropic.com/engineering/multi-agent-research-system). Describes parallel research benefits and substantial token costs; notes coding is less easily parallelized. Its approximately 15x figure is relative to chat interactions, not a universal multiplier over a single coding agent. Useful operational evidence, distinct from academic controlled experiments.

This is a targeted primary-source review, not a systematic review or replication. Benchmark gains, trained graph methods, and research-task results should not be presented as measured gains for this suite.

## Proposed coordination contract

### Controller and workers

Keep the main session as controller; do not add a supervising LLM above the existing lead. It selects ready tasks, assigns ownership, resolves conflicting evidence, and accepts the final artifact. Ordinary coupled coding work has one builder. Other roles are callable capabilities, not permanently running agents.

Use deterministic code for leases, queues, hashing, budgets, event delivery, and duplicate-command suppression. Invoke the controller model when a decision requires judgment. A software heartbeat can detect a lost worker without prompting an LLM for repeated status updates.

Initially allow the builder plus one supporting worker concurrently. This is a conservative experimental setting, not a research-derived optimum. Expand when independent work is ready and measured useful output exceeds briefing, verification, and integration cost. Disjoint filenames alone do not prove independence: shared contracts, generated artifacts, data, and integration requirements matter.

### Shared board

Keep small structured records on disk for a prototype, with one controller writer. Workers return structured events; they do not all edit one status document. A durable transactional store can replace this if restart recovery or actual concurrent scheduling requires it.

Task fields:

```text
task_id, attempt, state, owner, write_scope, dependencies,
acceptance, input_artifact_id, budget_remaining,
evidence_refs, blocking_findings, next_action
```

States: ready -> running -> awaiting_review -> awaiting_verification -> accepted. A blocking finding opens a linked repair attempt for the same owner. Terminal states also include blocked and cancelled. Accept only against the current artifact and all applicable gates; a worker's done report is not acceptance.

Events carry an event ID, task/attempt ID, observed artifact, result pointer, and requested action. Deduplicate repeated deliveries. Acknowledge durable recording before treating a completion as received. Scope leases must prevent late output from an old worker overwriting a reassigned task; a lease expiry alone is insufficient while the old process can still write.

### One controlled build execution path

Separate reasoning from command execution. The builder can request cheap local checks while editing. Expensive build/test requests go through a runner that deduplicates identical in-flight requests and records results. Reviewers can request a new discriminating check without independently launching the entire suite.

Check identity includes the actual input snapshot (including relevant untracked/generated files), command and arguments, toolchain, dependencies, relevant environment, and fixtures. A commit SHA alone is insufficient for a dirty worktree. Logs and artifacts live on disk; messages carry exit status, important output, and references. Preserve secrets outside prompts and records.

Freeze or snapshot inputs for a run; otherwise concurrent edits make its result ambiguous. Invalidate affected results when inputs change. Do not reuse results for external-state, flaky, time-dependent, or inadequately fingerprinted checks. Explicitly requested independent reruns remain separate executions.

The final verifier chooses acceptance checks and observes their execution on the integrated snapshot through the controlled runner. It is independent of the builder's self-assessment. The controller checks that evidence and scope match; it need not launch the same full suite again. Runtime/CI policies requiring a fresh run still apply.

### Context and messaging

Send objective, acceptance, bounded scope, relevant contracts, artifact identity, verified facts, failed approaches, and evidence pointers. Avoid full conversation forks by default where the host supports isolated briefs. Preserve authoritative instructions and relevant uncertainty.

Send events for completion, a blocker, a changed dependency, or a decision request. Idle workers need no model calls. Direct peer messages are appropriate for a concrete contract question; durable decisions return to the board. Reviewers receive criteria and code, without the author's persuasive narrative.

Two failed repairs of the same finding without new discriminating evidence trigger diagnosis rather than another rebuild or worker. Fingerprint the finding/check so renaming a task or spawning a fresh agent cannot reset its history. Keep the suite's existing stop rule, but make its accounting global and explicit.

## Smallest suite change to evaluate

1. Amend `team-lead` with adaptive worker admission, a run-wide budget, structured task/attempt state, and assignment of the final verification owner.
2. Amend context handoffs with artifact/task IDs and delta events; link large evidence instead of repeating it.
3. Align implementation, review, and verification: local regression checks, targeted independent findings, one designated final verification execution. Remove automatic duplicate full-suite work without removing required checks.
4. Add a small runner/ledger only after the protocol is explicit. Skill prose cannot enforce leases, atomic state, durable event delivery, or build deduplication.
5. Add scenarios for duplicate build requests, stale green results after edits, a late worker report, overlapping generated outputs, repeated repair under a new worker name, and an unrelated task continuing while another is blocked.

Do not create additional always-loaded skills for each mechanism. Put compact rules in the existing lead and reference the detailed protocol when needed.

## Evaluation before adoption

Compare (A) a single agent, (B) current suite defaults, and (C) this controller protocol on matched clean task snapshots. Include a tiny fix, a tightly coupled feature, independent investigation, independent implementation slices, and a difficult regression. Pilot with representative tasks; use a larger held-out set before claiming a general gain.

Hold model, permissions, acceptance oracles, and environment constant. Compare equal total spend ceilings, and report actual spend and time; separately measure minimum cost to achieve a chosen quality level. Count failed and aborted runs. Counterbalance execution order and distinguish repeated runs of one task from independent tasks.

Record acceptance and escaped defects; input/output and cached tokens where exposed; money per accepted task; elapsed and human time; spawns and peak concurrency; duplicate full builds; build compute time separately from LLM tokens; rework and repeated findings; stale-evidence incidents; and controller overhead. Trace the same task across worker replacement.

Adopt only if acceptance quality is maintained and the relevant cost/time tradeoff improves. No savings percentage or best agent count is established for team-ops today.
