# team-ops on Muse — usage report, round 4 (2026-10-27)

This round tested the two remaining unproven halves: the install
wrapper's failure branch, and `eng-policy-lead` bootstrap-policy
(drafts + owner/source verify + stop-before-write) with an independent
ground-truth judge. No files were created anywhere — the flow stops at
the skill's ask-user-to-approve gate by design.

## 1. Install wrapper: both branches proven (operator-verified)

- Success path: `OK: 'team-ops' enabled=True active=True warnings=35 errors=0`, exit 0.
- Missing-plugin path (`-Id bogus-plugin-id`): `Plugin 'bogus-plugin-id' not found after install.`, exit 1.
- The exit-1-on-success automation trap is closed on both sides.

## 2. Bootstrap: runnable from SKILL.md alone, judged honest

All 12 drafts name an owner and source skill (verify step PASS, no
retry needed), covering ownership, cadence, DoD, code review,
branching/CI, testing, release, SLOs, incidents, security, ADRs, and
the repo-adapter (item 12). Stop-before-write honored — live-confirmed
`docs/policy/`, `docs/CODEOWNERS`, `docs/SECURITY.md`, and the PR
template are all still absent.

Drafts 1–11 are low-risk planning scaffolds: conditionally approved.
Draft 12 (the adapter) is **ON HOLD as implement-loop ground truth** —
and this is the skill working, not failing: the drafter admitted its
gaps, and ground truth confirmed both the matches and one live
contradiction:

- MATCHES (corroborated live): k-check host shape (`config.toml:54`),
  u-check/u-build pid1 shapes (`:66–67`), package names
  (`mochios-wire-abi`, `-shell`, `-shell-parse`, `-gate`), lane-lock
  holder message and lock path, `docs/policy/` absent, no
  `repo-adapter.md` anywhere.
- GAPS (draft states as fact): per-bin slot/image-base table beyond
  pid1 unverified — and wrong in one spot (live `config.toml:74`
  gives compositor slot 160 = `0x5000`, absent from the draft table);
  shell-parse omitted from the name map; CI details, unsafe cap 795,
  `RUST_MIN_STACK`, toolchain pin, `docs_drift_baseline` hard-gate, and
  generated-file list all unverified; `lane_lock.rs` read only to line 60.

## 3. Rating: 9 / 10 (unchanged)

Round 4 closed the install branches and proved bootstrap drafts +
stop-before-write + judgeable output. It did not advance the score
because the two structural items are unchanged by design: the
written-adapter-file half still has no artifact (nothing approved for
writing yet), and SkillWren gates remain advisory on Muse. The path to
10 is now concrete: fix draft 12's named gaps, write the approved set
to `docs/policy/` (needs owner approval per the skill contract), and
run one implement loop consuming the written adapter. The audit's gap #1
(CODEOWNERS + required approvers) converges with bootstrap drafts 1/4 —
a natural first consumer.
