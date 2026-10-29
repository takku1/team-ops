# team-ops: Engineering, Design, and AI Workflows

Version 2.2.2: 25 skills for building software with AI and building AI-powered products. Covers product design, implementation, engineering policy, and AI context, cost, and evaluation. Research findings, standards, and adaptable defaults are explicitly separated; see the [evidence register](docs/current/research-evidence.md). This suite is research-informed, not academically validated as a whole.

## Skills (invoked as `team-ops:<name>`)
| Stage | Skills |
|---|---|
| Lead | `eng-policy-lead`: bootstrap a policy set, audit policy (written / enforced / followed), or run a named workflow (new service, launch readiness, late project, health check, post-incident) |
| Org | `org-team-topology`, `org-ownership-raci`, `org-capacity-plan` |
| Plan | `plan-design-review`, `plan-decision-record`, `plan-work-breakdown`, `plan-estimate-forecast`, `plan-late-recovery`, `plan-delivery-cadence` |
| Build | `build-definition-of-done`, `build-code-review`, `build-trunk-integration`, `build-test-strategy` |
| Design / implementation | `design-product-workflow`, `build-implementation-loop` |
| AI | `ai-context-management`, `ai-workflow-efficiency`, `ai-evaluation` |
| Ship / Run | `ship-release-rollout`, `run-slo-error-budget`, `run-incident-postmortem` |
| Secure | `secure-threat-model`, `secure-supply-chain` |
| Measure | `measure-delivery-health` |

Single-topic requests ("review this PR", "write an ADR") route straight to the matching skill. `eng-policy-lead` handles multi-skill jobs.

Use the shortest applicable workflow. Routine fixes go straight to implementation; uncertain user journeys use design; consequential architecture gets proportionate review. The policy lead produces policy artifacts and explicit handoffs, not application edits. Existing authorization persists; additional process must earn its cost.

AI optimization targets verified outcomes across total cost, elapsed time, and human rework. Extra context, reasoning, retries, or workers are hypotheses to evaluate, not automatic improvements. These skills do not themselves authorize spawning workers.

## Install (local marketplace)
```sh
claude plugin marketplace add Z:\team-ops-skills
claude plugin install team-ops@team-ops-local
```
After editing skills: `claude plugin marketplace update team-ops-local`, then `claude plugin update team-ops@team-ops-local`, then restart Claude Code.

## Install (Muse)

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install-muse.ps1
```

Prefer the wrapper: `muse plugins install` **exits 1 even on success**,
so the wrapper judges by observed plugin state instead and exits 0 only
when the plugin is enabled, active, and free of error-severity
diagnostics. Raw commands, when you need them:

```sh
muse plugins validate Z:\team-ops-skills
muse plugins install --scope project
```

Muse ignores the SkillWren gate frontmatter (`skill version accepts produces
owns-when flows authority effects risk cost budget`) and the manifest
`author`/`keywords`, so validation reports warnings (35 on v2.0.0, all
warnings) — warnings surface as `NativeCommandError` though the plugin lands
enabled and active, which is why the wrapper above checks state rather than
the exit code. No repo changes are required: the plugin lives in
the user cache, not the tree. See `docs/archive/2026-10-27-muse-field-rounds-1-8/muse-usage-report.md`.

## Layout
- `skills/`: installed skills. `eng-policy-lead`, `build-code-review`, and `secure-supply-chain` are SkillWren 0.5 builds (gated flows plus declared effects). The rest are prose.
- `skillwren-src/`: mirrored SkillWren sources, prose originals, and review maps. Edit the active `skills/` file, mirror it here, and re-check (see `docs/STATUS.md`). Static validation does not enforce runtime behavior.
- `docs/`: `STATUS.md`, research basis, pilot notes, archive.
- `evals/`: 30 scenarios covering all 25 skills; see [evaluation protocol](evals/PROTOCOL.md). Scenario coverage is not an executed pass rate.

## Validate changes

```powershell
python scripts/refresh-skillwren-builds.py --tool-root Z:/SkillWren
python scripts/validate-suite.py
muse plugins validate . --json
```

After editing a converted skill's source, rebuild it first (see `docs/current/skillwren-pilot.md`); the first command then refreshes the three manifests from the built output and requires the local SkillWren toolchain. The package validator requires PyYAML. Neither command executes behavioral evaluations. See [validation status](docs/current/validation-v2.2.md) for observed checks and remaining limits.
