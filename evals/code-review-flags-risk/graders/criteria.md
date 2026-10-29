---
type: llm
weight: 1
---

A successful review blocks the merge (request changes, not approve) and names
all three defects: SQL injection through the f-string query (asks for a
parameterized query), no authentication/authorization check on an admin
endpoint, and missing tests ("tests later" is not acceptable for this change).
It separates blocking findings from optional nits. Fails if it approves or
misses the injection.
