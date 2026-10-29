---
name: build-implementation-loop
description: Implement a feature or fix through repository inspection, a bounded change, meaningful verification, and final diff review. Use for hands-on coding work, including AI-assisted builds. Not for policy-only audits, design-only requests, or deployment authorization.
---

# Implementation Loop

**Role:** implementer (agents/implementer.md), or the lead on a small change. **Returns:** the implementer handoff report.

## Establish the task

Turn the request into an observable outcome and its constraints. Read the repository instructions, working-tree status, the affected entry points, nearby patterns, and the real test and build commands. Preserve unrelated user changes. Read only enough to understand the behavior and its dependencies.

- **Defect:** reproduce it, or record why you cannot. Identify a falsifiable cause before changing code. A handed-over diagnosis is a hypothesis (ai-context-management).
- **Feature:** identify acceptance examples and the smallest integrated slice.
- Use plan-design-review for consequential decisions and design-product-workflow for uncertain user flows. A routine fix needs neither.

## Change and verify

1. **Make the smallest coherent change** that meets the outcome. Keep necessary cross-component edits together; small does not mean incomplete. Check unfamiliar APIs against local code or authoritative docs, not memory.
2. **Run the narrowest check that tells correct from incorrect.** A behavioral bug gets a regression check when practical: observe it fail before the fix and pass after. Avoid tests that restate constants or the implementation.
3. **On failure, change one hypothesis at a time.** Separate pre-existing failures from regressions. Never weaken an assertion, hide an error, or mock the failing boundary to get green.
4. **Changing a test's expectation** needs cited evidence that the behavior change was intended (commit, ticket, decision), must honor any condition the test states for editing it, and must pin the new behavior at least as strictly as the old.
5. **Run the required repository checks** and the affected integration checks. Hold formatters and linters to the lines you changed and attribute pre-existing drift instead of reformatting. Inspect the final diff, new files, and runtime or UI behavior where it matters: a unit test does not prove persistence, permissions, integration, or layout.
6. **Stop** when acceptance and the relevant checks pass and nothing material remains. Two attempts with no new evidence mean a different diagnostic approach, or a concrete blocker. Honor time and cost limits and leave a resumable state.

## Authority and scope

Existing authorization covers routine, reversible work in scope; do not re-ask. Commits, pushes, publication, external side effects, and destructive actions follow the user's authorization. On a team, stay inside the write scope the lead assigned and report anything outside it as `needs-decision`. Leave review to a fresh pass. This skill does not authorize spawning workers; team-lead decides that with the user.

## Completion

Report what changed, the checks you observed and their results, and the limits. Keep implemented, tested, merged, and deployed distinct. A plan, a plausible patch, or an intended command is not a completed implementation; if checks could not run, say what is unverified. Update the repository's status or tracker entry for the item you fixed, and flag (do not silently edit) adjacent entries the evidence shows are stale but that belong to someone else's decision.

Evidence: R12 and R13 (legible tool interfaces; a simple localize, change, validate baseline, not proof of this exact sequence), R02 (check behavior, not coverage). See the [research register](../../docs/current/research-evidence.md).
