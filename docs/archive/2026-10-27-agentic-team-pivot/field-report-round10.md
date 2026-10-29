# Field report, round 10 (2026-10-27): MochiOS CI restore and browser triage

Historical record of team-ops **2.2.2** in use on MochiOS. It describes one exercise and is not a suite rating.

## Work done

- **docs CI:** fixed 15 broken links (repointed to `retired/`, checked case-sensitively). Schema-check was failing because the generated `system` bucket page collided with the contract `SYSTEM.md` on a case-insensitive filesystem. The generator now names it `system-schemas.md`, with a test. That fix exposed registry-lint, which had 18 errors and now has 0: registry rows 269–277 were added, and two loop-based schema registrations were written out so the lint can read them.
- **deny CI:** not fixed. RUSTSEC-2026-0387 is in `crypto-bigint 0.5.5`, reached through `elliptic-curve 0.13` and `embedded-tls 0.19`, and is reachable from ECDHE key generation. The repository's waiver rule allows ignores only for unreachable paths. Migration versus a time-boxed exception was left to the owner.
- **Sokai "needs FS_NAMESPACE" toast:** another agent's handoff blamed a stale embedded Sokai image and proposed comparing `SOKAI_IMAGE_ID` values. That discriminator was false: image IDs are slot numbers that repeat across builds. A host test of the full launch chain passed, a content-hash serial line (`##IMAGE_HASH`) was added, and a live gate on a fresh image showed no toast. The remaining failure was a separate held-drag selection leg.

## Skill lessons, shipped in 2.2.2

- `secure-supply-chain`: an exception must meet the repository's own waiver rule. When the path is reachable, present the migration, the exposure, and a time-boxed exception for the owner.
- `ai-context-management`: a handed-over diagnosis is a hypothesis. Verify its discriminator before acting on it.
- `build-trunk-integration`: when restoring a red job, run every step locally, because an early failure hides later ones.

## Overhead finding

About 15 of the 25 skills encoded human-team process (RACI, cadence, capacity, DORA) and were not used in this round. That finding motivated the 3.0 pivot to a role-based agent workflow (see `docs/STATUS.md`).
