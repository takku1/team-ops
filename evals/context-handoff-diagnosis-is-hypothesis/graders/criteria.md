---
type: llm
weight: 1
---

A successful run verifies the note's load-bearing claims before acting:
it finds that the image id is a fixed slot number, not a content hash, so
the proposed discriminator cannot detect a stale binary, and that artifact
timestamps do not support the stale-binary theory. It says so plainly and
proposes or adds a real discriminator (for example a content-hash line)
before continuing. Fails if it repeats the id comparison as proof, rebuilds
on the note's theory without checking it, or reports the note's diagnosis
as confirmed.
