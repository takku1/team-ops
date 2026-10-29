---
name: build-trunk-integration
description: "Set branching, CI, and versioning policy: trunk-based development, short-lived branches, required gates, branch protection, conventional commits, SemVer. Use when merges hurt or choosing a branch model."
---

# Trunk-Based Integration

**Role:** lead, when setting branch and CI policy. **Returns:** a target CI and branch configuration.

Integrating parallel agents' work and restoring a red CI job are in team-ops `build-definition-of-done`. This skill sets the policy around them.

## Policy

- **Integrate small changes often.** Short-lived branches and daily integration are practitioner guidance. Judge branch age, merge pain, and release obligations; there is no universal branch-count cap.
- **Unfinished work ships dark** behind flags or branch-by-abstraction, not on long-lived branches.
- **Trunk stays releasable.** Red main stops the line: fix or revert fast.
- **Protect the integration branch** with the applicable required reviews and status checks and no force-push. Linear history and signed commits are local choices; a signature does not prove correctness.
- **CI gates on every PR,** aiming for about 10 minutes: build, lint and format, type check, unit tests, integration tests, SAST plus secret and dependency scans, artifact build. Slow suites run post-merge or nightly with a named owner; do not hide a relevant blocking check there.
- **Release branches** only to support multiple versions. Cut from trunk and cherry-pick fixes *from* trunk.
- **Commits** follow the repo's adopted convention; propose Conventional Commits if automated release notes would benefit.
- **Versioning** follows the adopted consumer compatibility policy; use SemVer where appropriate. Build artifacts once and promote the same artifact. Coordinate local expensive checks through one execution owner; hosted CI gates remain authoritative.

## Audit procedure

1. Inspect branches, CI config, and protection settings.
2. Measure long-lived branches, integration failure duration, CI queue and runtime, and missing required gates against locally agreed thresholds. Keep configured, required, and actually passing checks distinct.
3. Output target protection rules, the CI stage list, and a migration path from the current model, preserving existing protections. Recommend a branching migration only with evidence of pain.

## Pitfalls

Long-lived `develop` branches on a continuously deployed service. "Merge Friday" big-bang integration. Flaky tests that teach people to ignore red (build-test-strategy).

Use referenced core playbooks when available; otherwise perform the applicable step inline. See [host fallbacks](../../references/host-compatibility.md) only when a capability is missing.

Evidence: DORA trunk-based development, continuous integration, and deployment automation (P03); trunkbaseddevelopment.com; Humble and Farley, *Continuous Delivery*; semver.org 2.0.0; conventionalcommits.org. R12 (legible tool feedback for agents). Ten-minute CI is a target to adapt. See the [research register](../../references/research-evidence.md).
