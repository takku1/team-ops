---
name: kanban-flow
description: Visualize flow and limit work in progress.
---

# Kanban Flow

Use for support or continuous work.

Prose: columns ToDo, Doing, Review, Done. Explicit WIP per column, 1-2 per dev. Track lead time, cycle time, throughput. Replenish as capacity opens.

Logic:
- require board with WIP limits exists
- find the single constraint, subordinate the rest
- flag blocked or over-limit cards
- pull next highest-rank card only
- return flow state plus constraint plus blockers
