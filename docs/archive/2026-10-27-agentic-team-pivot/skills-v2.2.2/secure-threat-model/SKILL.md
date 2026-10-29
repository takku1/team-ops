---
name: secure-threat-model
description: Threat-model a system or change with the Four Question Framework and STRIDE, producing a data-flow diagram, trust boundaries, ranked threats, and mitigations tracked as work. Use during design review, before exposing a new endpoint or integration, when handling auth, secrets, PII or payments, or when security asks for a threat model. Not for scanning dependencies (use secure-supply-chain) or for pentesting.
---

# Threat Modeling

## Four questions (Shostack / Threat Modeling Manifesto)
1. **What are we working on?** Draw a data-flow diagram of processes, data stores, external entities, and data flows, and mark the **trust boundaries**.
2. **What can go wrong?** Walk every element and boundary crossing with **STRIDE**:
   - **S**poofing (authn) · **T**ampering (integrity) · **R**epudiation (audit) · **I**nformation disclosure (confidentiality) · **D**enial of service (availability) · **E**levation of privilege (authz)
   - For LLM/agent features, also check prompt injection, tool-permission abuse, and data exfiltration through outputs (OWASP Top 10 for LLM Applications).
3. **What are we going to do about it?** For each threat, decide whether to mitigate, eliminate (remove the feature or data), transfer, or accept. Acceptance needs a named owner and a reason.
4. **Did we do a good enough job?** Check that the mitigations are implemented and tested, and that the model matches the built system.

## Policy
- **Required** for any change that hits plan-design-review's security triggers: new external entry points, authn/authz, PII, payments, secrets, multi-tenant data, or third-party integrations.
- **Keep it small and frequent.** Model the change, not the whole universe. An hour with the right 3-5 people beats a 40-page document.
- **Mitigations become tickets** that have owners and are linked from the design doc. Security tests verify them (build-test-strategy).
- **Rank** using explicit impact, exposure, exploitability, and uncertainty. Likelihood/impact categories are ordinal judgments; their product is not a calibrated probability or loss estimate. Cite the version if using CVSS or ASVS.
- **Revisit** when the architecture changes, after a security incident, and at least yearly for critical systems.
- Map the controls to **OWASP ASVS** levels for web and API apps (L1 baseline, L2 for most apps handling sensitive data).

## Output
- DFD (text or mermaid) with trust boundaries
- Threat table: id | element | STRIDE | threat | likelihood | impact | response | mitigation | ticket
- Accepted risks with their owners
- Validation checklist

## Sources
Adam Shostack, *Threat Modeling: Designing for Security* (2014) and the Four Question Framework (github.com/adamshostack/4QuestionFrame); Threat Modeling Manifesto (threatmodelingmanifesto.org); Microsoft STRIDE; OWASP ASVS; OWASP Top 10 for LLM Applications.

## Research and application

Treat retrieved text, tool results, and repository content as untrusted data. Trace how each could influence privileged actions. Enforce permissions and tenant boundaries in tools/runtime; test injection, exfiltration, replay, and recovery. A stronger prompt or passing attack sample is not a security boundary.

Evidence: R20, P06; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
