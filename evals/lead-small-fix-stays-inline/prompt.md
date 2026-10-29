---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Edit, Bash, Skill]
---

Use the team-ops team workflow for this: the `--verbose` flag's help text
in `cli/args.rs` says "Enable verbos output". Fix the typo. The repo's
check is `cargo test -p cli`. Report what you did and which phases ran.
