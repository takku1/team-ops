# Matched field evaluation

This is a small executable development evaluation, separate from the 38 scenario prompts. It compares a direct solo actor with a controller using the same raw task fixtures. The current four tasks cover a small fix, a coupled contract change, stale evidence, and continuing independent work while another task is blocked.

## Prepare and execute

```powershell
python scripts/evaluate_field.py prepare --output evals/runs/<fresh-run-id>
```

Preparation creates identical source states in `solo/` and `controller/`, per-task `TASK.md` requests, a frozen package snapshot for the candidate, and a manifest with starting-state and package hashes. Do not expose evaluator code, graders, other arms, or previous results to actors.

Use independent fresh sessions with the same selected model, tools, permissions, total limits, and task order. The solo actor works directly without suite instructions. The controller actor reads only relevant skills from `packages/`. Give both the same task and source scopes. Workers should either be available under the same budget with deliberate baseline design, or disabled in both arms; record which. A no-worker run evaluates the inline controller and fallback, not multi-agent scheduling.

Allow each actor to write only its assigned source paths, `REPORT.json`, and scratch `.log` files under its case. Preserve `check.py` and raw tasks. Reports record observed commands/exit codes, changes, task states, ownership, actual skill loads where applicable, workers, unknowns, next action, and measured timing boundaries. Retain host traces if available. Self-reports and log files alone do not authenticate complete chronology. Unexposed tokens/cost are null, never zero.

## Grade independently

```powershell
python scripts/evaluate_field.py grade --output evals/runs/<run-id>
```

The trusted evaluator inventories protected inputs and added files, runs the original visible checks and independent artifact oracles, records its own hash, and returns nonzero when any artifact fails. It tests multiple values and rejects legacy-only and mixed wire payloads. Scope violations skip execution. Python interpreter isolation is not a sandbox: run actors and grading only within an appropriately constrained workspace. This harness is for trusted development fixtures, not arbitrary hostile submissions.

Artifact correctness is not the whole behavioral verdict. A separate reviewer checks the raw request, resulting code, reports, logs, and oracle output for acceptance freshness, ownership, blocked-state handling, and limits. Judge by task requirements, not reporting style or assumed configuration superiority. Do not let the actor grade its own run.

## Compare and decide

Counterbalance or randomize order in future runs and use held-out real task snapshots for generalization. Preserve failures, aborted runs, grader corrections, configuration hashes, actual costs, and unknowns. Distinguish actor-reported execution windows from controlled end-to-end time. Compare accepted outcomes, severe failures, escaped defects, token/cost measurements, human rework, duplicate checks, and controller overhead.

The recorded [4.1 run](runs/paired-4.1/run-configuration.json) used two cold actors on one shared machine with no worker tools. Both passed four tasks under independent review. It establishes no cost, latency, or quality advantage. Retain small-work inline defaults; additional orchestration still needs evidence. The run is development data, not a held-out benchmark.
