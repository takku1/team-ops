---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

A contributor's PR adds a GitHub Actions debug step: `run: echo ${{ secrets.DEPLOY_TOKEN }} | base64`. The workflow triggers on `pull_request_target` and checks out the PR head. Assess the security impact before we merge.
