---
name: build-definition-of-done
description: Define and enforce the Definition of Done, a shared, checkable quality bar every change must meet before it is accepted (tests, review, security, docs, observability, deployability), automated as CI gates wherever possible. Use when the verifier or lead decides whether an agent's work is done, when setting up a repo, when "done" means different things to different agents or people, or when escaped defects rise. Verifier playbook. Not for per-story acceptance criteria (those live in plan-work-breakdown).
---

# Definition of Done

**Role:** verifier (agents/verifier.md); the lead applies it to accept work. **Returns:** each applicable item marked met, not met, unknown, or n/a, with evidence.

The DoD is the bar for accepting work into the product (the Scrum Guide's commitment for the Increment). Work below it is not accepted and not released, and everyone working on one product, agent or person, uses the same DoD. Apply it in proportion: a local doc fix needs its check rerun, not a staging deploy.

## Accepting an agent's work

- **Rerun, do not read.** Rerun the acceptance oracle and the required checks. "Tests pass" in a report is a claim until you see the output.
- **A review phase ran** and its blocking findings are resolved. Inline, that means re-reading the diff cold against the acceptance criteria and rerunning checks. For consequential, hard-to-reverse, or security changes, prefer a reviewer in a fresh context.
- **Security review ran** when the change hit a security trigger (team-lead section 1).
- **Integrated, not isolated.** Parallel work is checked on the combined result (build-trunk-integration).
- **Trackers are true.** The repository's status or tracker entries for the item match the observed result.
- **AI features** carry versioned eval evidence (ai-evaluation), not only a green unit suite.
- What cannot be checked here (a live device, production telemetry) is **unknown, with the reason**, never met.

## Baseline DoD (adapt; never shrink silently)

**Code**
- [ ] Merged through an approved review (build-code-review)
- [ ] CI green: build, lint and format, type checks, unit and integration tests (build-test-strategy)
- [ ] No new critical or high findings from SAST, secret scanning, or dependency scanning (secure-supply-chain)
- [ ] Acceptance criteria verified, with automated tests where feasible

**Operability**
- [ ] Logs, metrics, and traces cover the new paths; alerts updated if SLIs are affected (run-slo-error-budget)
- [ ] Behind a feature flag with a removal ticket, *or* safe to release directly (ship-release-rollout)
- [ ] Rollback or roll-forward path known

**Knowledge**
- [ ] User-facing and API docs and the changelog updated
- [ ] ADR written if a significant decision was made (plan-design-review)
- [ ] Runbook updated for new failure modes

**Deployable**
- [ ] Deployed to staging (or production behind a flag) and smoke-tested

## Written, enforced, observed

A DoD item can be **written** (in a doc), **configured** (a CI job exists), **enforced** (a required check or branch protection blocks merge), and **observed passing** (a recent run shows it green). A PR checkbox is an attestation, not enforcement. Report each item at the strongest level you can show.

1. Read the existing DoD, the CI config, branch protection, and the PR template.
2. Compare them with the baseline and with what CI actually enforces and has run.
3. Output the DoD plus a **claimed but not enforced** list, each with the CI, protection, or template change that would enforce it. Manual items need a named verifier and evidence.

## Policy

- **Automate every item that can be** as a required check.
- **Keep adopted items** unless an authorized decision changes them; record the reason and any replacement control. The DoD need not only grow, but it never shrinks quietly to declare something done.
- **Briefs replace a Definition of Ready.** A task is ready when its brief has acceptance criteria, a write scope, and an oracle (team-lead).
- Undone work goes back to the queue. There is no "done except testing".

Evidence: Scrum Guide 2020 (Increment, Definition of Done); DORA capabilities (continuous integration, test automation); Google SRE production readiness reviews. R02 (coverage is not effectiveness), R17 (readiness spans data, model, infrastructure, monitoring). See the [research register](../../docs/current/research-evidence.md).
