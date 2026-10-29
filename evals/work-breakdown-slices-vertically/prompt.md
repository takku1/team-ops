---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Decompose this epic for a two-person team: "Let support staff issue refunds
from the admin console, with an audit trail." Today refunds are issued by
engineers running SQL by hand. There is no refund API, no admin UI for it,
and no audit log. There are unknowns: nobody knows whether the payment
provider supports idempotent refunds. Give the work breakdown.
