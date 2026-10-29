---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Review this change before it merges. The diff renames the config key
`retry_limit` to `max_retries` in `client.py` (the reader) and
`defaults.toml`, and adds a test for the new key. `docs/operations.md`
is not in the diff; line 42 still tells operators to set `retry_limit`
to tune retries. The code change itself is correct. Give your review.
