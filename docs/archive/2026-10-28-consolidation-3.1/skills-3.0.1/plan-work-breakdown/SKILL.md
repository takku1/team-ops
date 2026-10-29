---
name: plan-work-breakdown
description: Decompose a deliverable into small, independently verifiable tasks (vertical slices for product work, a WBS for projects), each with acceptance criteria, an owner role, a write scope, and an oracle, so agents can take them one at a time or in parallel without colliding. Use when work is too big to assign, review, or verify in one piece, or when starting an epic. Not for dates or budgets (use plan-forecast-recovery after this). Lead playbook.
---

# Work Breakdown

**Role:** lead (team-lead), before assigning tasks. **Returns:** a task tree in which every leaf has an owner role, a write scope, an oracle, and its dependencies.

## Rules

- **100% rule:** a node's children cover all of its scope and nothing outside it.
- **Deliverables, not activities.** Nouns ("password reset flow"), not verbs ("do backend").
- **Vertical slices.** Each leaf delivers a thin, end-to-end, observable increment. Security and data integrity belong in every slice they touch, not in a final hardening slice.
- **Leaf size for agents:** one bounded context, a clear interface to its neighbors, and a cheap oracle. Do not translate tokens into days. For human work, one to three days is a planning heuristic.
- **Checkable acceptance criteria** on every leaf (Given/When/Then is fine). Each inherits the Definition of Done (build-definition-of-done).
- **One owner role and a write scope** per leaf. Leaves with overlapping scopes are sequenced or merged, never run in parallel.
- **Unknowns become spikes.** A leaf whose cause or approach is unknown becomes a time-boxed investigation whose oracle is the question it must answer.
- A plan does not dispatch agents. That follows team-lead's setup decision and the user's authorization.

## Procedure

1. Start from the deliverable, its goals, and its non-goals (from the design note if there is one).
2. Split top-down, applying the 100% rule at each level, until leaves meet the size and oracle bar.
3. Order by dependency and risk, with risky unknowns first.
4. Assign owner roles and write scopes. Mark which leaves can run in parallel (disjoint scopes, no dependency) and who integrates them, normally the lead.

Splitting patterns: workflow steps · business-rule variations · happy path first, then edge cases · data variations · interface variations (API first, UI later) · CRUD operations · make it work, then fast · spike plus implementation.

## Output

- Tree: id | item | acceptance criteria | owner role | write scope | oracle | depends on | parallel?
- The risk-first sequence for the first few tasks

## Pitfalls

Horizontal slicing ("DB layer", "API layer"), which pushes integration risk to the end. "Done when it's done" criteria, or leaves with no runnable oracle. Parallel leaves that both touch a shared file such as a registry, lockfile, or status doc.

Evidence: PMI *Practice Standard for Work Breakdown Structures*; Wake, INVEST (2003); Lawrence, "Patterns for Splitting User Stories". R12 and R13 (bounded, verifiable steps for agents). See the [research register](../../docs/current/research-evidence.md).
