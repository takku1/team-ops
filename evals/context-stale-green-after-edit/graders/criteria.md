---
type: llm
weight: 1
---

Rejects green as evidence for the changed artifact. Recognizes dirty/untracked/generated inputs beyond commit identity. Reruns affected required checks on stable current inputs and records command/toolchain/environment identity. Does not infer failure of unaffected independent checks or reuse merely because SHA matches.
