# P-Assist Plugin

A comprehensive productivity plugin for Claude Code that provides article summarization, journal management (Logseq), and bookmark organization (Linkwarden) capabilities.

## Prerequisites

**Important**: This plugin requires the `shared-mcp` plugin to be installed first. The shared-mcp plugin provides common MCP servers (Tavily, Jina) used for web search and content extraction.

```bash
# Install shared-mcp first
/plugin install shared-mcp@my-claude-code-marketplace

# Then install p-assist
/plugin install p-assist@my-claude-code-marketplace
```

## Features

- **Article Summarization**: Extract and summarize web articles using Tavily (from shared-mcp), optionally save to Linkwarden
- **Journal Management**: Create and search Logseq journal entries
- **Bookmark Management**: Save and organize bookmarks in Linkwarden
- **Web Research**: AI-powered web search and content extraction using shared-mcp tools

## MCP Server Configuration

This plugin uses MCP (Model Context Protocol) servers to integrate with external services.

### Dependency: shared-mcp Plugin

The following services are provided by the `shared-mcp` plugin (install it first):
- **Tavily**: Web search and content extraction
- **Jina**: Advanced web reading and content processing

See the [shared-mcp README](../00-shared-mcp/README.md) for API key configuration.

### Plugin-Specific Environment Variables

These environment variables are specific to p-assist:

#### Logseq Integration (`logseq`)
- `LOGSEQ_API_TOKEN`: Your Logseq API token
  - Get this from your Logseq instance (Settings → Features → Enable API)
- `LOGSEQ_API_URL`: Your Logseq API URL (default: `http://localhost:12315`)

#### Linkwarden Integration (`linkwd`)
- `LINKWARDEN_BASE_URL`: Your Linkwarden instance URL
  - Example: `https://your-linkwarden-instance.com`
- `LINKWARDEN_TOKEN`: Your Linkwarden API token
  - Get this from your Linkwarden account settings

### Setup Instructions

1. **Install and configure shared-mcp first** (for Tavily and Jina):
   ```bash
   /plugin install shared-mcp@my-claude-code-marketplace
   ```
   See [shared-mcp README](../00-shared-mcp/README.md) for API key setup.

2. **Set up Logseq:**
   ```bash
   export LOGSEQ_API_TOKEN="your_logseq_api_token_here"
   export LOGSEQ_API_URL="http://localhost:12315"  # or your Logseq instance URL
   ```

3. **Set up Linkwarden:**
   ```bash
   export LINKWARDEN_BASE_URL="https://your-linkwarden-instance.com"
   export LINKWARDEN_TOKEN="your_linkwarden_api_token_here"
   ```

4. **For persistent configuration**, add these to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.):
   ```bash
   # Logseq
   export LOGSEQ_API_TOKEN="your_logseq_api_token_here"
   export LOGSEQ_API_URL="http://localhost:12315"

   # Linkwarden
   export LINKWARDEN_BASE_URL="https://your-linkwarden-instance.com"
   export LINKWARDEN_TOKEN="your_linkwarden_api_token_here"
   ```

## Available Commands

### Journal Management

#### `/p-assist:journal-entry [entry content]`
Create a new journal entry in Logseq.

**Example:**
```bash
/p-assist:journal-entry Today I worked on the new feature launch and had a productive meeting with the team.
```

#### `/p-assist:search-journal [search query]`
Search through your Logseq journal entries.

**Example:**
```bash
/p-assist:search-journal project updates
```

### Bookmark Management

#### `/p-assist:save-bookmark [url] [description] [collection]`
Save a bookmark to Linkwarden.

**Example:**
```bash
/p-assist:save-bookmark https://example.com/article "Interesting article about AI" "AI Research"
```

#### `/p-assist:list-bookmarks [collection] [search query]`
List bookmarks from Linkwarden with optional filtering.

**Example:**
```bash
/p-assist:list-bookmarks "AI Research" machine learning
```

### Article Management

#### `/p-assist:summarize-article [url] [save]`
Summarize a web article and optionally save it to Linkwarden.

**Example:**
```bash
/p-assist:summarize-article https://example.com/article save
```

## Agents

### Productivity Orchestrator
A specialized agent that coordinates multi-step productivity workflows including:
- Research and summarization
- Bookmark management
- Journal operations

The orchestrator agent automatically handles complex tasks that involve multiple tools and services.

## Dependencies

### System Requirements
- **Docker**: Required for the Linkwarden MCP server
- **uv (Python package manager)**: Required for the Logseq MCP server
- **Internet connection**: For web search and article fetching

### MCP Servers Used
- **logseq** (p-assist): Logseq integration server
- **linkwd** (p-assist): Linkwarden bookmark management
- **tavily** (shared-mcp): AI-powered web search and content extraction
- **jina** (shared-mcp): Advanced web reading, screenshots, and image search

## Troubleshooting

### Common Issues

1. **Logseq connection failed:**
   - Ensure Logseq is running with API enabled
   - Verify `LOGSEQ_API_TOKEN` and `LOGSEQ_API_URL` are correct
   - Check that your Logseq instance is accessible at the specified URL

2. **Linkwarden connection failed:**
   - Verify Docker is running
   - Check `LINKWARDEN_BASE_URL` and `LINKWARDEN_TOKEN` are correct
   - Ensure your Linkwarden instance is accessible

3. **Docker MCP server not starting:**
   - Make sure Docker daemon is running
   - Check if you have permission to run Docker commands
   - Verify the Docker image `ghcr.io/irfansofyana/linkwarden-mcp-server:v0.1.0` can be pulled

### Verification

Test your configuration by running:
```bash
# Test Logseq integration
/p-assist:journal-entry "Test entry - please delete me"

# Test Linkwarden integration
/p-assist:list-bookmarks
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