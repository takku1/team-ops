---
name: secure-supply-chain
description: Secure the build and dependency supply chain with a dependency intake and update policy, vulnerability SLAs, secret scanning, SBOMs, SLSA build provenance, artifact signing, and least-privilege CI, mapped to NIST SSDF. Use when adding a dependency, hardening CI/CD, responding to a CVE, preparing for a security or compliance review, or defining a secure development policy. Not for design-level threat analysis (use secure-threat-model).
---

# Supply Chain and Secure Build

## Policy
**Dependencies**
- **Intake review for new direct dependencies:** maintenance activity, license compatibility, OpenSSF Scorecard, transitive footprint, and whether a few lines of code would do instead.
- **Pin and lock** with lockfiles committed. Container base images pinned by digest.
- **Automated updates** (Dependabot or Renovate), with grouped minor and patch updates merged weekly when CI is green.
- **Vulnerability fix SLAs** (from disclosure, for issues exploitable in context): Critical 7 days · High 30 days · Medium 90 days · Low best effort. Exceptions need an owner, an expiry date, and a compensating control.
- **License policy:** keep an allow-list (e.g. MIT, Apache-2.0, BSD). Copyleft needs legal review.

**Build and CI**
- **No secrets in code.** Secret scanning with push protection, and secrets come from a vault or OIDC short-lived credentials.
- **Least-privilege CI tokens** (read-only by default). Third-party CI actions are pinned to a commit SHA.
- **SLSA Build L2 as baseline** (hosted build platform, signed provenance). Aim for L3 (hardened, isolated builds) for released artifacts.
- **Build once, sign, and promote.** Sign artifacts (e.g. Sigstore cosign) and verify the signatures at deploy.
- **Generate an SBOM** (SPDX or CycloneDX) per release artifact and store it with the artifact.
- SAST and dependency scanning are required PR checks (build-definition-of-done).

**Process (NIST SSDF SP 800-218 practice groups)**
- **PO** Prepare the Organization: roles, training, tooling, this policy.
- **PS** Protect the Software: code and artifact integrity, access control, provenance.
- **PW** Produce Well-Secured Software: threat modeling, secure review, testing.
- **RV** Respond to Vulnerabilities: intake, triage, fix SLAs, root cause, disclosure (publish a `SECURITY.md`).

## Logic
1. Inventory the manifests, lockfiles, CI config, secrets handling, and release artifacts.
2. Score against the policy and the SLSA level, and list the gaps ranked by exploitability and blast radius.
3. Emit config changes (update bot, scanners, branch protection, OIDC, signing step, SBOM step) and a remediation plan with owners.

## Sources
NIST SP 800-218 (SSDF v1.1); SLSA v1.0 specification (slsa.dev); OpenSSF Scorecard and "Concise Guide for Evaluating Open Source Software"; CISA SBOM guidance; Sigstore docs; GitHub secret scanning and push protection docs.
