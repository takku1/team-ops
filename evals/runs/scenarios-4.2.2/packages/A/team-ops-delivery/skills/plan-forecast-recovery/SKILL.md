---
name: plan-forecast-recovery
description: "Forecast dates or agent-run budgets as honest ranges (reference class, throughput, labeled scenarios; no fake percentiles) and recover slipping work without blindly adding people or agents."
---

# Forecast and Recovery

Give honest ranges instead of false precision, and recover slipping work with levers that actually help.

**Return:** a forecast (supported percentiles with model assumptions, or explicitly uncalibrated scenarios, plus top risks and a re-forecast point), or a recovery memo (gap and cause, chosen levers and expected effect, new commitment range and what was cut, and the staffing or agent decision with the Brooks check shown).

## Forecast

1. **Define** remaining scope, dependencies, and capacity.
2. **Pick a method, history first:**
   - *Reference class or own throughput* (the outside view) beats guessing. Resample throughput only after checking that work type, scope size, capacity, and serial dependence are comparable. Eight to twelve weeks is a starting window, not a validity threshold.
   - *No history:* elicit optimistic, likely, and pessimistic scenarios with their assumptions, labeled uncalibrated. The PERT mean `(O + 4M + P) / 6` is not a median or percentile; never derive P50/P85 by summing means and variances without a justified distribution and dependence model.
   - *Little's Law* (average WIP = throughput × average time in system) relates long-run averages in a stable system. WIP ÷ throughput is an average cycle time, not an 85th-percentile promise; a service-level expectation needs the actual cycle-time distribution.
3. **Report** percentiles only when a model supports them, with inputs, seed, sample count, units, and sensitivity; otherwise a range. Explain missing data. Name the top three risks with trigger signals.
4. **Stay honest.** A deadline is not a forecast. Show buffers explicitly at the end instead of padding each task. Re-forecast with actuals and publish changes early. Estimates are not targets; never grade people or agents on estimate accuracy.

**Agent run budgets** use host-exposed units (turns, tokens, money, elapsed time) and include waits, repairs, review, and integration. Unknown cost stays unknown; comparable past runs beat benchmark scores. team-lead owns admission, retries, and stopping.

## Recover

Brooks's Law (adding people to a late project makes it later) is, by Brooks's own account, a simplification: capacity added early to cleanly partitioned work can help. The same test applies to agents. In order of preference:

1. **Re-baseline honestly.** Re-forecast with actuals and tell the user now, not at the deadline.
2. **Cut or defer scope.** Rank remaining items by value; ship the smallest useful slice.
3. **Remove the bottleneck,** measured first: review queue, flaky or slow checks, environment contention, waiting on a decision. Lower WIP.
4. **Protect the critical path** from interrupts.
5. **Add people or agents only when** the work splits into disjoint scopes, expected useful output exceeds onboarding, briefing, review, and integration cost within the remaining horizon, and someone can integrate it. N agents are not N times the throughput.
6. **Never** sustain overtime or cut verification to "save" time; that moves the cost into incidents.

**A stuck agent run** (repeated attempts without new evidence, rising rework, the same failing check): stop the loop, then re-diagnose, re-split, change capability or effort, or report blocked with resumable state. Never add parallel agents to an undiagnosed task.

Evidence: R05, R06, R15; Brooks is a practitioner warning, not a theorem; buffers and the stop rule are suite defaults ([register](../../references/research-evidence.md)).
