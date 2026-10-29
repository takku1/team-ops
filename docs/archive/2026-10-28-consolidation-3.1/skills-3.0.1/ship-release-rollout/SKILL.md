---
name: ship-release-rollout
description: Ship changes safely with progressive delivery covering feature-flag lifecycle, canary and staged rollouts with automated health gates, rollback and roll-forward rules, safe database migrations, and release notes. Use when planning a launch or risky deploy, defining deployment policy, adding a feature flag, or after a bad rollout. Not for branching and CI (use build-trunk-integration).
---

# Release and Rollout

**Role:** verifier and lead, before anything ships. Publishing and deploying are outward actions that need the user's authorization. **Returns:** a rollout plan with gates and a tested recovery path.

## Plan the rollout

1. **Classify risk** by blast radius, reversibility, data impact, and external side effects (charges, emails, writes to third parties).
2. **Pick a strategy:** direct (low risk), flag plus staged ramp (most changes), canary or blue-green (infrastructure and runtime), dark launch or shadow traffic (load risk). Shadow calls must not repeat side effects.
3. **Set gates from traffic and risk:** cohorts, health metrics that measure correctness (not just HTTP 200), minimum event counts, observation windows, and an owner on watch. A 1/10/50/100% ramp or a 30–60-minute bake is illustrative; at low traffic, a fixed bake time proves nothing.
4. **Define recovery before starting:** the trigger and the procedure. Automate rollback only where data and side effects allow it; otherwise roll forward or contain. Side effects that already happened need compensation, not rollback, so make them idempotent.
5. Output: stages, gates and thresholds, bake times, recovery trigger and procedure, owner, comms, and the flag removal ticket.

## Policy

- **Separate deploy from release.** Deploy dark, release by flag or traffic shift.
- **Watch the error budget.** Out of budget means only reliability and security fixes ship (run-slo-error-budget).
- **Flag lifecycle:** every flag has a type (release, experiment, ops kill switch, permission), an owner, and a removal date at creation. Release flags and their dead paths go within about two weeks of reaching 100%; CI warns, then fails, on expired flags. Kill switches may be permanent and live in the runbook.
- **Database changes** use expand, migrate, contract. Never ship a schema change and the code that needs it in one step; each migration stays compatible with the previous app version.
- **AI behavior** depends on model, prompt, tools, and retrieval index together; version and canary them together, gating on task quality, cost, latency, and harmful-action rates.
- **Ship small and often.** Avoid risky deploys before low-coverage periods, but do not freeze the routine pipeline.
- **Release notes** are generated from conventional commits and edited for humans.

Pitfalls: flags that never die; canaries judged by eyeballing dashboards; irreversible migrations bundled with app deploys.

Evidence: Google SRE Book ch. 8 and Workbook ch. 16 (P04); Hodgson, "Feature Toggles"; Unleash docs on flag debt; DORA deployment automation and small batches. R16, R17. See the [research register](../../docs/current/research-evidence.md).
