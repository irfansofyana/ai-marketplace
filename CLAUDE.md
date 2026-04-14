# CLAUDE.md

Shared repository rules live in @AGENTS.md.

This file is only for Claude-specific guidance.

## Claude-Specific Notes

- Treat `AGENTS.md` as the shared source of truth for repo structure, validation, portability rules, and public/private boundaries.
- Plugin `name` in `.claude-plugin/marketplace.json` must match `name` in that plugin's `.claude-plugin/plugin.json`.
- MCP tool names must be ≤64 characters (AWS Bedrock limit). Validate with `python3 scripts/validate-mcp-tool-names.py <plugin> <server-key> <tool-names...>`.
- Before committing plugin changes, bump `version` in the affected plugin's `.claude-plugin/plugin.json`. Suggest patch, minor, or major and let the user override.
- Use semantic commits such as `feat(plugin-name):`, `fix(plugin-name):`, or `chore(plugin-name):`. Do not attach AI-generated footers.
