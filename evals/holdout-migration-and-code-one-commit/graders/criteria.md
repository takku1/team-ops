---
type: llm
weight: 1
---

A successful review does not approve as-is: it identifies that dropping the column in the same deploy as the code change breaks old replicas during a rolling update, and asks for expand/migrate/contract sequencing (stop reading first, drop later) or an equivalent safe split. Findings carry severity labels (the ordering issue is blocking) and a verdict such as request-changes or split-required. It does not treat passing tests as proof of rollout safety. Fails if it approves, or if it only comments on style.
