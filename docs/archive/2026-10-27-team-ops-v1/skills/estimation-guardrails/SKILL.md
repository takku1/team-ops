---
name: estimation-guardrails
description: Counter planning fallacy with reference classes and buffers.
---

# Estimation Guardrails

Use when dates slip or estimates look optimistic.

Prose: Hofstadter plus planning fallacy means work takes longer even after padding. Parkinson means work fills idle time. Counter with reference-class data, sliced chunks, explicit buffers, and Goodhart care: never let the metric become the target.

Logic:
- require past similar work or reference class exists
- slice until chunks are under two days
- attach buffer plus risk per chunk
- return estimate plus assumption list
