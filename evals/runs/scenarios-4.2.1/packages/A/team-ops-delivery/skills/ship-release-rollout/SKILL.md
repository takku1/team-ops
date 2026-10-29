---
name: ship-release-rollout
description: "Plan a safe release: deploy vs release, staged or canary rollout with health gates, recovery defined first, flag lifecycle, expand-migrate-contract migrations. Use before risky deploys or launches."
---

# Release and Rollout

Plan how a change reaches users so failures stay small, visible, and recoverable. Publishing and deploying follow existing user authorization; prepare the artifact, gates, and recovery before asking for any missing decision.

**Return:** stages, gates and thresholds, bake times, recovery trigger and procedure, owner, comms, and the flag-removal ticket.

## Plan the rollout

1. **Classify risk** by blast radius, reversibility, data impact, and external side effects (charges, emails, third-party writes).
2. **Pick a strategy:** direct (low risk); flag plus staged ramp (most changes); canary or blue-green (infrastructure and runtime); dark launch or shadow traffic (load risk). Shadow calls must not repeat side effects.
3. **Set gates from traffic and risk:** cohorts, health metrics that measure correctness (not just HTTP 200), minimum event counts, observation windows, and an owner on watch. A 1/10/50/100% ramp or a 30–60-minute bake is illustrative; at low traffic a fixed bake time proves nothing.
4. **Define recovery before starting:** the trigger and the procedure. Automate rollback only where data and side effects allow it; otherwise roll forward or contain. Side effects that already happened need compensation, not rollback, so make them idempotent.

**Before returning, verify:** recovery trigger and procedure exist before the first stage; every gate names a metric, threshold, minimum event count, and owner; every new flag has an owner and removal date.

## Policy

- **Deploy is not release.** Deploy dark; release by flag or traffic shift.
- **Apply the adopted error-budget policy.** Without one, propose the applicable freeze/exception rule instead of imposing one (run-slo-error-budget).
- **Every flag** gets a type (release, experiment, ops kill switch, permission), an owner, and a removal date at creation. Propose a cleanup deadline (e.g. two weeks after 100%) and repo-appropriate enforcement, preserving any adopted deadline. Kill switches may be permanent and live in the runbook.
- **Database changes** use expand, migrate, contract. Never ship a schema change with the code that needs it in one step; each migration stays compatible with the previous app version.
- **AI behavior** depends on model, prompt, tools, and retrieval index together: version and canary them together, gating on task quality, cost, latency, and harmful-action rates.
- **Ship small and often.** Avoid risky deploys before low-coverage periods, but do not freeze the routine pipeline.
- **Release evidence follows the exact artifact promoted;** do not rebuild just because the stage changed. Generate notes from the repo's adopted metadata and edit them for users.

Evidence: P03, P04, P08, R16, R17, R32, R34 ([register](../../references/research-evidence.md)).
