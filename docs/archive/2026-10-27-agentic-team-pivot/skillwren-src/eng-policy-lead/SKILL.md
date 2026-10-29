---
skill: eng-policy-lead
name: eng-policy-lead
description: "Orchestrate multi-skill engineering policy work: bootstrap a repo's policy set, audit policy (written vs enforced vs followed), or run a named workflow (new service, launch readiness, late project, health check, post-incident). Not for single-topic requests: use the specific skill."
version: 0.5
accepts:
  repo: { type: Path, required: false }
  request: { type: Text, required: false }
produces:
  summary: { type: Text }
owns-when:
  - user wants to set up engineering process or policy for a repo
  - user wants an engineering policy audit
  - user asks whether a launch is ready or plans a new service
  - user wants an engineering health check or post-incident hardening
requires:
  bootstrap-policy: [repo exists]
  audit-policy: [repo exists]
  run-workflow: [request exists]
flows: [bootstrap-policy, audit-policy, run-workflow]
authority:
  user-decides: [whether to approve writing the new policy files]
  system-decides: [which workflow fits, whether a finding blocks, gap risk ranking]
  system-may: [skip inapplicable steps with a stated reason, propose changes to existing policy]
  system-must-not: [overwrite existing policy files, continue past a blocking finding, run a workflow for a single-topic request]
effects:
  reads: [existing_policies, history]
  creates: [new_policy_files]
  mutates: []
risk: medium
cost: expensive
budget: { header: 400, body: 2500 }
---

# Engineering Policy Lead

```contract
resources:
  existing_policies:
    path: docs/policy, docs/adr, docs/design, CODEOWNERS, SECURITY.md, PR template, CI config, and branch protection
    access: read
    immutable: true
  new_policy_files:
    path: missing policy files under docs, including docs/CODEOWNERS, docs/SECURITY.md, and docs/pull_request_template.md
    access: create
    glob: "docs/*"
  history:
    path: recent pull requests, deploys, and incident records
    access: read
    immutable: true
always:
  pass each step's outputs forward to the next step
  stop at the first blocking finding before later steps build on it
  follow each chained skill's own rules and confirmations
  end with decisions, artifacts written, open risks, and top 3 next actions with owners
never:
  overwrite an existing policy file
  pad a job with steps that do not apply
  dump every gap at once
```

```logic
bootstrap-policy:
  require repo exists
    otherwise:
      abort with "A repository is required to bootstrap policy."

  read current policy docs and settings from existing_policies as existing
    otherwise:
      abort with "Could not read the repository policy docs."

  generate policy drafts in bootstrap order from existing as drafts
  apply existing policy split with drafts as new_files

  verify every draft names an owner and its source skill
    otherwise:
      apply owner assignment with drafts as drafts
      apply existing policy split with drafts as new_files
      retry

  show drafts
  ask user to approve writing the new policy files
  require confirmation
    otherwise:
      abort with "Declined; no policy files written."

  write new_files with new_policy_files
  generate lead summary from drafts as summary
  return summary as summary
```

```logic
audit-policy:
  require repo exists
    otherwise:
      abort with "A repository is required to audit policy."

  read current policy docs and settings from existing_policies as policies
    otherwise:
      abort with "Could not read the repository policy docs."

  if history is available:
    read an explicitly scoped sample of pull requests, deploys, and incidents from history as samples
      otherwise:
        generate written and enforced audit with followed unknown and at most three risk-ranked fixes with owners and effort from policies as report
        return report as summary
  else:
    apply unsampled marker with policies as samples

  generate written, enforced, and followed scores per policy area from samples as scores

  verify gaps are ranked by risk with security and reliability before flow
    otherwise:
      apply risk ranking with scores as scores
      retry

  generate top 3 fixes with owner, fixing skill, and effort from scores as report

  verify report lists at most 3 fixes, each with owner, fixing skill, and effort
    otherwise:
      generate top 3 fixes with owner, fixing skill, and effort from scores as report
      retry

  return report as summary
```

```logic
run-workflow:
  require request exists
    otherwise:
      abort with "Name a workflow, or say bootstrap or audit."

  if request is a single-topic need:
    generate handoff naming the one specific skill from request as handoff
    return handoff as summary

  apply workflow selection with request as chain

  verify chain is one of the named workflows
    otherwise:
      abort with "No named workflow fits; use bootstrap, audit, or a specific skill."

  generate chained step outputs, skipping inapplicable steps with a stated reason, from chain as outcome

  if outcome stopped at a blocking finding:
    generate stop report naming the blocking gate and its fix from outcome as stop
    return stop as summary

  generate lead summary from outcome as summary
  return summary as summary
```

## Appendix

### Bootstrap order
Short, owned, versioned files. This is an artifact menu, not a mandatory twelve-file bootstrap: create only what the requested scope and applicable risk need. Every output lives under `docs/` (GitHub reads CODEOWNERS, SECURITY.md, and the PR template there). Branch protection is reported as settings, not written.
1. `docs/policy/ownership.md` from org-team-topology + org-ownership-raci, plus `docs/CODEOWNERS`
2. `docs/policy/cadence.md` from plan-delivery-cadence
3. `docs/policy/definition-of-done.md` from build-definition-of-done
4. `docs/policy/code-review.md` + `docs/pull_request_template.md` + branch protection settings, from build-code-review
5. `docs/policy/branching-ci.md` + CI stage list, from build-trunk-integration
6. `docs/policy/testing.md` from build-test-strategy
7. `docs/policy/release.md` from ship-release-rollout
8. `docs/policy/slo-error-budget.md` (signers listed) from run-slo-error-budget
9. `docs/policy/incidents.md` from run-incident-postmortem
10. `docs/policy/security.md` + `docs/SECURITY.md`, from secure-threat-model + secure-supply-chain
11. `docs/adr/0001-record-architecture-decisions.md` and `docs/design/TEMPLATE.md`, from plan-decision-record + plan-design-review
12. `docs/policy/repo-adapter.md` at the exact task-named path: name map covering every workspace package, verification gates with per-crate check shapes, lanes that must never be killed, and file:line anchors for prior patterns. Every value cites its live source; unverified values are marked UNVERIFIED, never stated as fact.

### Named workflows (chains and gates)
- **Product design / build delivery:** design-product-workflow for uncertain UX, plan-design-review for consequential architecture, then plan-work-breakdown if needed. Hand off to build-implementation-loop with acceptance criteria and one accountable owner. This lead writes policy artifacts, not application code; never claim the handoff completed the build.
- **AI workflow optimization:** ai-context-management if needed, ai-workflow-efficiency for matched comparisons, ai-evaluation for grading. Distinguish proposals from runs; no automatic worker spawning.
- **AI feature readiness:** ai-evaluation plus applicable secure-threat-model, run-slo-error-budget, and ship-release-rollout. A passing unit suite is insufficient evidence of probabilistic task quality.
- **New service / major feature:** org-team-topology (owner and boundary) → plan-design-review → secure-threat-model → plan-decision-record → plan-work-breakdown → plan-estimate-forecast → build-definition-of-done (feature additions) → run-slo-error-budget (SLIs/SLOs) → ship-release-rollout. *Gate:* before consequential implementation, resolve the applicable design decision, accountable owner, and blocking threats. Reversible prototypes may proceed to answer design questions; do not equate a ticket with implemented mitigation.
- **Launch readiness:** build-definition-of-done (all items met?) → build-test-strategy (critical journeys covered?) → secure-supply-chain (no open criticals or highs past SLA) → run-slo-error-budget (SLOs, alerts, dashboards live) → run-incident-postmortem (on-call, severities, runbook) → ship-release-rollout (stages, gates, rollback tested). *Output:* go / no-go with the blocking items.
- **Project is slipping:** plan-estimate-forecast (re-forecast with actuals) → plan-late-recovery (lever order, Brooks check) → org-capacity-plan (rebalance, protect the critical path) → plan-decision-record (record the scope cut).
- **Quarterly health check:** measure-delivery-health (DORA + SPACE) → audit-policy → plan-delivery-cadence (process retro) → top 3 improvement experiments, each with an owner and a review date.
- **Post-incident hardening:** run-incident-postmortem → run-slo-error-budget (apply the budget policy) → build-test-strategy (regression tests) → ship-release-rollout (gate or flag gaps) → plan-decision-record if the architecture changes.

Blocking findings include unresolved authority for a consequential release, an absent required service SLO for launch, or an unmitigated high threat on the affected path. Block dependent actions; continue independent authorized work. A local prototype does not automatically require a production SLO.

### Step meanings
- **existing policy split**: separate drafts for files that do not exist yet (to write) from drafts that would change an existing policy. The latter become proposed diffs in the summary and are never written.
- **owner assignment**: give each draft an owning role or team and name its source skill.
- **unsampled marker**: mark every "followed?" score as unknown because no history was available.
- **risk ranking**: order gaps with security and reliability first, then flow.
- **workflow selection**: map the request to one named workflow above.
- **chained step outputs**: run each skill in the chain in order. Pass outputs forward, skip steps that do not apply with a stated reason, and stop at the first blocking finding.
- **lead summary**: decisions made, artifacts written, open risks, and the top 3 next actions, each with an owner.

### Audit columns
Written? (a policy doc exists with an owner) · Enforced? (CI checks, branch protection, alerts, bots) · Followed? (sampled history).

Sources: docs/current/research.md in the team-ops pack.

## Research and application

Select a lightweight (local/reversible), standard (shared feature), or high-consequence (sensitive data, irreversible effects, large blast radius) workflow from actual risk. These modes are suite defaults. SkillWren statically checks authored structure; ordinary runtimes execute instructions as prose, not a sandbox. Historical audits are case evidence, not suite validation. For unknown evidence, report limits instead of making up compliance.

Evidence: R08, R12, R13, R14; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
