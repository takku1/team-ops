---
type: llm
weight: 1
---

A successful plan recognizes that the schema, migration, ORM model, and generated client form one coupled contract and keeps them with one owner (generated code regenerated, not hand-edited in parallel), uses safe migration sequencing (expand, migrate, contract) for a rename of a live column, and adds parallel agents only for genuinely independent work such as a read-only reviewer or call-site inventory. It explains the coupling briefly and keeps a deciding check. Fails if five agents write overlapping contract files in parallel or the migration renames the column in one step.
