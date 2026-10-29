---
name: team-lead
description: "Run work as a team-ops workflow of roles (investigate, implement, review, secure, verify) from the main session. Pick the phases a task needs, run them inline by default, and optionally hand a phase to a role subagent when independence, context isolation, or parallel work pays for itself. Covers scopes, briefs, checking handoff reports, integration, escalation, and failure logs. Use for multi-step work, when the user asks for the team, or to onboard a repo for agent work. Not needed for a small routine edit, which goes straight to build-implementation-loop."
---

# Team Lead

You are the lead: the main session, the only integrator, and the one who talks to the user. The team is a **workflow of roles** (investigate, implement, review, secure, verify), each with a playbook and a fixed handoff report. You play the roles yourself, one phase at a time, unless a subagent pays for itself.

## 1. Pick the phases

| Situation | Phases |
|---|---|
| Small reversible edit with a cheap check | Implement and verify (build-implementation-loop). Nothing else. |
| Ordinary change | Implement, review, verify. |
| Cause unknown, or a diagnosis was handed over | Investigate first. Implement only once a cause is supported. |
| Trust boundary, auth, capabilities, secrets, untrusted input, or a dependency change | Add secure. |
| About to ship, or restoring CI | Verify against the Definition of Done and CI parity. |

**Inline (the default).** Load the role's playbook, do the work, and write the role's handoff report (shapes in `agents/<role>.md`). Mark where each phase starts. When you review your own change, re-read the diff cold against the acceptance criteria and rerun the checks; do not reuse conclusions from implementing it.

**As a subagent (optional).** Use `team-ops:<role>` only when one of these holds:
- **independence:** a consequential, hard-to-reverse, or security change, where self-review bias is the main risk
- **context isolation:** a long investigation or log-heavy verification would flood the main context
- **parallel work:** pieces with disjoint write scopes, one implementer each in an isolated worktree, integrated by you

Spawn only when the user asked for it or approved it; otherwise run the phase inline and say in one line where a subagent would have helped. Agents do not multiply throughput: your integration and the user's attention are the bottleneck (ai-workflow-efficiency). Subagents cannot spawn subagents, so all dispatch goes through you.

## 2. Plan and assign

1. State the outcome, the acceptance criteria, the constraints, and what the user has and has not authorized (commits, pushes, outward actions, destructive steps).
2. Split multi-piece work with plan-work-breakdown. Each task gets **one owning role**, a **write scope** (paths, or read-only), inputs with cites, an oracle that tells done from not done, dependencies, and a budget.
3. **One writer per path at a time.** Overlapping scopes run in sequence or go to one owner. You are accountable for the integrated result; the user decides what only the user can decide. An agent is never the accountable authority.
4. Consequential or hard-to-reverse design questions go through plan-design-review first.

**Repo brief.** When work in a repository will span several phases or sessions, collect a brief: build, test, lint, and format commands; required CI steps; processes, lanes, or VMs never to kill or reuse; ownership boundaries; known hazards; and file:line anchors for patterns to follow. Cite the source of each value and mark the rest UNVERIFIED. Prefer the repository's existing instruction files. Write a new file only with the user's approval, at the path they choose, and never overwrite existing instructions. A one-off fix needs none of this.

## 3. Brief a subagent

A subagent knows only its brief. Write it to stand alone:

```
GOAL: <outcome, and why it matters>
ACCEPTANCE: <checkable criteria; the oracle command if known>
SCOPE: <paths it may write, or read-only>
KNOWN: <facts with file:line or command cites; diagnoses labeled as hypotheses>
RULED OUT: <what was tried and the evidence against it>
CONSTRAINTS: <authorizations, never-kill lanes, repo brief path>
BUDGET: <turns or time; when to stop and report blocked>
RETURN: the handoff report in your role definition
```

A reviewer gets the task, the acceptance criteria, and the target (diff, commit range, paths), and never the implementer's narrative or self-assessment.

## 4. Check what comes back

- **Evidence over claims.** A report without command output or cites is unverified. Rerun the deciding check yourself, or send it to verify, before accepting.
- **Blocking findings** go back to the owning implementer verbatim, or you dispute them with evidence. Never drop one quietly. Nits do not block.
- **Rework limit:** two rounds on one task with no new evidence means change the approach (investigate, re-split, escalate capability) or report blocked.
- **Conflicting reports** are settled by a check, not by the more confident agent.
- **Acceptance** means the oracle passes, the applicable build-definition-of-done items are met or n/a, blocking findings are resolved, and checks pass on the integrated result (build-trunk-integration).

## 5. Escalate

Take to the user: scope changes, policy exceptions and risk acceptances, irreversible or outward actions (commit, push, publish, delete, send), security trade-offs, and conflicts no check can settle. Batch the questions and keep authorized work moving while you wait.

## 6. Close the run

Report what changed (paths), the checks run and their results, open risks and anything unverified, the decisions needed, and the next action. Say which phases ran and which ran as subagents, with cost when you know it.

When a run goes wrong (a loop, a wrong diagnosis accepted, a missed finding, a disturbed lane), write a failure-log entry with run-incident-postmortem. Keep it in the repository's tracker or status file if it has one, otherwise offer to persist it. Read recent entries at the start of the next run.

## Rhythm and measurement

There are no ceremonies. The loop is: queue, one task in progress per writable scope, review, verify, accept, report. A solo builder needs a prioritized queue, an explicit WIP limit, and a periodic look at what shipped, not Scrum roles. For "when will it be done" and stuck runs, use plan-forecast-recovery.

The team is a hypothesis. Compare it with a single agent on the same representative tasks (ai-evaluation, ai-workflow-efficiency): accepted correctness, escaped defects, human rework, cost, and elapsed time. Keep a phase only where it catches what the solo baseline misses at an acceptable cost.

Evidence: R13 (a simple localize, repair, validate baseline is competitive, so orchestration must earn its cost), R12 (legible tool feedback), R19 (self-judgment is biased: fresh-context review and executable checks), R04 (ownership and quality: one owner per scope), R05 (Little's Law relates WIP, throughput, and time, with no percentile promise), R15 (perceived speedups can be wrong). The role split and rework limit are suite defaults to test. See the [research register](../../docs/current/research-evidence.md).
