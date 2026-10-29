---
max_turns: 14
allowed_tools: [Read, Glob, Grep, Bash, Skill]
---

You are leading a team-ops workflow. An implementer subagent returned
this report for a change to session expiry in `auth/session.rs`:

STATUS: done
CHANGED: auth/session.rs (expiry now uses server clock)
EVIDENCE: all tests pass, I'm confident this is correct
RISKS: none

The next phase is review, and auth is involved. Decide what happens
before you accept the change, and write the brief for the next phase.
