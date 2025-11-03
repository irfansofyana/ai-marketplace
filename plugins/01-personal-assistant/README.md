# Personal Assistant Plugin

A comprehensive productivity plugin for Claude Code that provides article summarization, journal management (Logseq), and bookmark organization (Linkwarden) capabilities.

## Features

- **Article Summarization**: Summarize web articles and optionally save them to Linkwarden
- **Journal Management**: Create and search Logseq journal entries
- **Bookmark Management**: Save and organize bookmarks in Linkwarden
- **Web Search**: AI-powered web search using Exa

## MCP Server Configuration

This plugin uses MCP (Model Context Protocol) servers to integrate with external services. You'll need to configure the following environment variables:

### Required Environment Variables

#### Logseq Integration (`mcp-logseq`)
- `LOGSEQ_API_TOKEN`: Your Logseq API token
  - Get this from your Logseq instance (Settings → Features → Enable API)
- `LOGSEQ_API_URL`: Your Logseq API URL (default: `http://localhost:12315`)

#### Linkwarden Integration (`linkwarden`)
- `LINKWARDEN_BASE_URL`: Your Linkwarden instance URL
  - Example: `https://your-linkwarden-instance.com`
- `LINKWARDEN_TOKEN`: Your Linkwarden API token
  - Get this from your Linkwarden account settings

### Setup Instructions

1. **Set up Logseq:**
   ```bash
   export LOGSEQ_API_TOKEN="your_logseq_api_token_here"
   export LOGSEQ_API_URL="http://localhost:12315"  # or your Logseq instance URL
   ```

2. **Set up Linkwarden:**
   ```bash
   export LINKWARDEN_BASE_URL="https://your-linkwarden-instance.com"
   export LINKWARDEN_TOKEN="your_linkwarden_api_token_here"
   ```

3. **For persistent configuration**, add these to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.):
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

#### `/personal-assistant:journal-entry [entry content]`
Create a new journal entry in Logseq.

**Example:**
```bash
/personal-assistant:journal-entry Today I worked on the new feature launch and had a productive meeting with the team.
```

#### `/personal-assistant:search-journal [search query]`
Search through your Logseq journal entries.

**Example:**
```bash
/personal-assistant:search-journal project updates
```

### Bookmark Management

#### `/personal-assistant:save-bookmark [url] [description] [collection]`
Save a bookmark to Linkwarden.

**Example:**
```bash
/personal-assistant:save-bookmark https://example.com/article "Interesting article about AI" "AI Research"
```

#### `/personal-assistant:list-bookmarks [collection] [search query]`
List bookmarks from Linkwarden with optional filtering.

**Example:**
```bash
/personal-assistant:list-bookmarks "AI Research" machine learning
```

### Article Management

#### `/personal-assistant:summarize-article [url] [save]`
Summarize a web article and optionally save it to Linkwarden.

**Example:**
```bash
/personal-assistant:summarize-article https://example.com/article save
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
- **mcp-logseq**: Logseq integration server
- **exa**: AI-powered web search
- **linkwarden-mcp-server**: Linkwarden bookmark management

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
/personal-assistant:journal-entry "Test entry - please delete me"

# Test Linkwarden integration
/personal-assistant:list-bookmarks
```

## Development

To modify or extend this plugin:

1. Edit commands in the `commands/` directory
2. Update MCP configuration in `.claude-plugin/plugin.json`
3. Test changes by reinstalling the plugin:
   ```bash
   /plugin uninstall personal-assistant@my-claude-code-marketplace
   /plugin install personal-assistant@my-claude-code-marketplace
   ```

## License

This plugin is part of the Claude Code Marketplace.