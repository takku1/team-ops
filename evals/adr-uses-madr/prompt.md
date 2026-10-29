---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We decided to move our job queue from Redis lists to Postgres (SKIP LOCKED),
because we already run Postgres, need transactional enqueue with our writes,
and our volume is ~200 jobs/s. We considered RabbitMQ and SQS. Write the
decision record.
