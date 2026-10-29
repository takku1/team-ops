---
name: measure-delivery-health
description: Measure software delivery performance and developer experience at team level with the DORA metrics (throughput and instability, including rework rate) and the SPACE framework, and turn the results into improvement experiments. Use when someone asks whether the team is getting faster or better, wants productivity metrics or a dashboard, or plans a retro or quarterly review. Not for individual performance evaluation, which is explicitly out of scope.
---

# Delivery Health (DORA + SPACE)

## DORA software delivery metrics
**Throughput**
- **Change lead time**: commit to running in production
- **Deployment frequency**: how often you deploy to production
- **Failed deployment recovery time**: how long to restore after a failed deployment

**Instability**
- **Change fail rate**: share of deployments that need immediate intervention (rollback, hotfix)
- **Deployment rework rate**: share of deployments that are unplanned and made to fix user-facing issues

Read them together. Speed and stability correlate positively in DORA's research, so a gain in one bought with the other is a warning sign.

## SPACE (developer productivity)
**S**atisfaction and well-being · **P**erformance (outcomes) · **A**ctivity · **C**ommunication and collaboration · **E**fficiency and flow. Use **at least 3 dimensions** and mix system data with survey data.

## Policy
- **Team-level only.** Never rank, compare, or evaluate individuals with these metrics, and never compare teams with different contexts.
- **Do not set the metrics as targets** (Goodhart). Pick a constraint and run an experiment, then watch the metrics move.
- **Prefer system data** (VCS, CI/CD, incident tool) plus a short quarterly developer survey.
- **Banned as productivity measures:** lines of code, commit count, PRs per person, story points per person, hours online.
- Pair DORA with outcome metrics (user value, SLO attainment from run-slo-error-budget). Being fast at the wrong thing is not success.

## Logic
1. Require the team scope, period (at least 1 quarter recommended), and data sources.
2. Compute the 5 DORA metrics and at least 3 SPACE signals. Note any data gaps honestly.
3. Identify the biggest constraint (e.g. review wait from build-code-review, a slow CI from build-trunk-integration, flaky tests from build-test-strategy).
4. Propose 1-2 improvement experiments, each with a hypothesis, the metric expected to move, and a review date.

## Output
- Snapshot table: metric | value | trend | data source
- Constraint diagnosis
- Experiments, each with owner and review date
- Metrics excluded on purpose and why

## Sources
DORA *Accelerate State of DevOps* reports and dora.dev guides (five software delivery metrics; rework rate added in 2024); Forsgren et al., "The SPACE of Developer Productivity" (ACM Queue, 2021); Forsgren, Humble & Kim, *Accelerate* (2018).

## Research and application

Compare AI workflows on representative tasks using elapsed time, active human time, accepted correctness, rework, and total cost. Record task mix and model/tool versions. Use randomized or matched comparisons where feasible; before/after differences alone are not causal. Do not claim today's AI speedup from an old trial.

Evidence: R08, R15, P03; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
