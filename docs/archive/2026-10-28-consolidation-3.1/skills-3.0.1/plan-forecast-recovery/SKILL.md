---
name: plan-forecast-recovery
description: Forecast when work will be done, and what an agent run will cost, as honest ranges, then recover slipping work or a stuck run without making it later. Uses reference-class data, throughput Monte Carlo, or labeled scenarios, and puts scope cuts and bottleneck removal ahead of adding people or agents (Brooks's Law). Use when someone asks "when will it be done?", commits to a date, sets an agent budget, or a forecast or run is slipping. Lead playbook.
---

# Forecast and Recovery

**Role:** lead (team-lead). **Returns:** a forecast or a recovery decision with its assumptions shown.

## Forecast

- **Deadlines and forecasts are different things.** Give a range, or a conditional percentile when a model supports one. Label expert scenarios as uncalibrated instead of inventing confidence.
- **Use history first (the outside view).** Reference-class data or your own throughput beats guessing. Resample throughput only after checking that work type, scope size, capacity, and serial dependence are comparable. Eight to twelve weeks of history is a starting window, not a validity threshold.
- **With no history,** elicit optimistic, likely, and pessimistic scenarios and their assumptions. The PERT mean `(O + 4M + P) / 6` is not a median or a percentile. Do not derive P50 or P85 by summing means and variances without a justified distribution and dependence model.
- **Little's Law** (average WIP = throughput × average time in system) relates long-run averages in a stable system. WIP divided by throughput gives an average cycle time, not an 85th-percentile promise. A service level expectation needs the actual cycle-time distribution.
- **Show buffers explicitly** at the end rather than hiding padding in each task. Re-forecast with actuals and publish changes early.
- **Estimates are not targets.** Never grade people or agents on estimate accuracy.

Procedure: define the remaining scope, dependencies, and capacity. Choose comparable reference data, a justified simulation, or labeled scenarios, and explain missing data. Report percentiles only when a model supports them, with inputs, seed, sample count, units, and sensitivity. Name the top three risks with trigger signals.

### Agent run budgets

Budget an agent task in turns, tokens or money, and wall time, from comparable past runs where you have them. Include waits, retries, review, and integration, not only generation. A benchmark score or a perceived speedup does not calibrate a forecast. Set the stop rule before the run starts: the budget, plus "two rounds with no new evidence".

## Recover

Brooks's Law: adding people to a late software project makes it later, because of ramp-up and coordination. Brooks called it an outrageous simplification: added capacity can help when the work partitions cleanly and is added early. The same test applies to agents. In order of preference:

1. **Re-baseline honestly.** Re-forecast with actuals and tell the user now, not at the deadline.
2. **Cut or defer scope.** Rank the remaining items by value and ship the smallest useful slice.
3. **Remove the bottleneck.** Measure it first: review queue, flaky or slow checks, environment contention, waiting on a decision. Lower WIP.
4. **Protect the critical path** from interrupts.
5. **Add people or agents only when** the work separates into disjoint scopes, the expected useful output exceeds onboarding, briefing, review, and integration cost within the remaining horizon, and someone has the capacity to integrate it. N agents are not N times the throughput.
6. **No sustained overtime,** and no cutting verification to "save" time. That moves the cost into incidents.

### A stuck agent run

Signs: repeated attempts with no new evidence, a rising rework count, or the same failing check. Stop the loop. Then re-diagnose (an investigate phase), re-split the task, change capability or effort, or report blocked with a resumable state. Do not add parallel agents to a task you have not diagnosed.

## Output

- Forecast: supported percentiles with model assumptions, or explicitly uncalibrated scenarios, with risks and a re-forecast point.
- Recovery memo: the gap and its cause, the levers chosen with their expected effect, the new commitment range and what was cut, and the staffing or agent decision with the Brooks check shown.

Evidence: R05 (Little's Law), R06 (reference-class forecasting), R15 (perceived versus measured AI speed). Brooks is a practitioner warning, not a theorem, and n(n-1)/2 counts possible communication pairs, not measured effort. Buffers and the two-round stop rule are suite defaults. See the [research register](../../docs/current/research-evidence.md).
