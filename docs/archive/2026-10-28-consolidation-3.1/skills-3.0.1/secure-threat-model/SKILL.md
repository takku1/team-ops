---
name: secure-threat-model
description: Threat-model a system or change with the Four Question Framework and STRIDE, producing a data-flow diagram, trust boundaries, ranked threats, and mitigations tracked as work. Use during design review, before exposing a new endpoint or integration, when handling auth, secrets, PII or payments, or when security asks for a threat model. Not for scanning dependencies (use secure-supply-chain) or for pentesting.
---

# Threat Modeling

**Role:** security-reviewer (agents/security-reviewer.md), run inline by the lead unless a subagent was approved. **Returns:** the security-reviewer handoff report with a DFD and a threat table.

## The four questions

1. **What are we working on?** Draw a data-flow diagram of processes, data stores, external entities, and flows, and mark the **trust boundaries**. Model the change and the boundaries it crosses, not the whole system.
2. **What can go wrong?** Walk every element and boundary crossing with **STRIDE**: **S**poofing (authn) · **T**ampering (integrity) · **R**epudiation (audit) · **I**nformation disclosure · **D**enial of service · **E**levation of privilege (authz). Where a model or agent sits on the path, add prompt injection, tool-permission abuse, and exfiltration through outputs (OWASP Top 10 for LLM Applications): trace how retrieved text, tool results, and repository content could reach a privileged action.
3. **What are we going to do about it?** For each threat: mitigate, eliminate (remove the feature or data), transfer, or accept. Acceptance is the user's decision, with a named owner and a reason.
4. **Did we do a good enough job?** Check that the mitigations are implemented and tested (build-test-strategy) and that the model matches what was built.

## Policy

- **Required** when a change hits plan-design-review's security triggers: new external entry points, authn or authz, PII, payments, secrets, multi-tenant data, third-party integrations, or agent tool permissions.
- **Small and frequent.** A threat model of one change beats a 40-page document of the system.
- **Rank** by impact, exposure, exploitability, and uncertainty. These are ordinal judgments; their product is not a probability or a loss estimate. Cite the version if you use CVSS or ASVS.
- **Enforce boundaries outside the model.** Permissions and tenant checks live in tools and runtime. A stronger prompt or a passing attack sample is not a security boundary; test injection, exfiltration, replay, and recovery.
- **Mitigations become tracked work** with owners, linked from the design note.
- **Revisit** when the architecture changes, after a security incident, and at least yearly for critical systems. Map web and API controls to OWASP ASVS (L1 baseline, L2 for sensitive data).

## Output

- DFD (text or mermaid) with trust boundaries
- Threat table: id | element | STRIDE | threat | rank | response | mitigation | file:line or ticket
- Accepted risks with owners
- Validation checklist

Evidence: Shostack, *Threat Modeling: Designing for Security* (2014); Threat Modeling Manifesto; Microsoft STRIDE; OWASP ASVS and Top 10 for LLM Applications. P06 (Four Question Framework), R20 (indirect prompt injection). See the [research register](../../docs/current/research-evidence.md).
