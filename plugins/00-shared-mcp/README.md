# Shared MCP Plugin

Shared MCP infrastructure providing common web search, content extraction, and research tools that other plugins can use.

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
| **Jina** | Content reading and URL processing | `read_url`, `search_web`, `search_images`, `search_arxiv`, and more | SSE (Server-Sent Events) |
| **Exa** | AI-powered web search and code context | `web_search_exa`, `get_code_context_exa`, `crawling_exa`, `deep_researcher_start/check` | stdio/npx |

## Installation

### 1. Install the plugin

```bash
/plugin install shared-mcp@my-claude-code-marketplace
```

### 2. Configure Environment Variables

**IMPORTANT**: Add these to your shell configuration file so they persist across sessions and are available to Claude Code.

**Shell Config File Location:**
- macOS (Zsh): `~/.zshrc`
- Linux (Bash): `~/.bashrc` or `~/.bash_profile`

**Add these lines to your shell config file:**
```bash
# Tavily API Key (https://tavily.com - free tier available)
export TAVILY_API_KEY="your-tavily-api-key"

# Jina API Key (https://jina.ai - free tier available)
export JINA_API_KEY="your-jina-api-key"

# Exa API Key (https://exa.ai - free tier available)
export EXA_API_KEY="your-exa-api-key"
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
echo $JINA_API_KEY
echo $EXA_API_KEY
```

**Getting API Keys:**
- **Tavily**: Sign up at [tavily.com](https://tavily.com) - Free tier available
- **Jina**: Sign up at [jina.ai](https://jina.ai) - Free tier available
- **Exa**: Sign up at [exa.ai](https://exa.ai) - Free tier available

## Tool Name Format

Tools from this plugin follow the naming pattern:
```
mcp__plugin_shared-mcp_[server]__[tool_name]
```

**Examples:**
- `mcp__plugin_shared-mcp_tavily__tavily_search`
- `mcp__plugin_shared-mcp_jina__read_url`
- `mcp__plugin_shared-mcp_exa__web_search_exa`

## Plugins That Depend on This

The following plugins require `shared-mcp` to be installed:

- **p-assist**: Uses Tavily and Jina for article summarization and web content extraction
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

### Tool not found

Ensure the plugin is installed and enabled:
```bash
/plugin list
/plugin enable shared-mcp@my-claude-code-marketplace
```

## Recent Updates

### November 2025: Jina MCP Configuration Updated

The Jina MCP server configuration has been updated to use a direct SSE (Server-Sent Events) connection instead of the previous stdio/npx approach. This change:
- Removes the dependency on `mcp-remote` npm package for Jina tools
- Improves connection reliability for Jina tools
- Reduces startup time for Jina tools
- Maintains all existing functionality
- Still requires Node.js/npx for Tavily and Exa tools

Previous configuration required npx and mcp-remote:
```json
"jina": {
  "type": "stdio",
  "command": "npx",
  "args": [
    "-y",
    "mcp-remote",
    "https://mcp.jina.ai/sse",
    "--header",
    "Authorization: Bearer ${JINA_API_KEY}"
  ],
  "env": {
    "JINA_API_KEY": "${JINA_API_KEY}"
  }
}
```

Updated configuration uses direct SSE:
```json
"jina": {
  "type": "sse",
  "url": "https://mcp.jina.ai/sse",
  "headers": {
    "Authorization": "Bearer ${JINA_API_KEY}"
  }
}
```

## Version History

- **1.0.0**: Initial release with Tavily, Jina, and Exa MCP servers
- **1.1.0**: Updated Jina MCP to use direct SSE connection instead of stdio/npx (November 2025)
