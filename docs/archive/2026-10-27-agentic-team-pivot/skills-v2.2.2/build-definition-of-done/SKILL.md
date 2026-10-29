---
name: build-definition-of-done
description: Define and enforce the team's Definition of Done, a shared, checkable quality bar every increment must meet (tests, review, security, docs, observability, deployability), automated as CI gates wherever possible. Use when setting up a team or repo, when "done" means different things to different people, or when escaped defects rise. Not for per-story acceptance criteria (those live in plan-work-breakdown).
---

# Definition of Done

Scrum Guide 2020: the DoD is the commitment for the Increment. Work that does not meet it is not part of the increment and is not released. Several teams on one product share one DoD.

## Baseline DoD (adapt, do not shrink silently)
**Code**
- [ ] Merged to trunk through an approved review (build-code-review)
- [ ] CI green: build, lint/format, type checks, unit and integration tests (build-test-strategy)
- [ ] No new critical or high findings from SAST, secret scanning, or dependency scanning (secure-supply-chain)
- [ ] Acceptance criteria verified, with automated tests where feasible

**Operability**
- [ ] Logs, metrics, and traces cover the new paths, and alerts are updated if SLIs are affected (run-slo-error-budget)
- [ ] Behind a feature flag with a removal ticket, *or* safe to release directly (ship-release-rollout)
- [ ] Rollback or roll-forward path known

**Knowledge**
- [ ] User-facing and API docs and the changelog updated
- [ ] ADR written if a significant decision was made (plan-decision-record)
- [ ] Runbook updated for new failure modes

**Deployable**
- [ ] Deployed to staging (or production behind a flag) and smoke-tested

## Policy
- **Automate every item that can be automated** as a required CI check where appropriate. PR checkboxes record attestations; manual items need a named verifier and evidence.
- **Review the DoD for effectiveness.** Preserve adopted requirements unless an authorized team decision changes them; record the reason and replacement control. It need not grow monotonically. A PR checkbox is an attestation, not technical enforcement.
- **Definition of Ready is optional and light.** Never use it as a gate that blocks collaboration.
- Undone work goes back to the backlog. It is never "done except testing".

## Logic
1. Read the existing DoD, CI config, and PR template if present.
2. Diff them against the baseline and against what CI actually enforces.
3. Output the DoD plus a list of "claimed but not enforced" items, each with the CI or PR-template change that enforces it.

## Sources
Scrum Guide 2020 (Increment, Definition of Done); DORA capabilities (continuous integration, test automation); Google SRE (production readiness reviews).

## Research and application

Classify each applicable requirement as written, configured, enforced, and observed passing; retain unknown and not-applicable states. For AI features, include versioned eval evidence via ai-evaluation, not just a green unit suite. Small local edits need proportional verification, not a staging deployment ritual.

Evidence: R02, R17; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
