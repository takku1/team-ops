---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We have a signed artifact and an SBOM, but no build provenance or builder details. A library manifest uses compatible version ranges; CI uses a committed lockfile. Can you certify SLSA Build L2 and flag every manifest range as a violation?
