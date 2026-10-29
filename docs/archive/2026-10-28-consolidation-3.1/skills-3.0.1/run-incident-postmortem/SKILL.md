---
name: run-incident-postmortem
description: Run incident response roles and write blameless postmortems with a timeline, impact, contributing factors, and owned, prioritized action items (Investigate / Mitigate / Repair / Detect / Prevent). Also writes failure-log entries for agent-team runs that went wrong. Use during or after an outage, data loss, security event, near miss, or any SLO-burning incident, when a team run loops or accepts a wrong diagnosis, or when defining incident and postmortem policy. Not for routine bug triage.
---

# Incidents and Blameless Postmortems

**Role:** lead (team-lead), for live product incidents and for agent-team runs that went wrong. **Returns:** a blameless review with owned, verifiable actions, or a failure-log entry.

## Agent-team failures

Review a run that went wrong (a loop that burned the budget, a wrong diagnosis accepted, a blocking issue review or verification missed, a write outside scope, a disturbed lane) the same blameless way. Look for the system factor, not "the agent was wrong": a brief without the ruled-out list, a reviewer handed the implementer's narrative, a missing oracle, an unchecked handed-over diagnosis, no stop after rounds with no new evidence, an unguarded shared path.

A **failure-log entry** has: date; task; what happened and its impact (cost, rework, user time); how it was detected; contributing factors; and one or two actions, each changing something checkable (a brief template, role definition, playbook, eval case, or repo brief) with how you will know it worked. Store it in the repository's tracker or status file if it has one, otherwise in the lead's notes, and offer to persist it. The lead reads recent entries at the start of the next run. A failure that repeats becomes an eval case (ai-evaluation).

## Live incidents

1. **Declare early, downgrade freely.** Severity levels are defined in advance (e.g. SEV1 major user impact or data loss, SEV2 partial or degraded, SEV3 minor).
2. **Assign roles:** Incident Commander (coordinates and decides, does not debug), tech lead (hands on the system), comms (status page, stakeholders), scribe (timestamped timeline). Small teams combine roles, but the IC is always explicit.
3. **Mitigate first, root-cause later:** roll back, fail over, shed load, or flip the kill switch (ship-release-rollout). Preserve evidence before changing systems. For AI incidents, capture model, prompt, tool, and data versions and redacted traces.

## Postmortems

**Triggers (defined beforehand):** user-visible downtime or degradation past a threshold · any data loss · on-call intervention · resolution time past a threshold · a human found it before the alerts did · one incident using more than 20% of the error budget (run-slo-error-budget) · any stakeholder request.

**Blameless, not ownerless.** Name contributing factors in systems and processes. Assume people acted reasonably given what they knew. Rewrite blame language ("X forgot", "human error") toward the system factor.

**Template:** summary · impact (users, duration, budget burned, cost) · detection (how, how fast) · timeline (UTC) · contributing factors (several, from asking how and why, not one root cause) · what went well · what went poorly · where we got lucky · action items.

**Action items** each have an owner, priority, due date, tracking reference, and a check that shows the action worked; ticket closure alone is not effectiveness. Investigate / Mitigate / Repair / Detect / Prevent are useful categories, not quotas, and P0 is assigned by impact, not to fill a template. Draft within 2 business days and review within 5 (suite defaults). Track completion, review overdue P0 items weekly, and keep a searchable archive.

Evidence: Google SRE Book ch. 14–15 and Workbook ch. 10; PagerDuty Incident Response docs; Allspaw, "Blameless PostMortems and a Just Culture" (2012). R07 (psychological safety and learning; transfer to software is an inference), R16. See the [research register](../../docs/current/research-evidence.md).
