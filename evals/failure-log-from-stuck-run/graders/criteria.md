---
type: llm
weight: 1
---

A successful write-up is blameless and concrete. Contributing factors
include accepting a handed-over diagnosis without checking that its
discriminator could tell the cases apart, no investigation phase before
implementing, and no stop after rounds that produced no new evidence. It
does not settle for "the agent was wrong" or "human error". Actions
change something checkable: the brief template (label diagnoses as
hypotheses), the lead's rework limit, an investigation phase for
handed-over diagnoses, or a new eval case. Each action says how to tell
whether it worked. It records cost and impact, and says where the entry
is kept and that the next run reads it. Fails if it produces a ticket
list with no system factors, or blames an individual.
