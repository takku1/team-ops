---
name: run-incident-postmortem
description: Run incident response roles and write blameless postmortems with a timeline, impact, contributing factors, and owned, prioritized action items (Investigate / Mitigate / Repair / Detect / Prevent). Use during or after an outage, data loss, security event, near miss, or any SLO-burning incident, or when defining incident and postmortem policy. Not for routine bug triage.
---

# Incidents and Blameless Postmortems

## Incident response policy
- **Declare early and downgrade freely.** Severity levels are defined in advance (e.g. SEV1 is major user impact or data loss, SEV2 is partial or degraded, SEV3 is minor).
- **Roles:** Incident Commander (coordinates and decides, does not debug), Ops/Tech lead (hands on the system), Comms lead (status page and stakeholders), Scribe (timeline). Small teams may combine roles, but the IC role is always explicit.
- **Mitigate first and root-cause later.** Roll back, fail over, shed load, or flip the kill switch (ship-release-rollout).
- A dedicated channel per incident, with timestamped notes.

## Postmortem triggers (define before incidents)
User-visible downtime or degradation beyond a threshold · any data loss · on-call intervention (rollback, rerouting) · resolution time over threshold · monitoring failure (a human found it before the alerts did) · a single incident using more than 20% of the error budget (run-slo-error-budget) · any stakeholder request.

## Postmortem policy
- **Blameless:** identify contributing causes in systems and processes without indicting individuals. Assume people acted reasonably given what they knew. Blameless does not mean ownerless.
- **Draft within 2 business days and review within 5.** One postmortem owner.
- **Template:** summary · impact (users, duration, budget burned, cost) · detection (how, and how fast) · timeline (UTC) · contributing factors (ask "how" and "why", and list several factors rather than one "root cause") · what went well · what went poorly · where we got lucky · action items.
- **Action items:** each needs an owner, priority, due date, tracking reference, and verification of effectiveness. Investigate / Mitigate / Repair / Detect / Prevent are useful categories; do not manufacture one of each or assign P0 solely to satisfy a template.
- **Track action-item completion** as a team metric. Review overdue P0 items weekly.
- **Share widely** and keep a searchable archive. Walk through a notable postmortem in a recurring forum.

## Logic
1. If the incident is live, assign roles, open a channel, set the severity, and mitigate.
2. Afterward, check the triggers, then draft from the template using the timeline and logs.
3. Flag blame language ("X forgot", "human error") and rewrite it toward system factors.
4. Validate the action items for owner, due date, category mix, and P0 when required.

## Sources
Google SRE Book ch. 14 (Managing Incidents) and ch. 15 (Postmortem Culture); SRE Workbook ch. 10 (Postmortem Culture); PagerDuty Incident Response docs (response.pagerduty.com); John Allspaw, "Blameless PostMortems and a Just Culture" (Etsy, 2012).

## Research and application

Two/five-day deadlines and action categories are suite defaults. Preserve evidence before changing systems. For AI incidents, capture model/prompt/tool/data versions and relevant redacted traces. Test whether follow-up controls prevent recurrence; ticket closure alone is not effectiveness.

Evidence: R07, R16; see the [research register](../../docs/current/research-evidence.md) for study scope, source links, and limitations.
