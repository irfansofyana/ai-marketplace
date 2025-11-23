# My Claude Code Marketplace

A personal Claude Code marketplace for hosting custom plugins that extend Claude Code with slash commands, agents, skills, hooks, and MCP server integrations.

## What is This?

This repository serves as a marketplace for [Claude Code](https://claude.com/claude-code) plugins. Marketplaces are catalogs that allow you to organize, discover, and install custom functionality into Claude Code.

## Available Plugins

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


## Getting Started

### 1. Clone This Repository

```bash
git clone https://github.com/irfansofyana/my-claude-code-marketplace.git
cd my-claude-code-marketplace
```

### 2. Add This Marketplace to Claude Code

```bash
/plugin marketplace add $(pwd)
```

Or use an absolute path:

```bash
/plugin marketplace add /path/to/my-claude-code-marketplace
```

### 3. Browse Available Plugins

```bash
/plugin
```

This opens an interactive browser to explore and install plugins from this marketplace.

### 4. Install a Plugin

```bash
/plugin install p-assist@my-claude-code-marketplace
```

### 5. Use Plugin Commands

After installation, use the slash commands provided by the plugin:

```bash
/p-assist:summarize-article https://example.com/article
```

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

## License

This is a personal marketplace. Individual plugins may have their own licenses.
