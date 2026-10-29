# Status

Version 4.2.2, 2026-10-29. The suite now uses an adaptive main-session controller, selective workers, one owner per coupled change, delta handoffs, and current artifact evidence. All 16 skill names remain available in the same two plugins.

## Implemented

- Refactored all 16 skills and four optional role agents (security review is a reviewer mode as of 4.2.0). Small work stays inline; planning and role names do not dispatch agents.
- Added an on-demand coordination contract: task/attempt/artifact identity, controller-owned state, sparse event routing, ownership transfer, stable issue history, budgets, and acceptance.
- Assigned one final verification owner while preserving focused builder checks, targeted review checks, required fresh runs, and CI gates.
- Added an optional standard-library local check runner for serialized execution, explicit identities, raw logs, and opt-in deterministic reuse. It is not an agent scheduler, distributed service, sandbox, or complete dependency scanner.
- Moved supply-chain details and the ADR shape into on-demand references. Delivery policy preserves adopted local rules and existing authorization.
- Added five evidence-register entries and six coordination scenarios; 38 development scenarios cover all 16 skills.

## 4.2.0 adopted concepts

Body-level verification gates in four acting skills, closed repair outcomes, build-vs-adopt resolution, error-analysis-first evaluation, runner log redaction, and register R26-R34. `security-reviewer` merged into `reviewer`. The 38-scenario corpus has now run once per arm: 4.2.0 is accepted as non-inferior to 4.1.0 ([report](../evals/runs/scenarios-4.2/REPORT.md)). Main finding: when the target skill loaded, 23/24 runs passed; 11 of 38 cases never loaded a skill in either arm. Latest evidence ([report](../evals/runs/scenarios-4.2.2/REPORT.md)): with the suite vs no suite (same model), 4.2.2 scores +0.111 (scenario-clustered CI [+0.037, +0.185]; held-out +0.159) at ~12% more cost per run, Opus-judged. Version-to-version quality gains are judge-dependent: an independent Codex judge erased the 4.2.1-vs-4.1.0 difference; skill-loading gains (judge-free) hold. Main limiter: the target skill still fails to load on some phrasings ("is the release ready?", "rename across five agents"). Pending: Codex re-grade of the solo run (`scripts/rejudge.py`), human calibration grades (`evals/calibration/round-1`), real coding tasks with oracles for efficiency, and more real-session traces.

## 4.1.1 context and language pass

Skills restructured around a purpose line and **Return:** contract with unified terminology; runner manual split from the coordination contract; agent boilerplate deduplicated; evidence citations moved to register P07-P09. Always-on descriptions -10%, delegated review run -28%. A keyword trigger proxy did not regress (26->27/38 top-1). Static validation only; behavioral equivalence is assumed, not measured.

## 4.1 improvements

- Both packages now include synchronized evidence and host references; package links cannot escape into the source checkout. Isolated archive/cache tests execute the copied helper.
- Cache diagnostics identify changed identity categories, failure/missing evidence, and deliberate fresh runs. `--explain` inspects eligibility without executing a check.
- Host-specific fallback rules avoid unsupported named-agent dispatch and mandatory companion installation.
- Added a repeatable matched fixture harness and executed four tasks in each arm with separate artifact oracles and independent task review. Both solo and inline-controller satisfied 4/4; there is no demonstrated advantage to justify more orchestration.

## Validation and limits

See [the current validation record](current/improvements-4.1-validation.md) for observed checks, independent forward testing, context measurements, and environment limitations. Runner tests are executable correctness checks, not proof that the skills improve model behavior. The full 38-scenario corpus and a held-out real-task team-versus-solo study remain unrun. The four-task paired development run tests inline workflows and fallback, not dispatch effectiveness.

The next useful experiment is solo vs current controller on representative clean task snapshots, measuring acceptance quality, tokens/cost, elapsed and human time, duplicate builds, and rework. No savings percentage or optimal agent count is established. Source changes do not update already installed/loaded plugin sessions.

## Historical evidence

The previously recorded real-task run was MochiOS `b3f44a40`, using 3.0.1 instructions. It is not a validation of 4.0. Retired skill versions, SkillWren artifacts, and earlier field reports remain under [archive](archive/2026-10-28-consolidation-3.1/). The [research register](current/research-evidence.md) separates empirical findings, standards, practitioner guidance, and suite defaults. The [coordination research](current/multi-agent-coordination-research.md) motivated this overhaul; it describes a proposal, not measured gains.

## MochiOS follow-up

See [the installation and test record](current/mochios-4.0-validation.md): both hosts accept local packages, the runner executed 32 admission-check tests successfully and demonstrated reuse. Live Muse installation remains at 2.2.0 because its store is outside writable access; a model-driven Claude test failed at API connection before tool use. A two-plugin project installer is prepared and dry-run validated. These are explicit incomplete integration checks, not a team-versus-solo result.
