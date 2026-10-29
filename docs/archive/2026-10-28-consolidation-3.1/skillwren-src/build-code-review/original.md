---
name: build-code-review
description: Set and apply a code review policy covering small changes, fast turnaround, an "improves code health" approval standard, what reviewers check, comment etiquette, and ownership routing. Use when defining review rules for a repo, when reviews are slow or contentious, when PRs are huge, or when actually reviewing a change. Not for automated security scanning (use secure-supply-chain).
---

# Code Review Policy

## Policy
- **Approval standard:** approve once the change *definitely improves overall code health*, even if it is not perfect. There is no perfect code, only better code (Google eng-practices).
- **Small changes.** One self-contained change per PR. About 100 lines changed is a healthy norm, and around 1000 is usually too large to review well. Separate refactors from behavior changes. Stack PRs for big features.
- **Speed:** first response within **one business day at most**, and faster is better. Review speed is a team throughput lever, not a courtesy.
- **Required approvals:** at least 1 owner (from CODEOWNERS) per touched area. Add a second approver for security-sensitive paths, schema migrations, and infra.
- **Authors** write a description of what changed, why, how it was tested, and the risk and rollback. They self-review before requesting review and keep CI green.
- **Automate the nits.** Formatters and linters enforce style. Humans review design.

## What reviewers check, in priority order
1. **Design**: does it belong here, and does it fit the architecture and the ADRs?
2. **Functionality**: correct behavior, edge cases, concurrency, user impact
3. **Complexity**: could it be simpler? Is anything over-engineered for needs that do not exist yet?
4. **Tests**: correct, meaningful, and able to fail
5. **Security and privacy**: input handling, authz, secrets, PII, injection
6. **Naming, comments** (the *why*, not the *what*), **docs**
7. **Operability**: logging, metrics, failure modes, flags

## Comment etiquette
- Comment on the code, not the person. Explain why.
- Label severity: `blocking:`, `nit:`, `optional:`, `question:`, `fyi:`.
- Resolve disagreements by technical facts and style guides. Escalate to the tech lead or owner after one round, or move to a call.

## Logic
1. To set policy: emit the rules above adapted to the repo, plus the branch-protection settings and a PR template.
2. To review: check size first (if it is too large, ask for a split), then walk the checklist in priority order and output labeled comments plus a verdict (`approve`, `approve with nits`, or `request changes`) with reasons.

## Pitfalls
- Rubber-stamp approvals on large PRs ("LGTM" on 2,000 lines).
- Gatekeeping on personal preference that no style guide supports.
- Review queues that age for days. Make PR age a visible metric.

## Sources
Google Engineering Practices (google.github.io/eng-practices): The Standard of Code Review, Small CLs, Speed of Code Reviews; DORA (code review speed as a capability); Microsoft Research, "Expectations, Outcomes, and Challenges of Modern Code Review" (Bacchelli & Bird, 2013).
