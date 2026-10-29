# team-ops on Muse — usage report, round 8 (2026-10-27): v2.2.0 release check

Verification-only round (no implement loop): the pack jumped to 2.2.0
with 25 skills, 26 behavioral scenarios, an eval protocol, static
validator tooling, and a version-pinned install wrapper. Every
releasable claim was checked live.

## Verified

- **Structure:** 25 skill dirs, 26 `case.json` files, every one
  `status: not-run`. No retroactive pass claims anywhere.
- **Static validation:** ran `python scripts/validate-suite.py`
  myself → 25 skills, 3 manifests, 26 cases, **0 errors**,
  `behavioral_evals_executed: false`. Matches `validation-v2.2.md`
  exactly (which honestly states static-only scope).
- **Install wrapper v2:** pins expected version from `plugin.json`
  and requires match. Ran it → `OK: 'team-ops' 2.2.0 enabled=True
  active=True warnings=35 errors=0`, exit 0; `plugins list`
  confirms 2.2.0 live. Closes the stale-cache false-positive hole.
- **Eval protocol:** `evals/PROTOCOL.md` is rigorous (freeze,
  blind rubrics, isolated workspace, cost retention, no invented
  thresholds) and explicitly scopes my rounds 1–7 as historical
  exercises against older text — which is what my reports already
  say. The new `implementation-zero-limit` fixture exists
  (`parser.py` + `test_parser.py`).
- **Docs consistency:** STATUS (2.2.0, 26-scenario eval line,
  historical-evidence disclaimer), CHANGELOG 2.2.0 entry, README —
  all agree. (One false alarm: the `→` in my 2.1.0 changelog line
  renders fine on disk; an earlier garble was terminal encoding,
  not file damage. No edit needed.)

## Rating: holding at “not run” for v2.2.0 content

No rating change today, by the protocol's own rule: new scenarios
are coverage, not proof, and nothing behavioral ran. My 9.5→10 arc
stands as scoped to the v2.0/v2.1-era skills it exercised. The next
honest number for v2.2.0 comes from running the protocol —
`implementation-zero-limit` is the natural first candidate since
it's executable and self-checking.
