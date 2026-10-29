---
name: org-team-topology
description: Shape team boundaries, team types, and interaction modes so the org chart produces the architecture you want (Conway's Law, Inverse Conway, Team Topologies). Use when handoffs between teams are slow, a service has no clear owner, a re-org or new service is planned, or a stream-aligned team is overloaded. Not for assigning individual tasks (use org-capacity-plan).
---

# Team Topology

Organizational communication and technical dependencies often correspond (R03); the relationship is not deterministic. Inspect both before proposing changes, and test whether a boundary change reduces coordination cost.

## Policy
- **Name an accountable team or person for each service or bounded context.** Shared contributors are useful when decision rights and support responsibilities are explicit.
- **Use Team Topologies as an optional vocabulary:** stream-aligned, platform, enabling, or complicated-subsystem. Mixed responsibilities are a diagnostic question, not automatically a defect.
- **Declare one interaction mode per team pair**: *collaboration* (time-boxed, high bandwidth), *X-as-a-service* (clear API, low bandwidth), or *facilitation* (enabling helps another team). Undeclared dependencies are defects.
- **Cognitive load is the sizing constraint.** If a stream-aligned team cannot own its domain without constant help, shrink the scope or add platform support. Do not add people first.
- **Review sustained collaboration:** it may reflect a legitimate dependency. Set a review point; change boundaries only with evidence of unnecessary coordination cost.

## Logic
1. Inspect available team ownership and architecture evidence. Ask only for missing facts that materially change the proposal; mark other gaps unknown and continue.
2. Build two graphs: who talks to whom (comms) and which component depends on which (deps).
3. Diff them. A dependency with no comms path means integration risk. Heavy comms with no dependency means a misplaced boundary or hidden coupling.
4. Classify team types and pair modes. Investigate mixed responsibilities, ambiguous service accountability, and collaboration without a review point; do not treat them as automatic defects.
5. Propose boundary moves. Each one names the owner, the reason, the expected comms reduction, and a review date.

## Output
- Topology table: team | type | owns | depends on (mode)
- Mismatch list: dependency or comms gap, then the proposed move and its owner
- Load risks: teams over cognitive budget, with the remedy

## Pitfalls
- A re-org that is only boxes on a chart, with no ownership or API change.
- A platform team that is really a ticket queue. It should be a self-service product.
- Splitting by tech layer (frontend/backend/DB) for stream work. That produces handoffs on every feature.

## Sources
Conway, "How Do Committees Invent?" (1968); MacCormack/Rusnak/Baldwin mirroring-hypothesis studies (HBS); Skelton & Pais, *Team Topologies* (2019, 2nd ed. 2025).

## Research and application

Treat reorganization as a hypothesis. Compare coordination delays and ownership clarity before/after, and consider changing interfaces before moving people. Team Topologies is a practitioner vocabulary, not a scientifically optimal taxonomy.

Evidence: R03, R04; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
