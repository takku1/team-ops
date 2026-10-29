---
skill: build-code-review
name: build-code-review
description: "Set a code review policy (small changes, one-business-day response, improves-code-health approval, owner routing, labeled comments) or review a change against it. Use when defining review rules for a repo, when reviews are slow or contentious, when PRs are huge, or when actually reviewing a change. Not for automated security scanning (use secure-supply-chain)."
version: 0.5
accepts:
  repo: { type: Path, required: false }
  target: { type: Text, required: false }
produces:
  review_policy: { type: Text, when: setting review policy }
  review_report: { type: Text, when: reviewing a change }
owns-when:
  - user wants code review rules or a review policy for a repo
  - user wants a review of a pull request or change
  - user says code reviews are slow or pull requests are too large
requires:
  set-review-policy: [repo exists]
  review-change: [target exists]
flows: [set-review-policy, review-change]
authority:
  user-decides: [whether to adopt the review policy]
  system-decides: [whether the change is reviewable in size, severity label of each comment, review verdict]
  system-may: [ask the author to split an oversized change]
  system-must-not: [modify reviewed code, block on preference no style guide supports]
effects:
  reads: [repository]
  creates: []
  mutates: []
risk: low
cost: cheap
budget: { header: 400, body: 2500 }
---

# Code Review Policy

```contract
resources:
  repository:
    path: repository review settings, CI config, CODEOWNERS, and PR template, plus the working tree status
    access: read
    immutable: true
always:
  approve once the change improves overall code health and has no unresolved blocking correctness or security issue, even if it is not perfect
  check in priority order: design, functionality, complexity, tests, security and privacy, naming and comments and docs, operability
  comment on the code, not the person, and explain why
  leave style nits to formatters and linters
  inspect working tree status and read in-scope untracked and unstaged paths before reviewing, and refuse or caveat the report when part of the change is unread
never:
  modify reviewed code
  block a change on personal preference that no style guide supports
  approve a change too large to review well
```

```logic
set-review-policy:
  require repo exists
    otherwise:
      abort with "A repository is required to set review policy."

  read current review settings from repository as current
    otherwise:
      abort with "Could not read the repository review settings."

  apply policy baseline with current as policy

  verify policy covers approval standard, change size, response time, required approvals, author duties, automation, branch protection, and PR template
    otherwise:
      apply policy baseline with current as policy
      retry

  show policy
  ask user to adopt the review policy
  require confirmation
    otherwise:
      abort with "Declined; no review policy adopted."

  return policy as review_policy
```

```logic
review-change:
  require target exists
    otherwise:
      abort with "A change to review is required."

  read target as changes
    otherwise:
      abort with "Could not read the change."

  read in-scope untracked and unstaged paths from repository as unscanned
    otherwise:
      abort with "Could not read the working tree status."

  generate reviewed change with unscanned from changes as reviewed

  verify reviewed covers every in-scope path in unscanned from unscanned
    otherwise:
      abort with "Part of the change is unread; review is partial."

  if reviewed is too large to review well:
    generate split request asking the author to split the oversized change from reviewed as report
    return report as review_report

  generate findings in checklist priority order from reviewed as findings

  verify every finding cites the changed lines it rests on, or the unchanged location the change leaves inconsistent
    otherwise:
      apply grounding filter with findings as findings
      retry

  verify every comment carries a severity label
    otherwise:
      apply label correction with findings as findings
      retry

  generate review report with verdict from findings as report

  verify report verdict is approve, approve with nits, or request changes, with reasons
    otherwise:
      generate review report with verdict from findings as report
      retry

  return report as review_report
```

## Appendix

### Policy baseline (rules adapted to the repo)
- **Approval standard:** approve once the change improves overall code health and has no unresolved blocking correctness or security issue, even if it is not perfect. There is no perfect code, only better code (Google eng-practices).
- **Small changes:** judge semantic complexity, coupling, and reviewer capacity. About 100 lines changed is a healthy norm, and around 1000 is usually too large **only as a historical heuristic, not a hard cutoff**. Separate refactors from behavior changes. Stack PRs for big features.
- **Speed:** first response within **one business day at most**, and faster is better. Review speed is a team throughput lever, not a courtesy. Make PR age a visible metric so queues do not age for days.
- **Required approvals:** at least 1 owner (from CODEOWNERS) per touched area. Add a second approver for security-sensitive paths, schema migrations, and infra.
- **Authors** write a description of what changed, why, how it was tested, and the risk and rollback. They self-review before requesting review and keep CI green.
- **Automate the nits:** formatters and linters enforce style. Humans review design.
- **Branch protection** settings and a **PR template** carrying the author description fields.

### Reviewer checklist (priority order)
1. Design: does it belong here, and does it fit the architecture and the ADRs?
2. Functionality: correct behavior, edge cases, concurrency, user impact
3. Complexity: could it be simpler? Is anything over-engineered for needs that do not exist yet?
4. Tests: correct, meaningful, and able to fail
5. Security and privacy: input handling, authz, secrets, PII, injection
6. Naming, comments (the *why*, not the *what*), docs
7. Operability: logging, metrics, failure modes, flags

### Comment etiquette
Severity labels: `blocking:`, `nit:`, `optional:`, `question:`, `fyi:`. Resolve disagreements by technical facts and style guides. Escalate to the tech lead or owner after one round, or move to a call.

### Untracked and unstaged files
First establish the review target (PR commit range, staged patch, or working tree). Do not mix unrelated local work into a PR review. A diff alone is not the whole working-tree change. New (`??`) and unstaged files carry
much of some features and are invisible to diff-only review — run the VCS status scan, establish which paths belong to the target, and read those paths. Mark unread in-scope material as partial coverage; report grounded findings from the material reviewed.

### Step meanings
- **policy baseline**: adapt relevant baseline rules to the repository and risk. Preserve adopted requirements; propose justified changes explicitly. Return the applicable policy, branch-protection settings, and PR template.
- **label correction**: give each unlabeled comment the label that matches its impact. Change labels only; never drop a comment.
- **grounding filter**: drop only the findings that cite nothing; keep every grounded one. A finding outside the diff (a stale doc, tracker row, caller, or config the change makes inconsistent) is grounded when it names both the changed line that implicates it and the unchanged location.

Sources: docs/current/research.md in the team-ops pack.

## Research and application

Response deadlines and line-count heuristics are local defaults. Review generated code with the same behavior, security, and maintainability standard. Check plausible-but-nonexistent APIs and untested edge cases. Scope all path discovery to the target; private unrelated files are not review inputs.

Evidence: R01, R02; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
