---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Threat model this feature: a desktop app can paste from a system clipboard.
Any app can copy; paste is only served to the app that owns keyboard focus.
The desktop shell can send "paste" commands to a window's app. Clips may hold
passwords copied from a password manager.
