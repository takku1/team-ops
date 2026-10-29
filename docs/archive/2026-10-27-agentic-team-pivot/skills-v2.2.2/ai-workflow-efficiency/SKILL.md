---
name: ai-workflow-efficiency
description: Optimize AI-assisted workflows for verified quality, total cost, elapsed time, and human effort. Use when choosing task routing, tool strategy, reasoning effort, retries, caching, or authorized concurrency, or comparing AI setups. Not for claiming a universal best model from benchmark rankings.
---

# AI Workflow Efficiency

## Define the objective

Identify the task distribution and minimum correctness/safety requirements. Record limits on money, wall time, human attention, and allowed actions. Optimize a constrained trade-off: lowest total cost/time for acceptable outcomes, or best verified quality within a stated budget. Never save tokens by dropping required evidence or verification.

Count the whole attempt: retrieval, model calls, tool latency, retries, review, repair, and integration. Report cost per accepted task as total cost including failures divided by accepted tasks; if none succeed it is undefined, not zero. Keep human minutes, machine cost, and elapsed time separate unless the user provides an explicit conversion.

## Start simple, escalate on evidence

- Use deterministic commands/scripts for exact transformations, calculation, and verifiable checks. Use models for ambiguity, synthesis, design alternatives, and diagnosis.
- Start with a single bounded workflow and appropriate capability. Compare cheaper routing or greater reasoning effort on actual task types; do not invent model rankings or change a user-selected model without authorization.
- Batch independent reads/tool calls where safe. Sequence dependent mutations and approvals. Cache stable results only with a source/version key and invalidation rule; stale evidence is not a saving.
- Retry transient failures with bounded attempts and observed state. For mutating tools, inspect the outcome before retrying and use idempotency where supported. Do not duplicate an action because the response was lost.
- More sampling, review passes, or workers require a reason: independent failure detection, separable work, or a measured quality gain. Correlated model agreement is not proof. Parallel workers require authorization, disjoint ownership, an integration plan, and budget for review.
- Stop when acceptance and applicable verification pass. Escalate capability or revise decomposition after a diagnosed limitation; stop repeated no-information loops at the explicit budget. Preserve a resumable artifact when blocked.

## Compare configurations

Use a fixed representative task set and held-out tasks, matched starting states, explicit success criteria, and the same limits. Randomize/counterbalance order where feasible; record contamination, environment failures, and repeated runs. Compare accepted correctness, severe failures, total cost, elapsed time, and human rework. Report uncertainty and task-specific trade-offs, not a single unqualified winner. Use ai-evaluation for model/product quality or grading design.

Deliver a selected configuration, supporting measurements, and fallback/escalation criteria. If no comparative run occurred, label the configuration a proposal rather than a demonstrated optimization.

Evidence: R12/R13 support testing interface design and simple baselines; R14 motivates measuring context overhead; R15 warns against substituting perceived speed for measured time. Results are setting-specific, not proof of a universal optimal agent count or model. See the [research register](../../docs/current/research-evidence.md).
