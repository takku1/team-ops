---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

A team run went badly. Another session handed over a diagnosis ("stale
app image embedded in the kernel; compare image IDs to confirm"). The
implementer accepted it and spent three rounds rebuilding images, and the
failure never changed. It later turned out that image IDs are slot
numbers that repeat across builds, so they could never tell a stale image
from a fresh one. Write up what the team should take from this.
