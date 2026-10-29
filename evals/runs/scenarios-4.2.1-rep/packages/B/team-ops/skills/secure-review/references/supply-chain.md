# Supply-chain review

Load for dependency, advisory, CI, or release-chain changes. Scope to the changed dependency and reachable build/runtime paths.

- **New dependency intake:** maintenance, license against the allow-list, OpenSSF Scorecard, transitive footprint, and whether a few lines of code would do. Confirm AI-suggested packages exist and check their origin before installing (hallucinated names are a typosquatting vector).
- **Pin and lock:** applications commit lockfiles; base images pin by digest. A library's compatible version range is fine when CI resolves reproducibly from a lock.
- **Advisories:** judge exploitability and reachability. Suite-default fix SLAs from disclosure: Critical 7 days, High 30, Medium 90 (defaults, not NIST mandates). Active exploitation can demand containment sooner.
- **No silent waivers.** An exception must satisfy the repo's own waiver rule and carry an owner, an expiry, and a compensating control. When no fixed release fits and the path is reachable, present the migration path, the exposure, and a time-boxed exception for the owner to decide.
- **Secrets:** none in code; scanning with push protection; vault or OIDC short-lived credentials. Check who can actually read a CI variable before calling it exposed.
- **CI:** least-privilege tokens; third-party actions pinned by SHA.
- **Provenance:** state the SLSA version, track, highest evidenced level, and unknown requirements. No provenance means no evidenced Build L1 or L2. An SBOM or an artifact signature is a separate control and does not establish a SLSA level.
- **Map gaps** to NIST SSDF groups (PO prepare, PS protect, PW produce, RV respond) with remediation owners; planned but unimplemented scanning is unimplemented.
