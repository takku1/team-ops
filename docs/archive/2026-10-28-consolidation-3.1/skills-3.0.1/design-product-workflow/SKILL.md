---
name: design-product-workflow
description: Design or improve product journeys and interfaces from user goals through alternatives, prototypes, validation, and implementation handoff. Use for new flows, UX redesigns, ambiguous interaction problems, and AI feature behavior. Not for purely architectural RFCs or a routine cosmetic edit.
---

# Product Design Workflow

**Role:** implementer, for user-facing flows; the lead, to scope uncertain UX before assigning work. **Returns:** the requested artifact with its tested states and open assumptions.

## Scope

Read the brief and the existing product before proposing a redesign. Name the user, task, context, success condition, constraints, and current failure. Separate what is known from what is assumed, and never invent user research. Keep the user's brand, platform, accessibility needs, and implementation constraints.

A routine interface edit is implemented and inspected directly. An uncertain journey gets cheap alternatives before polish: two or three is a budget choice, compared on information hierarchy, steps, error recovery, implementation cost, and accessibility. Color-only variants are not alternatives.

## Prototype and test

1. Map the states: entry, main action, success, empty, loading, partial, error, and recovery, plus keyboard and focus behavior and responsive limits.
2. Pick the lowest-fidelity artifact that answers the open question: flow, wireframe, interactive prototype, or a small working slice. Reuse existing design-system components first.
3. Before testing, define a realistic task and observable outcomes: completion, errors, recovery, comprehension, and time where it matters. Recruit representative users when available and state the sample's limits. There is no universal five-user rule.
4. Use the results to settle the specific question, then build the chosen flow. Inspect rendered states at the relevant viewports and exercise the interactions. A mockup or a pleasing screenshot does not show usability.
5. Hand off states, components, content, acceptance criteria, and open assumptions to build-implementation-loop. Use plan-design-review only for consequential architecture.

## AI interactions

Show what the feature can and cannot do. Let users correct inputs and outputs and recover from failure, with cancel, undo, or escalation to a human as fits. Distinguish suggestions from executed actions. Set confirmation by consequence and existing authorization, not on every AI action. Never display a model's verbal confidence as a calibrated probability. Evaluate quality and failure behavior with ai-evaluation.

Deliver the requested artifact, not a design report in place of a build, with its rationale, tested states, observed results, and what remains uncertain.

Evidence: R09 (parallel alternatives improved outcomes in the studied task) and R10 (design for AI capability limits and recovery). Variant count and testing budget are suite inferences. See the [research register](../../docs/current/research-evidence.md).
