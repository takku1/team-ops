---
name: ship-release-rollout
description: Ship changes safely with progressive delivery covering feature-flag lifecycle, canary and staged rollouts with automated health gates, rollback and roll-forward rules, safe database migrations, and release notes. Use when planning a launch or risky deploy, defining deployment policy, adding a feature flag, or after a bad rollout. Not for branching and CI (use build-trunk-integration).
---

# Release and Rollout

## Policy
- **Separate deploy from release.** Deploy code dark, then release by flag or traffic shift.
- **Progressive exposure:** choose cohorts, health gates, minimum event counts, observation windows, and owner from traffic and blast radius. A 1/10/50/100% ramp or 30-60-minute bake is illustrative, not evidence of safety at low traffic.
- **On gate failure:** stop exposure and execute the tested safe recovery. Automate rollback only when data and external side effects permit it; otherwise use roll-forward or containment. Record recovery time and preconditions.
- **Watch the error budget.** If the service is out of budget, only reliability and security fixes ship (run-slo-error-budget).
- **Feature-flag lifecycle:**
  - Every flag has a *type* (release, experiment, ops/kill-switch, permission), an *owner*, and a *removal date* at creation.
  - Release flags are removed (flag *and* dead code path) within ~2 weeks of reaching 100%. CI warns and then fails on expired flags.
  - Ops kill switches may be permanent. Document them in the runbook.
- **Database changes use expand → migrate → contract.** Never ship a schema change and the code that requires it in the same step. Every migration is backward-compatible with the previous app version.
- **Ship small and often.** Avoid deploying *risky* changes right before low-coverage periods (holidays, Friday night). Do not freeze the routine pipeline.
- **Release notes / changelog** are generated from conventional commits and edited for humans.

## Logic
1. Classify the change's risk by blast radius, reversibility, and data impact.
2. Pick a strategy: direct (low risk), flag plus staged ramp (most), canary or blue-green (infra and runtime), or dark launch or shadow traffic (high load risk).
3. Emit a rollout plan: stages, gates and thresholds, bake times, rollback trigger and procedure, owner on watch, comms, and the flag removal ticket.

## Pitfalls
- Flags that never die, which double the code paths to test.
- Canary without automated comparison, where someone eyeballs dashboards at midnight.
- Irreversible migrations bundled with app deploys.

## Sources
Google SRE Book ch. 8 (Release Engineering) and Workbook ch. 16 (Canarying Releases); Pete Hodgson, "Feature Toggles" (martinfowler.com); Unleash docs (flag technical debt); DORA capabilities (deployment automation, working in small batches).

## Research and application

Version model, prompt, tools, retrieval index/data, and application together where behavior depends on them. Canary quality, cost, latency, and harmful-action rates as applicable. A successful HTTP response is not proof of a correct AI answer. Shadow calls must not duplicate side effects.

Evidence: P04, R16, R17; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
