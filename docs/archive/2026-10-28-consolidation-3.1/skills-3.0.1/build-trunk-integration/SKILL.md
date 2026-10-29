---
name: build-trunk-integration
description: Set branching, continuous integration, and versioning policy with trunk-based development, short-lived branches, required CI gates, branch protection, conventional commits, and semantic versioning. Use when setting up a repo or CI pipeline, when merges are painful, when long-lived branches or code freezes appear, or when choosing a branching model. Not for production rollout strategy (use ship-release-rollout).
---

# Trunk-Based Integration

**Role:** verifier and lead, when integrating several agents' work, restoring a red CI job, or setting branch and CI policy. **Returns:** the integration result, or a target CI and branch configuration.

## Integrating agents' work

Parallel implementers each work in an isolated worktree or branch with a disjoint write scope. The lead integrates one at a time onto current trunk: rebase or merge, rerun the affected checks on the combined result, then take the next. Resolve conflicts in shared generated files (registries, lockfiles, generated docs, status files) by regenerating from the merged sources where a generator exists, not by hand-picking lines. A green check in one worktree says nothing about the combined result. Never restart or kill another worker's build to save time.

## Restoring a red CI job

Run every step of the job locally, because an early failure hides later ones. Account for runner differences: case-sensitive paths, line endings, tool versions. Revert first and debug second when trunk is red for others.

## Policy

- **Integrate small changes often.** Short-lived branches and daily integration are practitioner guidance. Judge branch age, merge pain, and release obligations; there is no universal branch-count cap.
- **Unfinished work ships dark** behind flags or branch-by-abstraction, not on long-lived branches.
- **Trunk stays releasable.** Red main stops the line: fix or revert fast.
- **Protect the integration branch** with the applicable required reviews and status checks and no force-push. Linear history and signed commits are local choices; a signature does not prove correctness.
- **CI gates on every PR,** aiming for about 10 minutes: build, lint and format, type check, unit tests, integration tests, SAST plus secret and dependency scans, artifact build. Slow suites run post-merge or nightly with a named owner; do not hide a relevant blocking check there.
- **Release branches** only to support multiple versions. Cut from trunk and cherry-pick fixes *from* trunk.
- **Commits** follow Conventional Commits, so changelogs can be generated.
- **Versioning** follows SemVer 2.0.0 for anything with consumers. Build artifacts once and promote the same artifact.

## Audit procedure

1. Inspect branches, CI config, and protection settings.
2. Measure long-lived branches, integration failure duration, CI queue and runtime, and missing required gates against locally agreed thresholds. Keep configured, required, and actually passing checks distinct.
3. Output target protection rules, the CI stage list, and a migration path from the current model, preserving existing protections. Recommend a branching migration only with evidence of pain.

## Pitfalls

Long-lived `develop` branches on a continuously deployed service. "Merge Friday" big-bang integration. Flaky tests that teach people to ignore red (build-test-strategy).

Evidence: DORA trunk-based development, continuous integration, and deployment automation (P03); trunkbaseddevelopment.com; Humble and Farley, *Continuous Delivery*; semver.org 2.0.0; conventionalcommits.org. R12 (legible tool feedback for agents). Ten-minute CI is a target to adapt. See the [research register](../../docs/current/research-evidence.md).
