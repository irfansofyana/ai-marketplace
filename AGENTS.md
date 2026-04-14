# AGENTS.md

This file is the repo contract for Codex and other agent tooling.

## Repository Purpose

This repository publishes reusable agent workflows as skills and packages them for Claude Code. The portable source of truth is the skill content under `plugins/*/skills/*`.

## Source of Truth

- Canonical workflow logic lives in `plugins/*/skills/*/SKILL.md`.
- Supporting files stay beside each canonical skill in `scripts/`, `references/`, and `assets/`.
- Claude-specific packaging lives in `plugins/*/.claude-plugin/`, `commands/`, and `agents/`.
- The existing nested skill layout is installable through `npx skills add` directly from this GitHub repo.

## Portable vs Claude-only

- Prefer adding reusable behavior as a skill.
- Use `commands/` only for Claude slash-command workflows that do not need portability.
- Use `agents/` only for Claude-specific delegation or isolation. If the behavior matters across agents, move it into a skill first.
- `plugins/p-assist` is personal/private. Do not market it as Codex-ready or recommend full-repo public installs unless the repo owner explicitly asks for that.

## Required Validation

Run these before finishing a change that touches skills, plugin metadata, or the README:

```bash
make validate
```

That command must pass before commit. It checks:

- Claude marketplace manifest consistency
- canonical skill frontmatter validity
- required Codex-facing docs and install guidance
- required docs and README markers

If you change MCP server names or tool names, also run:

```bash
python3 scripts/validate-mcp-tool-names.py <plugin-name> <server-key> <tool1> <tool2> ...
```

## Editing Rules

- Keep skill `name` equal to its directory name.
- Keep skill descriptions explicit about what the skill does and when to use it.
- When plugin or skill inventory changes, update `README.md`.
- When plugin behavior changes, bump the affected plugin version in `plugins/*/.claude-plugin/plugin.json`.
- Do not delete or rewrite user-owned local state such as `.codex`.
