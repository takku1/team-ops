---
name: plan-work-breakdown
description: "Split a deliverable into verifiable vertical slices with owners, dependencies, contracts, and write scopes, and find genuinely parallel work. Plans only; never dispatches agents."
---

# Work Breakdown

Split until every leaf has an observable outcome, one owner, and a deciding check. Small work stays one task; children cover their parent's scope with nothing invented.

**Return:** `ID | outcome / acceptance | owner / write scope | deciding check | depends on`, marking useful parallel branches and the integration owner, and naming the coupling that prevents parallelism. A plan never dispatches workers; team-lead decides whether a worker earns its cost.

- **Resolve before splitting.** Classify each capability BUY, ADOPT, WRAP, BUILD, or DEFER; never decompose a vendor's internals.
- **Slice vertically.** Thin end-to-end slices beat activity lists like "do backend". Put security and integrity work in the slice it affects.
- **Keep coupled changes together.** Separate filenames do not make tasks independent: check interfaces, generated outputs, migrations, build resources, and integration.
- **Specify each leaf:** one implementation owner, criteria, write scope, deciding check, dependencies, and a proportionate budget. An investigation is a bounded question with an evidence-based answer.
- **One writer per shared file.** Sequence overlapping scopes or give the shared file, including registries, lockfiles, generated docs, and status records, to one owner. Regenerate outputs from integrated sources.
- **Order by risk.** Unknowns and prerequisites first. A task is ready when its required inputs and contracts exist.
- **Route, don't broadcast.** The dependency graph and the communication graph differ; identify who needs each changed contract or result.

Evidence: R12, R13, R21, R23, R32, P09; task size and concurrency are local choices ([register](../../references/research-evidence.md)).
