---
name: ship-release-rollout
description: "Plan a safe release: deploy vs release, staged or canary rollout with health gates, recovery before start, flag lifecycle, expand-migrate-contract migrations. Use before risky deploys or launches."
---

# Release and Rollout

**Role:** verifier and lead, before anything ships. Publishing and deploying follow existing user authorization; prepare the artifact, gates, and recovery before requesting any missing decision. **Returns:** a rollout plan with gates and a tested recovery path.

## Plan the rollout

1. **Classify risk** by blast radius, reversibility, data impact, and external side effects (charges, emails, writes to third parties).
2. **Pick a strategy:** direct (low risk), flag plus staged ramp (most changes), canary or blue-green (infrastructure and runtime), dark launch or shadow traffic (load risk). Shadow calls must not repeat side effects.
3. **Set gates from traffic and risk:** cohorts, health metrics that measure correctness (not just HTTP 200), minimum event counts, observation windows, and an owner on watch. A 1/10/50/100% ramp or a 30–60-minute bake is illustrative; at low traffic, a fixed bake time proves nothing.
4. **Define recovery before starting:** the trigger and the procedure. Automate rollback only where data and side effects allow it; otherwise roll forward or contain. Side effects that already happened need compensation, not rollback, so make them idempotent.
5. Output: stages, gates and thresholds, bake times, recovery trigger and procedure, owner, comms, and the flag removal ticket.

## Policy

- **Separate deploy from release.** Deploy dark, release by flag or traffic shift.
- **Apply the adopted error-budget policy.** If none exists, propose the applicable freeze/exception rule instead of silently imposing one (run-slo-error-budget).
- **Flag lifecycle:** every flag has a type (release, experiment, ops kill switch, permission), an owner, and a removal date at creation. Propose a cleanup deadline (about two weeks after 100% is an example) and enforcement appropriate to the repo; preserve an adopted deadline. Kill switches may be permanent and live in the runbook.
- **Database changes** use expand, migrate, contract. Never ship a schema change and the code that needs it in one step; each migration stays compatible with the previous app version.
- **AI behavior** depends on model, prompt, tools, and retrieval index together; version and canary them together, gating on task quality, cost, latency, and harmful-action rates.
- **Ship small and often.** Avoid risky deploys before low-coverage periods, but do not freeze the routine pipeline.
- **Release evidence** follows the exact artifact being promoted; do not rebuild merely because the rollout stage changed. Generate notes from the repo's adopted metadata and edit for users.

Pitfalls: flags that never die; canaries judged by eyeballing dashboards; irreversible migrations bundled with app deploys.

Use referenced core playbooks when available; otherwise perform the applicable step inline. See [host fallbacks](../../references/host-compatibility.md) only when a capability is missing.

Evidence: Google SRE Book ch. 8 and Workbook ch. 16 (P04); Hodgson, "Feature Toggles"; Unleash docs on flag debt; DORA deployment automation and small batches. R16, R17. See the [research register](../../references/research-evidence.md).
