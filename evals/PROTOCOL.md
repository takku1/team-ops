# Behavioral evaluation protocol

The suite contains 38 development scenarios covering all 16 active skills across both plugins. Agent-team cases (`lead-*`, `failure-log-from-stuck-run`) grade the lead's task/contract coupling, check ownership, stale evidence, retry continuity, scopes, briefs, and acceptance decisions; record whether phases ran inline or as subagents. Coverage is not a pass result. `case.json` identifies targeted skills and the baseline execution status; every case reads `not-run` until exercised against the current skill text — earlier live runs in the round reports were against older text. Append actual runs to a separate result record instead of retroactively claiming these scenarios were executed. Historical reports retain their original scope.

## Controlled comparison

1. Freeze candidate skill contents and a baseline. Use the same task, fixture, model/configuration, tool permissions, resource limits, and initial state. Save content hashes and configuration. For routing, supply the normal skill catalog; for isolated adherence, explicitly supply the targeted skill. Report which was tested.
2. Give the agent only the prompt and permitted raw artifacts. Keep grader rubrics and expected answers out of its context. Run in an isolated workspace; do not evaluate against the live repository. For `implementation-zero-limit`, copy `fixtures/` into that workspace. The original zero test intentionally fails before a fix.
3. Counterbalance baseline/candidate order where possible. Repeat within the available budget and report the number of distinct tasks separately from stochastic repeats. Cases used to tune these skills are development cases, not an untouched holdout; add fresh representative tasks for a generalization claim.
4. Retain transcript, artifacts/diff, commands/exit status, elapsed time, active human minutes, tokens and measured cost, interventions, refusals, environment failures, and unauthorized side effects. Never exclude failed attempts from total cost. Unknown cost is unknown, not zero.
5. Check artifact state using executable oracles where available. For subjective rubrics, blind configuration identity, calibrate the judge against human judgments, and adjudicate disagreement. Style resemblance is not functional correctness.
6. Report acceptance rate and severe failures per scenario/slice, uncertainty justified by sampling, total cost per accepted task, elapsed time and human rework. Do not use repeated runs of one case as independent evidence across many tasks. Do not invent a universal numerical pass threshold.

Record spawns, peak concurrency, duplicate expensive builds, runner compute separately from model tokens, controller overhead, stale-evidence incidents, and rework by stable issue ID. Compare solo, current suite, and candidate with equal total ceilings and matched snapshots; report actual costs and quality. A read-only forward test is a limited development check, not execution of this entire scenario corpus.

## Result record

For each run, record: case ID, baseline/candidate ID and hashes, model/provider version, tool/runtime version, run ID and starting-state hash, limits, observed outcome (`pass`, `fail`, `incomplete`, `environment-error`), evidence/artifact paths, grader identity/configuration, rubric version, human adjudication, elapsed seconds, active human seconds, measured cost/currency, and limitations. Missing measurements use null with a reason.

## Running the corpus

`python scripts/run_scenarios.py --baseline <plugins-dir> --candidate <plugins-dir> --out evals/runs/<id> --work <scratch>` runs both arms through the local `claude` CLI in isolated workspaces, grades blind with a separate judge model, runs `graders/oracle.py` where a case supplies one, and writes `paired-results.json` and `contract.json` for `python -m prompt_optimization compare`. It resumes: environment and rate-limit failures leave no record and are retried. Calls are billed; `--budget-usd` stops new launches. Each case's `fixtures/` is copied into its workspace; `graders/` never is. First run: [scenarios-4.2](runs/scenarios-4.2/REPORT.md).

## Supporting tools

- `scripts/rejudge.py --run <dir>` re-grades a run with an independent judge from another model family (Codex CLI) and reports agreement (exact, Cohen's kappa). Billed.
- `scripts/trigger_proxy.py plugins evals` is a free keyword proxy for description edits; real routing comes from runs.
- `scripts/session_timeline.py <session.jsonl>` compacts a real Claude Code or Codex session (user turns, suite loads, tool errors) for error analysis. Analyze use outside this repository separately from development runs.
- `run_scenarios.py --solo` adds a no-suite arm with the same model and limits, writing `paired-results-solo.json` to compare orchestration value, not only compliance. Report correctness with efficiency (seconds, turns, tool calls, cost), and cluster uncertainty by scenario, not run.

## Checks available here

`python scripts/validate-suite.py` validates metadata, description length, local and cross-plugin references, evidence IDs, and scenario coverage. It does **not** run agents or score their answers.

Research basis: R18/R19 in [the register](../docs/current/research-evidence.md). Exact comparison and release criteria remain local design choices.

## Executed development fixtures

The [matched field procedure](FIELD-EVALUATION.md) is separate from this 38-scenario corpus. Four paired development tasks were executed for 4.1 with independent artifact and task review; the scenario manifests above remain not-run. The small paired run does not establish a held-out performance result.
