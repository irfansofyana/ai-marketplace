# CLAUDE.md

This file guides Claude Code when working with this repository.

## Repository Purpose

Claude Code Marketplace repository hosting custom plugins. Plugins live under `plugins/`; marketplace manifest at `.claude-plugin/marketplace.json`.

## Key Constraints

- Plugin `name` in marketplace.json **must match** `name` in that plugin's `.claude-plugin/plugin.json`.
- MCP tool names must be ≤64 characters (AWS Bedrock limit). Format: `mcp__plugin_[plugin-name]_[server-key]__[tool-name]`. Always validate: `python3 scripts/validate-mcp-tool-names.py <plugin> <server-key> <tool-names...>`

## Pre-commit: Version Bumping

Before committing plugin changes, bump `version` in that plugin's `.claude-plugin/plugin.json`. Suggest patch (fixes/tweaks), minor (new features/skills/commands), or major (breaking changes). Present suggestion to user and allow override. Bump each affected plugin independently.

## Pre-commit: README Sync

Before committing plugin or skill changes, update root `README.md` plugin and skills tables to match current state. Read `plugin.json` for descriptions and `SKILL.md` frontmatter for skill metadata. Never leave README stale relative to the commit.

## Creating Skills

New skills must follow [agentskills.io specification](https://agentskills.io/specification). Use `skill-creator` skill for initial draft, then iterate. Do **not** pattern-match existing skills; each skill owns its own approach. Required: `SKILL.md` with YAML frontmatter (`name` 1-64 chars lowercase+hyphens matching directory, `description` 1-1024 chars). Optional: `scripts/`, `references/`, `assets/`. Keep under 500 lines.

## Skills vs Commands vs Agents

- **Skills** (default): Model-invoked, triggered by natural language. Current standard.
- **Commands** (legacy): Slash-invoked (`/plugin:command`). Use only when user explicitly requests slash-style invocation.
- **Agents** (isolation): Use when task needs separate context window or specialized persona. Guide users toward skills when unsure.

## Git Conventions

Use semantic commits (e.g., `feat(plugin-name):`, `fix(plugin-name):`, `chore(plugin-name):`). Do not attach AI-generated footers.
