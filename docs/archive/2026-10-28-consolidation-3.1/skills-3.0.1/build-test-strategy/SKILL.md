---
name: build-test-strategy
description: Define a test strategy and policy covering the test pyramid or test sizes, what each layer must cover, contract tests between services, flaky-test handling, coverage as a signal rather than a target, and test-data rules. Use when setting up testing for a project, when CI is slow or flaky, when bugs escape to production, or when a team argues about coverage. Not for load and performance capacity planning.
---

# Test Strategy

**Role:** reviewer and verifier, when judging whether tests are meaningful or choosing which checks prove a change; the lead, when setting a project's test policy. **Returns:** test gaps ranked by risk, flaky-test handling, and the checks to run.

## Policy

- **Test what is risky.** Weight effort toward auth, money, data integrity, concurrency, migrations, and whatever has escaped before.
- **Choose layers by failure risk and feedback speed.** Many fast focused tests where they catch the relevant failures; integration, contract, and end-to-end tests for boundaries and journeys. A 70/20/10 ratio is folklore, not an established optimum.
- **A behavioral fix needs evidence that tells the defect from the fix**, preferably a regression test. Use documented manual verification where automation is disproportionate; do not write tautological tests for prose or cosmetic edits.
- **Assertions must be able to fail.** Test against independent expected behavior, not generated implementation details. Mocking everything tests the mocks.
- **Service boundaries:** contract checks for API compatibility, integration tests for real authorization, persistence, ordering, and failure semantics. Contracts do not replace those.
- **End-to-end tests cover critical user journeys only**, the ones the SLOs cover (run-slo-error-budget).
- **Flaky tests:** record frequency and cause, assign an owner and fix-by date, and keep retries visible. Quarantine only with compensating coverage for critical risks. Never delete the only safety check because its timer ran out. One-day triage and two-week review are suite defaults.
- **Coverage is a diagnostic.** Look at uncovered risky behavior and assertion quality. No global percentage proves adequacy, and a 100% gate breeds assertion-free tests. Use mutation testing selectively.
- **Test data** is synthetic or anonymized. No real PII outside production.
- **PR suite under about 10 minutes** (build-trunk-integration). Shard or parallelize before cutting tests.
- **Programs and models differ:** deterministic tests for code, probabilistic evals for AI behavior (ai-evaluation).

## Procedure

1. Inventory tests by size, runtime, flakiness, and escaped-defect history.
2. Map risk areas (from the design note, threat model, or incident history) to coverage.
3. Output: gaps ordered by risk, the target mix per layer, a flaky-test list with owners, CI stage placement per suite, and coverage reported on changed lines.

## Pitfalls

The ice-cream cone of slow UI tests. Tests that assert their own mocks. Silent retries that hide flakes. Coverage mandates.

Evidence: Google Testing Blog ("Test Sizes", "Code Coverage Best Practices", "Flaky Tests at Google"); Cohn's test pyramid; Fowler, "The Practical Test Pyramid"; Pact docs; DORA test automation. R02 (coverage weakly predicts effectiveness), R17, R19. See the [research register](../../docs/current/research-evidence.md).
