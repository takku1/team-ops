---
type: llm
weight: 1
---

A successful plan notices that both tasks write `abi/registry.rs` (and
possibly the generated docs). It does not run them as parallel writers
of that file. It either sequences the registry edits, gives the shared
file to one owner, or lets parallel work proceed only on disjoint
scopes, then integrates. Generated docs are regenerated from the merged
sources, not merged by hand. Every task has an owner, a write scope, and
an oracle, and the lead is the integrator who obtains current verification evidence on the
combined result through one designated owner. Fails if both tasks are assigned to edit the registry
concurrently, or if green checks in separate worktrees are treated as
proof that the combined result works.
