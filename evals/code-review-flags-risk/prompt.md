---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Review this pull request before it merges. It adds a `/admin/export` endpoint:

```python
@app.route("/admin/export")
def export():
    rows = db.execute(f"SELECT * FROM users WHERE org = '{request.args['org']}'")
    return jsonify([dict(r) for r in rows])
```

The PR description says "quick export for support, tests later". Give your review.
