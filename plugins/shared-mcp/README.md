# Shared MCP Plugin

Shared MCP infrastructure providing common web search, content extraction, and research tools that other plugins can use.

This repo also includes a Codex-native installer and config template under `codex/shared-mcp/` so the same MCP bundle can be added to Codex once and reused across Codex CLI and the IDE extension.

## Purpose

This plugin consolidates commonly-used MCP servers to:
- Reduce configuration overhead (configure API keys once)
- Share MCP server processes across plugins
- Provide consistent tool naming
- Simplify plugin dependencies

## Prerequisites

- Node.js (for npx - required by Tavily and Exa MCP servers)

## MCP Servers Included

| Server | Purpose | Tools Provided | Connection Type |
|--------|---------|----------------|-----------------|
| **Tavily** | Web search and content extraction | `tavily_search`, `tavily_extract`, `tavily_crawl`, `tavily_map` | stdio/npx |
| **Exa** | AI-powered web search and code context | `web_search_exa`, `get_code_context_exa`, `crawling_exa`, `deep_researcher_start/check` | stdio/npx |
| **Brave Search** | Privacy-focused web search with local business, image, video, and news search | `brave_web_search`, `brave_local_search`, `brave_image_search`, `brave_video_search`, `brave_news_search`, `brave_summarizer` | stdio/npx |

## Installation

### 1. Install the plugin

```bash
/plugin install shared-mcp@my-claude-code-marketplace
```

### 1b. Install the same MCP bundle for Codex

Codex stores MCP configuration in `~/.codex/config.toml` by default, and the CLI plus IDE extension share that configuration.

Global install:

```bash
bash codex/shared-mcp/install.sh --global
```

Project-scoped install:

```bash
bash codex/shared-mcp/install.sh --project
```

This writes a managed block with these Codex MCP server names:

- `shared_mcp_tavily`
- `shared_mcp_exa`
- `shared_mcp_brave_search`

The installer forwards your existing shell environment variables instead of copying API keys into the repo.

If you prefer to edit Codex config manually, copy the template from `codex/shared-mcp/config.toml` into `~/.codex/config.toml` or `.codex/config.toml`.

### 2. Configure Environment Variables

**IMPORTANT**: Add these to your shell configuration file so they persist across sessions and are available to Claude Code.

**Shell Config File Location:**
- macOS (Zsh): `~/.zshrc`
- Linux (Bash): `~/.bashrc` or `~/.bash_profile`

**Add these lines to your shell config file:**
```bash
# Tavily API Key (https://tavily.com - free tier available)
export TAVILY_API_KEY="your-tavily-api-key"

# Exa API Key (https://exa.ai - free tier available)
export EXA_API_KEY="your-exa-api-key"

# Brave Search API Key (https://brave.com/search/api - free tier available)
export BRAVE_API_KEY="your-brave-api-key"
```

**After adding**, reload your shell configuration:
```bash
# For Zsh (macOS)
source ~/.zshrc

# For Bash (Linux)
source ~/.bashrc
```

**Verify variables are loaded:**
```bash
echo $TAVILY_API_KEY  # Should display your API key
echo $EXA_API_KEY
echo $BRAVE_API_KEY
```

**Getting API Keys:**
- **Tavily**: Sign up at [tavily.com](https://tavily.com) - Free tier available
- **Exa**: Sign up at [exa.ai](https://exa.ai) - Free tier available
- **Brave Search**: Sign up at [brave.com/search/api](https://brave.com/search/api) - Free tier available

## Tool Name Format

Tools from this plugin follow the naming pattern:
```
mcp__plugin_shared-mcp_[server]__[tool_name]
```

**Examples:**
- `mcp__plugin_shared-mcp_tavily__tavily_search`
- `mcp__plugin_shared-mcp_exa__web_search_exa`

## Plugins That Depend on This

The following plugins require `shared-mcp` to be installed:

- **p-assist**: Uses Tavily for article summarization and web content extraction
- **common-engineering**: Uses Exa for web research and code context

## Troubleshooting

### Environment variables not found

**Problem**: MCP servers fail with "API key not set" errors.

**Solution**:
1. Verify variables are in your shell config file (`~/.zshrc` or `~/.bashrc`)
2. Reload config: `source ~/.zshrc` (or `source ~/.bashrc`)
3. Restart Claude Code completely
4. Test: `echo $TAVILY_API_KEY` should show your key

### MCP server not starting

1. Ensure environment variables are set correctly (see above)
2. Check that Node.js is installed: `node --version`
3. Check that `npx` is available: `npx --version` (required for Tavily and Exa)
4. Verify API keys are valid by testing at the provider's website
5. For Codex installs, verify the servers are registered: `codex mcp list`

### Tool not found

Ensure the plugin is installed and enabled:
```bash
/plugin list
/plugin enable shared-mcp@my-claude-code-marketplace
```

For Codex installs:

```bash
codex mcp list
```

If needed, reinstall the managed block:

```bash
bash codex/shared-mcp/install.sh --global
```

## Version History

- **1.0.0**: Initial release with Tavily, Jina, and Exa MCP servers
- **1.1.0**: Updated Jina MCP to use direct SSE connection instead of stdio/npx (November 2025)
- **1.2.0**: Updated Jina MCP endpoint from `/sse` to `/v1` with Streamable HTTP transport (December 2025)
- **1.3.0**: Removed Jina MCP server (December 2025)
- **1.4.0**: Added Brave Search MCP server for privacy-focused web search (April 2026)
- **1.5.0**: Added Codex-native MCP installer and config template for the shared Tavily, Exa, and Brave bundle (April 2026)
