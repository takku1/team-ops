---
name: ai-workflow-efficiency
description: Optimize an AI-assisted or agent-team workflow for verified quality, total cost, elapsed time, and human effort. Covers task routing, tool strategy, reasoning effort, retries, caching, how many agents to run, real review and integration capacity, and team-level delivery measures (accepted changes, rework, escaped defects, human minutes). Use when sizing or budgeting an agent team, comparing setups, or asking whether the team is getting faster or better. Not for claiming a universal best model from benchmark rankings, or for evaluating individuals. Lead playbook.
---

# AI Workflow Efficiency

**Role:** lead (team-lead), when setting budgets or deciding how many agents to run, and later when measuring the team. **Returns:** a configuration with its measurements, or a proposal labeled untested.

## Define the objective

Name the task mix, the minimum correctness and safety bar, and the limits on money, wall time, human attention, and allowed actions. Optimize a constrained trade-off: lowest cost or time for acceptable outcomes, or best verified quality within a budget. Never save tokens by dropping required evidence or verification.

Count the whole attempt: retrieval, model calls, tool latency, retries, review, repair, and integration. **Cost per accepted task** = total cost including failures ÷ accepted tasks; with zero accepted it is undefined, not zero. Keep human minutes, machine cost, and elapsed time separate unless the user supplies a conversion rate. Generation latency is not end-to-end time.

## Start simple, escalate on evidence

- Scripts and deterministic commands for exact transformations, calculations, and checks; models for ambiguity, synthesis, alternatives, and diagnosis.
- Start with one bounded workflow at a fitting capability. Compare cheaper routing or more effort on real task types. Never invent model rankings or change a user-selected model without authorization.
- Batch independent reads and calls; sequence dependent mutations and approvals. Cache only with a source or version key and an invalidation rule.
- Retry transient failures a bounded number of times. For mutating tools, inspect the outcome before retrying and use idempotency where supported.
- Extra samples, review passes, or agents need a reason: independent failure detection, separable work, or a measured gain. Correlated agreement is not proof.
- Stop when acceptance and verification pass. After a diagnosed limitation, escalate capability or re-split. Stop no-information loops at the budget and leave a resumable state.

## Team capacity

- **Agents do not multiply throughput.** Every agent's output costs the lead briefing, review, and integration, and the user decisions. Size the team to that capacity, not to how many agents could be spawned.
- **Compute capacity once.** If a measured focus factor already includes interrupts or support, do not subtract them again. Show units and assumptions.
- **WIP:** one task in progress per writable scope. Parallel agents need disjoint scopes, isolated worktrees, and an integrator.
- **Single points of knowledge:** if only one session or person understands a subsystem, record it in the repo brief or handoff and name the backup risk.
- Reserves of 15 to 30 percent for interrupts, review, and maintenance are starting hypotheses; tune them to measured interrupt rates.

## Measure the team

Measure at team or workflow level. Never rank individual people, and do not compare agents doing different tasks as if alike.

| Signal | Measure |
|---|---|
| Throughput | accepted changes per period; lead time from start to accepted |
| Instability | rework rate; defects that escaped review and verification |
| Cost | total cost per accepted task, failures included |
| Human effort | active human minutes per accepted task; interventions |
| Flow | time waiting on review, checks, or decisions versus working |

Read throughput and instability together: speed bought with rework is a warning. Pair them with outcomes (users served, SLOs met) and do not turn them into targets. Pick the biggest constraint, run one experiment with a hypothesis and a review date, and watch the measures. Lines of code, commits, and agent turns are not productivity.

## Compare configurations

Use a fixed representative task set plus held-out tasks, matched starting states, explicit success criteria, and equal limits; counterbalance order where feasible. Record contamination, environment failures, and repeats. Compare accepted correctness, severe failures, total cost, elapsed time, and human rework, and report uncertainty and per-task trade-offs instead of one unqualified winner. Team versus single agent is the main use; grading design is in ai-evaluation. Without a comparative run, label the configuration a proposal.

Evidence: R12 and R13 (test interfaces against simple baselines), R14 (measure context overhead), R15 (perceived speed is not measured time), R08 (SPACE) and P03 (DORA) for multidimensional team-level measures. No agent count or model is proven optimal. See the [research register](../../docs/current/research-evidence.md).
