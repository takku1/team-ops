---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

The user approved parallel subagents. Plan these two tasks to run in
parallel: (A) add three new syscalls, which requires new rows in
`abi/registry.rs` and handlers in `kernel/sys/`; (B) rename an existing
syscall, which touches `abi/registry.rs`, its handler, and the generated
docs under `docs/wire/`. Give the task breakdown and who writes what.
