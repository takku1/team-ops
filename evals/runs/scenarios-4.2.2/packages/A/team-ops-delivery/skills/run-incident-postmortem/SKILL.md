---
name: run-incident-postmortem
description: "Run a live incident (roles, mitigate first) and write a blameless postmortem with contributing factors and owned, verifiable actions. Use after outages, data loss, security events, or near misses."
---

# Incidents and Blameless Postmortems

Mitigate live incidents first, then learn from them without blame. Failed agent runs use team-lead's failure record instead; a routine failed check is not an incident.

**Return:** during an incident, severity, roles, and the mitigation path; afterwards, a blameless review with owned, verifiable actions.

## Live incident

1. **Declare early, downgrade freely,** using severity levels defined in advance (e.g. SEV1 major user impact or data loss, SEV2 partial or degraded, SEV3 minor).
2. **Assign roles:** Incident Commander (coordinates and decides; does not debug), tech lead (hands on the system), comms (status page, stakeholders), scribe (timestamped timeline). Small teams combine roles under one explicit coordinator. These are responsibilities, not four agents to spawn. Messaging others requires existing authorization.
3. **Mitigate first, root-cause later:** roll back, fail over, shed load, or flip the kill switch (ship-release-rollout). Preserve evidence before changing systems. AI incidents also capture model, prompt, tool, and data versions and redacted traces.

## Postmortem

**Triggers** (defined beforehand): user-visible downtime or degradation past a threshold · any data loss · on-call intervention · resolution time past a threshold · a human found it before the alerts did · one incident using more than 20% of the error budget (run-slo-error-budget) · any stakeholder request.

**Blameless, not ownerless.** Name contributing factors in systems and processes, assume people acted reasonably given what they knew, and rewrite blame language ("X forgot", "human error") toward the system factor.

**Template:** summary · impact (users, duration, budget burned, cost) · detection (how, how fast) · timeline (UTC) · contributing factors (several, found by asking how and why, not one root cause) · what went well · what went poorly · where we got lucky · action items.

**Action items** each carry an owner, priority, due date, tracking reference, and a check showing the action worked; closing the ticket is not proof of effect. Investigate / Mitigate / Repair / Detect / Prevent are useful categories, not quotas, and P0 follows impact, not the template. Draft within 2 business days and review within 5; track completion, review overdue P0s weekly, and keep a searchable archive.

**Before returning, verify:** no blame language remains; contributing factors are plural; every action has owner, priority, due date, tracking reference, and an effectiveness check.

Evidence: P08, R07, R16, R34; deadlines are suite defaults ([register](../../references/research-evidence.md)).
