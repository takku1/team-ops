# team-ops on Muse — usage report, round 3 (2026-10-27)

Third loop, on the new updates (`scripts/install-muse.ps1` + STATUS entry).
This round tested the two biggest remaining items: the install wrapper and
`eng-policy-lead` audit mode — the pack's stated Active Focus field test,
never before exercised. Both verified live.

## 1. Install wrapper: FIXED and verified by operator

Ran `scripts/install-muse.ps1` directly: plugin refreshed to the latest
source, output `OK: 'team-ops' enabled=True active=True warnings=35
errors=0`, **exit 0**. The wrapper judges by observed plugin state
(enabled + active + zero error diagnostics) instead of the misleading
`muse plugins install` exit code. The round-1/2 top automation complaint
is closed — scripts can now gate on this wrapper's exit code honestly.

## 2. Audit mode field test: WORKS from SKILL.md alone

`eng-policy-lead` audit flow executed repo-locally against MochiOS with
no external API, scoring three policies written / enforced / followed:

| Policy | Written | Enforced | Followed |
|---|---|---|---|
| Test strategy | NOT WRITTEN (no `docs/policy/`) | PARTIAL (CI: test, build, clippy `-D warnings`, deny, kani; no coverage, no flake quarantine) | PARTIAL (unit tests present; `storage-restart` exit-134 flake open with no quarantine owner/date; heavy QEMU E2E hints at inverted pyramid) |
| Code review | NOT WRITTEN (no CODEOWNERS, no PR template) | NOT ENFORCED (no approval gate visible; branch protection unobservable locally) | SIZE NORM NOT FOLLOWED (817+72, 30270-line, 549/1365/905-line commits vs ~100/1000 norms); response-time/approval UNKNOWN (no PR history locally) |
| Definition of done | NOT WRITTEN (CLAUDE.md Build & Test is the de-facto bar) | PARTIAL (build/lint/test/deny/kani/docs-audit; no SAST/secret-scan, staging, flag/rollback, changelog checks) | MIXED (gates demonstrably run; per-increment docs/ADR/changelog unverifiable from log sample) |

Top-3 risk-ranked gaps, each with owner/skill/effort: (1) no
CODEOWNERS/required-approver routing incl. second approver for security
paths (tech lead, build-code-review, S); (2) no secret/SAST scan gate
(security/CI owner, secure-supply-chain, S–M); (3) no test-strategy doc,
unquarantined flake, no coverage signal, oversized commits (eng/test
owner, build-test-strategy, M).

Known limits (named, not hidden): branch-protection settings need GitHub
API access; PR response-time/approval history unsampled (log shows pushed
commits, not PR sizes); coverage-tooling exclusion rests on a workflow
job-name scan. These bound the *enforced/followed* verdicts above, and
the skill is honest about what it cannot see locally — the right call
for an audit tool.

## 3. Eval regression: PASS on all five criteria

`policy-lead-audit-top-three` checked against the SKILL text:
written/enforced/followed scoring (L109/L188), security-and-reliability-
before-flow ranking (L111–113/182), at-most-3 fixes with owner/skill/
effort and retry loop (L116–121), stop-at-blocking-findings (L53/59/176
— the eval's exact two blockers), and none of the fail conditions
triggered. Every expectation MATCHed by line reference.

## 4. Rating: 9 / 10

Round 2 gave 8, with three items open: install exit code, inert gates,
untested audit mode. Two are now closed-verified (wrapper exits 0;
audit mode ran a real repo end-to-end and its eval passes). What keeps
the last point: SkillWren gates remain advisory on Muse by declared
decision (accepted, but still a capability gap vs Claude Code), and the
written-adapter-file half of the repo-adapter pattern is still
unexercised — inline values keep sufficing. A loop that tests the
bootstrap-written adapter, or one that closes an audit gap (CODEOWNERS
+ required approvals would be the S-effort highest-leverage pick),
earns the 10.
