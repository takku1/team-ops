---
name: run-slo-error-budget
description: "Define SLIs and SLOs for user journeys, compute error budgets and burn-rate alerts in the right units, and draft an error-budget policy. Use when launching or operating a service or tuning alerts."
---

# SLOs and Error Budget Policy

Turn user experience into measurable targets, budgets, and alerts, then draft a policy the user can adopt.

**Return:** SLIs, SLOs, budgets, burn-rate alerts, a dashboard spec, and a proposed budget policy. Verify that alerts and dashboards actually exist and fire.

## Procedure

1. List critical user journeys; pick one to three SLIs each and say where they are measured.
2. Set targets from user needs and history; compute budgets in each SLI's own unit.
3. Write burn-rate alert rules and the dashboard spec.
4. Draft the policy (thresholds, actions, escalation, signers). Mark proposed policy separately from adopted and enforced rules; writing a proposal never activates a release freeze.

## Define

- **SLIs measure user experience:** good events ÷ valid events (availability, latency under a threshold, correctness, freshness), measured as close to the user as practical. Not CPU or host metrics.
- **SLOs are user-journey commitments** chosen from user needs, current measurements, and feasibility. A rolling 28–30-day window is a common default. Do not reflexively set a target below current performance.
- **AI task quality is its own SLI,** separate from availability. Delayed or noisy quality labels need a sampling and adjudication plan.

## Compute in the SLI's unit

- **Budget fraction** = 1 − SLO. Allowed bad events = eligible events × budget fraction. Remaining = allowed − observed bad.
- **Minutes apply only to time-based SLIs:** 99.9% over 30 days is 43.2 minutes. Request-based SLOs have request budgets; never convert requests to minutes without an explicit traffic model.
- **Burn rate** = observed bad-event fraction ÷ (1 − SLO). Budget spent = burn rate × alert window ÷ SLO window. Over 30 days (720 h): 14.4× for 1 h spends 2%, 6× for 6 h spends 5%, 1× for 3 days spends 10%. Recompute for other windows: 14.4× for 1 h in a 7-day window spends about 8.6%.
- **Alert on paired windows** (e.g. 1 h with 5 min, 6 h with 30 min) and page only when both fire. Low traffic makes ratios noisy; set minimum event counts. Do not page on symptoms that self-heal. These are SRE examples, not universal thresholds.

## Example policy (adopt locally)

- Within budget: releases proceed.
- Budget exhausted for the window: only P0 bug fixes and security fixes ship until the service is back within SLO.
- One incident consuming more than 20% of the budget: postmortem with at least one P0 action (run-incident-postmortem).
- A recurring outage class consuming more than 20% per quarter: a P0 item in next quarter's plan.
- Disputes go to a named decision-maker, recorded beforehand along with exceptions and who can lift a freeze.
- Review SLOs quarterly; happy users at the current level may mean the SLO is too strict.

Evidence: P04, P08, R17; thresholds and freeze rules are example policy ([register](../../references/research-evidence.md)).
