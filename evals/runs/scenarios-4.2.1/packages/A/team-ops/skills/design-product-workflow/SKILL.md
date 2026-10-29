---
name: design-product-workflow
description: "Design or improve a user flow or UI: states, cheap alternatives, the lowest-fidelity prototype that answers the question, task-based validation, AI failure and recovery. Not for architecture or cosmetic edits."
---

# Product Design Workflow

Design the flow, prove it with the cheapest artifact that answers the question, then build it.

**Return:** the artifact requested, not a report in its place, with its tested states and open assumptions.

## Scope

Read the brief and the existing product. Name the user, task, context, success condition, constraints, and current failure. Separate known from assumed; never invent user research. Keep brand, platform, accessibility needs, and implementation limits.

A routine interface edit is built and inspected directly. An uncertain journey gets two or three cheap alternatives before polish, compared on hierarchy, steps, error recovery, cost, and accessibility. Color-only variants are not alternatives.

## Prototype and test

1. **Map every state:** entry, main action, success, empty, loading, partial, error, recovery, plus keyboard/focus behavior and responsive limits.
2. **Pick the lowest fidelity that answers the question** (flow, wireframe, prototype, or working slice), reusing existing components.
3. **Define the test before running it:** a realistic task and observable outcomes (completion, errors, recovery, comprehension). Use representative users when available and state the sample's limits; there is no universal five-user rule.
4. **Build the chosen flow and inspect rendered states** at the relevant viewports. A mockup or screenshot does not show usability.
5. **Hand off** states, components, content, acceptance criteria, and open assumptions. Coupled UI work stays with the same builder; moving to build-implementation-loop needs no new agent.

## AI features

- Show what the feature can and cannot do.
- Let users correct inputs and outputs, cancel, undo, or reach a human, as fits.
- Distinguish suggestions from actions already taken.
- Confirm by consequence and existing authorization, not on every action.
- Never present a model's verbal confidence as a calibrated probability.
- Evaluate failure behavior with ai-evaluation.

Evidence: R09, R10; variant counts and test budgets are suite inferences ([register](../../references/research-evidence.md)).
