# Validation status — v2.2.0 (2026-10-27)

Observed checks for this release. Static checks only; no behavioral evaluation was executed here.

## Ran and passing

- `python scripts/validate-suite.py` → 25 skills, 3 manifests, 26 eval cases covering all 25 skills, **0 errors**. Checks: skill name/directory match, description present (≤1024 chars), evidence IDs resolve against `docs/current/research-evidence.md` with a register link in every skill, no control characters, balanced fences, local links resolve, manifests hash-match embedded sources, every eval has a valid turn budget / tool scope / LLM grader, plugin and marketplace versions agree.
- `skillwren check` on all three converted sources (`skillwren-src/*/SKILL.md`) → clean, no errors or warnings. Review maps regenerated from `review-spec.json` with full anchor + original-line coverage.
- `skillwren build` for all three → installed byte-identical into `skills/` (verified `src==built` for each), manifests refreshed.
- `muse plugins validate . --json` → valid plugin; SkillWren gate frontmatter and manifest `author`/`keywords` report as warnings (35 on first import), which the runtime ignores. See `scripts/install-muse.ps1`, which judges install success by observed plugin state instead of the misleading exit code.

## Not run here

- The 26 behavioral scenarios (`evals/*/prompt.md` + `graders/`): all `case.json` baselines read `not-run` against the current skill text. Earlier live exercises in `docs/archive/2026-10-27-muse-field-rounds-1-8/` ran against older skill versions.
- No controlled baseline/candidate comparison, no cost/latency measurement, no judge calibration. See `evals/PROTOCOL.md` for the procedure to run them.

## Known limits

- Static validation cannot prove runtime compliance; a documented policy is not an enforced control.
- Research register entries bound claims to study populations and dates; association is not causation (see `docs/current/research-evidence.md`).
- The three hung Codex-session packaging processes observed during reconciliation (two `refresh-skillwren-builds.py` runs, one `skillwren build` to temp) were left untouched as foreign processes; the empty `.team-ops-build-*` staging directory they left was removed.
