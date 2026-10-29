---
name: plan-decision-record
description: Record architecturally significant decisions as immutable ADRs (Nygard or MADR format) in the repo, with status, context, options, decision, and consequences. Use when a team chooses a technology, pattern, boundary, or policy that is costly to reverse, when a design review concludes, or when someone asks "why did we do it this way?". Not for routine implementation choices.
---

# Decision Records (ADR)

## Policy
- **Location:** `docs/adr/NNNN-kebab-title.md` (or `docs/decisions/`), versioned with the code. Numbers are sequential and never reused.
- **Immutable once accepted.** To change a decision, write a new ADR that *supersedes* the old one, and set the old one's status to `superseded by NNNN`.
- **Statuses:** `proposed → accepted | rejected → deprecated | superseded`.
- **Write one when the decision is architecturally significant**: it affects structure, non-functional qualities, dependencies, interfaces, or build and deploy technique, or it is expensive to reverse.
- **One decision per ADR.** Keep it short, usually 1-2 pages.
- ADRs go through normal code review. The DACI Approver merges them.

## Template (MADR-lite)
```markdown
# NNNN. <decision as a short imperative phrase>
- Status: proposed | accepted | rejected | deprecated | superseded by NNNN
- Date: YYYY-MM-DD
- Deciders: <approver>, <contributors>

## Context and problem
<forces at play: requirements, constraints, facts>

## Decision drivers
- <driver 1> ...

## Options considered
1. <option A>: pros / cons
2. <option B>: pros / cons

## Decision
Chosen: <option>, because <justification tied to drivers>.

## Consequences
- Good: ...
- Bad / accepted trade-offs: ...
- Follow-ups: <tasks, re-evaluation trigger or date>
```

## Logic
1. Check significance. If it is a trivial or local choice, say "no ADR needed" and stop.
2. Find existing ADRs. Link related ones and mark any that are superseded.
3. Fill the template with at least two real options, and name the trade-offs honestly.
4. Add a **revisit trigger** (a date or condition) when the decision rests on assumptions that could change.

## Pitfalls
- Editing accepted ADRs in place, which erases history.
- An ADR with only one option. That records a conclusion, not a decision.
- ADRs kept in a wiki away from the code they govern.

## Sources
Michael Nygard, "Documenting Architecture Decisions" (2011); MADR (adr.github.io/madr); joelparkerhenderson/architecture-decision-record; ThoughtWorks Tech Radar (Lightweight ADRs: Adopt).

## Research and application

The format is a practitioner method, not proof of better outcomes. Keep decision history; factual corrections may be versioned without pretending the decision changed. For model or retrieval choices, record measured quality/cost, tested configuration, and a re-evaluation trigger.

Evidence: P02, R16; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
