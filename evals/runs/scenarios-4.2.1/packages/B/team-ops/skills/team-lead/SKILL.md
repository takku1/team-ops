---
name: team-lead
description: "Coordinate multi-step coding work: task dependencies, selective workers, one implementation owner, evidence-based acceptance, and run budgets. Small edits stay inline; planning alone never dispatches agents."
---

# Team Lead

The main session is the controller and sole integrator. Roles are capabilities you call when useful, not a roster to instantiate. Keep the user's goal, current artifact, blockers, and next decision clear.

## Choose the smallest workflow

| Work | Route |
|---|---|
| Small reversible edit | Implement and check inline; no board or worker |
| Ordinary change | Implement, inspect the diff, verify |
| Unknown cause or handed-over diagnosis | Investigate load-bearing claims before editing |
| Changed trust boundary, auth, secrets, untrusted input, or dependency | Add the relevant secure-review mode |
| Consequential architecture or interface decision | Use plan-design-review before dependent implementation |
| Review-only, design-only, or security-only | Use that skill directly; do not bootstrap the workflow |

Use plan-work-breakdown for multi-piece work. Each ready task needs criteria, dependencies, one owner, a write scope, and a deciding check. Keep coupled implementation with one builder; disjoint paths are insufficient when contracts or generated outputs are shared.

## Admit workers selectively

Follow the user's and host's delegation authorization. Existing authorization persists; do not repeatedly ask. Without it, work inline. A worker needs a concrete benefit: independent consequential review, isolation of a large investigation, or genuinely independent ready work.

Start with one builder and, when useful, one supporting worker concurrently. This is an adjustable starting point, not a mandatory cap or proven optimum. Add capacity only when it shortens the critical path enough to cover briefing, checks, and integration. Workers do not spawn workers. Reuse a suitable worker rather than resetting its context and failed-attempt history.

Before dispatch, check [host support and fallbacks](../../references/host-compatibility.md), then read [the coordination contract](references/coordination.md). If a named agent is unavailable, run the role inline or use an authorized generic worker with a bounded brief; never repeatedly attempt an unsupported type. Brief with criteria, scope, input artifact, evidence pointers, ruled-out approaches, authority, and budget. Reviewers get criteria and the target without the author's reasoning or confidence. Use isolated briefs where supported; never assume inherited context.

## Control execution

- One writer per overlapping scope, including generated files and shared status. Assign one integration owner. Pause conflicting writes during checks or use an immutable snapshot.
- For work spanning workers or sessions, maintain one compact task/evidence board owned by the controller. Workers send deltas and evidence pointers. Dependencies and message recipients are separate graphs. No model calls for idle polling or routine heartbeats.
- Assign final verification once. Builders use focused feedback checks; reviewers request discriminating checks; the verifier observes deciding checks on the integrated artifact. Accept trustworthy current execution records, not unsupported reports. Do not have every role launch the same full suite.
- Where duplicate expensive checks recur, use the optional runner in the contract. It coordinates checks, not agents or permissions.
- Track a run-wide budget and task limits in units exposed by the host. Unknown token/cost measurements stay unknown. Count repairs, waits, review, and integration.
- Keep stable issue IDs across repairs and replacement workers. Two repairs without new discriminating evidence trigger diagnosis or a changed approach. Renaming a task does not reset history. At a real limit, leave a resumable artifact and next action.

## Accept and close

Accept only when the current integrated artifact satisfies criteria, applicable checks/reviews, and has no unresolved blockers. A worker's `done` is a report, not acceptance. Settle conflicts with evidence; route repairs to the implementation owner. Nits do not reopen accepted work.

Continue authorized reversible work. Escalate unresolved scope choices, risk acceptances, and actions outside existing authority; prepare a concrete result before requesting a decision.

Report the result, material checks and limitations, and remaining decisions. Mention workers and measured cost when relevant; skip ceremonial reports for inline roles. After a failed run, append a short blameless record to the existing tracker: impact/cost, detection, contributing factors, failed approaches, and checkable improvements. Read relevant recent failures next time; repeated failures become evals.

Evidence: R13, R19, R21-R25. Worker counts, board format, and repair limits are defaults to evaluate. [Register](../../references/research-evidence.md).
