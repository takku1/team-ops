---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our suite: 40 end-to-end UI tests (25 minutes, 3 flaky for two weeks with
no owner), 10 integration tests against a shared staging environment, 50
unit tests. Coverage is gated hard at 100% globally, which the team meets
with assertion-free tests. Bugs keep escaping in the billing path, which
has no contract tests against the payment service. Define the test
strategy.
