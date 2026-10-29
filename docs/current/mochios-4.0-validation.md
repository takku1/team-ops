# MochiOS installation attempt and bounded validation

2026-10-28. Target: `Z:\MochiOS`. Suite source: v4.0.0. Installation is **not complete**; local package validation and a real crate check succeeded.

## Installation

From MochiOS, `muse plugins list --json` reported active/enabled `team-ops` **2.2.0**, sourced from the old suite root layout. No delivery plugin was listed.

The authorized command `muse plugins install Z:\team-ops-skills\plugins\team-ops --scope project --json` failed with `plugin-store-write-failed`: access denied to `C:\Users\dcarn\.local\share\muse\plugins\.installed.lock`. The command reported the error despite an outer shell exit status of zero. Observed installed state, not exit status alone, remains the acceptance criterion. The old installation was not upgraded. This session has write access to the skill-suite workspace, not the live Muse store or MochiOS source tree.

The Muse launcher's automatic update check also attempted an unrelated write to its application directory. Subsequent invocations used the launcher's supported `MUSE_NO_AUTO_UPDATE=1` setting to avoid updating the application during plugin checks.

A dedicated [suite installer](../../scripts/install-muse-suite.ps1) is ready. It selects the project explicitly, installs both plugin bundles, verifies active/enabled version and skill counts, checks that the cached core package contains the coordination reference and runner, and restores its temporary update setting. PowerShell syntax parsing and `-WhatIf` passed. Its actual live-store writes remain blocked here.

Run from a terminal with access to the live plugin store:

```powershell
powershell -ExecutionPolicy Bypass -File Z:\team-ops-skills\scripts\install-muse-suite.ps1 -Workspace Z:\MochiOS
```

Start a fresh Muse session in MochiOS afterward. No permission bypass or alternative live-store mutation was attempted.

## Host package validation

- Muse: both v4.0.0 bundles valid; core imports 10 skills, delivery imports 6; zero error diagnostics. Each has two presentation-only warnings (`author`, `keywords`). Raw reports are in [run artifacts](../../evals/runs/mochios-4.0/).
- Muse's reported capability lists expose skills; loading the five named Claude-compatible agent definitions was not established. Inline skill execution remains the supported baseline; no named-agent runtime compatibility claim is made.
- Claude: marketplace and both plugin bundles passed local validation. Separate directory-submission checks flagged missing per-package README/license and icon assets. These did not fail local plugin validation; no public directory submission or license choice was made.

## Real MochiOS execution

Read `CLAUDE.md`, governing architecture, crate manifests, toolchain, and check configuration. The checkout had substantial unrelated modifications and untracked files. No MochiOS source, policy, tracker, or existing build lane was edited by this test. No VM or boot-chain change was made; no whole-system or boot acceptance is claimed.

Through the v4 local check runner:

```text
cargo test --locked --offline --lib --target x86_64-pc-windows-msvc -p mochios-admission-check
```

Toolchain: `nightly-2026-04-15`, rustc commit `a5c825cd824ee0ef9463021078a2f464b4cc1a0d`. A dedicated `CARGO_TARGET_DIR` under the suite run artifacts avoided MochiOS's existing target lanes. Declared inputs included Cargo manifests/lock, toolchain, `.cargo`, and the ABI, contract-IR, and admission-check source trees. `RUST_MIN_STACK=134217728` follows the repo configuration.

**Observed: 32 passed, zero failed; command exit 0; declared inputs stable.** First runner execution: `4193b3540573486aad90b9f1b40f7f5f`, with retained [stdout](../../evals/runs/mochios-4.0/checks/4193b3540573486aad90b9f1b40f7f5f.stdout.log), [stderr](../../evals/runs/mochios-4.0/checks/4193b3540573486aad90b9f1b40f7f5f.stderr.log), and [result record](../../evals/runs/mochios-4.0/checks/4193b3540573486aad90b9f1b40f7f5f.result.json).

A subsequent cross-shell reuse request had a different complete identity and executed rather than reusing. The runner hashes the whole inherited environment; no claim is made that the differing identity was caused by a particular variable or file.

Two consecutive explicitly reusable requests under the same environment then returned execution `06742c802a4d4d5c8892cb7b3c25dc06`, first with `reused=false`, second with `reused=true`, both exit 0. The second skipped Cargo execution. [Recorded pair](../../evals/runs/mochios-4.0/reuse-check.json). This demonstrates reuse for this declared input/environment, not a measured overall workflow speedup.

## Model-driven test: environment failure

A fresh Claude headless session explicitly loaded both source plugin directories in session-only development mode. It used safe mode, read-only tools (`Read`, `Glob`, `Grep`, `Skill`), no session persistence, no worker tools, and a $2 maximum API budget. [Prompt](../../evals/runs/mochios-4.0/prompt.md): inspect actual admission-check binding/assurance tests and answer coupled-contract/stale-evidence coordination questions without edits or builds.

The session ended after about 171 seconds with `terminal_reason=api_error`, `ECONNREFUSED`, zero reported model tokens/cost, and zero spawned subagents. It did not produce a behavioral answer or inspect source through tools. This is an environment-error attempt, not a scenario pass. The API connection was not bypassed or redirected.

## Next validation

Complete installation with live-store access, start a fresh host session, and repeat the bounded read-only prompt with a working configured provider. Then test one authorized isolated implementation slice, recording task identity, worker count, expensive check executions, integrated acceptance, tokens/cost, and elapsed time. Preserve MochiOS's current work. No broader repair or kernel build is needed to complete this plugin smoke test.
