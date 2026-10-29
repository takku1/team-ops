---
name: plan-work-breakdown
description: "Split a deliverable into verifiable vertical slices with owners, dependencies, contracts, and write scopes. Identify genuinely parallel work without dispatching agents or fragmenting a coupled change."
---

# Work Breakdown

Split until each leaf has an observable outcome, bounded ownership, and a useful deciding check. Small work stays one task. Children cover their parent's scope without invented extras.

- Prefer thin end-to-end slices over activity lists such as "do backend". Include security/integrity in the slice they affect.
- Keep coupled contract changes together. Independent filenames do not make tasks independent: examine interfaces, generated outputs, migrations, build resources, and integration.
- Give each leaf one implementation owner, criteria, write scope, oracle, dependencies, and a proportionate budget. An investigation is a bounded question with an evidence-based answer.
- Sequence overlapping scopes or give the shared file to one owner. Include registries, lockfiles, generated docs, and status records. Regenerate outputs from integrated sources.
- Order risky unknowns and prerequisites first. Mark work ready when its required inputs/contracts exist.
- Separate the dependency graph from the communication graph. Identify who needs a changed contract or result; do not broadcast all work to all agents.

Return: ID | outcome/acceptance | owner/scope | oracle | depends on. Mark useful parallel branches and the integration owner; explain coupling that prevents parallel execution. A plan does not dispatch workers. team-lead determines whether a worker earns its cost within existing authority.

Evidence: R12, R13, R21, R23; PMI WBS Practice Standard, Wake's INVEST, Lawrence's splitting guidance. Task size/concurrency are local choices. [Register](../../references/research-evidence.md).
