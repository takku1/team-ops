---
name: build-test-strategy
description: "Set a project's test strategy: layers by risk and speed, contract vs integration tests, flaky-test ownership, coverage as a diagnostic, test data. Use when CI is slow or flaky or bugs escape."
---

# Test Strategy

**Role:** lead, when setting a project's test policy; reviewers use it to judge whether tests are meaningful. **Returns:** test gaps ranked by risk, flaky-test handling, and the checks to run.

## Policy

- **Test what is risky.** Weight effort toward auth, money, data integrity, concurrency, migrations, and whatever has escaped before.
- **Choose layers by failure risk and feedback speed.** Many fast focused tests where they catch the relevant failures; integration, contract, and end-to-end tests for boundaries and journeys. A 70/20/10 ratio is folklore, not an established optimum.
- **A behavioral fix needs evidence that tells the defect from the fix**, preferably a regression test. Use documented manual verification where automation is disproportionate; do not write tautological tests for prose or cosmetic edits.
- **Assertions must be able to fail.** Test against independent expected behavior, not generated implementation details. Mocking everything tests the mocks.
- **Service boundaries:** contract checks for API compatibility, integration tests for real authorization, persistence, ordering, and failure semantics. Contracts do not replace those.
- **End-to-end tests prioritize critical user journeys.** Tie them to user risks and adopted SLOs where available; do not require a service SLO for every test.
- **Flaky tests:** record frequency and cause, assign an owner and fix-by date, and keep retries visible. Quarantine only with compensating coverage for critical risks. Never delete the only safety check because its timer ran out. One-day triage and two-week review are suite defaults.
- **Coverage is a diagnostic.** Look at uncovered risky behavior and assertion quality. No global percentage proves adequacy, and a 100% gate breeds assertion-free tests. Use mutation testing selectively.
- **Test data** is synthetic or anonymized. No real PII outside production.
- **Keep feedback fast.** About ten minutes is an adjustable PR-suite target. Measure queue, runtime, cold builds, and duplicate executions before sharding. Share current evidence through the designated verification owner; never drop a required check just to reduce time.
- **Programs and models differ:** deterministic tests for code, probabilistic evals for AI behavior (ai-evaluation).

## Procedure

1. Inventory tests by size, runtime, flakiness, and escaped-defect history.
2. Map risk areas (from the design note, threat model, or incident history) to coverage.
3. Output: gaps ordered by risk, the target mix per layer, a flaky-test list with owners, CI stage placement per suite, and coverage reported on changed lines.

## Pitfalls

The ice-cream cone of slow UI tests. Tests that assert their own mocks. Silent retries that hide flakes. Coverage mandates.

Use referenced core playbooks when available; otherwise perform the applicable step inline. See [host fallbacks](../../references/host-compatibility.md) only when a capability is missing.

Evidence: Google Testing Blog ("Test Sizes", "Code Coverage Best Practices", "Flaky Tests at Google"); Cohn's test pyramid; Fowler, "The Practical Test Pyramid"; Pact docs; DORA test automation. R02 (coverage weakly predicts effectiveness), R17, R19. See the [research register](../../references/research-evidence.md).
