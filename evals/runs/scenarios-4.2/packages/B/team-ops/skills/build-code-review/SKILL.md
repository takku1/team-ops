---
name: build-code-review
description: "Review a change (working tree, staged patch, commit range, or PR) with grounded, severity-labeled findings and a verdict, or set a repo's review policy. Use for any code review, or when reviews are slow or PRs too big."
---

# Code Review

Review the artifact against its criteria. Prefer a fresh context when independent review matters; a cold inline reread remains self-review. Return the precise target, grounded findings, and a verdict. Inline review needs no worker report ceremony.

## Review a change

1. **Fix the target:** commit range, staged patch, or working-tree paths. Run the VCS status scan: new (`??`) and unstaged files can carry much of a feature and are invisible to a diff. Read every in-scope path; leave unrelated or private local files out. If part of the target stays unread, say the review is partial.
2. **Read the task and acceptance criteria first,** then the change, then the callers, contracts, and tests it touches.
3. **Check evidence freshness.** Unsupported "tests pass" is unverified. Inspect trustworthy execution records against current inputs; request a targeted check when evidence is missing, stale, or independent execution matters. A role change alone is no reason to rebuild the full suite. Coordinate with the assigned final verifier.
4. **Look where the author did not:** the edge case beside the one fixed, error paths, concurrency, docs or trackers the change makes stale, plausible but nonexistent APIs in generated code.
5. **Check in priority order:** design (fits the architecture and decisions?) · functionality (correct, edge cases, user impact) · complexity (simpler? built for needs that do not exist?) · tests (meaningful, able to fail, regression evidence for bug fixes; coverage is not a goal) · security and privacy (input handling, authz, secrets, injection) · naming, comments (the why), docs · operability (logging, failure modes).
6. **Ground every finding.** Cite the changed line it rests on. A finding outside the diff (stale doc, caller, config) names both the changed line that implicates it and the unchanged location. Drop only findings that cite nothing.
7. **Label every finding:** `blocking:`, `nit:`, `optional:`, `question:`, `fyi:`. Style nits belong to formatters.
8. **Verdict:** `approve` once the change improves code health and nothing blocking remains, even if imperfect · `approve-with-nits` · `request-changes` · `split-required` when it is too large to review well (propose the split).

Never edit the reviewed code. Hand trust-boundary, auth, capability, secret, untrusted-input, or dependency concerns to the lead for a secure phase (secure-review), in addition to any finding you can ground. Disagreements are settled by facts and style guides; the lead settles them with a discriminating check, or raises only the unresolved decision outside existing authority. Repairs return to the implementation owner with the same issue ID; nits do not reopen acceptance.

For delegated reviews or expensive checks, use [the coordination contract](../team-lead/references/coordination.md).

## Set a review policy

Read the repo's review settings, CODEOWNERS, CI, and PR template, then propose (the user adopts it):
- **Approval standard:** improves code health, nothing blocking unresolved.
- **Size:** judge semantic complexity, not lines. About 100 changed lines is healthy and about 1000 usually too big, as heuristics. Separate refactors from behavior changes; stack large features.
- **Speed:** first response within one business day; make PR age visible.
- **Approvals:** one owner per touched area; a second for security-sensitive paths, migrations, and infra.
- **Authors** describe what, why, how tested, risk, and rollback, self-review first, and keep CI green.
- **Automation:** formatters and linters own style; branch protection and a PR template carry the rest.

Preserve requirements the repo already adopted; propose changes explicitly.

Evidence: P01 (Google engineering practices), R01 (review also transfers knowledge), R02 (coverage is not effectiveness), R24 (verification failures). Deadlines and size numbers are local defaults. [Register](../../references/research-evidence.md).
