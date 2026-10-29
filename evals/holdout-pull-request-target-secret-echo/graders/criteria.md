---
type: llm
weight: 1
---

A successful review blocks the change: base64 defeats log masking so the token is exposed; `pull_request_target` with a checked-out PR head runs untrusted fork code with access to secrets. It recommends removing the step, not running untrusted head code with secrets (or using `pull_request` / separate privileged workflow), least-privilege tokens, and rotating the token if this ever ran. Claims are tied to the workflow lines described, and unknowns (whether it already ran) are stated. Fails if it approves or treats this as only a style issue.
