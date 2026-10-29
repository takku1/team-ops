# team-ops field test, round 9 (2026-10-27): v2.2.0 on a real MochiOS fix

Harness: Claude Code (Opus 5.5), not Muse. One real task, so this is a
field observation, not a controlled run under `evals/PROTOCOL.md`.

## Task

MochiOS `docs/STATUS.md` listed "the `hid_table_stage…` terminal test
fails on a clean checkout" as open. Skills used: `build-implementation-loop`
for the fix, then `build-code-review` on the result, with each flow followed
literally.

## What happened

| Step | Observed |
|---|---|
| Reproduce | `cargo test -p mochios-userspace-terminal --lib`: 263 pass, 1 fail (`left: Some(73) right: None`) |
| Cause | The test pinned the R-263 gap (no PageUp/PageDown HID rows) and said not to edit it until the cause was named. ROADMAP R-305 (DONE 2026-10-15) named the cause and added the rows, so the pin was stale, not a regression |
| Change | Renamed the test and turned the `None` pins into `Some` pins on both sides, plus the terminal `keys::decode` end. The edit is stricter than before, not weaker |
| Verify | Terminal 264/264, keymap suites green; `cargo fmt --check` clean on the changed lines (the rest of the crate has older drift, not touched) |
| Docs | MochiOS STATUS line updated |
| Review | Approve with nits; `question:` ROADMAP R-263 (`docs/ROADMAP.md:725`) still says "Live proof needs the lane" after R-305. Flagged for the owner, not edited |

MochiOS changes are left uncommitted for the owner.

## Skill findings

1. **`build-code-review`, P1 defect.** `verify every finding cites the changed
   lines ... otherwise: discard findings; abort`. The most useful finding (a
   stale ROADMAP row the change leaves inconsistent) sits on an unchanged
   line, so literal execution would have discarded *all* findings, the
   grounded ones included. Fixed in 2.2.1: a `grounding filter` drops only
   uncited findings, and an out-of-diff finding is grounded when it names
   both the implicating changed line and the unchanged location.
2. **`build-implementation-loop`, gap.** "Do not weaken assertions" doesn't
   cover a fix that changes a test's expectation. The skill's "falsifiable
   cause first" rule did lead to R-305, but nothing required citing the
   evidence or honoring the test's own edit condition. Added.
3. **`build-implementation-loop`, gap.** No rule held fmt/lint to the
   changed lines; the whole-crate check showed unrelated drift that a
   literal agent could reformat. Added (it matches the "attributed by hunk"
   practice already used on MochiOS).
4. **`build-implementation-loop`, gap.** Completion didn't mention the
   repo's own tracker entry for the fixed item, or stale adjacent entries.
   Added: update your own entry, flag the rest.
5. **Pack docs contradiction.** STATUS and the README said to edit
   `skillwren-src/` and rebuild, while `refresh-skillwren-builds.py` and the
   pilot banner say `skills/` is authoritative. Reconciled to the code.

Worked as intended: the reproduce-then-cause discipline, separating
pre-existing failures from regressions, the untracked-path scan (2.1.0
fix), severity labels, and the approve-when-healthier standard.

## Regression cases added

`code-review-keeps-out-of-diff-findings`, `implementation-stale-test-pin`.
Both `not-run`.

## Rating

No behavioral rating claimed under the protocol. Field impression: the two
build skills carried a real fix cleanly. One flow defect would have hurt
output quality if followed literally, and it is now fixed.
