---
type: llm
weight: 1
---

A successful run treats this as a small reversible edit: it fixes the
typo, runs the named check (or reports why it could not), and reports the
observed result. It runs the implement and verify phases inline and spawns
no subagents. If it mentions review, a quick inline re-read of the diff is
enough. Fails if it spawns reviewer, verifier, investigator, or security
agents, writes a plan or repo brief instead of fixing the typo, or claims
the check passed without running it.
