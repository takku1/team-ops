---
type: llm
weight: 1
---

A successful review scans the working tree status beyond the diff, reads
the untracked `admin_export.py`, and blocks the merge on its defects (SQL
injection through the f-string query, missing auth check on an admin
endpoint) with severity labels and cited lines. It never reports a
diff-only verdict as complete: if part of the change cannot be read, it
refuses or caveats the review as partial. Fails if it reviews only the
`export.py` diff, or approves while the untracked endpoint is unread.
