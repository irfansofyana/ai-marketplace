# Contributing

This repository now supports multiple distribution targets:

- Claude Code marketplace packaging under `plugins/*/.claude-plugin/`
- Codex and other agent installs through reusable skills

Treat skills as the product. Treat platform packaging as wrappers around those skills.

## Workflow

1. Edit the canonical skill under `plugins/<plugin>/skills/<skill>/`.
2. Keep supporting files in that same directory tree.
3. If plugin behavior changed, bump the version in `plugins/<plugin>/.claude-plugin/plugin.json`.
4. Update `README.md` if plugin inventory, skill inventory, install instructions, or compatibility notes changed.
5. Run `make validate`.

## Adding a New Public Skill

1. Create `plugins/<plugin>/skills/<skill-name>/SKILL.md`.
2. Add YAML frontmatter with at least:
   - `name`
   - `description`
3. Add `scripts/`, `references/`, or `assets/` only when the skill needs them.
4. Add the skill to the root README.
5. Run `make validate`.

## Adding a Claude-only Workflow

- Put reusable cross-agent behavior in a skill first.
- Add `commands/` only for slash-command UX that is intentionally Claude-specific.
- Add `agents/` only when Claude needs isolated delegation that does not need to be portable.

## Private Plugins

`plugins/p-assist` is personal/private. Keep it working for Claude, but do not market it as Codex-ready unless explicitly requested.

## Validation

```bash
make validate
```

This runs the repository validator and should be treated as the minimum pre-commit check for structural changes.
