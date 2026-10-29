# team-ops on Muse — fix / update list (2026-10-27)

## Status after round 6 (2026-10-27) — verified live

- [x] Supply-chain eval gap closed — 9th eval on disk, format-matched, worked end-to-end through `audit-supply-chain`: SLA-breach-first, all gaps evidenced, SLSA named, "planned" = unknown. No fail conditions triggered.
- [x] Drift check clean — all round-report citations land; STATUS count (9) matches disk; version 2.0.0 deliberately held.
- [ ] Deferred by owner decision (not forgotten): remaining SkillWren conversions (needs owner call), 2.1.0 + changelog (bundle with next reinstall), MochiOS-side findings (other repo).
- [ ] Gate to 10 unchanged: approve 12 drafts, write `docs/policy/`, run consuming loop.

## Status after round 8 (v2.2.0 release check) — verified live

- [x] v2.2.0 structure: 25 skills, 26 case.json all `not-run`, validator re-run by operator → 0 errors (matches claims), install wrapper v2 pins version (2.2.0 confirmed live), executable fixture present, docs consistent. False alarm noted: changelog arrow intact on disk (terminal-encoding artifact only).
- [ ] No rating change: v2.2.0 behavioral content is NOT RUN. Next honest number comes from the protocol — suggest `implementation-zero-limit` first (executable, self-checking).
- Rating posture going forward: rounds 1–7 (9.5→10) scoped to v2.0/v2.1-era skills per PROTOCOL.md; v2.2.0 starts at not-run.

## Status after round 7 (2026-10-27) — close-out, verified live

- [x] Draft set APPROVED 12/12 by independent judge; written byte-identical to `docs/policy/` in MochiOS (owner approval gated, granted this round).
- [x] Consuming loop delivered: S2 `<` input-redirect, parse 34/34, shell 254/254, clippy clean in touched files; adapter judged HELPED with logged gaps (wrong task-named path, no per-crate shapes, no file anchors) — next-revision items, not blockers.
- [x] Independently corroborated by operator: 12 files on disk, both suites re-run green, clippy scope clean.
- Rating rationale: 10/10 on evaluated scope — every fix-list item is either live-verified or explicitly UNVERIFIED/out-of-scope; remaining opens are environmental (hosting UI, owner confirmations) or owner-deferred.
- Still open / next loops: audit gap #1 (CODEOWNERS + required approvers, effort S), adapter v1 gaps above, deferred SkillWren conversions (owner call), MochiOS-side cleanups incl. stale slot comments (other repo).

## Status after round 5 (2026-10-27) — verified live

- [x] Draft 12 slot table APPROVED — bounded re-test: 9/9 boot-slot rows MATCH slot 128 / base 0x4000 live, shell-parse correctly excluded, UNVERIFIED marks confirmed correct, stop-before-write honored. (First attempt failed on evidence-contract overflow — full draft text doesn't fit; bounded row-strings do. Methodology note, not a skill gap.)
- [ ] Write approved drafts to `docs/policy/` + one consuming loop — needs owner approval per the skill contract. This is the last item before 10.
- [ ] MochiOS-side (owner repo, not the pack): `.cargo/config.toml:74–100` slot comments confirmed stale vs live JSONs + M.6 unification; consider a `slot` metadata key in target JSONs.

## Status after round 4 (2026-10-27) — verified live

- [x] Install wrapper both branches — exit 0 success AND exit 1 missing-plugin, both operator-verified. Automation trust closed.
- [x] Bootstrap drafts — all 12 name owner + source skill, stop-before-write honored (nothing created). Drafts 1–11 conditionally approved.
- [ ] Draft 12 (repo-adapter) ON HOLD — core facts match ground truth, but per-bin slot table has one live contradiction (compositor slot 160 = 0x5000 missing) plus unverified CI/toolchain/baseline claims. Fix the named gaps before any loop treats it as authoritative.
- [ ] Written-adapter-file half — still no artifact (by design: needs owner approval). Path to 10: fix draft 12, write approved set to `docs/policy/`, run one loop consuming it.

## Status after round 3 (2026-10-27) — verified live

- [x] Install exit-1 — CLOSED by `scripts/install-muse.ps1`: operator ran it, `OK: enabled=True active=True warnings=35 errors=0`, exit 0. Automation can gate on the wrapper.
- [x] Audit mode field test — `eng-policy-lead` audit ran on MochiOS from SKILL.md alone (3 policies scored, top-3 gaps with owner/skill/effort); `policy-lead-audit-top-three` eval passes on all 5 criteria. Known limits named: branch protection needs API access, PR history unsampled, coverage exclusion rests on job-name scan.
- [ ] Written-adapter-file half — still untested (inline values keep sufficing). Suggested next loop: bootstrap-written adapter, or close audit gap #1 (CODEOWNERS + required approvals, effort S).
- [ ] SkillWren gates inert on Muse — accepted by declaration; remains the one structural gap vs Claude Code.

## Status after round 2 (2026-10-27) — verified live

- [x] Evals for build loop — 5 new evals on disk; `code-review-covers-untracked` exercised end-to-end (caught planted SQLi + missing auth). `policy-lead-audit-top-three` exists but audit mode itself still unrun.
- [x] Untracked review coverage — L47/L90–98/L149–153 verified; the refuse-or-caveat branch fired for real on a dirty-tree scoped review (round-2 report §4B).
- [x] SkillWren semantics — declared prose-level in `skillwren-pilot.md` L37–49. Gates remain inert on Muse by decision, not by accident.
- [x] Repo-adapter slot — specified (eng-policy-lead L167, STATUS L13). Inline values sufficed for S1 with no harm; the *written-file* half is still untested.
- [x] STATUS.md scope line — qualified per harness.
- [ ] Install exit-1 on success — still fires (seen again on `plugins update`); documented only. Still the top automation trust issue.
- Round-1 MochiOS review questions (EDIT-flag fallthrough, Offered-state silence, dialog kind 3) and the wire-abi + Cargo.lock commit remain owner-side; the S1 slice added two non-blocking notes (`>>>` message wording, live-gate denial text).

---

Source: first Muse field test (`docs/current/muse-usage-report.md`).
Ordered by priority. [P1] blocks trust or automation; [P2] narrows the
next field test; [P3] polish.

## [P1] Install reports failure on success

`muse plugins install` exits 1 when the only issues are
unsupported-field warnings, even though the plugin lands enabled and
active. Any script wrapping the install reads this as failure.
Fix: warnings must not fail a successful install (or document the exit
code as expected). Repro: install log in the usage report §1.

## [P1] Evals cover 3 of 19 skills — none on the build loop

Existing evals: `adr-uses-madr`, `code-review-flags-risk`,
`threat-model-four-questions`. The skills that carried the MochiOS loop
(`plan-work-breakdown`, `build-test-strategy`,
`build-definition-of-done`) have zero evals, so the most-used path is
the least-tested. Fix: add evals mirroring the existing
`prompt.md` + `graders/` format for at least those three, plus
`eng-policy-lead` audit mode (the stated Active Focus field test).

## [P1] Decide what SkillWren means on Muse

Muse ignores the entire gate frontmatter (`flows authority effects risk
cost budget owns-when accepts produces`) — 35 diagnostics, all
warnings. The 3 converted skills' `contract`/`logic` blocks are
advisory prose here, not enforced gates. Either port the semantics to
something this runtime honors, or state in `skillwren-pilot.md` that
Muse execution is prose-level and agents must self-enforce. Silent
degradation is the current behavior and the worst option.

## [P2] `build-code-review`: cover untracked files

The `review-change` flow reads "the change" as the diff. On the MochiOS
test it missed three new files (`?? clip.rs`, `clipboard.cpp/.h`) that
carried much of the feature. Fix: require a `git status` (or equivalent
VCS scan) for untracked/unstaged paths as part of "read target",
and refuse or caveat the review when part of the change is unread.

## [P2] Ship a repo-adapter note pattern

Two MochiOS-specific round-trips recur anywhere: package shorthand vs
real Cargo names (`wire-abi` → `mochios-wire-abi`), and repo gates
(`cargo xtask run` is the real bar; per-crate `k-check`/target-JSON
shapes when the lane is held). Add a documented slot for a
repo-adapter (gates, name maps, lanes that must never be killed) that
`eng-policy-lead` bootstrap writes. The MochiOS values are in the usage
report §4.

## [P3] Doc nits in `docs/STATUS.md`

- "installed at user scope" no longer describes every install: the
  Muse test installed with `--scope project` (trust recorded as
  `user-local`). Qualify the line per-harness.
- Active Focus still lists the `eng-policy-lead` audit-mode field test
  as next — the Muse loop is a down payment on it; link the usage
  report when recording the result.

## Out of scope (MochiOS-side, not skill-side)

- Match-arm order `0,2,1` in the new `spawn_marker_image` kind-2 arm
  (re-review nit) — fix when committing the MochiOS change.
- `Cargo.lock` rustls drift from the test runs — revert before commit.
- The committed MochiOS change from the earlier review session still
  carries three open questions (EDIT-flag fallthrough, `Offered`-state
  failure silence, dialog kind 3) — tracked by the repo owner.
