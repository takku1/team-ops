# team-ops on Muse — usage report, round 6 (2026-10-27)

Small round: verify the newly added supply-chain eval on disk, then
actually run it through `secure-supply-chain` — coverage only becomes
proof when a loop runs it.

## 1. Drift check: clean (operator-verified live)

All five round-report citations still land: pilot L37–49 (Muse
execution), eng-policy-lead L167 (item 12, cite-or-UNVERIFIED),
review L47 (untracked/unstaged scan; L90–98/149–153 unchanged since
round 2 — file untouched). STATUS eval count correct (3 original + 6 =
9 dirs on disk). Version deliberately still 2.0.0.

## 2. New eval: well-formed + worked end-to-end (PASS)

`evals/supply-chain-audit-cites-evidence` matches house format
(frontmatter, planted repo with unpinned deps / no secret scanning /
30-day-open Critical / "planned" tooling / no SBOM or signatures /
floating action tags; criteria demand SLA-breach-first ranking,
per-gap evidence, named SLSA level, owners, "planned" = unknown).

Worked application of `audit-supply-chain` against the prompt:

- 30-day-open Critical ranks first (Critical SLA is 7 days from
  disclosure — breach, cited to the disclosure + still-open state).
- Every gap carries its file/setting evidence (package.json ranges,
  missing lockfile, repo-var secrets, unconfigured scanning, unsigned
  releases, floating tags); "planned" scanning marked unknown, never
  passing; SLSA named as below the L2 baseline (no hosted provenance,
  no signing, no SBOM); remediations owner-assigned and SSDF-mapped.
- None of the fail conditions trigger (no evidence-less gap, no
  silent pass, SLSA level named).

This was a worked verification, not a full loop run — one notch below
rounds 2–3 evidence, one notch above on-disk coverage. The eval has
now earned its keep pending a live loop run.

## 3. Rating: 9.5 / 10 (unchanged, agreed)

The update adds coverage plus one worked pass, not a new closed loop.
The gate to 10 is unchanged and owner-side: approve the 12 drafts,
write `docs/policy/`, run the consuming loop. Explicitly deferred
with reasons: remaining SkillWren conversions (weeks of review-map
work, needs an owner call), 2.1.0 + changelog (bundle with the next
reinstall), MochiOS-side findings (other repo).
