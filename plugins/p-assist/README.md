# P-Assist Plugin

> **⚠️ NOTICE: This plugin is for personal use only.**
>
> This plugin integrates with a private n8n instance (`automate.irfansp.dev`) and is configured specifically for the author's personal infrastructure. It is **not intended for use by others**.
>
> If you're interested in building similar functionality, use this plugin as a reference and adapt it to your own services and infrastructure.

A comprehensive productivity plugin for Claude Code that provides expense tracking, RSS feed monitoring, and VPS management capabilities.

## Prerequisites

**Important**: This plugin requires the `shared-mcp` plugin to be installed first. The shared-mcp plugin provides common MCP servers (Tavily, Exa) used for web search and content extraction.

```bash
# Install shared-mcp first
/plugin install shared-mcp@my-claude-code-marketplace

# Then install p-assist
/plugin install p-assist@my-claude-code-marketplace
```

## Features

- **Expense Tracking**: Track and query expenses with flexible date ranges
- **RSS Monitoring**: Fetch unread items from FreshRSS, curated news briefings with full content extraction
- **VPS Management**: Check utilization and restart your VPS
- **Web Research**: AI-powered web search and content extraction using shared-mcp tools

## MCP Server Configuration

This plugin uses MCP (Model Context Protocol) servers to integrate with external services.

### Dependency: shared-mcp Plugin

The following services are provided by the `shared-mcp` plugin (install it first):
- **Tavily**: Web search and content extraction
- **Exa**: AI-powered web search and code context

See the [shared-mcp README](../shared-mcp/README.md) for API key configuration.

### Plugin-Specific Environment Variables

This plugin uses the n8n MCP server for all integrations:

#### n8n Personal Assistant Integration (`n8n_pa`)
- `N8N_API_TOKEN`: Your n8n personal assistant API token
  - Required for accessing expenses, RSS, and VPS tools

### Setup Instructions

**IMPORTANT**: All environment variables must be added to your shell configuration file to persist across sessions.

**Shell Config File Location:**
- macOS (Zsh): `~/.zshrc`
- Linux (Bash): `~/.bashrc` or `~/.bash_profile`

1. **Install and configure shared-mcp first** (provides Tavily and Exa):
   ```bash
   /plugin install shared-mcp@my-claude-code-marketplace
   ```
   See [shared-mcp README](../shared-mcp/README.md) for API key setup.

2. **Set up n8n API token** (add to shell config file):
   ```bash
   export N8N_API_TOKEN="your_n8n_api_token_here"
   ```

3. **Reload your shell configuration:**
   ```bash
   # For Zsh (macOS)
   source ~/.zshrc

   # For Bash (Linux)
   source ~/.bashrc
   ```

4. **Verify variables are loaded:**
   ```bash
   echo $N8N_API_TOKEN  # Should show your token
   ```

5. **Restart Claude Code** to ensure it picks up the new environment variables.

## Available Commands

### Expense Management

#### `/p-assist:expenses [range]`
Query expenses by date range (interactive). The command will prompt you to select from:
- Today
- Last 7 days
- Last 2 weeks
- Last 1 month
- Custom range (within 1 month)

**Example:**
```bash
/p-assist:expenses
# Or specify a range directly:
/p-assist:expenses last week
```

#### `/p-assist:add-expense [amount] [currency] [description]`
Add a new expense to your tracking sheet.

**Example:**
```bash
/p-assist:add-expense 29.99 USD "Cloud hosting services"
```

#### `/p-assist:update-expense [expense_id] [new_amount] [new_currency]`
Update an existing expense record.

**Example:**
```bash
/p-assist:update-expense abc123@example.com 39.99 USD
```

### Article Management

#### `/p-assist:summarize-article [url]`
Summarize a web article.

**Example:**
```bash
/p-assist:summarize-article https://example.com/article
```

### RSS & System Management

#### `/p-assist:curated-news [limit] [keywords]`
Get a curated news briefing from FreshRSS with full content extraction and summarization.

**Arguments:**
- `limit` - Number of items to process (default: 5)
- `keywords` - Optional keywords to filter items

**Example:**
```bash
/p-assist:curated-news 10 AI startup
```

#### `/p-assist:list-rss`
Get unread items from FreshRSS.

#### `/p-assist:check-vps`
Check your VPS resource utilization.

#### `/p-assist:restart-vps`
Restart your VPS (requires confirmation).

## Skills

### `analyze-cc-statements`

Analyze credit card statement CSV files, categorize transactions, and produce a markdown spending report with month-over-month comparison.

**Directory structure required** (invoke from this root):
```
your-cc-directory/
├── trxns/
│   ├── 2026-02.csv
│   └── 2026-03.csv
└── analysis/          # Created by the skill
    ├── 2026-02.md
    └── 2026-03.md
```

**CSV schema:**
```
card_last4, transaction_date, posting_date, description, amount, type, installment_info
```

**Usage:**
```
analyze-cc-statements 2026-03
```

The skill will:
1. Read and parse `trxns/2026-03.csv`
2. Filter out credit card payments (`type = credit`)
3. Categorize each transaction: Food & Drinks (Essential/Social), Transport, Shopping, Subscriptions, Health, Bills & Utilities, Other
4. Flag categories exceeding 40% of total spend
5. Compare with previous month's analysis if available
6. Write `analysis/2026-03.md` with full breakdown and savings recommendations

## Dependencies

### MCP Servers Used
- **n8n_pa** (p-assist): n8n personal assistant integration
- **tavily** (shared-mcp): AI-powered web search and content extraction
- **exa** (shared-mcp): AI-powered web search and code context

## Troubleshooting

### Common Issues

1. **n8n API connection failed:**
   - Verify `N8N_API_TOKEN` is set correctly
   - Check that your n8n instance is accessible at `https://automate.irfansp.dev/mcp/personal-assistant`

2. **Web search/content extraction not working:**
   - Ensure shared-mcp plugin is installed
   - Verify `TAVILY_API_KEY` and `EXA_API_KEY` are set

3. **Environment variables not loaded:**
   - Make sure variables are in your shell config file (~/.zshrc or ~/.bashrc)
   - Run `source ~/.zshrc` (or ~/.bashrc) to reload
   - Restart Claude Code after setting variables

### Verification

Test your configuration by running:
```bash
# Test expense tracking
/p-assist:expenses

# Test RSS
/p-assist:list-rss

# Test curated news briefing
/p-assist:curated-news 3
```

## Development

To modify or extend this plugin:

1. Edit commands in the `commands/` directory
2. Update MCP configuration in `.claude-plugin/plugin.json`
3. Test changes by reinstalling the plugin:
   ```bash
   /plugin uninstall p-assist@my-claude-code-marketplace
   /plugin install p-assist@my-claude-code-marketplace
   ```

## License

This plugin is part of the Claude Code Marketplace.
