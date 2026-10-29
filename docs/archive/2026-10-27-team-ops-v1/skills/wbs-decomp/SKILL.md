---
name: wbs-decomp
description: Split deliverables into verifiable chunks with done criteria.
---

# WBS Decomp

Use when a project is too big to estimate.

Prose: break deliverables until each chunk is under two days with a checkable done test.

Logic:
- require deliverable list exists
- split until each chunk is small and testable
- attach done criteria per chunk
- return tree plus estimates
