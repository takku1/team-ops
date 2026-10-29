> As of 3.0.0, only `build-code-review` and `secure-supply-chain` remain SkillWren builds; `eng-policy-lead` was retired and its sources archived in `docs/archive/2026-10-27-agentic-team-pivot/skillwren-src/`.
> Historical pilot record. Current workflow (see `docs/STATUS.md`): edit `skills/<id>/SKILL.md`, copy it to `skillwren-src/<id>/SKILL.md`, run `skillwren check` and `python skillwren-src/mkreview.py skillwren-src/<id>` (update `review-spec.json` anchors if you moved anchored text), then `python scripts/refresh-skillwren-builds.py --tool-root Z:/SkillWren`. The rebuild instructions below are superseded. Claims below of hard gates or provably read-only behavior refer at most to authored static structure: ordinary skill execution is not a sandbox, including in Claude Code. Conform observes some final-state effects; it does not prove runtime compliance or semantic equivalence. Current manifests are refreshed from active skills.

# SkillWren Conversion Pilot (2026-10-27)

Toolchain: `Z:\SkillWren` v0.5.0 (`PYTHONPATH=Z:/SkillWren/src python -m skillwren ...`).

## Layout
```
skillwren-src/<id>/
  original.md        prose v2 skill (provenance, not loaded)
  SKILL.md           SkillWren source (edit this)
  review-spec.json   requirement map input: [id, [first,last original line], [anchors]]
  review.json        hash-bound map, regenerated from review-spec.json
skills/<id>/
  SKILL.md           built, validated output (do not hand-edit)
  manifest.json      build manifest with source hashes
```
Rebuild: `skillwren check` → regenerate review.json (`python skillwren-src/mkreview.py skillwren-src/<id>`, which validates anchors plus full original-line coverage via `skillwren.review.validate_review`) → `skillwren build <src> --out <new dir>` → replace `skills/<id>/`.

## Results
| Skill | Flows | Prose → SkillWren (cl100k) | check | Review map | Optimized build |
|---|---|---|---|---|---|
| eng-policy-lead | bootstrap-policy, audit-policy, run-workflow | 1526 → 2080 (trimmed) | clean | 18 reqs, all lines covered | rejected (not smaller) |
| build-code-review | set-review-policy, review-change | 720 → 1371 (trimmed) | clean | 14 reqs, all lines covered | rejected (not smaller) |
| secure-supply-chain | audit-supply-chain, review-dependency | 696 → 1335 (trimmed) | clean | 18 reqs, all lines covered | rejected (not smaller) |

**Conform (headless, sonnet-5-5, $0.11):** `eng-policy-lead`, prompt "Bootstrap our engineering policy set for this repo." on a 3-file Node sample repo, gave **conforms, 0 files changed**. That is the expected dismissal behavior: headless, the approval `ask` cannot reach a user, so nothing is written. Caveat: a run that never loaded the skill would also change nothing. The transcript was not inspected.

## What the conversion added (beyond the prose)
- **Hard gates:** bootstrap cannot write before confirmation (M1). Existing policy is `immutable`, so the no-overwrite rule is enforced statically. A workflow stops at a blocking finding. Audits cannot report a gap without evidence.
- **Declared effects:** two of the three skills are provably read-only. The orchestrator's writes are confined to `docs/*`, which conform can check.
- **Header routing:** `owns-when` and `requires` allow headers-only selection.

## Behavior changes vs prose (reviewed, intentional)
- Bootstrap outputs moved under `docs/` (CODEOWNERS, SECURITY.md, PR template). Branch protection is reported as settings, not written.
- `secure-supply-chain` gained an explicit `review-dependency` intake flow (the prose had the intake policy but no procedure) and a "never treat an unavailable check as passing" invariant.
- `audit-policy` marks "followed?" as unknown when there is no history, rather than skipping the column.

## Muse execution (2026-10-27 field test)

Muse ignores the entire SkillWren gate frontmatter (`flows authority
effects risk cost budget owns-when accepts produces`) — 35 diagnostics on
v2.0.0, all warnings — and the `contract`/`logic` blocks execute as
advisory prose, not enforced gates. Decision: **port nothing; declare
prose-level execution.** On Muse, the agent must self-enforce each flow's
`require`/`verify`/`never` steps as checklist discipline, because the
runtime will not stop it from skipping them. Silent degradation (assuming
gates hold) is rejected. Field evidence: the MochiOS loop succeeded on
prose strength alone, and the one real gap (untracked files invisible to
`review-change`) was a flow-completeness bug, not a gate-enforcement bug.
See `docs/archive/2026-10-27-muse-field-rounds-1-8/muse-usage-report.md`.

## Recommendation
Convert a skill only when it **acts** (writes files, gates a decision, or audits with evidence). Candidates: `build-definition-of-done` (audit vs CI), `run-incident-postmortem` (action-item validation gate), `ship-release-rollout` (rollout-plan gates). Leave reference-style skills (ADR, estimation, topology, metrics) as prose, since conversion only adds size there.
