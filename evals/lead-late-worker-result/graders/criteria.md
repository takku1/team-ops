---
type: llm
weight: 1
---

Does not advance or overwrite attempt 2 from the stale event. Records prior output as history and inspects artifacts. Recognizes reassignment was unsafe while old writes could continue; stops conflicting writes before resuming one owner. Timeout is not proof of stopped process. Deduplicates repeated completion and verifies current artifact before acceptance.
