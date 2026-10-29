---
name: build-implementation-loop
description: "Implement a bounded fix or feature, prove it with proportionate checks, and inspect the resulting diff. The default for hands-on coding; small work stays inline with no team setup."
---

# Implementation Loop

Make a bounded change, prove it works, and inspect what actually changed.

**Return:** changes, observed checks, and limitations, keeping implemented, tested, integrated, and deployed distinct. Delegated workers use the contract's delta report; inline work needs only a concise result.

## Before editing

Read repo instructions, working-tree status, affected contracts, nearby patterns, and the real check commands. Preserve unrelated changes. Define the observable outcome.

- **Defect:** reproduce it or record why you cannot, and support a falsifiable cause. A handed-over diagnosis is a hypothesis until its load-bearing claims are checked.
- **Feature:** choose the smallest coherent integrated slice and write acceptance examples. Uncertain user flows go to design-product-workflow; consequential decisions to plan-design-review.

## Change and check

1. Keep necessary cross-component edits together. Verify unfamiliar APIs against local code or current authoritative docs.
2. For a behavioral defect, prefer a regression check that fails before the fix and passes after. Low-impact prose or cosmetics get proportionate manual inspection, not tautological tests.
3. On failure, test one hypothesis at a time and separate baseline failures from regressions. Never weaken assertions or mock the failing boundary just to get green.
4. Change a test expectation only with cited evidence that the new behavior is intended. Honor any edit condition in that test, and pin behavior at least as strictly as before.
5. Run focused checks while editing. On the stable artifact, run the required checks or hand them to the assigned final verifier, recording exact inputs and results. Changing roles is no reason for another full build.
6. Inspect the final diff and in-scope untracked files. Where units cannot establish persistence, permissions, integration, or layout, inspect the running behavior. Attribute pre-existing format/lint drift; keep incidental edits out.

**Stop** when acceptance and assigned checks pass; rereading your own change is not verification. Two repairs without new discriminating evidence mean diagnose or change approach; keep that history across workers. At a run or task limit, leave resumable state.

## Ownership and authority

- One implementation owner controls a coupled change. Stay in the assigned scope; report needed changes elsewhere.
- Never kill or reuse another session's process, build lane, VM, or port.
- This skill never dispatches workers; delegated work follows [the coordination contract](../team-lead/references/coordination.md).
- Continue authorized reversible work without re-asking. Commits, pushes, publication, and destructive actions follow existing user authority and host limits.
- Update this item's existing tracker entry when applicable; flag adjacent stale entries instead of silently deciding them.

Evidence: R02, R12, R13, R21, R24, R29 ([register](../../references/research-evidence.md)).
