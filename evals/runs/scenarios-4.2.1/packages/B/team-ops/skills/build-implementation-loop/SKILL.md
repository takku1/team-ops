---
name: build-implementation-loop
description: "Implement a bounded fix or feature, prove the behavior with proportionate checks, and inspect the resulting diff. Use for hands-on coding; small work runs inline without team setup."
---

# Implementation Loop

Read repo instructions, working-tree status, affected contracts, nearby patterns, and actual check commands. Preserve unrelated changes. Define an observable outcome before editing.

- **Defect:** reproduce or record the limitation; support a falsifiable cause. A handed-over diagnosis remains a hypothesis until its load-bearing claims are checked.
- **Feature:** choose the smallest coherent integrated slice and acceptance examples. Use design-product-workflow for uncertain user flows and plan-design-review for consequential decisions.

## Change and check

1. Keep necessary cross-component edits together. Check unfamiliar APIs against local code or current authoritative docs.
2. For a behavioral defect, prefer a regression check that fails before and passes after. Use proportionate manual inspection for low-impact prose/cosmetics; avoid tautological tests.
3. On failure, test one hypothesis at a time. Separate baseline failures from regressions. Never weaken assertions or mock the failing boundary merely to get green.
4. Changing a test expectation needs cited evidence that the behavior is intended, must honor any edit condition in that test, and must pin behavior at least as strictly.
5. Run focused checks during editing. On the stable artifact, run required checks or hand them to the assigned final verifier. Record exact inputs/results; a role change alone does not justify another full build.
6. Inspect the final diff and in-scope untracked files. Inspect runtime/UI behavior where units cannot establish persistence, permissions, integration, or layout. Attribute baseline format/lint drift and keep incidental edits scoped.

Stop when acceptance and assigned checks pass. Two repairs without new discriminating evidence require diagnosis or a changed approach; preserve that history across workers. Respect run/task limits and leave resumable state when blocked.

## Ownership and result

One implementation owner controls a coupled change. Stay in the assigned scope; report needed changes elsewhere. Never kill or reuse another session's process, build lane, VM, or port. Use [the coordination contract](../team-lead/references/coordination.md) when delegated; this skill does not dispatch workers.

Continue authorized reversible work without re-asking. Commits, pushes, publication, and destructive work follow existing user authority and host constraints.

Return changes, observed checks, and limitations. Workers use the contract's delta report; inline work needs only a concise result. Keep implemented, tested, integrated, and deployed distinct. Update the existing tracker for this item when applicable; flag adjacent stale entries rather than silently deciding them.

Evidence: R02, R12, R13, R21, R24. [Register](../../references/research-evidence.md).
