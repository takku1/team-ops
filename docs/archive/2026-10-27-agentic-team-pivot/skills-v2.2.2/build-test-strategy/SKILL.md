---
name: build-test-strategy
description: Define a test strategy and policy covering the test pyramid or test sizes, what each layer must cover, contract tests between services, flaky-test handling, coverage as a signal rather than a target, and test-data rules. Use when setting up testing for a project, when CI is slow or flaky, when bugs escape to production, or when a team argues about coverage. Not for load and performance capacity planning.
---

# Test Strategy

## Policy
- **Choose test layers by failure risk and feedback speed.** Prefer many fast focused tests where they detect the relevant failures; add integration, contract, and end-to-end tests for boundaries and journeys. A 70/20/10 count ratio is not a scientifically established optimum.
- **Behavioral fixes need evidence that distinguishes the defect from the fix**, preferably a regression test. Use documented reproduction or manual verification when automation is disproportionate; do not create tautological tests for prose or trivial cosmetic edits.
- **Service boundaries:** use contract checks for API compatibility and integration tests for real authorization, persistence, ordering, and failure semantics. Contract tests do not replace all integration or end-to-end coverage.
- **End-to-end tests cover only critical user journeys**, the same journeys your SLOs cover (run-slo-error-budget).
- **Flaky tests:** record frequency and cause, assign an owner and fix-by date, and expose retries. Quarantine promptly only with compensating coverage for critical risks. One-day triage and two-week review are suite defaults; never delete the sole safety check merely because its timer expired.
- **Coverage is a diagnostic signal.** Inspect uncovered risky behavior and assertion quality. No universal 60/75/90 tier or global percentage proves adequacy. Use mutation testing selectively, accounting for equivalent mutants and runtime cost.
- **Test data:** synthetic or anonymized. Never use real PII in non-production environments.
- **Speed budget:** PR suite under 10 minutes (build-trunk-integration). Shard or parallelize before cutting tests.
- **Test what is risky.** Weight effort toward auth, money, data integrity, concurrency, and migrations.

## Logic
1. Inventory the existing tests by size, runtime, flakiness rate, and escaped-defect history.
2. Map the risk areas (from the design doc or threat model) to coverage.
3. Emit: a target mix per layer, gaps ordered by risk, a flaky-test quarantine list, a CI stage placement per suite, and coverage reporting configured for changed lines.

## Pitfalls
- The inverted pyramid: an ice-cream cone of slow UI tests.
- Mocking everything, so the tests assert the mocks.
- 100% coverage mandates that produce assertion-free tests.

## Sources
Google Testing Blog: "Test Sizes", "Code Coverage Best Practices" (2020), "Flaky Tests at Google"; Mike Cohn, test pyramid; Martin Fowler, "The Practical Test Pyramid"; Pact docs (consumer-driven contracts); DORA capability: test automation.

## Research and application

Separate deterministic program tests from probabilistic product evals (ai-evaluation). Test outputs against independent expected behavior, not generated implementation details. Inventory risk, suite time, and flakiness before choosing a mix; count ratios alone do not diagnose the suite.

Evidence: R02, R17, R19; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
