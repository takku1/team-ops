---
name: plan-work-breakdown
description: Decompose a deliverable into small, independently verifiable work items (WBS for projects, vertical slices or story splitting for product work), each with acceptance criteria. Use when work is too big to estimate, assign, or review, or when starting a project or epic. Not for estimating dates (use plan-estimate-forecast after this).
---

# Work Breakdown

## Policy
- **100% rule:** the children of a node cover all of its scope and nothing outside it.
- **Decompose to deliverables, not activities.** Nouns ("password reset flow"), not verbs ("do backend").
- **Prefer vertical slices.** Each item delivers a thin end-to-end, user-observable increment over a layer-by-layer split.
- **Leaf size:** one independently verifiable, reviewable outcome. About 1-3 human workdays is a planning heuristic; for AI work, use bounded context, clear interfaces, and a cheap verification oracle instead of translating tokens into days.
- **Every leaf has acceptance criteria** written as checkable statements (Given/When/Then is fine), and it inherits the team's Definition of Done (build-definition-of-done).
- **INVEST** for stories: Independent, Negotiable, Valuable, Estimable, Small, Testable.

## Splitting patterns
Workflow steps · business-rule variations · happy path first, then edge cases · data variations · interface variations (API first, UI later) · CRUD operations · defer performance or quality ("make it work, then make it fast") · spike plus implementation.

## Logic
1. Require a deliverable or epic statement plus its goals and non-goals (pull them from the design doc if one exists).
2. Split top-down and apply the 100% rule at each level.
3. Stop when the leaves meet the size and testability bar. Mark unknowns as spikes.
4. Order the leaves by dependency and risk, putting risky unknowns early.
5. Name an owner and order dependencies. Invoke ownership or forecasting skills only if those decisions are requested or needed; routine implementation can proceed to build-implementation-loop.

## Output
- Tree: id | item | acceptance criteria | depends on | spike?
- Risk-first sequence for the first 2 weeks

## Pitfalls
- Horizontal slicing ("DB layer", "API layer"), which delays integration risk to the end.
- Leaves with "done when it's done" criteria.

## Sources
PMI *Practice Standard for Work Breakdown Structures*; Bill Wake, INVEST (2003); Richard Lawrence, "Patterns for Splitting User Stories"; Mike Cohn, *User Stories Applied*.

## Research and application

For AI execution, each leaf needs its relevant inputs, writable scope, dependency contract, and verification oracle. Parallelize only independent work with integration ownership and available authorization. A plan should not trigger agents by itself. Keep security and data integrity in every relevant slice.

Evidence: R12, R13; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
