---
name: build-trunk-integration
description: "Set branching, CI, and versioning policy: trunk-based development, short-lived branches, required gates, branch protection, commit conventions, SemVer. Use when merges hurt or choosing a branch model."
---

# Trunk-Based Integration

Set the branch, CI, and versioning policy that keeps trunk releasable. Integrating parallel work and restoring red CI belong to `build-definition-of-done`.

**Return:** target protection rules, the CI stage list, and a migration path from the current model that preserves existing protections.

## Audit first

1. Inspect branches, CI config, and protection settings.
2. Measure long-lived branches, integration-failure duration, CI queue and runtime, and missing required gates against locally agreed thresholds. Keep configured, required, and actually passing checks distinct.
3. Recommend a branching migration only with evidence of pain.

## Policy

- **Integrate small changes often.** Short-lived branches and daily integration are practitioner guidance; judge branch age, merge pain, and release obligations. There is no universal branch-count cap.
- **Ship unfinished work dark** behind flags or branch-by-abstraction, not on long-lived branches.
- **Keep trunk releasable.** Red main stops the line: fix or revert fast.
- **Protect the integration branch** with the applicable required reviews and status checks, and no force-push. Linear history and signed commits are local choices; a signature does not prove correctness.
- **Gate every PR,** aiming for about ten minutes: build, lint and format, type check, unit and integration tests, SAST plus secret and dependency scans, artifact build. Slow suites run post-merge or nightly with a named owner; never move a relevant blocking check there to hide it.
- **Release branches** only to support multiple versions: cut from trunk and cherry-pick fixes *from* trunk.
- **Commits** follow the repo's convention; propose Conventional Commits only if automated release notes would benefit.
- **Versioning** follows the adopted consumer-compatibility policy (SemVer where appropriate). Build artifacts once and promote the same artifact. Route local expensive checks through one execution owner; hosted CI gates stay authoritative.

Evidence: P03, P07, R12, R32; ten-minute CI is a target to adapt ([register](../../references/research-evidence.md)).
