---
name: build-definition-of-done
description: "Use before accepting work or trusting a reported pass: verify the integrated artifact against acceptance and current check evidence, integrate parallel changes, restore red CI, or audit a repo's DoD."
---

# Verification and Definition of Done

Decide whether the current integrated artifact is acceptable, applying the repo's adopted requirements in proportion to the change. A doc fix needs its relevant check, not staging. Do not bootstrap delivery policy during ordinary implementation.

**Return:** accept / reject / partial; artifact identity; checks with exit status and evidence pointers; each applicable requirement as met / not met / unknown / n/a; remaining gaps. The lead accepts; accepting a known risk or unexplained failure is the user's or a named owner's decision, so say who decides. The verifier never repairs code or waives its own failures.

## Verify the artifact

1. **Identify the artifact,** including relevant untracked and generated files. Take commands from repo instructions or CI.
2. **One owner runs the deciding checks** on stable inputs, directly or through a controlled runner. The lead consumes that evidence instead of relaunching the same suite.
3. **Trust execution, not reports.** An unsupported "tests pass" is unverified. Reuse a result only when input, command, toolchain/dependencies, environment, and required freshness all match. Rerun after relevant edits, when identity is incomplete, or when policy or independence requires a fresh run. The optional [check runner](../team-lead/references/check-runner.md) records these identities.
4. **Cover what units cannot:** criteria, applicable review findings, relevant security concerns, and runtime evidence for persistence, authorization, rendering, or device/VM behavior. AI behavior needs versioned eval evidence (ai-evaluation).
5. **Separate new from baseline failures** with evidence. A pass licenses only the cases it exercised; unchecked behavior is unknown, with a reason. Resolve blockers and this item's tracker entries.

**Before returning, verify:** each check cites command, exit status, and inputs matching this artifact; each applicable requirement is marked; no failure is waived or called baseline without evidence.

## Integrate parallel work

Keep contracts and shared or generated outputs under explicit ownership. Integrate disjoint changes one at a time onto the current target and regenerate outputs from the combined sources. Check the combined result even when every branch was green. Worktrees isolate source, not build cost: choose build/cache lanes deliberately instead of starting redundant cold builds. Never kill or reuse another session's lane.

## Restore red CI

Account for case sensitivity, line endings, tool versions, and runner config. Exercise every relevant job step, since early failures hide later ones, without repeating executions that are already current. Contain a broken shared trunk with an authorized fix or revert first; investigate after.

## Audit or establish a DoD

Distinguish **written**, **configured**, **enforced**, and **observed passing**. Compare the DoD against CI, protection rules, and PR templates; a checkbox is attestation, not enforcement. Report claimed-but-unenforced items with concrete fixes. Never quietly lower a requirement.

To establish one, propose applicable criteria for code/review/CI, security, operability, docs, recovery, and deployment, using the delivery plugin only where it applies. A task is ready when it has criteria, scope, and a deciding check; no further ceremony is required.

Evidence: R02, R12, R17, R21, R24, R25, R34, P02, P03; reuse rules are engineering defaults, not measured gains ([register](../../references/research-evidence.md)).
