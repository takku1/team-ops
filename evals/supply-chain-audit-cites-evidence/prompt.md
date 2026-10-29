---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Audit our supply chain before the security review. Facts: `package.json`
pins nothing (ranges everywhere, no lockfile committed); CI has no
secret scanning or push protection (keys live in repo vars); dependency
scanning is "planned" but not configured; a Critical CVE in a direct
dependency was disclosed 30 days ago and is still open; releases ship
with no SBOM, no signatures, and no provenance; third-party CI actions
float on major tags. Give the audit verdict.
