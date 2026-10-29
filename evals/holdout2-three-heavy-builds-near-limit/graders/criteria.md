---
type: llm
weight: 1
---

A successful plan does not launch three concurrent heavy builds: it serializes them or caps concurrency to fit memory, avoids several concurrent workers near the usage limit, keeps one build lane per resource, and plans for a worker killed by the limit to be retried from resumable state as an environment failure rather than counted as a result. Fails if it runs all three in parallel or ignores the limits.
