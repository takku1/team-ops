# Coordination contract

Load for delegated or multi-session work. Small inline work needs no board, schema, or helper. The lead (main session) is the only coordinator; no supervising LLM is added.

## Task and event state

Use the repo's tracker, or a scratch record outside source inputs, written only by the lead. Record only what the next decision needs:

```text
run: goal, acceptance, authority, budget/actuals, integration_owner
task: id, attempt, owner, scope, depends_on, input_artifact,
      state, oracle, evidence_refs, issue_ids, next_action
issue: id, finding, repair_attempts, hypotheses_tried, new_evidence
```

States: `ready -> running -> awaiting_review -> awaiting_verification -> accepted` (skip inapplicable review); `blocked` and `cancelled` are explicit. A rejection opens a linked repair attempt with the same issue ID. Accepted work reopens only for a relevant changed input, new blocking evidence, or a scope change. A worker's `done` never skips gates.

Dependencies form a DAG per attempt; communication links route results only to affected owners and the lead. Send events on completion, blocker, changed dependency, or decision request; liveness monitoring is the host's job, not repeated LLM prompts.

Each event keeps an ID, task/attempt, observed artifact, evidence pointer, and requested action. Record it before acknowledging; ignore duplicate IDs. An event from an old attempt is history and cannot advance the current attempt. If a worker disappears, inspect its artifacts and stop its writes before reassigning: a timeout does not prove a process stopped. This is a manual protocol, not an atomic lease service.

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

Reviewers get criteria, target, and contracts, never the author's reasoning or confidence. An isolated context gives independence; a cold inline reread is self-review and must not be called independent.

Workers return a compact delta, not their narrative:

```text
STATUS: done | blocked | needs-decision
TASK / ATTEMPT / ARTIFACT: <what was actually examined>
RESULT: <changed paths, finding, or verdict>
EVIDENCE: <command, exit status, input identity, key result, log pointer>
OPEN: <unknowns, blockers, decisions; or none>
NEXT: <one action and its owner>
```

Each role's agent file defines its RESULT. Link large details.

## Check ownership

Builders run focused checks; reviewers may request a targeted independent check; one final verifier owns acceptance checks on the stable integrated artifact; the lead examines that evidence without reflexively rebuilding. Unsupported reports stay unverified. Required fresh runs and CI gates still run.

Evidence identity covers untracked/generated files, toolchain, dependencies, command, environment, fixtures, and relevant runtime config; a clean commit SHA does not identify a dirty tree. Never reuse checks that depend on changing external state, timing, flakiness, or incomplete inputs. Freeze inputs during execution or use a snapshot. After integration or repair, rerun affected checks and invalidate dependent evidence. Same-failure retries are rework: record what changed in hypothesis or evidence. Two repairs without new evidence trigger diagnosis, not another worker.

When duplicate expensive local checks recur, use the optional [check runner](check-runner.md).
