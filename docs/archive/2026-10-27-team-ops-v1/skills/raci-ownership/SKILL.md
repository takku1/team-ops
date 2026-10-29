---
name: raci-ownership
description: Name one accountable owner per task with RACI.
---

# RACI Ownership

Use when ownership or approvals stall work.

Prose: Responsible does, one Accountable owns, Consulted advises, Informed gets updates. Variants RASCI, DACI. No task ships without exactly one A.

Logic:
- require task list exists
- assign R, single A, C, I per task
- flag tasks with zero or double A
- return matrix plus gaps
