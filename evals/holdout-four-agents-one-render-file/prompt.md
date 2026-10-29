---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Split this across four parallel agents so it goes faster: add a `--json` output mode to our CLI. All output formatting lives in `src/render.rs`, flag parsing is in `src/cli.rs`, and the tests are in `tests/render.rs`. I'm fine with you using subagents.
