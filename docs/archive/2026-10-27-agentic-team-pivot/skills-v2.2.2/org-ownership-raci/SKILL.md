---
name: org-ownership-raci
description: Make ownership and decision rights explicit with RACI (work) and DACI (decisions), and with CODEOWNERS (code), so every item has exactly one accountable owner. Use when approvals stall, two people think they own something, nobody owns something, or a cross-team decision is stuck. Not for team structure (use org-team-topology).
---

# Ownership (RACI / DACI)

## Policy
- **One clear accountable decision-maker per consequential outcome** is this suite's default. Shared contributors and owning teams are valid. Resolve ambiguous authority before the affected release; do not block unrelated work or create a RACI for routine edits.
- **R** does the work. **A** signs off and answers for the outcome. **C** is consulted before the work (two-way). **I** is informed after (one-way).
- **Keep C small.** Each C adds a sync point. Move people to I unless their input changes the outcome.
- **Decisions use DACI**: one Driver, one Approver, Contributors, Informed. Record the result as an ADR (see plan-decision-record).
- **Code ownership is machine-readable.** Keep a `CODEOWNERS` file (or equivalent) so reviews route automatically. Each path needs at least one owning team, not a lone individual.
- **Ownership survives people.** Assign A to a role or team, and name the current person beside it.

## Logic
1. Require a task or deliverable list (a WBS output is ideal, see plan-work-breakdown).
2. Fill R/A/C/I per row. For decisions, fill the D/A/C/I roles instead.
3. Flag missing responsibility and unclear approval authority. Investigate approver queue time and workload; 7 live items or 3 consultees are discussion prompts, not research-backed limits.
4. Cross-check CODEOWNERS against the service owners from org-team-topology.

## Output
- Matrix: item | R | A | C | I
- Gaps: missing or double A, overloaded approvers, orphaned paths in CODEOWNERS
- Fix list with the proposed owner for each gap

## Pitfalls
- RACI for every micro-task. Apply it at the work-package or decision level.
- Treating A as "the manager". A should be the person closest to the outcome who has the authority to decide.

## Sources
PMI PMBOK responsibility assignment matrix; Atlassian Team Playbook (DACI); GitHub/GitLab CODEOWNERS docs.

## Research and application

RACI/DACI and one accountable owner are coordination defaults, not proven causal interventions. Expertise-aware review is evidence-informed; an AI worker is not the accountable human authority. Record actual decision rights, not invented approvers.

Evidence: R04; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
