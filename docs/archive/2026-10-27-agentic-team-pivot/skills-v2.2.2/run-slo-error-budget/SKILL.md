---
name: run-slo-error-budget
description: Define SLIs and SLOs for user journeys, compute error budgets and burn-rate alerts, and adopt an error budget policy that decides when feature work pauses for reliability. Use when launching or operating a service, when setting alerting, when product and engineering disagree on reliability versus velocity, or when on-call is noisy. Not for incident write-ups (use run-incident-postmortem).
---

# SLOs and Error Budget Policy

## Policy
- **SLIs measure user experience.** Use the ratio of good events to valid events (availability, latency at threshold, correctness, freshness) at the edge closest to the user.
- **SLOs are user-journey commitments**, selected from user needs, current measurements, and feasibility. A rolling 28-30-day window is a common default; do not automatically choose a target below current performance. For a time-based 99.9% SLO over 30 days, the budget is 43.2 minutes; request-based SLOs have a request budget instead.
- **Budget fraction = 1 - SLO.** Allowed bad events = eligible events x budget fraction. Remaining budget subtracts observed bad events. Minutes apply only to a time-based denominator.
- **Burn rate = observed bad-event fraction / (1 - SLO).** For a 30-day window, 14.4x over 1h spends 2% of budget, 6x over 6h spends 5%, and 1x over 3d spends 10% under the example assumptions. Pair long/short windows (e.g. 1h/5m, 6h/30m), require both to fire, and account for low traffic. Recompute for other windows; these are SRE examples, not universal thresholds.
- **Error budget policy (signed by product + eng + SRE):**
  - Within budget: releases proceed normally.
  - **Budget exhausted** over the window: halt changes other than P0 bug fixes and security fixes until the service is back within SLO.
  - **A single incident consuming more than 20% of the budget** requires a postmortem with at least one P0 action item (run-incident-postmortem).
  - **A recurring class of outage consuming more than 20% of the budget per quarter** gets a P0 item on next quarter's plan.
  - Disputes escalate to a named exec (e.g. CTO). Write the escalation path down beforehand.
- **Review SLOs quarterly.** If users are happy at the current level, the SLO may be too strict, and vice versa.

## Logic
1. List the critical user journeys and pick 1-3 SLIs each, saying where they are measured.
2. Set targets from user needs and historical data. Compute budgets in the SLI's actual unit; never convert requests to outage minutes without an explicit traffic model.
3. Emit the burn-rate alert rules and dashboard spec.
4. Emit an error budget policy doc (goals, non-goals, thresholds, actions, escalation, signers).

## Pitfalls
- SLOs on CPU or host metrics rather than on user experience.
- A policy nobody signed, which gets ignored at the first deadline.
- Pages for symptoms that self-heal, which fatigues on-call.

## Sources
Google SRE Book ch. 4 (Service Level Objectives); SRE Workbook ch. 2 (Implementing SLOs), ch. 5 (Alerting on SLOs), Appendix B (Example Error Budget Policy, sre.google/workbook/error-budget-policy).

## Research and application

The 20% incident trigger, P0 action, release pause, and quarterly review are example policies requiring local adoption. Set exceptions and recovery authority explicitly. Track AI task quality separately from availability; delayed/noisy quality labels need a sampling and adjudication plan.

Evidence: P04, R17; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
