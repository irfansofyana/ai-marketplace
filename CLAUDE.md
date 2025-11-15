# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a Claude Code Marketplace repository for hosting custom plugins. Marketplaces are catalogs that contain plugins, which extend Claude Code with custom functionality (slash commands, agents, Skills, hooks, and MCP servers).

## Architecture

### Two-Level Configuration System

1. **Marketplace Manifest** (`.claude-plugin/marketplace.json`):
   - Defines the marketplace identity and owner
   - Lists all available plugins with their source paths
   - Acts as the registry for discovering and installing plugins

2. **Plugin Manifests** (each plugin's `.claude-plugin/plugin.json`):
   - Contains plugin metadata: name, description, version, author
   - Must match the plugin name referenced in marketplace.json

### Plugin Directory Structure

```
plugin-directory/
├── .claude-plugin/
│   └── plugin.json          # Required: plugin metadata
├── commands/                 # Optional: custom slash commands
│   └── command-name.md
├── agents/                   # Optional: custom agent definitions
├── skills/                   # Optional: Agent Skills (model-invoked capabilities)
│   └── skill-name/
│       └── SKILL.md
├── hooks/                    # Optional: event handlers
│   └── hooks.json
└── .mcp.json                # Optional: MCP server integration
```

### Command Definition Format

Commands are Markdown files in `commands/` directory:

```markdown
---
description: Brief description shown in command list
---

# Command Title

Detailed instructions for Claude Code when this command is executed.
The content here becomes the prompt that Claude receives.
```

Commands are invoked as: `/plugin-name:command-name`

## Development Commands

### Testing Plugins Locally

1. **Add this marketplace to Claude Code:**
   ```bash
   /plugin marketplace add /Users/irfanputra/Personal/my-claude-code-marketplace
   ```

2. **Install a plugin from this marketplace:**
   ```bash
   /plugin install plugin-name@my-claude-code-marketplace
   ```

3. **Browse available plugins interactively:**
   ```bash
   /plugin
   ```

4. **After making changes, reload the plugin:**
   ```bash
   /plugin uninstall plugin-name@my-claude-code-marketplace
   /plugin install plugin-name@my-claude-code-marketplace
   ```

### Plugin Management

- **Enable a plugin:** `/plugin enable plugin-name@my-claude-code-marketplace`
- **Disable a plugin:** `/plugin disable plugin-name@my-claude-code-marketplace`
- **Check installed commands:** `/help` (shows all available slash commands)

## Adding a New Plugin

1. **Create plugin directory** (all plugins are organized in `plugins/` directory with numbered prefix, e.g., `plugins/02-my-plugin/`):
   ```bash
   mkdir -p plugins/02-my-plugin/.claude-plugin
   mkdir -p plugins/02-my-plugin/commands
   ```

2. **Create `plugins/02-my-plugin/.claude-plugin/plugin.json`:**
   ```json
   {
     "name": "my-plugin",
     "description": "Description of what the plugin does",
     "version": "1.0.0",
     "author": {
       "name": "irfansofyana"
     }
   }
   ```

3. **Register in `.claude-plugin/marketplace.json`:**
   ```json
   {
     "name": "my-claude-code-marketplace",
     "owner": {
       "name": "irfansofyana"
     },
     "plugins": [
       {
         "name": "my-plugin",
         "source": "./plugins/02-my-plugin",
         "description": "Brief description for marketplace listing"
       }
     ]
   }
   ```

4. **Add commands, skills, agents, or hooks** as needed in their respective directories

## Current Plugins

- **00-test** (`./plugins/00-test`): Test plugin for learning the basics
- **01-p-assist** (`./plugins/01-p-assist`): Productivity plugin for article summarization, journal management (Logseq), and bookmark organization (Linkwarden). **Requires environment variables** - see `plugins/01-p-assist/README.md` for setup instructions.

## Adding a Command to an Existing Plugin

1. Create `plugin-directory/commands/my-command.md`:
   ```markdown
   ---
   description: What this command does
   ---

   # Command Instructions

   Tell Claude exactly what to do when this command is invoked.
   ```

2. The command becomes available as `/plugin-name:my-command`

3. Uninstall and reinstall the plugin to test the new command

## MCP Server Integration & AWS Bedrock Compatibility

### Tool Name Length Constraint

**CRITICAL**: AWS Bedrock has a **64-character maximum** for tool names. When adding MCP servers to plugins, you MUST ensure all generated tool names stay within this limit.

### Tool Name Format

Claude Code generates MCP tool names using this pattern:
```
mcp__plugin_[plugin-name]_[server-key]__[tool-name]
```

**Example:**
- Plugin name: `p-assist`
- Server key: `linkwd`
- Tool name: `get_public_collections_links`
- Full tool name: `mcp__plugin_p-assist_linkwd__get_public_collections_links` (57 chars ✓)

### Naming Best Practices

1. **Keep plugin names short but meaningful**:
   - ✓ Good: `p-assist` (productivity assistant)
   - ✗ Bad: `personal-assistant` (too long)

2. **Abbreviate MCP server keys when necessary**:
   - ✓ Good: `linkwd` (linkwarden), `logseq` (logseq)
   - ✗ Bad: `linkwarden`, `mcp-logseq`

3. **Validation is MANDATORY**: Always verify tool names before deploying:
   ```python
   # Calculate: mcp__plugin_[plugin]_[server]__[longest-tool]
   # Example: mcp__plugin_p-assist_linkwd__get_public_collections_links
   # Length must be ≤ 64 characters
   ```

### Adding MCP Servers Checklist

When adding a new MCP server to any plugin:

1. ✓ Choose a short, meaningful server key name
2. ✓ List all tools that the MCP server provides
3. ✓ Calculate the longest tool name using the format above
4. ✓ Verify the longest name is ≤64 characters
5. ✓ If over 64 chars, shorten the plugin name or server key
6. ✓ Update plugin.json with the MCP server configuration
7. ✓ Update all command/agent files with correct tool references

### Validation Script

Use the provided validation script to check tool names:

```bash
# Validate tool names for a specific MCP server
python3 scripts/validate-mcp-tool-names.py <plugin-name> <server-key> <tool-names...>

# Example:
python3 scripts/validate-mcp-tool-names.py p-assist linkwd \
    archive_link create_link get_public_collections_links
```

The script will:
- Calculate the full tool name for each tool
- Check if any exceed 64 characters
- Provide suggestions if validation fails
- Exit with code 0 if valid, 1 if invalid

### Example Validation

```python
# Plugin: p-assist, Server: linkwd
# Longest tool: get_public_collections_links (28 chars)
full_name = "mcp__plugin_p-assist_linkwd__get_public_collections_links"
assert len(full_name) <= 64  # 57 chars ✓ PASS
```

## Key Constraints

- Plugin `name` in marketplace.json MUST match the `name` in the plugin's plugin.json
- The `source` path in marketplace.json is relative to the repository root
- Command files must be `.md` files with valid YAML frontmatter
- Changes to plugins require reinstalling them to take effect in Claude Code
- Use semantic versioning (1.0.0, 1.1.0, 2.0.0) when updating plugins
- **MCP tool names MUST be ≤64 characters for AWS Bedrock compatibility**
