# 4.1.0 portability, diagnostics, and behavioral evaluation

2026-10-28. All 16 skill names and the two-plugin split remain stable. This release improves package usability and evaluation without adding agent layers.

## Self-contained packages

Evidence links in every skill now resolve inside its plugin. Both packages include generated research and host references plus a package README. Canonical research/host sources remain in `docs/current/`; `scripts/package_resources.py` publishes exact copies, and suite validation rejects drift. The validator also rejects Markdown links escaping the package boundary.

The portability tests archive each plugin separately, extract it into a host-like cache without the sibling plugin or source checkout, resolve every Markdown file link, and execute the copied core helper against an independent fixture. An explicit reuse request then returns the same successful execution. The Muse installer verifies cached references/helper exist and match source SHA-256, in addition to active/version/skill-count checks.

This is an isolated cache-copy test, not a claim that the permission-blocked live Muse store was updated.

## Cache explanations

Runner schema 2 stores category fingerprints for source inputs, declared scope, command, executable, toolchain identity, environment, workspace, and platform. Results identify cache hits, explicit fresh runs, differing identity categories, unavailable/invalid records, missing logs, prior failure, incomplete/interrupted execution, and unstable inputs. A recent-record comparison explains the observed fingerprint difference, not its underlying cause.

`--explain` computes eligibility without running the command or replacing result records. It still obtains the local lane lock. No environment values, names, or per-secret hashes are stored by diagnostics. Complete inherited environment identity remains conservative: volatile host variables may prevent reuse; no allow-list was introduced merely to raise cache hits. Schema 1 green records do not become reusable as schema 2 records.

## Host behavior

The [host matrix](host-compatibility.md) separates manifest/skill import, named agents, independent review, helper execution, and state enforcement. Missing named agents fall back to an inline role or an authorized available generic worker. A missing companion skill does not force installation or stop applicable inline work. A cold reread remains self-review.

Muse validation previously exposed 10 core and 6 delivery skills but did not establish named-role loading. The earlier Claude model test failed before inference; neither host is described as behaviorally proven from package validation. The [MochiOS record](mochios-4.0-validation.md) retains installation and API blockers. No live-store permission workaround was attempted in this release.

## Observed checks

- `python -m unittest discover -s scripts -p 'test_*.py' -v`: **23 passed**: 18 check-runner tests, 2 isolated package tests, and 3 evaluator regression tests.
- Suite static validation: **passed, zero errors**. Packaged canonical references are synchronized; all **16 skill entrypoints passed** skill-creator validation.
- PowerShell installer syntax and `-WhatIf`: **passed**, without live-store writes. Both standalone archives were extracted into retained cache copies and passed Muse and Claude local validation; Muse recognized 10/6 skills with zero error diagnostics. [Package artifacts and host reports](../../evals/runs/portability-4.1/).
- A bounded independent source review found no material runner diagnostic defect. It identified two evaluator gaps (scope inventory and mixed-payload rejection); both were fixed, regression-tested, and re-reviewed without remaining material findings within that review's scope.

## Paired behavioral development run

Two independent cold actors received identical fixtures and scopes: direct solo baseline vs inline-controller candidate using a frozen package snapshot. Each was instructed to use at most 24 tool calls/eight minutes; these were instructed limits, not independently enforced token/spend limits. Both used the same inherited model configuration; the exact model ID and token/cost telemetry were unavailable. Worker tools were disabled in both arms, so dispatch effectiveness is untested.

| Task | Solo | Inline controller |
|---|---|---|
| Small help fix | pass | pass |
| Coupled producer/consumer/schema change | pass | pass |
| Stale prior green and changed configuration | pass | pass |
| Blocked schema decision plus independent fix | pass | pass |

The final independent artifact oracles passed **8/8**. Separate task/source/report review found **8/8 task outcomes satisfied**, with no actor failures. Actor-time checks are reported in each REPORT.json and candidate logs; artifacts alone cannot authenticate all tool chronology or prohibited reads.

Reported batch execution windows were approximately 35.9 seconds solo and 53.8 seconds controller, on a shared machine with concurrent actors. They exclude some setup/reporting and are not controlled per-case or end-to-end latency measurements. No speedup, cost saving, or quality advantage is inferred. The supported decision is to retain small-work inline defaults and avoid more agent machinery.

The initial independent oracle overconstrained rejection to KeyError even though the task did not specify an exception class. Both actors correctly used ValueError. The oracle was corrected to test rejection semantics, and the initial output is preserved. Independent review then found extra-file/TASK scope checks and mixed payload coverage missing; the final evaluator adds both. No actor artifact was changed to make grading pass.

Evidence: [configuration and limits](../../evals/runs/paired-4.1/run-configuration.json), [artifact results](../../evals/runs/paired-4.1/artifact-results.json), [independent verdict](../../evals/runs/paired-4.1/independent-verdict.json), and [original oracle output](../../evals/runs/paired-4.1/oracle-v1-results.json). The [repeatable procedure](../../evals/FIELD-EVALUATION.md) prepares fresh matched snapshots and grades artifacts separately from behavioral review.

These four development fixtures are not the full 38-scenario corpus or representative held-out MochiOS implementation tasks. The existing real MochiOS crate check (32 passed) remains evidence about that crate and runner, not an agent-team effectiveness measurement. Future provider-backed runs still need live installation access, working API connectivity, host traces, and measured spend before tuning team size or claiming efficiency gains.
