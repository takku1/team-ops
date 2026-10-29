---
type: llm
weight: 1
---

A successful answer is a decision record in MADR shape: title, status, context
and problem statement, decision drivers, the considered options (Redis lists,
Postgres SKIP LOCKED, RabbitMQ, SQS), the decision outcome with its
justification, and consequences including at least one honest negative (e.g.
added load on the primary database, throughput ceiling). Fails if options are
missing or no downside is recorded.
