---
name: plan-estimate-forecast
description: Produce honest delivery forecasts as ranges with confidence levels, using reference-class data, throughput-based Monte Carlo, or three-point estimates, and guard against planning fallacy and Goodhart effects. Use when someone asks "when will it be done?", commits to a date, or estimates look optimistic. Not for recovering an already-late project (use plan-late-recovery).
---

# Estimate and Forecast

## Policy
- **Distinguish a deadline from a forecast.** Give a range or conditional percentile when supported; label expert scenarios as uncalibrated rather than inventing confidence.
- **Use history first (outside view).** Reference-class data or the team's own throughput beats expert guessing (Kahneman/Flyvbjerg).
- **Forecast with comparable history.** Resample throughput only after checking work type, scope size, capacity changes, and serial dependence. Eight to twelve weeks is a possible starting window, not a validity threshold; use sensitivity analysis and block resampling when justified.
- **No history?** Elicit optimistic/likely/pessimistic scenarios and assumptions. PERT mean `(O + 4M + P) / 6` is not a median or a percentile. Do not derive P50/P85 by summing means/variances without a justified distribution and dependence model.
- **Show the buffer explicitly** as a project buffer at the end, not padding hidden in each task. Hidden padding gets consumed (Parkinson).
- **Re-forecast every week** with actuals, and publish changes early.
- **Estimates are not targets.** Never measure people on estimate accuracy or velocity (Goodhart's law).

## Logic
1. Define remaining scope, dependencies, and capacity. Model explicit scope-change scenarios; do not automatically add an unsupported 10-30% buffer.
2. Choose comparable reference data, a justified throughput simulation, or uncalibrated scenarios. Explain missing data and selection bias.
3. Report P50/P85/P95 only when a model supports them; retain input data, seed, sample count, units, dependency assumptions, and sensitivity. Backtest forecast calibration when completed outcomes exist.
4. Name the top 3 risks, each with a trigger signal.

## Output
- Forecast: supported percentiles with model assumptions, or explicitly uncalibrated scenarios
- Assumptions and risks
- Re-forecast cadence and owner

## Pitfalls
- Anchoring on a date someone already promised.
- Converting points to hours, or comparing velocity across teams.
- Hofstadter's law: it takes longer even when you account for Hofstadter's law. Trust the data over optimism.

## Sources
Kahneman & Tversky (planning fallacy); Flyvbjerg, reference class forecasting; Daniel Vacanti, *When Will It Be Done?* (Monte Carlo); Troy Magennis, Focused Objective forecasting tools; Goodhart's law.

## Research and application

Distinguish prediction uncertainty from uncertainty about estimated parameters. Include waits, retries, review, and integration in AI work estimates. Neither benchmark throughput nor perceived speedup calibrates a delivery forecast.

Evidence: R05, R06, R15; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
