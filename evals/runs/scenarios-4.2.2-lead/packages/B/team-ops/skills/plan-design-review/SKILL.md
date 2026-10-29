---
name: plan-design-review
description: "Write a proportionate design note before a consequential change (cross-component, public API/schema/protocol, critical dependency, hard to reverse) and record the decision as an immutable ADR. Not for changes ordinary review covers."
---

# Design Review and Decision Records

**Role:** lead (team-lead), before assigning implementation. **Returns:** the design note, its open questions, and the ADRs to write.

A design note surfaces trade-offs while code is still cheap to throw away. Most changes do not need one.

## When

Write a note when a change crosses component or service boundaries; changes a public API, schema, or wire protocol; adds a language, framework, datastore, or critical-path dependency; touches authn/authz, capabilities, PII, payments, or retention; is hard to reverse (migrations, deletions, lock-in); or requires unresolved coordination across agents or sessions. Worker count alone does not require an ADR. Otherwise say so and use normal review. Expand to an RFC only when coordination or irreversibility justifies it; a paragraph may be enough.

## Note

1. **Context:** the problem and current state, as cited facts.
2. **Goals and non-goals:** measurable goals; non-goals a reader might reasonably expect.
3. **Design:** architecture, interfaces, data model, key flows.
4. **Alternatives:** the credible ones (including no change), each with why it lost. No straw options.
5. **Cross-cutting:** security (secure-review), privacy, reliability, observability, cost, accessibility, migration and rollback.
6. **Rollout and verification:** slices and how each is checked. AI features specify failure and recovery behavior, acceptance evals, and a deterministic alternative.
7. **Open questions, risks, owners.**

## Review

- **Respect decision ownership.** Make routine authorized implementation choices. Escalate consequential choices outside existing scope or authority after preparing concrete alternatives; do not ask again for decisions already authorized. An agent review cannot grant missing authority.
- **Critique first:** a cold re-read against goals and alternatives (a reviewer subagent if approved), plus a secure phase when security triggers hit.
- **Resolve every comment:** accept, reject with a reason, or log it open. Silence is not approval.
- If the build diverges materially, update or supersede the note.

## ADR

Write one when a decision affects structure, quality attributes, dependencies, interfaces, or build and deploy technique, or is expensive to reverse; otherwise say "no ADR needed". Store it at the repo's existing location, else `docs/adr/NNNN-kebab-title.md`, numbered sequentially and never reused. One decision per ADR, at least two real options. **Accepted ADRs are immutable:** a change is a new ADR that supersedes the old (`superseded by NNNN`). Add a revisit trigger when the decision rests on assumptions that can change; for model or retrieval choices record the measured quality, cost, and configuration.

Use [the ADR shape](references/adr.md) when writing a new decision record; follow an existing repo format first.

Pitfalls: design written after the code; no non-goals; no approver; ADRs edited in place; decisions stored away from the code.

Evidence: Nygard (2011); P02 (MADR); R09, R10, R16. Triggers are suite heuristics. [Register](../../references/research-evidence.md).
