# Error analysis of real sessions (2026-10-29)

Method: open coding of compact timelines (user turns, suite loads, tool errors) extracted from every local Claude Code and Codex session that used the suite outside this repository. Field-test subagent sessions run from this repo were excluded as development, not use.

**Sample:** 3 sessions: Claude Code in MochiOS (team-ops 3.x, team-lead loaded, three workers spawned), Codex in MochiOS and in chilicrisp (no plugin; the suite was read from the source checkout). Far below the 30-50 traces the method recommends (R33); treat these as leads, not rates.

| Code | Observed | Evidence | Status in 4.2.1 |
|---|---|---|---|
| Shared host limits | Two parallel investigators were killed by the account usage limit; RAM filled ("why is my memory full?"); a rebuild was killed for low memory | Claude MochiOS | New team-lead rule: workers share usage limit, memory, CPU, build locks; serialize heavy builds; a limit kill is an environment failure |
| Duplicate builds | "the other agent was compiling multiple things over and over" | Claude MochiOS | Covered since 4.0 (one final verifier, focused checks, runner) |
| Build-lane collision | `failed to remove ... xtask.exe: Access is denied` while another build ran | Claude MochiOS | Covered (never reuse another session's lane; one writer per scope) |
| Worker returned with background work running | Reviewer reported "waiting on its own background work" | Claude MochiOS | New coordination rule: finish or hand back background jobs before reporting |
| Non-plugin discovery | Codex grepped the repo for AGENTS.md/SKILL.md/README and read up to 175 README lines before a skill | Codex MochiOS, chilicrisp | README rewritten as a router: skill paths first, ~40 lines |

The same two environment failures (usage-limit kills and memory reaps) also hit this session's scenario runs; the harness now retries limit failures instead of recording them.
