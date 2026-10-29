---
name: build-test-strategy
description: "Set a test strategy: layers by risk and speed, contract vs integration tests, flaky-test ownership, coverage as a diagnostic, test data. Use when CI is slow or flaky or bugs escape."
---

# Test Strategy

Put testing effort where failures are likely and costly, and keep feedback fast. Reviewers can use the same rules to judge whether tests are meaningful.

**Return:** test gaps ranked by risk, the target mix per layer, a flaky-test list with owners, CI stage placement per suite, and coverage on changed lines.

## Procedure

1. Inventory tests by size, runtime, flakiness, and escaped-defect history.
2. Map risk areas (from the design note, threat model, or incident history) to coverage.
3. Apply the rules below to produce the return.

## Rules

- **Test what is risky:** auth, money, data integrity, concurrency, migrations, and whatever has escaped before.
- **Choose layers by failure risk and feedback speed.** Many fast focused tests where they catch the relevant failures; integration, contract, and end-to-end tests for boundaries and journeys. A 70/20/10 ratio is folklore, not an optimum.
- **Bug fixes need evidence that tells the defect from the fix,** preferably a regression test. Use documented manual verification where automation is disproportionate; no tautological tests for prose or cosmetic edits.
- **Assertions must be able to fail.** Test against independent expected behavior, not generated implementation details. Mocking everything tests the mocks.
- **At service boundaries,** contract checks cover API compatibility; integration tests cover real authorization, persistence, ordering, and failure semantics. Neither replaces the other.
- **End-to-end tests cover critical user journeys,** tied to user risks and adopted SLOs where they exist. Not every test needs a service SLO.
- **Flaky tests** get a recorded frequency and cause, an owner, a fix-by date, and visible retries. Quarantine only with compensating coverage for critical risks; never delete the only safety check because its timer ran out. Defaults: triage within a day, review within two weeks.
- **Coverage is a diagnostic.** Look at uncovered risky behavior and assertion quality. No global percentage proves adequacy, and a 100% gate breeds assertion-free tests. Use mutation testing selectively.
- **Test data** is synthetic or anonymized; no real PII outside production.
- **Keep feedback fast.** About ten minutes is an adjustable PR-suite target. Measure queue, runtime, cold builds, and duplicate executions before sharding. Share current evidence through the designated verification owner; never drop a required check just to save time.
- **Code and models differ:** deterministic tests for code, probabilistic evals for AI behavior (ai-evaluation).

Evidence: P07, R02, R17, R19; thresholds are suite defaults ([register](../../references/research-evidence.md)).
