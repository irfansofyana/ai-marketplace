# Shared MCP Plugin

Shared MCP infrastructure providing common web search, content extraction, and research tools that other plugins can use.

## Purpose

This plugin consolidates commonly-used MCP servers to:
- Reduce configuration overhead (configure API keys once)
- Share MCP server processes across plugins
- Provide consistent tool naming
- Simplify plugin dependencies

## Prerequisites

- Node.js (for npx)
- npm

## MCP Servers Included

| Server | Purpose | Tools Provided |
|--------|---------|----------------|
| **Tavily** | Web search and content extraction | `tavily_search`, `tavily_extract`, `tavily_crawl`, `tavily_map` |
| **Jina** | Content reading and URL processing | `read_url`, `search_web`, `search_images`, `search_arxiv`, and more |
| **Exa** | AI-powered web search and code context | `web_search_exa`, `get_code_context_exa`, `crawling_exa`, `deep_researcher_start/check` |

## Installation

### 1. Install the plugin

```bash
/plugin install shared-mcp@my-claude-code-marketplace
```

### 2. Configure Environment Variables

Add the following to your environment or Claude Code settings:

```bash
# Tavily API Key (https://tavily.com)
export TAVILY_API_KEY="your-tavily-api-key"

# Jina API Key (https://jina.ai)
export JINA_API_KEY="your-jina-api-key"

# Exa API Key (https://exa.ai)
export EXA_API_KEY="your-exa-api-key"
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

### MCP server not starting

1. Ensure environment variables are set correctly
2. Check that `npx` is available in your PATH
3. Verify API keys are valid

### Tool not found

Ensure the plugin is installed and enabled:
```bash
/plugin list
/plugin enable shared-mcp@my-claude-code-marketplace
```

## Version History

- **1.0.0**: Initial release with Tavily, Jina, and Exa MCP servers
