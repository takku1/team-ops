# 4.0.0 overhaul and validation

Date: 2026-10-28. Source-level implementation and local checks. No publication, plugin installation, commit, or push was performed.

## Change and compatibility

All 16 public skill names and the two-plugin split are preserved. All active skills and five optional agent definitions were revised. Worker reports now use task/attempt/artifact identity and a compact result/evidence/open/next shape; callers expecting the old role-specific headings must adapt. The lead remains the main session; no always-running supervisor was added.

One builder owns a coupled change. Selective supporting workers receive bounded briefs and send event deltas. The controller records task state, authority, budget, issue history, and acceptance. Roles no longer each require an identical full-suite rerun. One final verification owner observes deciding checks on stable integrated inputs; required independent runs and hosted CI gates remain.

The new helper is optional and standard-library only. It serializes a local check lane, fingerprints explicitly declared inputs/command/executable/environment/toolchain identity, retains logs, and allows deterministic reuse only by explicit request. It rejects failed/stale evidence and removes prior green evidence before a new execution can fail at launch. It does not enforce agent ownership, freeze writers, discover complete dependencies, provide distributed locks, or enforce token budgets.

## Local checks

- `python -m unittest discover -s scripts -p test_check_runner.py -v`: **passed, 14 tests**. Covers fresh vs opt-in reuse, retained logs, input/environment invalidation, non-reuse of failure, failed fresh-run invalidation, input mutation during execution, concurrent request coalescing, bounded lane waits, missing inputs/invalid scratch state, untracked directory inputs, corrupt/missing records, launch failure, workspace-relative PATH, and nonfinite timeout rejection.
- `python scripts/validate-suite.py`: **passed, zero errors**; checks metadata, package version consistency, local supporting links, evidence IDs, report presence, and scenario coverage. It reports instruction/reference word counts and description characters separately.
- Skill-creator frontmatter validation: **all 16 entrypoints passed**.
- Claude host validation and live Muse integration depend on tools outside this source validation. The Claude CLI was not available in this session; no host validation result is claimed.

## Independent development forward test

One read-only evaluator received the revised lead, coordination, verification, work-breakdown instructions and two realistic requests, without grader rubrics or the research proposal. It did not edit files, build the suite, or spawn workers.

1. Incompatible producer, consumer, schema, and generated client changes: it kept the coupled implementation under one owner, identified the compatibility/deployment decision, and assigned one integrated verification owner. Permission to parallelize did not become a mandate to spawn builders.
2. Prior-revision unsupported green plus a changed untracked configuration and three proposed full-suite runs: it rejected stale evidence, identified current inputs, and assigned one deciding run while retaining targeted independent checks.

The evaluator found an ambiguity about unauthorized lane takeover vs coordinated runner use; agent wording now makes the distinction explicit. Static runner review identified prior-green retention after launch failure, caller-relative PATH lookup, and nonfinite timeout handling. Regression tests reproduced these defects before fixes. Follow-up static review found those issues addressed with no remaining material issue within the documented local/trusted-input model.

These are two development forward tests and static code review, not the full 38-scenario behavioral evaluation or a comparative performance study. Scenario manifests retain `not-run` status; no corpus pass rate is claimed.

## Context measurements

Compared with the local pre-overhaul source snapshot, discovery-description characters decreased from 4,549 to 4,192 across both plugins and five agents (about 7.8%). This counts characters, not tokenizer measurements. Skill body words decreased from 7,393 to 7,043 (about 4.7%); 1,349 words of conditional references are separately loaded on demand. These are whitespace word counts, not tokens; moving conditional detail changes when context loads, not necessarily total documentation size. No token, latency, or dollar savings is inferred from these static counts.

## Environment limits

The initial test harness used Python private temporary-directory permissions, which this managed Windows sandbox could create but not reopen. A minimal normal-vs-private directory probe isolated the difference. Tests now create ordinary scoped scratch directories and verify cleanup remains within the workspace. Twelve empty private scratch directories remain for owner cleanup because the sandbox could not reopen/delete them. Automatic approval review rejected recursive scratch cleanup because sandbox approval is disabled. Safer exact-file deletion and nonrecursive directory cleanup removed the comparison baseline and accessible scratch artifacts; no permissions bypass was attempted.

Windows Store app-execution aliases could be launched but not read for executable hashing. Execution tests use the actual interpreter binary. Users should pass the real command executable path when an alias cannot be read.

No git repository metadata was present in this workspace, so no git diff/commit was available. Validation inspects actual files; the temporary local baseline was used only for content comparison and context measurements.

## Remaining validation

Run installed-host validation, exercise the full development corpus and new held-out tasks, and compare solo/current/candidate workflows under matched snapshots, tools, models, permissions, and total ceilings. Count failures, aborted runs, actual spend, controller overhead, stale evidence, and duplicate build compute. Adoption claims depend on acceptance quality and measured cost/time tradeoffs.
