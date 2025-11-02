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
- **01-personal-assistant** (`./plugins/01-personal-assistant`): Productivity plugin for article summarization, journal management (Logseq), and bookmark organization (Linkwarden)

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

## Key Constraints

- Plugin `name` in marketplace.json MUST match the `name` in the plugin's plugin.json
- The `source` path in marketplace.json is relative to the repository root
- Command files must be `.md` files with valid YAML frontmatter
- Changes to plugins require reinstalling them to take effect in Claude Code
- Use semantic versioning (1.0.0, 1.1.0, 2.0.0) when updating plugins
