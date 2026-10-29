# Changelog

## 4.2.2 (2026-10-29)

- Repeat + held-out run of 4.2.1 vs 4.1.0 (180 runs, two per case, 7 new held-out cases): **accepted**, delta +0.033, CI [0.000, +0.067]. Held-out target-skill loading 2/14 -> 8/14 runs; dev 49/76 -> 62/76; no severe failures. Corrects the 4.2 report: with repeats, loading explains less of the pass rate than single runs suggested. [Report](evals/runs/scenarios-4.2.1-rep/REPORT.md).
- Error analysis of the three real sessions that used the suite outside this repo ([record](docs/current/error-analysis-2026-10-29.md)): team-lead now says workers share the account usage limit, memory, CPU, and build locks (serialize heavy builds; a limit kill is an environment failure); coordination says a worker finishes or hands back its background jobs before reporting. These two rules are unmeasured.
- README rewritten as a router for hosts without plugin support (skill paths first; 73 -> ~40 lines; stale agent count fixed).
- Two held-out gaps recorded, deliberately not tuned (risk-acceptance owner on retry-green; "split across N agents" not loading team-lead).
- Then tuned on those two gaps (cases reclassified to dev): definition of done says who decides risk acceptance; team-lead triggers on splitting work across agents. Six fresh held-out cases added (51 total).
- Check runner job registry: `--status` reports running, waiting, orphaned, and recent jobs per lane with `--owner`; team-lead's shared-limits rule points to it. Two new tests (26 pass).
- Evaluation: `run_scenarios.py --solo` (no-suite arm with efficiency metrics), `rejudge.py` (independent Codex judge), `trigger_proxy.py`, `session_timeline.py`, and a blind human calibration pack (`evals/calibration/round-1`, `score_calibration.py`).
- Solo vs 4.1.0 vs 4.2.2 on 27 cases x 2 ([report](evals/runs/scenarios-4.2.2/REPORT.md)): 4.2.2 beats solo by +0.111, scenario-clustered CI [+0.037, +0.185] (held-out +0.159), at +2 s median, +1.5 turns, +12% cost per run. Opus-judged only; the Codex re-grade is pending (usage limit). A Codex re-grade of the earlier 180 runs erased the 4.2.1-vs-4.1.0 quality difference, so version-to-version quality claims are judge-dependent.

## 4.2.1 (2026-10-29)

Trigger-first descriptions for the seven skills that failed to load in the 4.2.0 corpus run (ai-evaluation, ai-context-management, build-definition-of-done, team-lead, build-implementation-loop, build-code-review, secure-review). Each now opens "Use when..." and names trigger situations (trusting a reported pass, relying on another agent's diagnosis, certifying a security level, sizing agent count). Always-on +43 chars.

- Full 38-case candidate run against the stored 4.1.0 baseline: target skill loaded in 32/38 (4.2.0: 24/38), passes 29 vs 28, no severe failures, same cost; `compare` accepted (delta +0.026, CI [-0.040, +0.092]). [Report](evals/runs/scenarios-4.2.1/REPORT.md).
- That run dropped two team-lead cases from routing; restoring "dependencies, blocked work, who runs which checks" fixed both in a 12-case targeted rerun (passes 10/12 vs 9/12 for 4.2.0). The targeted rerun covers team-lead cases only.
- Single samples per case: per-case routing varies between runs; read totals, not individual flips. Descriptions were tuned on development cases.

## 4.2.0 (2026-10-28)

Adopted concepts from local repos (SkillWren, recurspec, prompt-optimization, Runtime-Capability-Lifecycle) and outside research, at roughly flat body size.

- **Breaking:** `security-reviewer` merged into `reviewer` as a security mode (four agents). Briefs naming `security-reviewer` should name `reviewer` with security mode.
- "Before returning, verify" checks in code review, definition of done, postmortem, and rollout (R34: gates beat prose, small-sample local evidence).
- Repairs end `KEEP`, `REVERT`, or `ESCALATE`; ruled-out approaches are never retried. Work breakdown resolves BUY/ADOPT/WRAP/BUILD/DEFER before splitting. A passing check licenses only the cases it exercised.
- ai-evaluation starts from error analysis of real traces. Context guidance: critical rules first, just-in-time loading.
- Check runner redacts secret-shaped spans (private keys, AWS/GitHub/`sk-` keys, bearer tokens, `key=value` secrets) from logs and reports `redactions`; new test. Fixed `test_relative_path_entry_resolves_from_workspace`, which copied whichever `whoami` was first on PATH (Git's MSYS build needs msys-2.0.dll); it now pins System32. 24/24 tests pass.
- Register R26-R34 (IFScale, Cognition, Anthropic multi-agent and context engineering, self-correction limits, context rot, DORA 2025, error analysis, SkillWren r2). Redundant "Pitfalls" lines and duplicated role/budget text removed.
- First executed scenario corpus run (`scripts/run_scenarios.py`, prompt-optimization `compare`): **accepted** as non-inferior to 4.1.0 on all 38 cases (delta +0.013, 95% CI [-0.040, +0.066], no severe failures, oracles 6/6). Runs that loaded the target skill passed 23/24; 11 cases loaded no skill in either arm. Two edit cases gained fixtures and oracles. [Report](evals/runs/scenarios-4.2/REPORT.md).
- Against 4.1.0 (chars/4): always-on -13%, skill bodies -8%, agents -30%, delegated code/security review runs -26%/-29%. Trigger proxy 27/38 top-1 (baseline 26). No behavioral eval run.

## 4.1.1 (2026-10-28)

Context and language pass. No skill names, report shapes, or eval-covered rules removed.

- Every skill now leads with its purpose and a **Return:** contract, then procedure, then rules. Unified terms: "lead" for the main session, "deciding check" for oracles. Descriptions follow "what. Use when... Not for...".
- Split the check-runner manual out of the coordination contract into `team-lead/references/check-runner.md`, loaded only when the runner is used (dispatch-path contract ~-53%).
- Agents: shared boilerplate deduplicated; each role's result shape now lives in its report block; descriptions shortened.
- Evidence footers keep IDs and the register link; named practitioner citations moved to new register entries P07-P09. Removed the repeated host-fallback paragraph from delivery skills.
- Measured (chars/4) against 4.1.0: always-on descriptions ~1,048 -> ~942 tokens (-10%); delegated review run -28%; all skill bodies -8%; inline small fix +4% (added Return contract). A keyword trigger proxy over the 38 eval prompts (skill names stripped) improved from top-1 26/38, top-3 32/38 to 27/38, 33/38. No behavioral eval was run.

## 4.1.0 (2026-10-28)

- Self-contained packages: local evidence/host references, package READMEs, generated-resource drift checks, package-boundary link validation, and independent archive/cache execution tests. Muse installer now checks cached resource hashes.
- Runner schema 2: category fingerprints and cache reasons; `--explain` inspects reuse eligibility without executing. Complete environment identity and freshness/independence requirements remain intact.
- Explicit host compatibility and inline/generic-worker fallback; unavailable companion skills do not force installation.
- Repeatable solo vs inline-controller fixture preparation and independent artifact oracles. Executed four tasks per arm; both satisfied 4/4 under independent task review. Tokens/cost unavailable; no quality, speed, or savings advantage claimed. Retain small-work inline defaults.
- 23 executable tests pass. Evaluation corrections are recorded, including rejection exception semantics, protected-task/extra-file inventory, and mixed legacy-payload coverage. Full scenario corpus and held-out real-task study remain separate.

## 4.0.0 (2026-10-28)

Refactor coordination from phase reports to an adaptive controller, explicit artifact evidence, and selective event handoffs. All 16 skill names and the two-plugin split remain stable; the five worker report shapes change.

- One owner per coupled implementation, adaptive worker admission, controller-owned task state, stable issue/retry history, and run-wide budgets. Small inline work needs no board or role ceremony.
- One designated final verification owner; focused builder checks and targeted reviewer checks remain. Current trustworthy execution records replace mandatory duplicate full-suite runs by every role.
- Optional standard-library local check runner: serialized execution, declared input/environment/executable identities, opt-in deterministic reuse, retained logs, stale/failure rejection, and bounded lock waits. No agent scheduler or distributed service is claimed.
- Refactored all skills and role agents. Coordination, supply-chain detail, and ADR shape load on demand. Delivery defaults respect adopted local policy and existing authorization.
- Added five primary-source evidence entries and six coordination scenarios (38 total). Extended supporting-reference validation and context-size reporting; added 14 executable runner tests.
- See the current validation report for observed results and limitations. No team-versus-solo gain is established.

## 3.1.0 (2026-10-28)

Consolidation for token cost. Everything that makes it into a session should earn its place.

- **Two plugins:** `plugins/team-ops` (core: lead, five phases, 10 skills, 5 optional agents) and `plugins/team-ops-delivery` (optional: `build-test-strategy`, `build-trunk-integration`, `ship-release-rollout`, `run-slo-error-budget`, `run-incident-postmortem`, `plan-forecast-recovery`). The marketplace lists both.
- **Merged:**
  - `ai-workflow-efficiency` into `ai-evaluation`.
  - `secure-threat-model` and `secure-supply-chain` into `secure-review`.
  - Agent failure logs into `team-lead`, so the core no longer depends on the incident skill.
  - Parallel-work integration and red-CI restoration into `build-definition-of-done`, which is now the whole verify playbook.
- **`build-code-review` is prose.** The SkillWren header (which Claude Code ignores) and the duplicated appendix are gone. It keeps the untracked-file scan, target scoping, grounding for out-of-diff findings, labels, verdicts, and policy setting. It also gains a test-meaningfulness check.
- **Short descriptions:** every skill and agent description is at most 260 characters, enforced by the validator. Agent bodies no longer repeat their playbook.
- **Measured:**
  - Always-on (core) went from about 2,470 tokens to 840; core plus delivery is about 1,140.
  - All bodies went from about 23,800 tokens to 15,400.
  - A typical lead, implement, and review run went from about 5,000 tokens to 3,100.
- **Evals:** 6 cases retargeted to merged skills; all 16 skills covered.
- **Archived** to `docs/archive/2026-10-28-consolidation-3.1/`: the 3.0.1 skills and agents, `skillwren-src/`, the pilot record, and `refresh-skillwren-builds.py`.

## 3.0.1 (2026-10-27)

Sharpening pass over all 18 skills and 5 agents. No skills were added or removed, and no behavioral claim changed.

- **Subagents are opt-in in the agent definitions too.** All five `agents/*.md` descriptions now say "spawn only when the user asked for or approved subagents" and name the condition that justifies one. Before, descriptions such as "use after an implementer finishes any non-trivial change" invited spawning a subagent by default, which contradicted `team-lead`. Removed the redundant "optional subagent form" banner from the agent bodies.
- **One shape per skill:** role and returns, then the body, then optional pitfalls, then a single evidence footer that combines practitioner sources and register IDs. The bolted-on "Research and application", "Logic", and "Sources" sections were folded into the body where they apply, removing contradictions between the two halves. For example, trunk integration no longer says "~10 minutes" in one section and "targets to adapt" in another.
- **`team-lead`:** the repo brief is built only when work spans several phases or sessions, not on first use in any repo. Dropped the unproven claim that inline review "keeps most of the benefit at no extra cost".
- **`plan-design-review`:** critique is a cold re-read, or a reviewer subagent only if one was approved, instead of a required fresh-context reviewer.
- **`build-definition-of-done`:** adds a written / configured / enforced / observed ladder and makes proportionality explicit, so a doc fix doesn't need a staging deploy.
- **`run-slo-error-budget`:** fixed the role (lead and verifier, not security-reviewer). Gives the general budget-spent formula and a worked 7-day window.
- **`run-incident-postmortem`:** agent-run failure logs come first, and the description now triggers on looping or misdiagnosed team runs.
- **`ship-release-rollout`:** recovery is defined before the rollout starts, and compensation is distinguished from rollback for side effects that already happened.
- **SkillWren builds** (`build-code-review`, `secure-supply-chain`): research notes were moved into the appendix, sources mirrored, the review-map anchor for the evidence line updated, the maps regenerated, and the manifests refreshed. `skillwren check` is clean.
- Static validation is clean (18 skills, 5 agents, 32 cases), and `claude plugin validate` passes. No behavioral eval was run.

## 3.0.0 (2026-10-27)

Pivot from human-team engineering policy to an agent-team workflow. The v2.2.2 pack is archived in `docs/archive/2026-10-27-agentic-team-pivot/`.

- **Roles as a workflow:** the lead runs investigate, implement, review, secure, and verify as phases. Phases run inline by default. New `agents/` (`implementer`, `reviewer`, `security-reviewer`, `verifier`, `investigator`) provide optional subagent forms with scoped tools and a fixed handoff report. They are used only when you ask for or approve them, and when independence, context isolation, or parallel work pays for itself.
- **New `team-lead`:** phase selection, the repo brief, one writer per path, a brief template, evidence-over-claims acceptance, a two-round rework limit, escalation, and failure logs. Replaces `eng-policy-lead` and absorbs `org-team-topology`, `org-ownership-raci`, and `plan-delivery-cadence`.
- **Merged:** `plan-forecast-recovery` (from `plan-estimate-forecast` and `plan-late-recovery`, adding agent run budgets and stuck-run recovery). `plan-design-review` now includes ADRs (from `plan-decision-record`). `ai-workflow-efficiency` now includes team capacity and team-level delivery measures (from `org-capacity-plan` and `measure-delivery-health`). 25 skills down to 18.
- **Reframed playbooks:** every skill names its role and what it returns. The DoD gains acceptance rules for agent work. Code review and supply chain gain team-role sections (both SkillWren sources mirrored, checked, review maps regenerated, manifests refreshed). Integration gains merging parallel worktrees. Postmortems gain agent-run failure logs. Context management defines briefs and handoff reports.
- **Evals 30 → 32:** archived `policy-lead-audit-top-three` and `topology-shared-contributors`. Added `lead-small-fix-stays-inline`, `lead-verifies-reported-claims`, `lead-one-writer-per-scope`, and `failure-log-from-stuck-run`. Retargeted 7 cases to merged skills and rewrote the `lead-prototype-no-policy-bootstrap` rubric.
- **Validator:** checks agent frontmatter, playbook references, the report shape, `team-ops:`/`agents/` references, and references to retired skill names.
- Wrote the round-10 field report (archived with the pivot).

## 2.2.2 (2026-10-27)

Round-10 field test on MochiOS: restoring red CI (docs, schema, registry, deny) and triaging a browser cap failure from another agent's handoff (`docs/archive/2026-10-27-agentic-team-pivot/field-report-round10.md`).

- **`secure-supply-chain`:** an advisory exception must also satisfy the repository's own waiver rule; when no fixed release fits and the path is reachable, present the migration, exposure, and a time-boxed exception for the owner instead of waiving to turn CI green.
- **`ai-context-management`:** a handed-over diagnosis is a hypothesis; verify its load-bearing claims, especially a proposed discriminator or test, before acting on it.
- **`build-trunk-integration`:** when restoring a red job, run every step locally (an early failure hides later ones) and account for runner differences such as case-sensitive paths.
- **Evals 28 → 30:** `supply-reachable-advisory-no-silent-waiver`, `context-handoff-diagnosis-is-hypothesis`.
- **Housekeeping:** Muse rounds 1–8 and the fix list archived to `docs/archive/2026-10-27-muse-field-rounds-1-8/`; stray `.claude-flow/` state moved out of `skills/` and `skillwren-src/`; plugin keywords cover design, implementation, and AI skills.

## 2.2.1 (2026-10-27)

Round-9 field test: a real MochiOS fix (stale `hid_table_stage` test pin) run through `build-implementation-loop` then `build-code-review` (`docs/archive/2026-10-27-agentic-team-pivot/muse-usage-report-round9.md`).

- **`build-code-review` keeps grounded findings.** The `review-change` verify step discarded *every* finding and aborted if any one did not cite a changed line, which also blocked legitimate out-of-diff findings (stale docs or trackers the change makes inconsistent). It now drops only uncited findings (new `grounding filter` step) and accepts a finding that names both the implicating changed line and the unchanged location.
- **`build-implementation-loop`:** changing a test expectation needs cited evidence the behavior change was intended, must honor the test's own edit condition, and must pin at least as strictly; formatters and linters are held to changed lines with pre-existing drift attributed; completion updates the repo's tracker entry for the fixed item and flags (not edits) stale adjacent entries.
- **Evals 26 → 28:** `code-review-keeps-out-of-diff-findings`, `implementation-stale-test-pin`.
- **Docs:** STATUS/README no longer say to edit `skillwren-src/` and rebuild; `skills/` is authoritative, matching `refresh-skillwren-builds.py` and the pilot banner.

## 2.2.0 (2026-10-27)

- Revised all 20 existing active skills with scoped research references and context-sensitive policy defaults.
- Added design-product-workflow, build-implementation-loop, ai-context-management, ai-workflow-efficiency, and ai-evaluation (25 total).
- Corrected PERT percentile claims, SLO denominator/window handling, capacity double-counting, universal branch/test-ratio cutoffs, review target scope, and SLSA/SBOM conflation.
- Added a 20-entry research register distinguishing evidence from operational inferences, plus primary practice/standard references.
- Added 17 behavioral scenarios; revised 4 existing graders; indexed 26 cases covering all active skills. Added a controlled comparison protocol and static validation tooling. No new behavioral pass rate or speedup is claimed.
- Converted-skill sources stay authoritative: Codex's research-backed rewrites were ported back into `skillwren-src/`, review maps regenerated, and all three rebuilt (chain verified `src==built`, manifests refreshed).

## 2.1.0 (2026-10-27)

Behavioral changes since 2.0.0, all driven by the six-round Muse field
test on MochiOS (`docs/archive/2026-10-27-muse-field-rounds-1-8/`):

- **Evals 3 → 9.** Added `work-breakdown-slices-vertically`,
  `test-strategy-pyramid-and-flaky`,
  `definition-of-done-enforced-vs-claimed`,
  `policy-lead-audit-top-three`,
  `code-review-covers-untracked` (regression for a gap the old review
  flow missed), and `supply-chain-audit-cites-evidence` (covers the
  third SkillWren skill). The build-loop skills are now tested, not
  just the peripheral ones.
- **`build-code-review` reads untracked/unstaged paths** before
  reviewing and refuses or caveats when part of the change is unread
  (contract L47, flow L90–98, appendix L149–153). Verified live: the
  new flow flags a planted SQL-injection file the old flow could not
  see, and caveated a real review on a dirty tree.
- **Bootstrap item 12 (`repo-adapter.md`) demands evidence.**
  Every adapter value cites its live source (file + line), every
  workspace package is covered with none omitted, and anything
  unverified is marked UNVERIFIED — never stated as fact. Added after
  a judged draft stated stale per-bin slot data as fact.
- **`scripts/install-muse.ps1`.** `muse plugins install` exits 1 on
  success when only warnings exist; the wrapper judges by observed
  plugin state (enabled + active + zero error diagnostics) instead.
  Verified exit 0 on success, exit 1 on missing plugin.
- **SkillWren declared prose-level on Muse** (`skillwren-pilot.md`).
  The runtime ignores gate frontmatter, so flows execute as
  self-enforced checklist discipline. Silent degradation rejected.
- **README** gained a Muse install section documenting the wrapper
  and the exit-1 behavior.

No skill that worked was rewritten. Version deliberately held at 2.0.0
through rounds 1–6 and cut here with the reinstall.
