---
name: design-product-workflow
description: "Design or improve a user flow or interface: states, cheap alternatives, lowest-fidelity prototype that answers the question, task-based validation, and AI failure and recovery behavior. Not for architecture RFCs or a cosmetic edit."
---

# Product Design Workflow

**Role:** implementer for user-facing flows; the lead, to scope uncertain UX. **Returns:** the requested artifact with tested states and open assumptions.

## Scope

Read the brief and the existing product first. Name the user, task, context, success condition, constraints, and current failure. Separate known from assumed; never invent user research. Keep the brand, platform, accessibility needs, and implementation limits.

A routine interface edit is built and inspected directly. An uncertain journey gets two or three cheap alternatives before polish, compared on hierarchy, steps, error recovery, cost, and accessibility. Color-only variants are not alternatives.

## Prototype and test

1. Map the states: entry, main action, success, empty, loading, partial, error, recovery, plus keyboard and focus behavior and responsive limits.
2. Use the lowest-fidelity artifact that answers the question (flow, wireframe, prototype, working slice), reusing existing components.
3. Before testing, define a realistic task and observable outcomes (completion, errors, recovery, comprehension). Use representative users when available and state the sample's limits; there is no universal five-user rule.
4. Build the chosen flow and inspect rendered states at relevant viewports. A mockup or screenshot does not show usability.
5. Carry states, components, content, acceptance criteria, and open assumptions into implementation. Keep the same builder on coupled UI work; a handoff to build-implementation-loop does not require a new agent.

## AI interactions

Show what the feature can and cannot do. Let users correct inputs and outputs, cancel, undo, or reach a human as fits. Distinguish suggestions from executed actions. Confirm by consequence and existing authorization, not on every action. Never show a model's verbal confidence as a calibrated probability. Evaluate failure behavior with ai-evaluation.

Deliver the artifact asked for, not a report in place of a build.

Evidence: R09 (parallel alternatives), R10 (designing for AI limits and recovery). Variant counts and test budgets are suite inferences. [Register](../../references/research-evidence.md).
