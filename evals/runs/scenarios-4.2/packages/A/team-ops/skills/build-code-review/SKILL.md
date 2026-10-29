---
name: build-code-review
description: "Review a change (working tree, staged patch, commit range, or PR) with grounded, severity-labeled findings and a verdict, or set a repo's review policy. Use for any code review."
---

# Code Review

Review an artifact against its criteria. For independence, prefer a fresh context; rereading your own work inline is still self-review. Inline reviews skip worker-report ceremony.

**Return:** the precise target, grounded labeled findings, and a verdict.

## Review a change

1. **Pin the target:** commit range, staged patch, or working-tree paths. Run the VCS status scan: new (`??`) and unstaged files can hold much of a feature and never appear in a diff. Read every in-scope path; leave unrelated or private local files out. If anything in scope stays unread, call the review partial.
2. **Read in order:** task and acceptance criteria, then the change, then the callers, contracts, and tests it touches.
3. **Check evidence freshness.** An unsupported "tests pass" is unverified. Accept trustworthy execution records whose inputs match the change; request a targeted check when evidence is missing or stale or independence matters. Being the reviewer is no reason to rerun the full suite; coordinate with the final verifier.
4. **Look where the author did not:** the edge case beside the one fixed, error paths, concurrency, docs or trackers the change makes stale, plausible-but-nonexistent APIs in generated code.
5. **Check in priority order:** design (fits the architecture and decisions) → functionality (correctness, edge cases, user impact) → complexity (simpler? built for needs that do not exist?) → tests (meaningful, able to fail, regression evidence for bug fixes; coverage is not a goal) → security and privacy (input handling, authz, secrets, injection) → naming, comments (the why), docs → operability (logging, failure modes).
6. **Ground every finding** in the changed line it rests on. A finding outside the diff (stale doc, caller, config) cites both the implicating changed line and the unchanged location. Drop only findings that cite nothing.
7. **Label every finding:** `blocking:`, `nit:`, `optional:`, `question:`, `fyi:`. Leave style to formatters.
8. **Verdict:** `approve` (improves code health, nothing blocking, even if imperfect) · `approve-with-nits` · `request-changes` · `split-required` (too large to review well; propose the split).

**Before returning, verify:** every in-scope path, untracked included, was read or the review says partial; every finding has a label and a cited line; the verdict matches the blocking findings.

## Boundaries

- Never edit the reviewed code.
- Send trust-boundary, auth, capability, secret, untrusted-input, or dependency concerns to the lead for secure-review, in addition to any finding you can ground.
- Settle disagreements with facts, style guides, or a discriminating check run by the lead.
- Repairs return to the implementation owner under the same issue ID; nits never reopen acceptance. Delegated reviews follow [the coordination contract](../team-lead/references/coordination.md).

## Set a review policy

Read the repo's review settings, CODEOWNERS, CI, and PR template. Propose changes for the user to adopt, preserving what the repo already requires:

- **Standard:** approve when the change improves code health and nothing blocking is unresolved.
- **Size:** judge semantic complexity, not lines. Heuristics: about 100 changed lines is healthy, about 1000 usually too big. Separate refactors from behavior changes; stack large features.
- **Speed:** first response within one business day; make PR age visible.
- **Approvals:** one owner per touched area; a second for security-sensitive paths, migrations, and infra.
- **Authors** state what, why, how tested, risk, and rollback; self-review first; keep CI green.
- **Automation:** formatters and linters own style; branch protection and the PR template carry the rest.

Evidence: P01, R01, R02, R24, R34; deadlines and size numbers are local defaults ([register](../../references/research-evidence.md)).
