---
name: plan-design-review
description: "Write a proportionate design note before a consequential change (cross-component, public API/schema, critical dependency, hard to reverse) and record the decision as an immutable ADR. Not for routine changes."
---

# Design Review and Decision Records

Surface trade-offs while code is still cheap to throw away, then record the decision. Most changes need neither.

**Return:** before implementation is assigned, the design note, its open questions, and the ADRs to write; or "no note needed".

## When a note is needed

Write one when a change:
- crosses component or service boundaries;
- changes a public API, schema, or wire protocol;
- adds a language, framework, datastore, or critical-path dependency;
- touches authn/authz, capabilities, PII, payments, or retention;
- is hard to reverse (migrations, deletions, lock-in); or
- needs unresolved coordination across agents or sessions.

Worker count alone never requires one. Otherwise say so and rely on normal review. A paragraph may be enough; grow to an RFC only when coordination or irreversibility justifies it.

## Write the note

1. **Context:** the problem and current state, as cited facts.
2. **Goals and non-goals:** measurable goals; non-goals a reader might reasonably expect.
3. **Design:** architecture, interfaces, data model, key flows.
4. **Alternatives:** the credible ones, including no change, each with why it lost. No straw options.
5. **Cross-cutting:** security (secure-review), privacy, reliability, observability, cost, accessibility, migration and rollback.
6. **Rollout and verification:** slices and how each is checked. AI features add failure/recovery behavior, acceptance evals, and a deterministic alternative.
7. **Open questions, risks, owners.**

## Review it

- **Respect decision ownership.** Make routine authorized choices yourself. Escalate consequential choices outside existing scope or authority with concrete alternatives prepared; never re-ask decisions already authorized. An agent review cannot grant missing authority.
- **Critique before approval:** a cold re-read against goals and alternatives (a reviewer subagent if approved), plus secure-review when its triggers hit.
- **Resolve every comment:** accept, reject with a reason, or log it open. Silence is not approval.
- If the build diverges materially, update or supersede the note.

## Record the decision (ADR)

Write an ADR when the decision affects structure, quality attributes, dependencies, interfaces, or build/deploy technique, or is expensive to reverse; otherwise state "no ADR needed".

- **Location:** the repo's existing ADR directory, else `docs/adr/NNNN-kebab-title.md`, numbered sequentially and never reused.
- **Scope:** one decision per ADR, with at least two real options.
- **Accepted ADRs are immutable.** Change a decision with a new ADR that supersedes the old (`superseded by NNNN`).
- **Revisit trigger** when the decision rests on assumptions that can change; for model or retrieval choices, record measured quality, cost, and configuration.
- **Format:** the repo's existing one, else [the MADR-based shape](references/adr.md).

Evidence: P02, P09, R09, R10, R16; triggers are suite heuristics ([register](../../references/research-evidence.md)).
