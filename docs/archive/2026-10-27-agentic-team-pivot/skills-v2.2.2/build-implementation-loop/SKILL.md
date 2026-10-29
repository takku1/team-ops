---
name: build-implementation-loop
description: Implement a feature or fix through repository inspection, a bounded change, meaningful verification, and final diff review. Use for hands-on coding work, including AI-assisted builds. Not for policy-only audits, design-only requests, or deployment authorization.
---

# Implementation Loop

## Establish the task

Turn the request into an observable outcome and relevant constraints. Inspect repository instructions, working-tree status, the affected entry points, nearby patterns, and actual test/build commands. Preserve unrelated user changes. Read only enough context to understand the behavior and dependencies; use ai-context-management if retrieval or continuity is the bottleneck.

For a defect, reproduce it or document why reproduction is unavailable. Identify a falsifiable cause before changing code. For a feature, identify acceptance examples and the smallest integrated slice. Use plan-design-review for consequential decisions and design-product-workflow for uncertain user flows; do not require either for a routine fix.

## Change and verify

1. Make the smallest coherent change that satisfies the outcome. Keep necessary cross-component changes together; small does not mean incomplete. Verify unfamiliar APIs against local code or authoritative documentation.
2. Run the narrowest meaningful check that can distinguish correct from incorrect behavior. Behavioral bugs should have a regression check when practical. Avoid tests that merely restate constants or generated implementation structure.
3. On failure, inspect evidence and change one hypothesis at a time. Separate pre-existing failures from regressions. Do not weaken assertions, hide errors, or substitute a mock for the failing boundary merely to pass. When the fix is to change a test's expectation, cite the evidence that the behavior change was intended (commit, ticket, decision), honor any condition the test states for editing it, and pin the new behavior at least as strictly as the old.
4. Run required repository checks and affected integration checks. Hold formatters and linters to the lines you changed; attribute pre-existing drift instead of reformatting unrelated code. Inspect the final diff, new files, and relevant runtime/UI behavior. A passing unit test does not establish correct persistence, permissions, integration, or visual layout.
5. Stop iterating when acceptance and relevant checks pass and no material issue remains. If repeated attempts yield no new evidence, change the diagnostic approach; report a concrete blocker if none is available. Honor explicit time/cost limits and leave a resumable state.

## Authority and concurrency

Existing authorization covers routine reversible implementation within scope. Do not re-ask permission already given. Publication, external side effects, and destructive actions follow the user's authorization and host permissions. If parallel workers are authorized and useful, assign non-conflicting scopes and one integration owner; verify the combined result. This skill alone does not authorize spawning workers.

## Completion

Report what changed, the observed checks and outcomes, and material limitations. Distinguish implemented, tested, merged, and deployed. A plan, a plausible patch, or an intended command is not completed implementation. If checks cannot run, state what is unverified without claiming success. Update the repository's own status or tracker entries that record the item you fixed; flag, rather than silently edit, adjacent entries the evidence shows are stale but that belong to someone else's decision.

Evidence: R12/R13 motivate legible tool interfaces and a simple localization/change/validation baseline; they do not prove this exact sequence. R02 motivates checking behavior beyond coverage. See the [research register](../../docs/current/research-evidence.md).
