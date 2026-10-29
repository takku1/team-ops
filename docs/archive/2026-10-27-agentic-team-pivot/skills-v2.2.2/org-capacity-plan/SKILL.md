---
name: org-capacity-plan
description: Allocate people and work by real capacity, skills, and WIP limits, keeping teams small and stable. Use when distributing work across people or squads, planning a quarter, onboarding, or when someone is overloaded or a bus-factor risk appears. Not for date forecasting (use plan-estimate-forecast).
---

# Capacity Planning

## Policy
- **Plan at no more than ~70-80% of nominal capacity.** Reserve the rest for interrupts, support, review, and unplanned work. Track the real interrupt rate and tune this reserve with it.
- **WIP limit: 1-2 active items per person.** Finish before starting. Context switching is a cost, not a free resource.
- **Team size:** inspect coordination and expertise needs. Scrum recommends typically 10 or fewer; do not impose that limit on every team or count AI agents as independent human capacity.
- **Keep teams stable.** Move work to teams, not people to work. Each reshuffle resets the team toward forming.
- **Bus factor of at least 2** for every critical area. Pair, rotate, and write runbooks until it is met.
- **Reserve an explicit allocation for maintenance and tech debt** (commonly 15-25%). Do not let it be "whatever is left".
- Assign by skill fit *and* growth. Give stretch work a named reviewer or mentor.

## Logic
1. Require: people with availability (PTO, on-call, % allocation), skill tags, and the ranked work list.
2. Compute available hours after leave and fixed duties; subtract measured support/review reserves once. If a focus factor already includes interrupts, do not subtract them again. Show units and assumptions.
3. Assign the top-ranked work first by fit. Stop at the capacity line and do not cram.
4. Flag: anyone over their WIP cap or above 100% effective load, skills held by only one person, coordination overload, and work above the line that has no owner.

## Output
- Allocation table: person | effective capacity | assigned | load %
- Below-the-line list (explicitly deferred)
- Risks: overload, single points of knowledge, and the mitigation for each

## Pitfalls
- Planning to 100% and calling the overflow "stretch goals".
- Using individual output metrics to balance load (see measure-delivery-health).
- Treating team-role personality models (e.g. Belbin) as hard constraints. The evidence for them is mixed, so use them only for discussion.

## Sources
Scrum Guide 2020 (team size); Reinertsen, *Principles of Product Development Flow* (queues, WIP); Skelton & Pais, *Team Topologies* (cognitive load, stable teams).

## Research and application

The 70-80% allocation, 1-2 WIP, 15-25% maintenance, and two-person backup numbers are starting hypotheses. Measure interrupts, queue delay, skill coverage, and reviewer capacity. AI concurrency consumes integration and review capacity; it does not multiply throughput automatically.

Evidence: R05, R08; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
