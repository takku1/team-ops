# team-ops on Muse — usage report (2026-10-27)

First field test of the pack outside Claude Code: installed `team-ops`
v2.0.0 on Muse (Muse Code) and drove it through a full loop on a real repo
([MochiOS](https://github.com/takku1/mochiOS), commit `61f0823`): install,
single-skill review, then inventory → slice → implement → re-review of an
open docs item. Verdict: **the prose policies transfer cleanly; the
SkillWren machinery does not; eval coverage is the thinnest part.**

## 1. Install and load

- `muse plugins validate Z:\team-ops-skills` → valid, `team-ops`,
  claude-compatible, 20 skills/commands-hooks-mcp/reminders counted as
  `skills=20`, with **35 diagnostics, all warnings**: Muse ignores the
  SkillWren frontmatter (`skill version accepts produces owns-when flows
  authority effects risk cost budget`) and the manifest `author`/`keywords`.
- `muse plugins install --scope project` → installed, `enabled=true
  active=true`, all 19 skills live as `plugin:team-ops:*` with descriptions
  intact. Wart: the command **exits 1 on success** — warnings surface as
  `NativeCommandError` and fail the run even though the install landed.
- No repo changes required: the plugin lives in the user cache, not the tree.

## 2. Skills exercised (4 of 19)

- `build-code-review` (review-change flow) on a real 33-file MochiOS diff
  (Sokai page clipboard over WEP minor 5): produced severity-labeled
  findings citing changed lines and a `request changes` verdict with three
  genuine questions (unvalidated `WEP_EDIT` flag fallthrough to Cut,
  unreported failure for downloads dying in `Offered` state, unanswered
  before-unload dialog kind 3). This is the skill working as designed.
  One gap found (carried to the fix list): the flow reviewed `git diff`
  only and never asked about **untracked files** — three new files
  (`clip.rs`, `clipboard.cpp/.h`) were invisible to it.
- `plan-work-breakdown` on ROADMAP TERM-002: produced a real WBS (WI-1
  failing repro test, WI-2 decode fix, WI-3 regression sweep) with
  acceptance criteria and explicit non-goals. Usable as-is.
- `build-test-strategy` + `build-definition-of-done`: governed the build
  (pyramid-appropriate unit test, DoD bar). Their influence is visible in
  the output (repro-first test, clippy-clean bar) rather than quoted.
- The other 15 skills were loaded but not invoked. `eng-policy-lead` was
  not exercised.

## 3. Implement-loop result (the real test)

Item: TERM-002 SPAWN_REQ marker decode for plan-wrapped spawns
(`docs/ROADMAP.md:425-426`) — `spawn_marker_image` in
`crates/abi/wire-abi/src/lib.rs` had no kind=2 (deadline) arm, so
deadline spawns fell through to `u32::MAX` (cosmetic `image=MAX`).

- Fix: one file, +40/−2 — new `Some(2)` arm reading `inner[17..21)`,
  matching gate `off=17` and the kind-2 payload layout. No ABI change
  (`syscall.rs:821` untouched).
- Tests: new `spawn_marker_image_decodes_deadline_spawns_direct_and_plan_wrapped`
  failed pre-fix (`left: 4294967295, right: 7`), passes post-fix.
  Full per-crate suites green: wire-abi 715 passed, shell 248 passed,
  gate ok, clippy clean on changed lines. Re-verified by operator:
  targeted test re-run → 2 passed, 0 failed; worktree holds the fix.
- Re-review verdict: **approve with nits** (one nit: match arms ordered
  0,2,1 — MochiOS-side, not skill-side).
- Left uncommitted in the MochiOS worktree by design (no commit asked).
  Note: `Cargo.lock` drifted incidentally (`rustls` 0.23.45→46,
  `rustls-webpki` 0.103.15→16) from cargo runs — revert with
  `git checkout -- Cargo.lock` before committing so the commit stays
  single-file.

## 4. Friction observed (Muse-specific)

- Package-name mapping: the slice said `cargo test -p wire-abi -p shell`;
  real names are `mochios-wire-abi` / `mochios-userspace-shell`. The
  implementer resolved it; a repo adapter note would save the round-trip.
- Build lane: `cargo xtask build` refused while the user's own `xtask
  interactive` held the lane (correct behavior — the agent must not kill
  it). Per-crate check shapes from `.cargo/config.toml` aliases covered
  verification instead. C++ engine files were never compiled (needs the
  full WebKit build) — the loop is currently Rust-only in practice.
- Inventory was partial by design: 12 open items catalogued (10 light,
  2 heavy); wiki sampling and R-20x deferred rows explicitly unresolved.

## 5. Outcome

Four skills carried a real docs-to-landed-fix loop with tests and a
passing re-review. Nothing in the prose policies misfired on a bare-metal
`no_std` repo. The gaps are coverage and platform fit, not content
quality — see `muse-fix-list.md`.
