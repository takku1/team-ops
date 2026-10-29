---
name: plan-design-review
description: Write and review a design doc or RFC before building anything consequential. Covers goals and non-goals, alternatives, cross-cutting concerns (security, privacy, reliability, observability, cost), and a time-boxed review with a clear approver. Use when a change spans teams or services, adds a dependency or datastore, changes a public API or data model, is hard to reverse, or takes more than ~2 engineer-weeks. Not for small changes that ordinary code review covers.
---

# Design Review (Design Doc / RFC)

A design doc exists to surface trade-offs and get the right review *before* code is cheap to throw away. Most changes do not need one.

## When it is required
Use a proportionate design note for consequential changes; expand into an RFC when coordination, uncertainty, or irreversible impact justifies it. Assess these triggers:
- crosses team or service boundaries, or changes a public API, schema, or wire protocol
- adds a new language, framework, datastore, or third-party dependency in a critical path
- touches authn/authz, PII, payments, or data retention
- is hard to reverse (migrations, deletions, vendor lock-in)
- costs more than ~2 engineer-weeks or more than one sprint

Otherwise use a PR description and normal code review (build-code-review).

## Template
1. **Context and scope**: the problem and the current state. Facts only.
2. **Goals / Non-goals**: measurable goals. Non-goals are things a reasonable reader might expect but that are explicitly out of scope.
3. **Proposed design**: architecture, APIs, data model, sequence of key flows. Diagrams are welcome.
4. **Alternatives considered**: at least two, including "do nothing", each with the reason it was rejected.
5. **Cross-cutting concerns**: security (run secure-threat-model), privacy, reliability/SLO impact (run-slo-error-budget), observability, cost, accessibility, migration and rollback plan (ship-release-rollout).
6. **Rollout and testing plan**: how it ships incrementally and how it is verified (build-test-strategy).
7. **Open questions, risks, owners.**

Use the shortest artifact that resolves the decision. A paragraph or sketch may suffice; a multi-service migration may need a full RFC. Page count and the two-week trigger are suite heuristics.

## Review process
- Statuses: `draft → in-review → approved | rejected → implemented | superseded`.
- Name **one approver** (DACI Approver, see org-ownership-raci) and the required reviewers: owning team(s), security if it touches security surfaces, and SRE if SLOs are affected.
- **Time-box review to 5 working days.** Silence is not approval. The Driver chases reviewers or escalates to the approver.
- Resolve every comment: accept it, reject it with a reason, or log it as an open question.
- On approval, record the key decisions as ADRs (plan-decision-record) and link them from the doc.
- Keep the doc current through implementation. If the build diverges materially, update the doc or supersede it.

## Logic
1. Check the triggers above. If none hit, say so and stop.
2. Draft the applicable template sections. Compare credible alternatives (including no change when meaningful); do not invent straw alternatives to hit a quota. Mark assumptions and missing evidence.
3. Assign the approver and reviewers and set the review deadline.
4. Output the doc plus a review checklist and a list of the ADRs to write.

## Pitfalls
- Writing the doc after the code ("design-as-documentation").
- A design that has no non-goals, which invites scope creep.
- Review by committee without an approver. It never converges.

## Sources
Google "Design Docs at Google" (Industrial Empathy, 2020); Oxide RFD 1; Rust RFC process; Fuchsia RFC-0001 (most changes do not need an RFC); Pragmatic Engineer, "RFCs and Design Docs".

## Research and application

Separate observed user needs from assumptions. Use design-product-workflow for uncertain interaction flows; use spikes to test architecture risks. For AI features, specify failure/recovery behavior and acceptance evals, including a deterministic alternative.

Evidence: R09, R10, R16; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
