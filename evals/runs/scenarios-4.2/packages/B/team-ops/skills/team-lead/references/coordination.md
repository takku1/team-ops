# Coordination contract

Load for delegated or multi-session work, or when duplicate expensive checks warrant the runner. Small inline work needs no board, schema, or helper. The main session remains the controller; no supervising LLM is added.

## Task and event state

Use the repo's existing tracker, or a scratch record outside source inputs. The controller is its sole writer. Record only what the next decision requires:

```text
run: goal, acceptance, authority, budget/actuals, integration_owner
task: id, attempt, owner, scope, depends_on, input_artifact,
      state, oracle, evidence_refs, issue_ids, next_action
issue: id, finding, repair_attempts, hypotheses_tried, new_evidence
```

States: `ready -> running -> awaiting_review -> awaiting_verification -> accepted`; omit inapplicable review. `blocked` and `cancelled` are explicit outcomes. A rejection opens a linked repair attempt with the same issue ID. Accepted work reopens only for a relevant changed input, new blocking evidence, or scope change. A worker's `done` never skips acceptance gates.

Task dependencies form a DAG per attempt. Communication links route results to affected owners and the controller. Neither requires all-to-all chat. Send events on completion, blocker, changed dependency, or decision request; routine liveness monitoring belongs to the host, not repeated LLM prompts.

For each event keep an ID, task/attempt, observed artifact, evidence pointer, and requested action. Record it before acknowledging completion; ignore duplicate IDs. An event from an old attempt is retained as history but cannot advance the current attempt. If a worker disappears, inspect its artifacts before reassignment. Stop its writes before transferring ownership: a timeout is not proof that a process stopped. This manual protocol is not an atomic lease service.

## Bounded brief

```text
TASK / ATTEMPT: <stable identifiers>
GOAL / ACCEPTANCE: <outcome and deciding check>
INPUT: <snapshot/revision + relevant local/untracked changes>
SCOPE / CONTRACTS: <writable paths or read-only; interfaces>
KNOWN: <verified facts and pointers; hypotheses labeled>
TRIED: <failed approaches and discriminating evidence>
AUTHORITY / LIMITS: <existing authorization, protected lanes, budget>
RETURN: <delta report below and role-specific result>
```

Give reviewers criteria, target, and relevant contracts, excluding the author's reasoning/confidence. An isolated context helps independence; a cold inline reread is a limited alternative. Do not describe self-review as independent.

Workers return a compact delta, not their internal narrative:

```text
STATUS: done | blocked | needs-decision
TASK / ATTEMPT / ARTIFACT: <what was actually examined>
RESULT: <changed paths, finding, or verdict>
EVIDENCE: <command, exit status, input identity, key result, log pointer>
OPEN: <unknowns, blockers, decisions; or none>
NEXT: <one action and its owner>
```

Investigation adds supported cause, ruled-out hypotheses, and the discriminating test. Review adds severity-labeled grounded findings and verdict. Security adds threats/advisories, unknown controls, and proposed responses. Verification adds accept/reject/partial and applicable DoD gaps. Keep details in linked artifacts when large.

## Check ownership

The builder runs focused feedback checks. A reviewer may request a targeted independent check. One final verifier owns acceptance checks on the stable integrated artifact. The lead examines execution evidence and scope, without reflexively rebuilding. Unsupported reports remain unverified.

Required fresh/independent runs and CI gates still run. Do not reuse checks involving changing external state, timing, flakiness, or incomplete inputs. Untracked/generated files, toolchain, dependencies, command, environment, fixtures, and relevant runtime configuration all affect identity. A clean commit SHA alone does not identify a dirty tree.

Freeze inputs during execution, or use an immutable snapshot. After integration/repair, rerun affected checks and invalidate dependent evidence. Treat same-failure retries as rework; record what changed in the hypothesis or evidence. Two repairs without new evidence trigger diagnosis, not another worker.

## Optional local check runner

The [check runner](../scripts/check_runner.py) uses only Python's standard library. Invoke via its actual installed path; it is bundled with this skill. It launches argument arrays without a shell. It writes logs and a result ledger into a caller-selected scratch directory **outside the checked workspace**. It does not dispatch agents, enforce write scopes, sandbox commands, provide distributed locks, or enforce token budgets.

```powershell
python <installed-skill>/scripts/check_runner.py --cwd <workspace> --state-dir <scratch-outside-workspace> --input src --input tests --input pyproject.toml --input uv.lock --identity <toolchain-and-dependency-id> -- python -m pytest
```

Supply every relevant file/directory explicitly, including instruction/configuration and generated inputs when they affect behavior. Directories include hidden/untracked files. Symlinks are rejected; use real input paths or run without reuse. The command executable is resolved and hashed; use its real binary path when a Windows app-execution alias is unreadable. Batch wrappers need an explicit shell executable and complete dependency identity; the inherited environment is hashed but not printed or stored as plaintext. Provide toolchain/dependency identity and include relevant lockfiles; indirect tools and installed packages are not automatically discovered.

Default: execute fresh. `--reuse` is an explicit assertion that the check is deterministic, inputs complete, and results eligible for reuse. Matching concurrent reusable requests share a successful completed execution. Failures and stale results are never reused. Use `--fresh` for explicitly independent verification; it is the default and mutually exclusive with `--reuse`. A waiter has a bounded `--lock-timeout` (default 60 seconds) and can retry later without bypassing ownership.

Use `--explain` with the same inputs and command to inspect eligibility without executing the check or replacing execution records. JSON `cache.reasons` identifies changed inputs, input scope, command, executable, toolchain identity, environment, workspace, or platform. Other reasons identify a first compatible execution, corrupt records, missing logs, prior failure/unstable inputs, or an explicit fresh run. Comparison is against an exact record or the most recent execution in this lane; it is not a causal diagnosis of the underlying change. Only category fingerprints are stored; environment names/values and per-secret hashes are not exposed. The whole inherited environment remains part of identity, so volatile host variables can cause conservative misses. Do not exclude environment inputs merely to raise the hit rate.

Schema 2 identity records are distinct from older records. Old green records without compatible identity details do not become eligible after upgrading. `--explain` predicts eligibility only for checks you have independently established are deterministic with complete declared inputs; it does not certify that assertion.

The state directory has one local execution lane: all runner commands using it serialize, including fresh checks. Use separate state directories only for genuinely independent build resources. Native file locks release on process exit; a parent crash can leave a child command alive. Inspect the process/lane before reuse after an interrupted run. Shared network filesystems and multi-host execution require a real scheduling service.

Each JSON result includes input identity, command, exit code, log paths, reuse status, and whether inputs remained stable. Changed inputs during execution make the result stale even when the command returned zero; runner exit is then nonzero. Pre/post hashing does not detect change-and-restore races. Writer pauses or immutable snapshots are required for trustworthy results. Checks must keep generated outputs outside declared input trees or they will deliberately invalidate themselves.

Logs can contain secrets emitted by the command. Keep state private, redact before sharing, and do not commit it. Reuse is only as trustworthy as this local ledger and its input declaration. Existing external CI evidence may be consumed directly when it provides equivalent current provenance; this helper is optional.
