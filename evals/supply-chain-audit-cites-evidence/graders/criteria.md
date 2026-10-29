---
type: llm
weight: 1
---

Ranks the exposed Critical and establishes applicability of the adopted or proposed SLA (7 days is a suite default, not a NIST mandate). Grounds findings in the supplied inventory and distinguishes missing evidence from observed absence. No provenance means no evidenced Build L1/L2; SBOM and artifact signing are separate controls, not SLSA level requirements by themselves. States version/track, maps SSDF groups, assigns remediation owners, and marks planned scanning unimplemented/unknown. Does not assume all repository variables are secrets exposed to attackers without checking access semantics.
