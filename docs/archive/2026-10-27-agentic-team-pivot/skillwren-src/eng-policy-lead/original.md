---
name: eng-policy-lead
description: Engineering-lead orchestrator for work that spans several build-policy skills. It bootstraps a full engineering policy set for a new team or repo, audits existing policy (written vs enforced vs followed), or runs a multi-stage workflow (new service, launch readiness, late project, quarterly health check) by chaining the right skills in order. Use for "set up our engineering process", "audit our dev policy", "are we ready to launch?", or "plan a new service end to end". Not for single-topic requests: go straight to the specific skill (e.g. a PR review goes to build-code-review).
---

# Engineering Policy Lead

Orchestrates the pack. A single-topic need goes directly to its skill. This skill is for jobs that need **several skills in a deliberate order**, and it carries the results from one step to the next.

## Operating rules
- **Pick one mode:** Bootstrap, Audit, or a named Workflow. If the request is single-topic, name the skill and hand off.
- **Run the steps in order and pass the outputs forward.** For example, the design doc's goals feed the work breakdown, and the threat-model mitigations become DoD items and tickets.
- **Skip steps that do not apply** and say why. Do not pad the job.
- **Stop at gates.** If a step produces a blocking finding (no accountable owner, no SLO for a launch, an unmitigated high threat), report it and stop before later steps build on it.
- **End with one consolidated summary:** decisions made, artifacts written, open risks, and the top 3 next actions, each with an owner.

## Skill map
| Stage | Skill | Covers |
|---|---|---|
| Org | `org-team-topology` | team boundaries, types, interaction modes |
| Org | `org-ownership-raci` | RACI/DACI, CODEOWNERS |
| Org | `org-capacity-plan` | load, WIP, team size, bus factor |
| Plan | `plan-design-review` | design doc / RFC and review |
| Plan | `plan-decision-record` | ADRs |
| Plan | `plan-work-breakdown` | vertical slices, acceptance criteria |
| Plan | `plan-estimate-forecast` | ranged forecasts |
| Plan | `plan-late-recovery` | slipping projects, Brooks check |
| Plan | `plan-delivery-cadence` | Scrum vs Kanban |
| Build | `build-definition-of-done` | quality bar, CI-enforced |
| Build | `build-code-review` | review policy or a review |
| Build | `build-trunk-integration` | branching, CI gates, SemVer |
| Build | `build-test-strategy` | test mix, flakes, coverage |
| Ship | `ship-release-rollout` | staged rollout, flags, migrations |
| Run | `run-slo-error-budget` | SLOs, burn alerts, budget policy |
| Run | `run-incident-postmortem` | incident roles, postmortems |
| Secure | `secure-threat-model` | 4QF + STRIDE |
| Secure | `secure-supply-chain` | deps, SBOM, SLSA, SSDF |
| Measure | `measure-delivery-health` | DORA + SPACE |

## Mode: Bootstrap (new team or repo)
Produce short, owned, versioned policy files in this order:
1. `docs/policy/ownership.md` from org-team-topology + org-ownership-raci, plus `CODEOWNERS`
2. `docs/policy/cadence.md` from plan-delivery-cadence
3. `docs/policy/definition-of-done.md` from build-definition-of-done
4. `docs/policy/code-review.md` + PR template + branch protection, from build-code-review
5. `docs/policy/branching-ci.md` + CI stage list, from build-trunk-integration
6. `docs/policy/testing.md` from build-test-strategy
7. `docs/policy/release.md` from ship-release-rollout
8. `docs/policy/slo-error-budget.md` (signers listed) from run-slo-error-budget
9. `docs/policy/incidents.md` from run-incident-postmortem
10. `docs/policy/security.md` + `SECURITY.md`, from secure-threat-model + secure-supply-chain
11. `docs/adr/0001-record-architecture-decisions.md` and `docs/design/TEMPLATE.md`, from plan-decision-record + plan-design-review

Adapt to what exists. Do not overwrite an existing policy; diff it and propose changes instead.

## Mode: Audit
For each policy area, score three columns:
- **Written?** A policy doc exists and has an owner.
- **Enforced?** Tooling enforces it: CI checks, branch protection, alerts, bots.
- **Followed?** Sample the last ~20 PRs, ~10 deploys, and the recent incidents.

Rank the gaps by risk (security and reliability first, then flow) and output the **top 3 fixes**, each with an owner, the skill that fixes it, and the effort. Do not dump every gap as a to-do list.

## Workflows
**New service / major feature**
org-team-topology (owner and boundary) → plan-design-review → secure-threat-model → plan-decision-record (key choices) → plan-work-breakdown → plan-estimate-forecast → build-definition-of-done (feature-specific additions) → run-slo-error-budget (SLIs/SLOs) → ship-release-rollout (rollout plan).
*Gate:* no build starts without an approved design, one accountable owner, and threat mitigations ticketed.

**Launch readiness ("are we ready to ship?")**
build-definition-of-done (all items met?) → build-test-strategy (critical journeys covered?) → secure-supply-chain (no open criticals or highs past SLA) → run-slo-error-budget (SLOs, alerts, dashboards live) → run-incident-postmortem (on-call, severities, runbook) → ship-release-rollout (stages, gates, rollback tested).
*Output:* go / no-go with the blocking items.

**Project is slipping**
plan-estimate-forecast (re-forecast with actuals) → plan-late-recovery (lever order, Brooks check) → org-capacity-plan (rebalance, protect the critical path) → plan-decision-record (record the scope cut).

**Quarterly engineering health check**
measure-delivery-health (DORA + SPACE) → Audit mode → plan-delivery-cadence (retro on the process) → top 3 improvement experiments, each with an owner and a review date.

**Post-incident hardening**
run-incident-postmortem → run-slo-error-budget (apply the budget policy) → build-test-strategy (regression tests) → ship-release-rollout (gate or flag gaps) → plan-decision-record if the architecture changes.

## Principles across the pack
Small batches · one accountable owner · automate the gate rather than trusting memory · measure teams, not individuals · policies are versioned, reviewed, and only tightened deliberately.
