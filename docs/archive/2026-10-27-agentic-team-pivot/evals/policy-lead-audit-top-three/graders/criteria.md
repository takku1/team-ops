---
type: llm
weight: 1
---

A successful answer scores each area on written / enforced / followed,
ranks gaps with security and reliability before flow (missing ownership
for reviews and no SLOs/alerts outrank the slow suite and the retro
follow-through), and returns at most 3 fixes, each with an owner, the
fixing skill, and effort — stopping at the blocking findings (no
accountable owner, no SLO for launch) rather than dumping every gap at
once. Fails if it lists more than 3 fixes, omits owners, or ranks the
slow suite above the missing SLOs.
