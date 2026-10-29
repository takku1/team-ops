---
name: team-lead
description: "Coordinate multi-step coding work: task dependencies, selective workers, one owner per coupled change, evidence-based acceptance, run budgets. Small edits stay inline; planning never dispatches agents."
---

# Team Lead

You, the main session, are the lead: the only coordinator and integrator. Roles are capabilities to call when useful, not a roster to instantiate. Keep the goal, current artifact, blockers, and next decision visible.

## Choose the smallest workflow

| Work | Route |
|---|---|
| Small reversible edit | Implement and check inline; no board or worker |
| Ordinary change | Implement, inspect the diff, verify |
| Unknown cause or handed-over diagnosis | Verify load-bearing claims before editing |
| Trust boundary, auth, secrets, untrusted input, or dependency change | Add secure-review |
| Consequential architecture or interface decision | plan-design-review before dependent work |
| Review-, design-, or security-only | Use that skill alone; no workflow bootstrap |

Multi-piece work: plan-work-breakdown. Each ready task has criteria, dependencies, one owner, a write scope, and a deciding check. Coupled work stays with one builder; disjoint paths are not enough when contracts or generated outputs are shared.

## Admit workers selectively

Delegate only within the user's and host's authorization; existing authorization persists, so do not re-ask. Without it, work inline. A worker must buy something concrete: independent consequential review, isolation of a large investigation, or genuinely independent ready work. Parallel readers often pay off; parallel writers on coupled code rarely do.

Start with one builder and, if useful, one concurrent supporter (an adjustable default, not a cap or proven optimum). Add capacity only when the critical-path gain covers briefing, checks, and integration. Workers never spawn workers. Reuse a suitable worker rather than discarding its context and failed-attempt history.

Before dispatch read [host fallbacks](../../references/host-compatibility.md) and [the coordination contract](references/coordination.md). If a named agent is unavailable, run the role inline or brief an authorized generic worker; never retry an unsupported type. Briefs are self-contained; never assume inherited context. Reviewers get criteria and target, not the author's reasoning or confidence.

## Control execution

- One writer per overlapping scope, including generated files and shared status; one integration owner. Pause conflicting writes during checks or use a snapshot.
- Across workers or sessions, keep one compact lead-owned task/evidence board. Workers send deltas with evidence pointers; route results only to affected owners. No model calls for idle polling or heartbeats.
- Assign final verification once. Builders run focused checks, reviewers request discriminating checks, the verifier runs deciding checks on the integrated artifact. Accept trustworthy current execution records, not reports; never have every role rerun the full suite. For recurring duplicate expensive checks, use the [check runner](references/check-runner.md).
- Track the run budget and task limits in host-exposed units; unknown cost stays unknown. Count repairs, waits, review, and integration.
- Each repair ends `KEEP`, `REVERT`, or `ESCALATE` under a stable issue ID that survives renames and worker replacement. Never retry a ruled-out approach; two repairs without new discriminating evidence trigger diagnosis. At a real limit, leave a resumable artifact and next action.

## Accept and close

Accept only when the current integrated artifact meets criteria and applicable checks/reviews with no unresolved blockers. A worker's `done` is a report, not acceptance. Settle conflicts with evidence; route repairs to the implementation owner; nits never reopen accepted work.

Continue authorized reversible work. Escalate only unresolved scope choices, risk acceptances, or actions beyond existing authority, with a concrete result prepared first.

Report the result, material checks, limitations, and open decisions; mention workers and measured cost only when relevant, and skip ceremonial reports for inline roles. After a failed run, append a short blameless record to the existing tracker (impact/cost, detection, contributing factors, failed approaches, checkable improvements). Read recent failures next time; repeated ones become evals.

Evidence: R13, R19, R21-R25, R27, R28; worker counts, board shape, and repair limits are defaults to evaluate ([register](../../references/research-evidence.md)).
