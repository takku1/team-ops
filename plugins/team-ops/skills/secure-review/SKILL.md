---
name: secure-review
description: "Use for security questions about a change or its supply chain: threat models, trust boundaries, prompt injection, dependency advisories, waivers, secrets, SLSA levels, SBOMs, provenance. Not pentesting."
---

# Security Review

Model the change and the boundaries it crosses, not the whole system, read-only. Run inline by default; an optional reviewer worker in security mode adds independence when authorized and useful. Risk decisions follow existing user authority.

**Return:** grounded threats and advisory findings, proposed responses, unknown controls, and blocking issues. Repairs go to the implementation owner.

## Ground rules

- Every gap cites a file, setting, or command output.
- A control you cannot inspect is **unknown**: never passing, never proven absent.
- Never edit code, CI, lockfiles, or waivers to turn a check green; propose the change.
- Use current check evidence or request a targeted check; do not restart a full build just to complete this review.

## Threat model: four questions

1. **What are we working on?** A data-flow diagram (text or mermaid) of processes, stores, external entities, and flows, with **trust boundaries** marked.
2. **What can go wrong?** Walk each element and crossing through STRIDE: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. Where a model or agent is on the path, add prompt injection, tool-permission abuse, and exfiltration through outputs: trace how retrieved text, tool results, and repo content could reach a privileged action.
3. **What will we do?** Per threat: mitigate, eliminate, transfer, or accept. Acceptance is the user's call, with an owner and a reason. Enforce boundaries in tools and runtime; a stronger prompt is not a boundary.
4. **Did we do a good job?** Mitigations are implemented and tested, and the model matches what was built.

Rank by impact, exposure, exploitability, and uncertainty: ordinal judgments, not probabilities. Cite the version if you use CVSS or ASVS. Output `id | element | STRIDE | threat | rank | response | file:line`.

## Supply chain

For dependency, advisory, CI, or release-chain changes, load [the supply-chain checklist](references/supply-chain.md). Use both modes only when both apply.

Evidence: P05, P06, P09, R20 ([register](../../references/research-evidence.md)).
