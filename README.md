# team-ops

Version 4.2.2. A coding workflow for AI agents: the main session leads, one builder owns each coupled change, optional workers investigate or review when that pays, and acceptance rests on current execution evidence. Small work stays inline.

## Start here

Hosts without plugin support: read only the one SKILL.md for the request.

| Request | Skill |
|---|---|
| Fix a bug or failing test, add a feature | [build-implementation-loop](plugins/team-ops/skills/build-implementation-loop/SKILL.md) |
| Multi-step work, workers, accepting a report | [team-lead](plugins/team-ops/skills/team-lead/SKILL.md) |
| Split a deliverable | [plan-work-breakdown](plugins/team-ops/skills/plan-work-breakdown/SKILL.md) |
| Code review | [build-code-review](plugins/team-ops/skills/build-code-review/SKILL.md) |
| Security, dependencies, supply chain | [secure-review](plugins/team-ops/skills/secure-review/SKILL.md) |
| Accept work, final checks, red CI, DoD audit | [build-definition-of-done](plugins/team-ops/skills/build-definition-of-done/SKILL.md) |
| Handoffs, someone else's diagnosis, context | [ai-context-management](plugins/team-ops/skills/ai-context-management/SKILL.md) |
| Evaluate an AI feature, prompt, or agent | [ai-evaluation](plugins/team-ops/skills/ai-evaluation/SKILL.md) |
| Consequential design or ADR | [plan-design-review](plugins/team-ops/skills/plan-design-review/SKILL.md) |
| User flow or UI | [design-product-workflow](plugins/team-ops/skills/design-product-workflow/SKILL.md) |
| Tests/CI policy, releases, SLOs, incidents, forecasts | [team-ops-delivery](plugins/team-ops-delivery/skills/) |

Plugins: `team-ops` (10 skills, 4 optional agents: implementer, investigator, reviewer with a security mode, verifier; [check runner](plugins/team-ops/skills/team-lead/references/check-runner.md)) and optional `team-ops-delivery` (6 skills). Descriptions load at discovery; bodies and references load on use.

## Install or update

```sh
claude plugin marketplace add Z:\team-ops-skills
claude plugin install team-ops@team-ops-local
claude plugin install team-ops-delivery@team-ops-local
# update: claude plugin marketplace update team-ops-local, then claude plugin update <plugin>@team-ops-local
```

Restart the session after updating; edits here do not reach a loaded session. Muse: `scripts/install-muse-suite.ps1 -Workspace <repo>` (`-CoreOnly` for the core); see the [MochiOS record](docs/current/mochios-4.0-validation.md) for host limits.

## Validate and evaluate

```sh
python scripts/validate-suite.py                    # metadata, links, evidence IDs, scenario coverage
python scripts/package_resources.py --check         # packaged references in sync
python -m unittest discover -s scripts -p "test_*.py"
python scripts/run_scenarios.py --help              # billed: paired behavioral corpus via the claude CLI
```

The behavioral corpus (38 development + 7 held-out scenarios) runs both versions blind-graded and gates with prompt-optimization's paired non-inferiority `compare`; see the [protocol](evals/PROTOCOL.md) and [latest report](evals/runs/scenarios-4.2.1-rep/REPORT.md). State and next steps: [STATUS](docs/STATUS.md). Evidence: [research register](docs/current/research-evidence.md). History: `docs/archive/`.
