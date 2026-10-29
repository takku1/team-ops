---
name: plan-late-recovery
description: Recover a slipping project without making it later. Apply Brooks's Law, cut scope before adding people, protect the critical path, and re-baseline honestly. Use when a deadline is at risk, someone proposes adding staff or overtime to a late project, or a forecast just moved right. Not for initial estimation (use plan-estimate-forecast).
---

# Late Project Recovery

Brooks's Law: adding people to a late software project makes it later. New staff cost ramp-up time, and communication paths grow as n(n-1)/2. Brooks himself called this an outrageous simplification: added people *can* help when the work partitions cleanly and the addition happens early.

## Policy, in this order of preference
1. **Re-baseline honestly.** Re-forecast with actuals (plan-estimate-forecast) and tell stakeholders now, not at the deadline.
2. **Cut or defer scope.** Rank the remaining items by value. Ship the minimum lovable slice and move the rest below the line.
3. **Remove waste and blockers.** Clear queues: review wait, environment and test bottlenecks, approval delays. Lower WIP.
4. **Protect the critical path.** Its owners stop doing interrupts, meetings, and support rotation, and other people absorb those.
5. **Add people only when expected useful work exceeds onboarding and coordination cost within the remaining horizon.** Check separability, expertise, integration effort, and critical-path impact. The former one-third-timeline rule is not an empirical cutoff; apply the same test before adding AI workers.
6. **Sustained overtime is not a plan.** At most a short, time-boxed push, followed by recovery.

## Logic
1. Require: the deadline and what it is tied to (fixed or negotiable), the remaining scope, the critical path, and current throughput.
2. Quantify the gap using the supported forecast range (or a calibrated percentile), not an invented P85. Identify which constraints actually drive the deadline.
3. Apply levers 1-4 and recompute. Consider lever 5 only if a gap remains, and check every one of its conditions.
4. Output a decision memo.

## Output
- Gap and cause (scope growth, estimation error, blockers, attrition)
- Chosen levers, each with its expected effect on the forecast
- The new commitment (range) and what was cut
- Staffing decision with the Brooks check shown

## Pitfalls
- Shrinking test or review time to "save" days. That moves the cost into incidents (run-incident-postmortem).
- Silently slipping without re-baselining.

## Sources
Fred Brooks, *The Mythical Man-Month* (1975, anniversary ed. 1995); Steve McConnell, "Brooks' Law Repealed?" (IEEE Software, 1999); Goldratt, *Critical Chain*.

## Research and application

Brooks is a practitioner warning, not a universal theorem; n(n-1)/2 counts possible communication pairs, not measured coordination effort. Measure the bottleneck before adding humans, agents, or compute; retain necessary verification.

Evidence: R05, R15; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
