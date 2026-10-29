---
name: plan-design-review
description: Write and review a proportionate design note or RFC before building anything consequential, then record the decision as an immutable ADR (Nygard or MADR format). Covers goals and non-goals, real alternatives, cross-cutting concerns (security, privacy, reliability, observability, cost), one approver, and supersede-not-edit decision history. Use when a change crosses components or services, changes a public API, schema, or wire protocol, adds a critical dependency, is hard to reverse, or someone asks "why did we do it this way?". Not for small changes that ordinary code review covers. Lead playbook.
---

# Design Review and Decision Records

**Role:** lead (team-lead), before assigning implementation. **Returns:** the design note, its open questions, and the ADRs to write.

A design note exists to surface trade-offs while code is still cheap to throw away. Most changes do not need one.

## When it is needed

Write a note when any of these hold; expand it to an RFC only when coordination, uncertainty, or irreversible impact justifies it:
- crosses component or service boundaries, or changes a public API, schema, or wire protocol
- adds a language, framework, datastore, or third-party dependency on a critical path
- touches authn/authz, capabilities, PII, payments, or data retention
- is hard to reverse (migrations, deletions, vendor lock-in)
- is large enough that several agents or several sessions will build it

Otherwise use the change description and normal review (build-code-review). If no trigger hits, say so and stop.

## Template

1. **Context and scope:** the problem and the current state, as facts with cites.
2. **Goals and non-goals:** measurable goals. Non-goals are what a reasonable reader might expect but is out of scope.
3. **Proposed design:** architecture, interfaces, data model, key flows.
4. **Alternatives considered:** the credible ones, including no change when that is meaningful, each with why it was rejected. Do not invent straw alternatives.
5. **Cross-cutting concerns:** security (secure-threat-model), privacy, reliability (run-slo-error-budget), observability, cost, accessibility, migration and rollback (ship-release-rollout).
6. **Rollout and verification:** how it ships in slices and how each slice is checked (build-test-strategy). For AI features, specify failure and recovery behavior and acceptance evals, including a deterministic alternative.
7. **Open questions, risks, owners.**

Use the shortest artifact that resolves the decision. A paragraph may be enough.

## Review

- Name **one approver**: the user, for anything that is their decision. An agent's review is input, not approval.
- Critique before approval: a cold re-read against the goals and alternatives (a reviewer subagent when the user approved one), plus a security phase when security triggers hit.
- Resolve every comment: accept, reject with a reason, or log it as an open question. Silence is not approval.
- Keep the note current. If the build diverges materially, update or supersede it.

## Record the decision (ADR)

Write an ADR when the decision is architecturally significant: it affects structure, quality attributes, dependencies, interfaces, or build and deploy technique, or it is expensive to reverse. Otherwise say "no ADR needed".

- Store it with the code, at the repository's existing location, else `docs/adr/NNNN-kebab-title.md`. Numbers are sequential and never reused.
- **Accepted ADRs are immutable.** To change a decision, write a new ADR that supersedes the old one and set the old status to `superseded by NNNN`. Factual corrections may be versioned without pretending the decision changed.
- Statuses: `proposed`, `accepted`, `rejected`, `deprecated`, `superseded by NNNN`. One decision per ADR.
- Consider at least two real options. An ADR with one option records a conclusion, not a decision.
- Add a revisit trigger (date or condition) when the decision rests on assumptions that can change. For model or retrieval choices, record measured quality and cost and the tested configuration.

```markdown
# NNNN. <decision as a short imperative phrase>
- Status: proposed | accepted | rejected | deprecated | superseded by NNNN
- Date: YYYY-MM-DD
- Deciders: <approver>, <contributors>

## Context and problem
## Decision drivers
## Options considered
1. <option A>: pros / cons
2. <option B>: pros / cons
## Decision
Chosen: <option>, because <justification tied to drivers>.
## Consequences
- Good / Bad (accepted trade-offs) / Follow-ups and revisit trigger
```

## Pitfalls

Writing the design after the code. No non-goals. Review without an approver. Editing accepted ADRs in place, which erases history. Decision records kept away from the code they govern.

Evidence: Nygard, "Documenting Architecture Decisions" (2011); P02 (MADR); R09 (parallel alternatives), R10 (designing for AI failure), R16 (system-level ML dependencies). The triggers are suite heuristics. See the [research register](../../docs/current/research-evidence.md).
