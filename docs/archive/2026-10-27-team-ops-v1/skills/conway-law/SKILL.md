---
name: conway-law
description: Align team boundaries with architecture before refactoring.
---

# Conway Law

Use when handoffs are slow or ownership is unclear.

Prose: map communication paths, then draw service boundaries to match. One team owns each service. Inverse Conway: design teams first. Evidence: MIT/Harvard mirroring work, distributed teams ship more modular code.

Logic:
- require team list and service list exists
- map who talks to whom vs who depends on what
- propose boundary move with owner and reason
- return boundary map plus mismatches
