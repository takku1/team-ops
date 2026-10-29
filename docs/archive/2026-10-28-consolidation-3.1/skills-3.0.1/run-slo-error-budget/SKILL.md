---
name: run-slo-error-budget
description: Define SLIs and SLOs for user journeys, compute error budgets and burn-rate alerts, and adopt an error budget policy that decides when feature work pauses for reliability. Use when launching or operating a service, when setting alerting, when product and engineering disagree on reliability versus velocity, or when on-call is noisy. Not for incident write-ups (use run-incident-postmortem).
---

# SLOs and Error Budget Policy

**Role:** lead, when the product runs as a service; the verifier checks that the alerts and dashboards actually exist and fire. **Returns:** SLIs, SLOs, budgets, burn-rate alerts, and a budget policy for the user to adopt.

## Define

- **SLIs measure user experience:** good events ÷ valid events (availability, latency under a threshold, correctness, freshness), measured as close to the user as practical. Not CPU or host metrics.
- **SLOs are user-journey commitments,** chosen from user needs, current measurements, and feasibility. A rolling 28–30-day window is a common default. Do not set a target below current performance by reflex.
- **AI task quality is its own SLI,** tracked separately from availability. Delayed or noisy quality labels need a sampling and adjudication plan.

## Compute (in the SLI's own unit)

- **Budget fraction** = 1 − SLO. Allowed bad events = eligible events × budget fraction. Remaining = allowed − observed bad.
- Minutes apply only to a time-based SLI: 99.9% over 30 days is 43.2 minutes. A request-based SLO has a request budget. Never convert requests to minutes without an explicit traffic model.
- **Burn rate** = observed bad-event fraction ÷ (1 − SLO). Budget spent = burn rate × alert window ÷ SLO window. Over 30 days (720 h), 14.4× for 1 h spends 2%, 6× for 6 h spends 5%, 1× for 3 days spends 10%. For another SLO window, recompute: the same 14.4× over 1 h in a 7-day window spends about 8.6%.
- **Alert on paired windows** (e.g. 1 h with 5 min, 6 h with 30 min) and require both to fire. Low traffic makes ratios noisy; set minimum event counts. These are SRE examples, not universal thresholds.

## Error budget policy (example; adopt locally)

- Within budget: releases proceed.
- Budget exhausted over the window: only P0 bug fixes and security fixes ship until the service is back within SLO.
- One incident consuming more than 20% of the budget: postmortem with at least one P0 action (run-incident-postmortem).
- A recurring outage class consuming more than 20% per quarter: a P0 item in next quarter's plan.
- Disputes escalate to a named decision-maker, written down beforehand, along with exceptions and who can lift a freeze.
- Review SLOs quarterly. Happy users at the current level may mean the SLO is too strict.

## Procedure

1. List critical user journeys and pick one to three SLIs each, saying where they are measured.
2. Set targets from user needs and history, and compute budgets in each SLI's unit.
3. Output burn-rate alert rules and a dashboard spec.
4. Output the policy (thresholds, actions, escalation, signers) for the user to adopt. An unsigned policy is ignored at the first deadline.

Pitfalls: SLOs on host metrics; pages for symptoms that self-heal; a policy nobody signed.

Evidence: Google SRE Book ch. 4; SRE Workbook ch. 2, ch. 5, and the example error budget policy (P04). R17. The 20% triggers, P0 rule, release pause, and quarterly review are example policy. See the [research register](../../docs/current/research-evidence.md).
