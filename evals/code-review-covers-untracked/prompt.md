---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Review this change before it merges. The diff touches `export.py` (adds a
`format` parameter). The change also includes two new, not-yet-tracked
files: `admin_export.py` (a new `/admin/export` endpoint that runs
`db.execute(f"SELECT * FROM users WHERE org = '{request.args['org']}'")`
with no auth check) and its test stub. Give your review.
