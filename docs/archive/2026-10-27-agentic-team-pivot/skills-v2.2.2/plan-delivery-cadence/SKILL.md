---
name: plan-delivery-cadence
description: Choose and run the team's delivery system, either Scrum (time-boxed sprints) or Kanban (continuous flow with WIP limits), with its events, artifacts, and flow metrics. Use when setting up a team's working rhythm, when sprints keep failing, or when flow is clogged. Not for org structure or metrics dashboards.
---

# Delivery Cadence (Scrum / Kanban)

## Choose
| Signal | Scrum | Kanban |
|---|---|---|
| Work type | product work, evolving scope | support, ops, platform, interrupt-heavy |
| Planning horizon | 1-4 week goals | continuous replenishment |
| Commitment | Sprint Goal | service level expectation (SLE) |
| Change mid-cycle | protect the Sprint Goal | pull anytime under the WIP limit |

Choose the minimum coordination needed. A solo builder can use a queue, WIP limit, and review of delivered outcomes; do not invent Scrum roles or ceremonies. Hybrid practice is valid but is not necessarily Scrum.

## Scrum policy (Scrum Guide 2020)
- Accountabilities: Product Owner (orders the backlog, owns the Product Goal), Scrum Master, Developers. Team of 10 or fewer.
- Events: Sprint Planning (sets the Sprint Goal), Daily Scrum (15 min, progress toward the goal), Sprint Review (demo working increments to stakeholders), Retrospective (pick at least one improvement and put it in the next sprint).
- Commitments: Product Goal → Product Backlog, Sprint Goal → Sprint Backlog, **Definition of Done → Increment** (build-definition-of-done).
- Plan by measured capacity (org-capacity-plan), never by wish.

## Kanban policy
- Visualize every work type. Columns follow the real workflow, e.g. `Ready → In Progress → Review → Test → Done`.
- **Explicit WIP limits per column.** Start with about team size, then tighten. Stop starting, start finishing.
- Explicit entry and exit policies per column.
- Track **cycle time, throughput, WIP, and work item age**. Publish an SLE (e.g. "85% of items done in 8 days").
- Find the single constraint (Theory of Constraints), subordinate the rest to it, then elevate it.
- Replenishment and review meetings run on a cadence even without sprints.

## Logic
1. Classify the work using the table and recommend Scrum, Kanban, or a hybrid with reasons.
2. Emit the board columns, WIP limits, events calendar, and metrics.
3. On a health check: flag items over the SLE age, columns over their WIP limit, blocked items older than 2 days, and sprints that missed their goal 3 times in a row (re-check capacity and splitting).

## Pitfalls
- "Scrum-but" with no Definition of Done and no review with real stakeholders.
- WIP limits that are never enforced.
- Velocity used as a performance target.

## Sources
Schwaber & Sutherland, *The Scrum Guide* (2020); Vacanti & Coleman, *The Kanban Guide* (2020); David Anderson, *Kanban*; Goldratt, *The Goal*.

## Research and application

Choose cadence empirically. Little's Law concerns consistent long-run averages; it does not prove that lowering WIP alone increases throughput. WIP/aging thresholds and meeting frequencies are local defaults. Track queue time as well as active work.

Evidence: R05, P02; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
