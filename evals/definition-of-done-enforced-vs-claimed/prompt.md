---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our Definition of Done says: approved review, CI green, no open
critical/high dependency findings, docs updated, deployed to staging and
smoke-tested. In practice: CI runs build and unit tests only (no lint,
no integration tests); dependency scanning is not configured at all; the
PR template has no docs checkbox; staging deploys are manual and often
skipped. Give us the DoD review.
