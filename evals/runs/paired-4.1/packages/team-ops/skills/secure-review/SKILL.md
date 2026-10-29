---
name: secure-review
description: "Security phase: threat-model a change (four questions, STRIDE, trust boundaries, prompt injection) and audit the dependencies and build chain it touches (advisories, waivers, secrets, SLSA, SBOM). Not for pentesting."
---

# Security Review

Review read-only. An optional security-reviewer worker provides independence when authorized and useful; ordinary work uses this checklist inline. Risk decisions follow existing user authority.

Model the change and the boundaries it crosses, not the whole system. Every gap cites a file, setting, or command output; a control you cannot inspect is **unknown**, never passing and never proven absent. Never edit code, CI, lockfiles, or waivers to turn a check green. Propose the change instead.

## Threat model (four questions)

1. **What are we working on?** A data-flow diagram (text or mermaid) of processes, stores, external entities, and flows, with **trust boundaries** marked.
2. **What can go wrong?** Walk each element and crossing with STRIDE: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. Where a model or agent is on the path, add prompt injection, tool-permission abuse, and exfiltration through outputs: trace how retrieved text, tool results, and repo content could reach a privileged action.
3. **What will we do?** Per threat: mitigate, eliminate, transfer, or accept. Acceptance is the user's call, with an owner and a reason. Enforce boundaries in tools and runtime; a stronger prompt is not a boundary.
4. **Did we do a good job?** Mitigations are implemented and tested, and the model matches what was built.

Rank by impact, exposure, exploitability, and uncertainty. These are ordinal judgments, not probabilities; cite the version if you use CVSS or ASVS. Output a threat table: id | element | STRIDE | threat | rank | response | file:line.

## Supply chain

For dependency, advisory, CI, or release-chain changes, read [the supply-chain checklist](references/supply-chain.md). For boundary changes use the four questions above; load both only when both apply.

Return grounded threats/advisory findings, proposed responses, unknowns, and blocking issues. Route repairs to the implementation owner. Use current check evidence or request a targeted check; do not independently restart a full build merely to complete this role.

Evidence: P06 (Four Question Framework), P05 (NIST SSDF 1.1, SLSA 1.2), R20 (indirect prompt injection); Shostack, *Threat Modeling* (2014); OWASP ASVS and Top 10 for LLM Applications. [Register](../../references/research-evidence.md).
