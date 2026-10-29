---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

A new AI billing workflow sends charges to an external provider. Our 1% canary got two requests in 30 minutes, both HTTP 200. Rollback restores old code but cannot undo charges. Is it safe to ramp to 100%?
