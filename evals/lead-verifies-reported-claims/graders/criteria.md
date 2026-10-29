---
type: llm
weight: 1
---

A successful answer treats "all tests pass" as an unverified claim
because the report has no commands, exit status, or cites. It reruns the
relevant checks, or routes them to a verifier phase, before accepting.
Because the change touches auth, it adds a security phase. The review
brief stands alone: it gives the task, acceptance criteria, and target
(the diff and paths), and leaves out the implementer's confidence and
narrative. It does not accept the change, mark it done, or report it to
the user as done on the strength of the report. A subagent reviewer is
justified here but not required, if an inline review re-reads the diff
cold and obtains current observed check evidence through the assigned owner. It does not require duplicate full-suite execution by each role.
