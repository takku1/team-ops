---
name: build-trunk-integration
description: Set branching, continuous integration, and versioning policy with trunk-based development, short-lived branches, required CI gates, branch protection, conventional commits, and semantic versioning. Use when setting up a repo or CI pipeline, when merges are painful, when long-lived branches or code freezes appear, or when choosing a branching model. Not for production rollout strategy (use ship-release-rollout).
---

# Trunk-Based Integration

## Policy
- **Prefer frequent integration of small changes.** Daily integration and short-lived branches are practitioner guidance. Assess branch age, merge pain, and release obligations; do not enforce a universal maximum of 3 active branches across a repository.
- **Unfinished work ships dark** behind feature flags or branch-by-abstraction, never on long-lived branches.
- **Trunk is always releasable.** A red main is a stop-the-line event: fix or revert within ~10 minutes. Revert first and debug second.
- **Protect the integration branch** with applicable reviews/status checks and restricted force-push. Linear history and signed commits are local policy choices; signatures do not prove code correctness.
- **CI gates on every PR** (aim for under 10 minutes): build → lint/format → type check → unit tests → integration tests → SAST, secret scan, and dependency scan → artifact build. Slow suites run post-merge or on a nightly schedule, with a named owner.
- **Release branches** only if you must support multiple versions. Cut them from trunk and cherry-pick fixes *from* trunk, never into it first.
- **Commits:** Conventional Commits (`feat:`, `fix:`, `chore:`, `BREAKING CHANGE:`), which lets changelogs generate automatically.
- **Versioning:** SemVer 2.0.0 for anything with consumers. MAJOR for breaking changes, MINOR for compatible features, PATCH for fixes. Build artifacts once and promote the same artifact through environments.

## Logic
1. Inspect the current branches, CI config, and protection settings.
2. Inspect long-lived branches, integration failure duration, CI queue/runtime, and missing required gates. Use locally agreed thresholds, not raw branch count. Distinguish configured checks from required and successfully executed checks. When restoring a red job, run every step of it locally, since an early failure hides later ones, and account for runner differences such as case-sensitive paths.
3. Emit the target config: protection rules, CI stage list, a flags-over-branches note, and a migration plan from the current model (e.g. GitFlow) to trunk-based.

## Pitfalls
- GitFlow-style long-lived `develop` branches on a continuously deployed service.
- "Merge Friday": big-bang integration.
- Flaky tests that train people to ignore red builds (see build-test-strategy).

## Sources
DORA capabilities: Trunk-based development, Continuous integration, Deployment automation (dora.dev); Paul Hammant, trunkbaseddevelopment.com; Humble & Farley, *Continuous Delivery*; semver.org 2.0.0; conventionalcommits.org.

## Research and application

Use isolated writable scopes for concurrent workers and verify their integrated result. Do not restart or kill another worker's build to save time. Ten-minute CI and rapid repair are targets to adapt; preserve relevant blocking checks rather than hiding slow failures post-merge.

Evidence: P03, R12; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
