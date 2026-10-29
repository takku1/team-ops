# team-ops on Muse — usage report, round 2 (2026-10-27)

Second field-test loop with the updated pack (5 new evals, untracked-aware
`review-change`, prose-level SkillWren declaration, repo-adapter slot,
STATUS updates). This round: verified all four fixes, implemented a new
MochiOS slice with the updated skills, and reviewed it with the updated
skill — including the new eval regression. Verdict: **the fixes work in
practice; the loop completed for real this time.**

## 1. Fix verification (all four PASS)

- 5 new eval dirs exist with `prompt.md`: `work-breakdown-slices-vertically`,
  `test-strategy-pyramid-and-flaky`, `definition-of-done-enforced-vs-claimed`,
  `policy-lead-audit-top-three`, `code-review-covers-untracked`.
- `build-code-review` L47 / L90–98 / L149–153: contract reads
  untracked/unstaged, review-change aborts on unread paths, appendix
  refuses partial reviews. The L149–153 branch was exercised for real
  in §4 below (scope caveat on a dirty tree).
- `skillwren-pilot.md` L37–49 declares prose-level execution on Muse.
- Repo-adapter pattern specified (`eng-policy-lead` L167, fix-list L43–51,
  STATUS L13). No written adapter file exists; adapter values were passed
  inline this round with **no harm** (S1 gates map to plain per-crate
  host checks). The write-the-file half of the pattern is still untested.

## 2. Implemented: S1 `>>` append-redirect (TERM-002 slice)

Picked per priority order (b) SGR grid and (c) CAS reclaim verified
still-open and deferred. S1 is independent of the S0 eventlog-sink
spike and S2 `<`, so it stands alone; S2–S4 remain open.

- Parse (`mochios-userspace-shell-parse`): `>>` lexes to a new
  `Token::RedirectAppend`; grammar maps it to `Redirect { path, append }`;
  `Pipeline.redirect` is now `Option<Redirect>`. `>>>` still refuses
  (falls out as needs-a-path — see nit in §4).
- Dispatch (`mochios-userspace-shell`): `append` threads plan → run.
  `>>` plans `FS_APPEND` only (create rebinds to zero bytes, so it is
  skipped); `install` keeps truncate semantics (`false`). `>` paths are
  byte-identical in behavior.
- Semantics (no gate change): `>>` never creates — appending to a
  missing file refuses at the gate (FakePort agrees: `PATH_NOT_FOUND`).
  Documented on the `Redirect` struct and module docs; POSIX deviation
  is explicit, not accidental.
- Files touched (10, all tracked, all in the two picked crates):
  shell-parse `lexer.rs grammar.rs lib.rs tests.rs`; shell
  `commands/files/redirect.rs commands/mod.rs commands/net/install.rs
  dispatch.rs planning.rs dispatch_tests.rs`.

## 3. Verification (independent re-runs by operator)

- `cargo test -p mochios-userspace-shell-parse`: **33 passed, 0 failed**
  (incl. new `append_redirect_parses_with_mode` + malformed `>>` cases;
  old `>>`-refusal pin removed).
- `cargo test -p mochios-userspace-shell`: **250 passed, 0 failed**
  (incl. new append-preserves-content, missing-file-refuses, no-plan_begin
  for the append line).
- `cargo clippy --all-targets` on both crates: **zero warnings in changed
  files** (3 of my own fixed: 2 missing-`;`, 1 `get().is_none()`; the
  `fg.rs`/`ping.rs` warnings are pre-existing).
- Pre-fix behavior: old lexer refused `>>` (was pinned by the removed
  test); new tests fail without the fix at parse. New tests were not
  executed against old code — stated, not implied.
- One self-inflicted test bug (plan_begin asserted over setup-line
  calls too) was caught by the suite itself; root-caused via failure
  output and fixed minimally. No product change needed.

## 4. Reviews with the updated skill

**(A) Eval regression** (`code-review-covers-untracked` prompt): the new
untracked-scan step surfaces `admin_export.py` outside the diff.
Findings: `blocking:` SQL injection (f-string-interpolated
`request.args['org']`), `blocking:` no auth on a bulk `/admin/export`,
`question:` "tests later" with only a stub, `fyi:` the in-diff
`format` param is benign. Verdict: **request changes**. The exact gap
round 1 missed is now caught — eval-fix verified in practice, not just
present on disk.

**(B) Scoped real-diff review** (S1 files only): verdict **approve**
— the change definitely improves health. `fyi:` design fits layering,
no gate change; offsets mirror existing `fs_append` chunking;
`install` correctly stays truncate; refusal paths fail-stop.
`nit:` `>>>` reports "`>>` needs a path", which misdescribes the real
problem (stray operator). `question:` live-gate denial text for the
missing-file case is unverified against a real gate (FakePort says
`PATH_NOT_FOUND`; message quality on hardware unknown) — safe refusal
either way, polish only. Scope caveat per L149–153: the worktree holds
the user's other in-flight work (18 modified + 2 untracked, incl.
round-1's wire-abi/Cargo.lock) which was **not** reviewed; this report
covers the 10 S1 files only.

## 5. Leftovers and notes

- Changes left uncommitted (not asked to commit). Round-1's
  wire-abi fix + `Cargo.lock` rustls drift still ride along untouched.
- Full `cargo xtask run` was not used (lane discipline + S1 is
  grammar/unit-verifiable); honesty preserved, no live proof claimed.
- Methodology note (my harness, not the skills): the round-2 workflow
  stalled because its brief baked a stale "clean tree" precondition —
  strict schema gating turned new worktree dirt into incompleteness.
  Slice/select/updates agents still delivered; implement/review ran
  inline here instead.

## 6. Rating: 8 / 10

Round 1 gave 7 ("fix those and it's a 9"). The top fixes verified live:
evals exist where the loop needs them, the untracked scan caught a real
planted bug and shaped a real review caveat, prose-level execution is
declared. Remaining point: install still exits 1 on success
(documented, not fixed), SkillWren gates remain inert by declaration,
`eng-policy-lead` audit mode and the written-adapter-file half are still
unexercised. One more loop covering those earns the 9.
