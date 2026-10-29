---
skill: secure-supply-chain
name: secure-supply-chain
description: "Audit and secure the build and dependency supply chain: dependency intake and updates, vulnerability SLAs, secret scanning, SBOMs, SLSA provenance, artifact signing, least-privilege CI, mapped to NIST SSDF. Use when adding a dependency, hardening CI/CD, responding to a CVE, or preparing a security review. Not for design-level threat analysis (use secure-threat-model)."
version: 0.5
accepts:
  repo: { type: Path, required: false }
  dependency: { type: Text, required: false }
produces:
  supply_chain_report: { type: Text, when: auditing a repo }
  intake_decision: { type: Text, when: reviewing a new dependency }
owns-when:
  - user wants to harden CI/CD or audit supply chain security
  - user wants to add a new dependency or package
  - user is responding to a CVE or vulnerability alert
requires:
  audit-supply-chain: [repo exists]
  review-dependency: [dependency exists]
flows: [audit-supply-chain, review-dependency]
authority:
  user-decides: []
  system-decides: [policy compliance per control, SLSA level reached, gap ranking, intake verdict]
  system-may: [propose CI and dependency config changes]
  system-must-not: [change repo files or CI config, report a gap without file evidence]
effects:
  reads: [repository]
  creates: []
  mutates: []
risk: low
cost: moderate
budget: { header: 400, body: 2500 }
---

# Supply Chain and Secure Build

```contract
resources:
  repository:
    path: manifests, lockfiles, CI config, secrets handling, and release artifacts
    access: read
    immutable: true
always:
  rank gaps by exploitability and blast radius
  map each control to its NIST SSDF group
  give every remediation an owner
never:
  change repository files or CI config
  report a gap without file or setting evidence
  treat an unavailable check as passing
```

```logic
audit-supply-chain:
  require repo exists
    otherwise:
      abort with "A repository is required for a supply chain audit."

  read manifests, lockfiles, CI config, secrets handling, and release artifacts from repository as inventory
    otherwise:
      abort with "Could not read the repository build inputs."

  apply policy scoring with inventory as scores

  verify every gap cites the file or setting it rests on
    otherwise:
      apply evidence pass with scores as scores
      retry

  generate ranked gaps with SLSA level and SSDF group from scores as gaps
  generate proposed CI and dependency config changes for update bots, scanners, branch protection, OIDC, signing, and SBOM steps with remediation owners from gaps as report

  verify report contains SLSA level, ranked gaps, config changes, and remediation owners
    otherwise:
      generate proposed CI and dependency config changes for update bots, scanners, branch protection, OIDC, signing, and SBOM steps with remediation owners from gaps as report
      retry

  return report as supply_chain_report
```

```logic
review-dependency:
  require dependency exists
    otherwise:
      abort with "Name the dependency to review."

  apply intake checks with dependency as intake

  verify intake covers maintenance, license, Scorecard, transitive footprint, and a few-lines alternative
    otherwise:
      apply intake checks with dependency as intake
      retry

  generate intake verdict of adopt, adopt with conditions, or reject from intake as verdict
  return verdict as intake_decision
```

## Appendix

### Policy: dependencies
- **Intake review for new direct dependencies:** maintenance activity, license compatibility, OpenSSF Scorecard, transitive footprint, and whether a few lines of code would do instead.
- **Pin and lock** with lockfiles committed. Container base images pinned by digest.
- **Automated updates** (Dependabot or Renovate), with grouped minor and patch updates merged weekly when CI is green.
- **Proposed vulnerability fix SLAs** (suite defaults, not NIST requirements; from disclosure for issues exploitable in context): Critical 7 days · High 30 days · Medium 90 days · Low best effort. Exceptions need an owner, an expiry date, and a compensating control, and must meet the repository's own waiver rule (for example, a required unreachability argument). When no fixed release fits and the vulnerable path is reachable, do not waive it to turn CI green: present the upgrade or migration path, the exposure, and a time-boxed exception for the owner to decide.
- **License policy:** keep an allow-list (e.g. MIT, Apache-2.0, BSD). Copyleft needs legal review.

### Policy: build and CI
- **No secrets in code.** Secret scanning with push protection, and secrets come from a vault or OIDC short-lived credentials.
- **Least-privilege CI tokens** (read-only by default). Third-party CI actions are pinned to a commit SHA.
- **SLSA Build L2 as baseline** for this suite's released-artifact policy, when adopted (hosted build platform, signed provenance). Aim for L3 (hardened, isolated builds) for released artifacts.
- **Build once, sign, and promote.** Sign artifacts (e.g. Sigstore cosign) and verify the signatures at deploy.
- **Generate an SBOM** (SPDX or CycloneDX) per release artifact and store it with the artifact.
- SAST and dependency scanning are required PR checks (build-definition-of-done).

### NIST SSDF SP 800-218 groups
**PO** Prepare the Organization: roles, training, tooling, this policy · **PS** Protect the Software: code and artifact integrity, access control, provenance · **PW** Produce Well-Secured Software: threat modeling, secure review, testing · **RV** Respond to Vulnerabilities: intake, triage, fix SLAs, root cause, disclosure (publish a `SECURITY.md`).

### Step meanings
- **policy scoring**: score the inventory against every policy line above and the SLSA level. Mark controls you cannot check as unknown, never as passing.
- **evidence pass**: attach the file path or setting to each gap. If evidence is unavailable, report an unknown control and its inspection limit, not an established absence or a silent pass.
- **intake checks**: evaluate the dependency on each intake criterion, plus its license against the allow-list and any open vulnerabilities against the fix SLAs.

Sources: docs/current/research.md in the team-ops pack.

## Research and application

State SLSA version, track, highest evidenced level, and unknown requirements. An SBOM or artifact signature alone does not establish SLSA Build L2. An unlocked application dependency differs from a library version range with a reproducible CI lock. Check exploitability/exposure; active exploitation can demand containment before the default SLA. Verify AI-suggested packages exist and their origin before installation.

Evidence: P05, R20; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
