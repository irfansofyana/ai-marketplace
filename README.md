# My Claude Code Marketplace

A personal Claude Code marketplace for hosting custom plugins that extend Claude Code with slash commands, agents, skills, hooks, and MCP server integrations.

## What is This?

This repository serves as a marketplace for [Claude Code](https://claude.com/claude-code) plugins. Marketplaces are catalogs that allow you to organize, discover, and install custom functionality into Claude Code.

## Available Plugins

### [shared-mcp](./plugins/00-shared-mcp/)
**INSTALL FIRST** - Shared MCP infrastructure providing common web search, content extraction, and research tools. This plugin provides Tavily (web search), Jina (content extraction), and Exa (AI-powered search) tools that are used by other plugins in this marketplace.

**Required dependency** for p-assist and common-engineering plugins.

See [plugins/00-shared-mcp/README.md](./plugins/00-shared-mcp/README.md) for detailed setup instructions and API key configuration.

### [p-assist](./plugins/01-p-assist/)
Productivity plugin for article summarization, journal management (Logseq), and bookmark organization (Linkwarden).

See [plugins/01-p-assist/README.md](./plugins/01-p-assist/README.md) for detailed setup and usage instructions.

### [common-engineering](./plugins/02-common-engineering/)
Essential toolkit for software engineers that currently focuses on professional Mermaid diagram generation with automatic
validation, self-healing, and support for sequence, architecture, and flowchart diagrams. Future updates will add more
common engineering utilities.

See [plugins/02-common-engineering/README.md](./plugins/02-common-engineering/README.md) for installation prerequisites and
full feature documentation.

### [sys-maint](./plugins/03-sys-maint/)
System maintenance and cleanup utilities for Docker and disk space management. Provides interactive commands with preview
and confirmation workflows for safely cleaning up Docker resources and analyzing disk usage.

See [plugins/03-sys-maint/README.md](./plugins/03-sys-maint/README.md) for usage instructions and safety features.


## Prerequisites

### System Dependencies

Different plugins require different system dependencies. Install what you need:

**For all plugins:**
- Node.js (required for Tavily and Exa MCP servers in shared-mcp)
  - Check: `node --version`
  - Install: https://nodejs.org

**For common-engineering plugin:**
- mermaid-cli (for diagram generation)
  - Install: `npm install -g @mermaid-js/mermaid-cli`
  - Verify: `mmdc --version`

**For p-assist plugin:**
- Docker (for Linkwarden integration)
  - Check: `docker --version`
  - Install: https://www.docker.com/get-started
- uv (Python package manager, for Logseq integration)
  - Install: `pip install uv` or use system package manager

**For sys-maint plugin:**
- macOS only (uses platform-specific tools)
- Docker (optional, for docker-cleanup command)

### API Keys

The following API keys are required for shared-mcp (used by multiple plugins):

| Service | Free Tier | Sign Up URL | Required For |
|---------|-----------|-------------|--------------|
| Tavily | ✓ Yes | https://tavily.com | Web search, article extraction |
| Jina | ✓ Yes | https://jina.ai | Content reading, screenshots |
| Exa | ✓ Yes | https://exa.ai | AI-powered search, code context |
| Logseq | N/A (local) | - | Journal management (p-assist) |
| Linkwarden | Self-hosted | - | Bookmark management (p-assist) |

See the "Environment Setup" section in Quick Start for configuration details.

## Quick Start (Automated)

### 1. Add Marketplace via GitHub

```bash
/plugin marketplace add https://github.com/irfansofyana/my-claude-code-marketplace
```

This automatically clones the marketplace and makes all plugins available for installation.

### 2. Configure Environment Variables (Required)

The plugins in this marketplace require API keys for MCP servers. Add these to your shell configuration file:

**For Zsh (macOS default):** `~/.zshrc`
**For Bash:** `~/.bashrc` or `~/.bash_profile`

```bash
# Required for shared-mcp plugin (install this first)
export TAVILY_API_KEY="your-tavily-api-key"     # Get from https://tavily.com
export JINA_API_KEY="your-jina-api-key"         # Get from https://jina.ai
export EXA_API_KEY="your-exa-api-key"           # Get from https://exa.ai

# Optional: For p-assist plugin features
export LOGSEQ_API_TOKEN="your-logseq-token"     # Logseq Settings → Features → Enable API
export LOGSEQ_API_URL="http://localhost:12315" # Default Logseq API URL
export LINKWARDEN_BASE_URL="https://your-linkwarden.com"
export LINKWARDEN_TOKEN="your-linkwarden-token"
```

**After adding these variables**, reload your shell configuration:
```bash
# For Zsh
source ~/.zshrc

# For Bash
source ~/.bashrc
```

### 3. Verify Environment Variables

Check that variables are loaded correctly:
```bash
echo $TAVILY_API_KEY  # Should show your API key
echo $JINA_API_KEY    # Should show your API key
echo $EXA_API_KEY     # Should show your API key
```

### 4. Install Plugins

Browse and install plugins interactively:
```bash
/plugin
```

Or install directly in dependency order:
```bash
# Install in this order (respects dependencies)
/plugin install shared-mcp@my-claude-code-marketplace     # REQUIRED: Install first
/plugin install p-assist@my-claude-code-marketplace       # Optional
/plugin install common-engineering@my-claude-code-marketplace  # Optional
/plugin install sys-maint@my-claude-code-marketplace      # Optional (macOS only)
```

## Manual Installation (Alternative)

If you prefer to manage the repository yourself or need offline access:

### 1. Clone This Repository
```bash
git clone https://github.com/irfansofyana/my-claude-code-marketplace.git
cd my-claude-code-marketplace
```

### 2. Add Local Marketplace to Claude Code
```bash
/plugin marketplace add $(pwd)
```

Or use an absolute path:
```bash
/plugin marketplace add /path/to/my-claude-code-marketplace
```

### 3. Configure Environment Variables

Follow the same environment setup steps from "Quick Start" section above.

### 4. Install Plugins

Follow the same plugin installation steps from "Quick Start" section above.

## Plugin Management

### Enable/Disable Plugins

```bash
/plugin enable p-assist@my-claude-code-marketplace
/plugin disable p-assist@my-claude-code-marketplace
```

### Uninstall Plugins

```bash
/plugin uninstall p-assist@my-claude-code-marketplace
```

### View Available Commands

```bash
/help
```

Shows all installed slash commands from all enabled plugins.

## Creating a New Plugin

### Directory Structure

```
plugins/02-my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Required: plugin metadata
├── commands/                 # Optional: custom slash commands
│   └── command-name.md
├── agents/                   # Optional: custom agent definitions
├── skills/                   # Optional: Agent Skills
│   └── skill-name/
│       └── SKILL.md
├── hooks/                    # Optional: event handlers
│   └── hooks.json
└── .mcp.json                # Optional: MCP server integration
```

### Step-by-Step Guide

1. **Create Plugin Directory:**

```bash
mkdir -p plugins/02-my-plugin/.claude-plugin
mkdir -p plugins/02-my-plugin/commands
```

2. **Create `plugin.json`:**

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

3. **Register in Marketplace:**

Edit `.claude-plugin/marketplace.json` and add your plugin to the `plugins` array:

```json
{
  "name": "my-plugin",
  "source": "./plugins/02-my-plugin",
  "description": "Brief description for marketplace listing"
}
```

4. **Add Commands:**

Create `commands/my-command.md`:

```markdown
---
description: What this command does
---

# Command Instructions

Detailed instructions for Claude Code when this command is executed.
This becomes the prompt that Claude receives.
```

5. **Test Your Plugin:**

```bash
/plugin uninstall my-plugin@my-claude-code-marketplace  # if previously installed
/plugin install my-plugin@my-claude-code-marketplace
/my-plugin:my-command
```

## Plugin Components

### Slash Commands
Markdown files in `commands/` directory that provide custom prompts to Claude Code. Commands are invoked as `/plugin-name:command-name`.

### Agents
Custom agent definitions that can be invoked via the Task tool for specialized workflows.

### Skills
Agent Skills are model-invoked capabilities that agents can use. Defined in `skills/` directory with a `SKILL.md` file.

### Hooks
Event handlers defined in `hooks/hooks.json` that execute shell commands in response to Claude Code events.

### MCP Servers
Model Context Protocol server configurations in `.mcp.json` for external tool integrations.

## Development Workflow

1. Make changes to your plugin files
2. Uninstall the plugin: `/plugin uninstall plugin-name@my-claude-code-marketplace`
3. Reinstall the plugin: `/plugin install plugin-name@my-claude-code-marketplace`
4. Test your changes

## Key Requirements

- Plugin `name` in marketplace.json MUST match the `name` in the plugin's plugin.json
- The `source` path in marketplace.json is relative to the repository root
- Command files must be `.md` files with valid YAML frontmatter
- Use semantic versioning (1.0.0, 1.1.0, 2.0.0) when updating plugins

## Contributing

1. Create a new plugin following the structure above
2. Register it in `.claude-plugin/marketplace.json`
3. Test locally using the development workflow
4. Commit your changes

## Repository Structure

```
my-claude-code-marketplace/
├── .claude-plugin/
│   └── marketplace.json     # Marketplace manifest
├── plugins/
│   ├── 00-shared-mcp/      # Shared MCP infrastructure (Tavily, Jina, Exa)
│   ├── 01-p-assist/        # Productivity assistant plugin
│   ├── 02-common-engineering/ # Engineering tools and diagram generation
│   └── 03-sys-maint/       # System maintenance and cleanup
├── CLAUDE.md               # Instructions for Claude Code
└── README.md               # This file
```

## Author

**irfansofyana**

## Learn More

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Plugin Development Guide](https://docs.claude.com/en/docs/claude-code)

## Troubleshooting

### Environment Variables Not Loaded

**Problem**: MCP servers fail to start with "API key not found" errors.

**Solution**:
1. Verify variables are in your shell config file (`~/.zshrc` or `~/.bashrc`)
2. Reload the config: `source ~/.zshrc` (or `source ~/.bashrc`)
3. Restart Claude Code completely
4. Check variables are loaded: `echo $TAVILY_API_KEY`

### MCP Server Connection Failed

**Problem**: Plugin shows "MCP server not responding" errors.

**Solution**:
1. Check Node.js is installed: `node --version`
2. For Tavily/Exa: Verify `npx` works: `npx --version`
3. For p-assist: Verify Docker is running: `docker ps`
4. Check API keys are valid by testing the service websites

### Plugin Installation Failed

**Problem**: `/plugin install` command fails.

**Solution**:
1. Ensure marketplace is added first: `/plugin marketplace list`
2. Check internet connection (for GitHub-based installation)
3. Install shared-mcp before other plugins (dependency requirement)

### Shell Config File Not Loading

**Problem**: Variables disappear after closing terminal.

**Solution**:
1. macOS: Add to `~/.zshrc` (default shell is Zsh)
2. Linux: Add to `~/.bashrc` or `~/.bash_profile`
3. Ensure file is being sourced automatically (add if missing):
   ```bash
   # In ~/.zshrc or ~/.bashrc
   export TAVILY_API_KEY="..."
   # ... other exports
   ```

## License

This is a personal marketplace. Individual plugins may have their own licenses.
