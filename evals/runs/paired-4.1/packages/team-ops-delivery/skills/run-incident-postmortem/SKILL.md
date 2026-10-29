---
name: run-incident-postmortem
description: "Run a live incident (roles, mitigate first) and write a blameless postmortem with contributing factors and owned, verifiable actions. Use after outages, data loss, security events, or near misses."
---

# Incidents and Blameless Postmortems

**Role:** lead, for live product incidents. **Returns:** a blameless review with owned, verifiable actions.

Failure logs for agent-team runs that went wrong are in team-ops `team-lead`; they follow the same blameless rules as below. Keep software incidents and agent coordination failures distinct; do not start incident ceremony for routine failed checks.

## Live incidents

1. **Declare early, downgrade freely.** Severity levels are defined in advance (e.g. SEV1 major user impact or data loss, SEV2 partial or degraded, SEV3 minor).
2. **Assign roles:** Incident Commander (coordinates and decides, does not debug), tech lead (hands on the system), comms (status page, stakeholders), scribe (timestamped timeline). Small teams combine responsibilities with one explicit coordinator. These are incident responsibilities, not instructions to spawn four agents. Messages to others require existing authorization.
3. **Mitigate first, root-cause later:** roll back, fail over, shed load, or flip the kill switch (ship-release-rollout). Preserve evidence before changing systems. For AI incidents, capture model, prompt, tool, and data versions and redacted traces.

## Postmortems

**Triggers (defined beforehand):** user-visible downtime or degradation past a threshold · any data loss · on-call intervention · resolution time past a threshold · a human found it before the alerts did · one incident using more than 20% of the error budget (run-slo-error-budget) · any stakeholder request.

**Blameless, not ownerless.** Name contributing factors in systems and processes. Assume people acted reasonably given what they knew. Rewrite blame language ("X forgot", "human error") toward the system factor.

**Template:** summary · impact (users, duration, budget burned, cost) · detection (how, how fast) · timeline (UTC) · contributing factors (several, from asking how and why, not one root cause) · what went well · what went poorly · where we got lucky · action items.

**Action items** each have an owner, priority, due date, tracking reference, and a check that shows the action worked; ticket closure alone is not effectiveness. Investigate / Mitigate / Repair / Detect / Prevent are useful categories, not quotas, and P0 is assigned by impact, not to fill a template. Draft within 2 business days and review within 5 (suite defaults). Track completion, review overdue P0 items weekly, and keep a searchable archive.

Use referenced core playbooks when available; otherwise perform the applicable step inline. See [host fallbacks](../../references/host-compatibility.md) only when a capability is missing.

Evidence: Google SRE Book ch. 14–15 and Workbook ch. 10; PagerDuty Incident Response docs; Allspaw, "Blameless PostMortems and a Just Culture" (2012). R07 (psychological safety and learning; transfer to software is an inference), R16. See the [research register](../../references/research-evidence.md).
