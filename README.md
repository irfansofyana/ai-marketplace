# My Claude Code Marketplace

A personal Claude Code marketplace for hosting custom plugins that extend Claude Code with slash commands, agents, skills, hooks, and MCP server integrations.

## What is This?

This repository serves as a marketplace for [Claude Code](https://claude.com/claude-code) plugins. Marketplaces are catalogs that allow you to organize, discover, and install custom functionality into Claude Code.

## Available Plugins

| Plugin | Description | Requirements |
|--------|-------------|--------------|
| **[shared-mcp](./plugins/shared-mcp/)** | **INSTALL FIRST** - MCP infrastructure for web search (Tavily, Exa) | Node.js, TAVILY_API_KEY, EXA_API_KEY |
| **[p-assist](./plugins/p-assist/)** | Productivity: expenses, RSS, VPS | shared-mcp, N8N_API_TOKEN |
| **[common-engineering](./plugins/common-engineering/)** | Engineering tools: code review, Mermaid diagrams, tech docs (RFCs, proposals, ADRs) | shared-mcp, mermaid-cli, CONTEXT7_API_KEY |
| **[sys-maint](./plugins/sys-maint/)** | System maintenance: Docker cleanup, disk analysis | macOS only |
| **[thinking-tools](./plugins/thinking-tools/)** | Idea refinery: pressure-test ideas through conversation, produce concise Idea Briefs | None |
| **[softskills](./plugins/softskills/)** | Office politics coach for navigating workplace dynamics | None |

See individual plugin READMEs for detailed setup instructions.

## Available Skills

Skills are model-invoked capabilities that Claude can activate when triggered by natural language. They are organized by plugin:

### common-engineering Skills

| Skill | Trigger Phrases | Output |
|-------|-----------------|--------|
| `mermaid` | "create a diagram", "draw architecture", "sequence diagram for..." | Validated Mermaid diagrams (sequence, architecture, flowchart) |
| `one-pager` | "write a one-pager", "create a proposal", "draft a one-pager" | 1-3 page stakeholder approval document |
| `adr` | "write an ADR", "document architecture decision", "compare X vs Y" | 1-3 page Architecture Decision Record |
| `rfc` | "write an RFC", "design proposal for cross-team review" | 5-15 page Request for Comments |
| `tsd` | "write a TSD", "document an API", "API spec" | 5-20 page Technical Specification Document |
| `poc-experiment` | "write a POC document", "Go/No-Go recommendation" | 3-8 page proof of concept with decision |
| `code-review` | "review my code", "review this branch", "check my diff" | Structured review report with severity-classified findings |
| `project-management-plan` | "project plan excel", "Gantt chart", "project tracker" | Excel workbook with 4 tabs (plan, charters, budget, RAID) |

### thinking-tools Skills

| Skill | Trigger Phrases | Output |
|-------|-----------------|--------|
| `idea-refinery` | "pressure-test my idea", "sparring partner", "gut-check this idea" | Concise Idea Brief with problem, MVP, risks, next actions |

### softskills Skills

| Skill | Trigger Phrases | Output |
|-------|-----------------|--------|
| `office-politics-coach` | "office politics", "navigate this situation", "difficult coworker" | Reframe, options, and word-for-word scripts for workplace dynamics |

## Quick Start

### 1. Add Marketplace

```bash
/plugin marketplace add https://github.com/irfansofyana/my-claude-code-marketplace
```

### 2. Configure Environment Variables

Add to `~/.zshrc` (macOS) or `~/.bashrc` (Linux):

```bash
export TAVILY_API_KEY="your-tavily-api-key"     # https://tavily.com
export EXA_API_KEY="your-exa-api-key"           # https://exa.ai
export N8N_API_TOKEN="your-n8n-token"           # https://n8n.io (for p-assist)
```

Reload: `source ~/.zshrc` or `source ~/.bashrc`

### 3. Install Plugins (in dependency order)

```bash
/plugin install shared-mcp@my-claude-code-marketplace     # REQUIRED - install first
/plugin install p-assist@my-claude-code-marketplace       # Optional
/plugin install common-engineering@my-claude-code-marketplace  # Optional
/plugin install sys-maint@my-claude-code-marketplace      # Optional (macOS only)
/plugin install thinking-tools@my-claude-code-marketplace # Optional
```

### Manual Installation (Alternative)

For local development or offline access:

```bash
git clone https://github.com/irfansofyana/my-claude-code-marketplace.git
cd my-claude-code-marketplace
/plugin marketplace add $(pwd)
```

## Using with Other AI Agents (via OPKG)

This marketplace works with [OpenPackage (OPKG)](https://openpackage.dev) for 30+ AI platforms (Cursor, Windsurf, Cline, OpenCode, etc.).

OPKG maps the universal structure to your platform's format:

| Universal | Claude Code | Cursor | OpenCode |
|-----------|-------------|--------|----------|
| `commands/` | `.claude/commands/` | `.cursor/commands/` | `.opencode/commands/` |
| `agents/` | `.claude/agents/` | `.cursor/agents/` | `.opencode/agents/` |
| `skills/` | `.claude/skills/` | `.cursor/skills/` | `.opencode/skills/` |

**Learn More:** [OPKG Docs](https://openpackage.dev/docs) | [GitHub](https://github.com/enulus/OpenPackage)

## Plugin Management

```bash
/plugin                                    # Browse and install plugins
/plugin enable|disable <plugin>@marketplace
/plugin uninstall <plugin>@marketplace
/help                                      # View all commands
```

## Creating a Plugin

```
plugins/my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Required: name, description, version, author
├── commands/                 # Optional: slash commands (.md files)
├── agents/                   # Optional: subagent definitions
├── skills/                   # Optional: SKILL.md files
├── hooks/                    # Optional: hooks.json
└── .mcp.json                # Optional: MCP server config
```

**1. Create `plugin.json`:**
```json
{
  "name": "my-plugin",
  "description": "What it does",
  "version": "1.0.0",
  "author": { "name": "irfansofyana" }
}
```

**2. Register in `.claude-plugin/marketplace.json`:**
```json
{
  "name": "my-plugin",
  "source": "./plugins/my-plugin",
  "description": "Brief description"
}
```

**3. Test:**
```bash
/plugin uninstall my-plugin@my-claude-code-marketplace
/plugin install my-plugin@my-claude-code-marketplace
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| API key not found | Add to shell config, reload (`source ~/.zshrc`), restart Claude Code |
| MCP server not responding | Check Node.js (`node --version`), verify API keys |
| Plugin install failed | Ensure marketplace added first, install shared-mcp first |

## Learn More

- [Claude Code Docs](https://docs.claude.com/en/docs/claude-code)
- [OPKG Docs](https://openpackage.dev/docs)

---

**Author:** irfansofyana
