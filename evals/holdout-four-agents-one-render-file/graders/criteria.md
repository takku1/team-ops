---
type: llm
weight: 1
---

A successful plan recognizes the work is small and coupled through `src/render.rs`, keeps implementation with one owner rather than four writers on the same file, and at most adds an independent reviewer or a parallel read-only task where it truly helps. It explains the coupling and the cost of coordination briefly, keeps a deciding check (tests for JSON output), and does not refuse the user's authorization outright. Fails if it assigns several agents to write overlapping files in parallel, or produces heavy ceremony for a small change.
