# STATUS

**Current version:** 2.2.2, updated 2026-10-27.

**Scope:** 25 active skills: the existing 20 revised plus product design, hands-on implementation, AI context management, AI workflow efficiency, and AI evaluation. Supports both building with AI and building AI-powered products.

**Evidence:** 20 research entries and 6 groups of primary practice/standard references in [research-evidence.md](current/research-evidence.md). Findings, standards, suite defaults, and local requirements are distinguished. This is a targeted literature-informed revision, not a systematic review or proof that the suite improves outcomes.

**Authoritative files:** edit every skill in `skills/<name>/SKILL.md` directly. The three converted skills are literal builds: after an edit, copy the file to `skillwren-src/<id>/SKILL.md`, run `skillwren check` and `skillwren-src/mkreview.py` on it, then refresh manifests with `scripts/refresh-skillwren-builds.py` (which reads only `skills/`). Static structure checking is not runtime enforcement on Muse or other ordinary skill loaders.

**Evaluation:** 30 scenarios cover all 25 skills (four regression cases added in 2.2.1–2.2.2 from MochiOS field rounds [9](current/muse-usage-report-round9.md) and [10](current/field-report-round10.md)). Four existing rubrics corrected; 17 cases added, including an executable implementation fixture. New scenario definitions are not behavioral pass results. See [eval protocol](../evals/PROTOCOL.md) and the separate validation report for checks actually run.

**Historical evidence:** Muse rounds and archived conversions remain records of particular exercises. Their ratings are not current suite ratings or a controlled benchmark. Existing reports are preserved.

**Next evidence needed:** controlled baseline/candidate runs on representative held-out tasks, including real code/UI artifacts, with measured correctness, human rework, total cost, and elapsed time. No measured efficiency gain is claimed by this release.
