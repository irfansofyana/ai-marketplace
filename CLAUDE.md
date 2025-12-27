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

## Installation Methods

### Automated Installation (Recommended)

**Add marketplace directly from GitHub:**
```bash
/plugin marketplace add https://github.com/irfansofyana/my-claude-code-marketplace
```

This automatically clones the repository and makes all plugins available.

### Manual Installation (For Development)

Useful when developing plugins or working offline:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/irfansofyana/my-claude-code-marketplace.git
   cd my-claude-code-marketplace
   ```

2. **Add this marketplace to Claude Code:**
   ```bash
   /plugin marketplace add $(pwd)
   ```

   Or use an absolute path:
   ```bash
   /plugin marketplace add /path/to/my-claude-code-marketplace
   ```

3. **Browse available plugins interactively:**
   ```bash
   /plugin
   ```

4. **Install a plugin from this marketplace:**
   ```bash
   /plugin install plugin-name@my-claude-code-marketplace
   ```

5. **After making changes, reload the plugin:**
   ```bash
   /plugin uninstall plugin-name@my-claude-code-marketplace
   /plugin install plugin-name@my-claude-code-marketplace
   ```

### Plugin Management

- **Enable a plugin:** `/plugin enable plugin-name@my-claude-code-marketplace`
- **Disable a plugin:** `/plugin disable plugin-name@my-claude-code-marketplace`
- **Check installed commands:** `/help` (shows all available slash commands)

## Environment Configuration

### Required Environment Variables

Many plugins use MCP servers that require API keys. These MUST be configured in your shell configuration file for Claude Code to access them.

**Shell Configuration Files:**
- macOS (Zsh): `~/.zshrc`
- Linux (Bash): `~/.bashrc` or `~/.bash_profile`

**Required for shared-mcp plugin** (dependency for p-assist and common-engineering):
```bash
export TAVILY_API_KEY="your-tavily-api-key"     # https://tavily.com (free tier)
export EXA_API_KEY="your-exa-api-key"           # https://exa.ai (free tier)
```

**Optional for common-engineering plugin**:
```bash
export CONTEXT7_API_KEY="your-context7-api-key"  # https://context7.ai (for library docs)
```

**Required for p-assist plugin**:
```bash
export N8N_API_TOKEN="your-n8n-api-token"  # Your n8n personal assistant API token
```

**After adding variables**, reload your shell config:
```bash
source ~/.zshrc  # or source ~/.bashrc
```

**IMPORTANT**: Environment variables must be set in your shell config file (not just in terminal session) for Claude Code to access them. Claude Code reads environment variables from your shell at startup.

### Verifying Configuration

After configuring, verify variables are loaded:
```bash
echo $TAVILY_API_KEY  # Should display your API key
echo $EXA_API_KEY
echo $N8N_API_TOKEN   # Should display your n8n token
echo $CONTEXT7_API_KEY  # Should display your Context7 key (if using common-engineering)
```

If empty, reload your shell config or restart Claude Code.

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

- **00-shared-mcp** (`./plugins/00-shared-mcp`): **INSTALL FIRST** - Shared MCP infrastructure providing common web search (Tavily, Exa) and content extraction tools. Required by p-assist and common-engineering plugins.
  - **Requirements**: Node.js, API keys (TAVILY_API_KEY, EXA_API_KEY)
  - See environment configuration section above

- **01-p-assist** (`./plugins/01-p-assist`): Productivity plugin for knowledge management (Capacities), expense tracking, RSS feed monitoring (FreshRSS), and VPS management.
  - **Requires**: shared-mcp plugin, N8N_API_TOKEN
  - See `plugins/01-p-assist/README.md` for setup instructions

- **02-common-engineering** (`./plugins/02-common-engineering`): Essential toolkit for software engineers with Mermaid diagram generation, technical documentation writer (one-pagers, RFCs, proposals), automatic validation, and self-healing capabilities.
  - **Requires**: shared-mcp plugin, mermaid-cli (`npm install -g @mermaid-js/mermaid-cli`), CONTEXT7_API_KEY
  - **Optional**: document-skills plugin (for Word/PDF export from techdocs-writer)
  - See `plugins/02-common-engineering/README.md` for setup

- **03-sys-maint** (`./plugins/03-sys-maint`): System maintenance and cleanup utilities for Docker and disk space management with interactive preview and confirmation workflows.
  - **Requirements**: macOS, Docker (optional for docker-cleanup)

## Plugin Dependencies

Some plugins depend on others. Install dependencies first:

```
shared-mcp (install first)
├── p-assist (depends on shared-mcp for Tavily)
└── common-engineering (depends on shared-mcp for Exa)
```

Installation order:
1. `/plugin install shared-mcp@my-claude-code-marketplace`
2. `/plugin install p-assist@my-claude-code-marketplace` (optional)
3. `/plugin install common-engineering@my-claude-code-marketplace` (optional)

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
- Server key: `n8n_pa`
- Tool name: `get_public_collections_links`
- Full tool name: `mcp__plugin_p-assist_n8n_pa__get_public_collections_links` (57 chars ✓)

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
python3 scripts/validate-mcp-tool-names.py p-assist n8n_pa \
    archive_link create_link get_public_collections_links
```

The script will:
- Calculate the full tool name for each tool
- Check if any exceed 64 characters
- Provide suggestions if validation fails
- Exit with code 0 if valid, 1 if invalid

### Example Validation

```python
# Plugin: p-assist, Server: n8n_pa
# Longest tool: get_public_collections_links (28 chars)
full_name = "mcp__plugin_p-assist_n8n_pa__get_public_collections_links"
assert len(full_name) <= 64  # 57 chars ✓ PASS
```

## Key Constraints

- Plugin `name` in marketplace.json MUST match the `name` in the plugin's plugin.json
- The `source` path in marketplace.json is relative to the repository root
- Command files must be `.md` files with valid YAML frontmatter
- Changes to plugins require reinstalling them to take effect in Claude Code
- Use semantic versioning (1.0.0, 1.1.0, 2.0.0) when updating plugins
- **MCP tool names MUST be ≤64 characters for AWS Bedrock compatibility**
