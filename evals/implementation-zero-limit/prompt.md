---
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill, Bash, Edit, Write]
---

Use build-implementation-loop to fix parse_limit: integer zero is valid but currently becomes 20. Work on the supplied fixture copied to an isolated workspace. Preserve the default for None and the rejection of negative values. Run the relevant tests and report observed results.
