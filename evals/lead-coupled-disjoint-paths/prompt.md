---
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill]
---

The user permits parallel workers. Task A changes an API response in server/session.rs. Task B changes the consumer in web/session.ts. A shared wire schema and generated client must change too. The old and new wire formats are incompatible. Plan ownership and useful parallel work. Filenames A and B are disjoint.
