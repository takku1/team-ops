---
name: build-definition-of-done
description: "Verify the current integrated artifact against acceptance and required checks; coordinate final check execution, integrate parallel changes, or audit what a repo's Definition of Done actually enforces."
---

# Verification and Definition of Done

Apply adopted repo requirements proportionately. A doc fix needs its relevant check, not staging. Do not bootstrap delivery policy during ordinary implementation.

## Verify the artifact

- Identify the integrated artifact, including relevant untracked/generated files. Obtain commands from repo instructions or CI.
- Assign one final verification owner. It observes deciding checks on stable inputs, directly or through a controlled runner. The controller consumes that evidence instead of launching the identical suite again.
- A reported "tests pass" without trustworthy execution evidence is unverified. Reuse a result only when input, command, toolchain/dependencies, environment, and required freshness match. Rerun after relevant edits, incomplete identity, or when policy/independence requires a fresh execution. [The coordination contract](../team-lead/references/coordination.md) defines the optional runner and limits.
- Verify criteria, applicable review findings, and relevant security concerns. Use runtime evidence for behavior units cannot demonstrate: persistence, authorization, rendering, a device or VM.
- Separate new failures from baseline failures with evidence. Unchecked behavior is unknown with a reason, not passing.
- Resolve blockers and check tracker entries for this item. AI behavior uses versioned eval evidence from ai-evaluation.

Return accept/reject/partial, artifact identity, checks with exit status and evidence pointers, applicable requirements met/not met/unknown/n/a, and remaining gaps. The lead accepts; the verifier does not repair code or self-waive failures.

## Integrate parallel work

Keep contracts and shared/generated outputs under explicit ownership. Integrate disjoint changes one at a time onto the current target; regenerate outputs from combined sources. Check the combined result even when each branch was green. Isolated worktrees protect source; choose build/cache lanes deliberately instead of starting redundant cold builds. Never kill or reuse another session's lane.

## Restore red CI

Account for case sensitivity, line endings, tool versions, and runner config. Exercise every relevant job step because early failures hide later ones; avoid repeating current executions. Contain a shared broken trunk with an authorized fix/revert, then investigate.

## Audit adopted requirements

Distinguish **written**, **configured**, **enforced**, and **observed passing**. Compare DoD, CI, protection rules, and PR templates. A checkbox is attestation, not enforcement. Report claimed-but-unenforced items and concrete changes; never quietly lower requirements.

If asked to establish a DoD, propose applicable code/review/CI, security, operability, docs, recovery, and deployment criteria. Use the delivery plugin only where applicable. A task is ready with criteria, scope, and a deciding check; no extra ceremony is required.

Evidence: R02, R12, R17, R21, R24, R25; P02, P03. Execution reuse rules are engineering defaults, not measured suite gains. [Register](../../references/research-evidence.md).
