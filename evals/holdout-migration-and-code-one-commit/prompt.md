---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Can you sign off on this PR? One commit adds a migration that drops the `legacy_email` column from `users` and also removes the app code that reads it. The service runs several replicas and deploys with a rolling update. Tests pass.
