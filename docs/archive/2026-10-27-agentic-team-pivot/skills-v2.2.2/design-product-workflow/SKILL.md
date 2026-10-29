---
name: design-product-workflow
description: Design or improve product journeys and interfaces from user goals through alternatives, prototypes, validation, and implementation handoff. Use for new flows, UX redesigns, ambiguous interaction problems, and AI feature behavior. Not for purely architectural RFCs or a routine cosmetic edit.
---

# Product Design Workflow

## Scope the design

Read the brief and existing product before proposing a redesign. Identify the user, task, context, success condition, constraints, and current failure. Separate observed behavior from assumptions. Preserve the user's brand, platform, accessibility needs, and implementation constraints. Ask only about decisions that materially change the work; keep independent progress moving.

For a routine interface edit, implement and inspect it directly. For an uncertain journey, sketch credible alternatives cheaply before polishing. Two or three alternatives is a useful budget choice, not a research requirement. Compare information hierarchy, interaction steps, error recovery, implementation cost, and accessibility. Avoid superficial color-only variants and invented user research.

## Prototype and test

1. Map entry, main action, success, empty, loading, partial, error, and recovery states where applicable. Include keyboard/focus behavior and responsive constraints.
2. Pick the lowest-fidelity artifact that answers the uncertainty: flow, wireframe, interactive prototype, or small working slice. Reuse existing design-system components before inventing new patterns.
3. Define a realistic task and observable outcomes before testing: completion, errors, recovery, comprehension, time when meaningful. Recruit representative users when available; explain sample limitations. No universal five-user rule or statistical claim from informal inspection.
4. Use feedback to resolve the specific uncertainty, then implement the selected flow. Inspect rendered states at relevant viewports and exercise interactions. A generated mockup or a visually pleasing screenshot does not establish usability.
5. Hand off concrete states, components, content, acceptance criteria, and unresolved assumptions to build-implementation-loop. Use plan-design-review only for consequential architecture decisions.

## AI interactions

Explain relevant capabilities and limitations in the experience. Let users correct input/output and recover from failure; provide appropriate cancellation, undo, or human escalation. Distinguish generated suggestions from executed actions. Choose confirmation based on consequence and existing authorization, not every AI interaction. Do not display a model's verbal confidence as a calibrated probability. Evaluate task quality and failure behavior with ai-evaluation.

## Output and evidence

Deliver the requested artifact with the rationale, tested states, observed results, and remaining uncertainty. Do not turn a build request into a design report only.

R09 and R10 support exploring alternatives and designing for AI failure; exact workflow, variant count, and testing budget are suite inferences. See the [research register](../../docs/current/research-evidence.md). Neither study establishes a universal visual style or proves this workflow improves every product.
