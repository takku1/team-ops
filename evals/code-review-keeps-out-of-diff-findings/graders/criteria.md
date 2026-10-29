---
type: llm
weight: 1
---

A successful review reports the stale `docs/operations.md:42` instruction
as a labeled finding grounded in both the changed line (the renamed key
in `client.py`/`defaults.toml`) and the unchanged location it leaves
inconsistent, and still reports its findings on the diff itself. The
verdict matches the impact (request changes or approve with a required
doc follow-up), with reasons. Fails if it drops the out-of-diff finding
because it is not on a changed line, discards all findings, or reports
nothing.
