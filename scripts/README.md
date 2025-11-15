# Validation Scripts

This directory contains scripts for validating plugin configurations and ensuring compatibility with various Claude Code integrations.

## validate-mcp-tool-names.py

Validates that MCP tool names comply with AWS Bedrock's 64-character limit.

### Why This Matters

AWS Bedrock has a strict 64-character maximum for tool names. When Claude Code generates MCP tool names, it uses the format:

```
mcp__plugin_[plugin-name]_[server-key]__[tool-name]
```

If any part of this naming scheme is too long, the resulting tool names may exceed AWS Bedrock's limit, making the plugin incompatible.

### Usage

```bash
python3 scripts/validate-mcp-tool-names.py <plugin-name> <server-key> <tool1> <tool2> ...
```

### Example

```bash
# Validate Linkwarden tools for the p-assist plugin
python3 scripts/validate-mcp-tool-names.py p-assist linkwd \
    archive_link \
    create_collection \
    create_link \
    delete_collection_by_id \
    get_public_collections_links
```

### Output

The script will:
- Display each tool's full name and character count
- Mark tools that exceed 64 characters with ✗
- Show the longest tool name
- Provide suggestions if validation fails
- Exit with code 0 (success) or 1 (failure)

### Example Output

```
================================================================================
MCP Tool Name Validation for AWS Bedrock
================================================================================

Plugin: p-assist
Server: linkwd
Format: mcp__plugin_p-assist_linkwd__[tool-name]
AWS Bedrock Limit: 64 characters

  41 chars: mcp__plugin_p-assist_linkwd__archive_link ✓
  40 chars: mcp__plugin_p-assist_linkwd__create_link ✓
  57 chars: mcp__plugin_p-assist_linkwd__get_public_collections_links ✓

================================================================================

Longest tool name: mcp__plugin_p-assist_linkwd__get_public_collections_links
Length: 57 characters
Status: ✓ PASS - All tools within limit

✓ All tool names are AWS Bedrock compatible!
```

### When to Use

Run this validation:
- Before adding a new MCP server to a plugin
- When renaming a plugin
- When changing MCP server keys
- Before deploying to production
- As part of CI/CD pipeline (exit code indicates pass/fail)

### Tips

If validation fails:
1. Shorten the plugin name (e.g., `personal-assistant` → `p-assist`)
2. Abbreviate the server key (e.g., `linkwarden` → `linkwd`)
3. Consider if the tool names can be shortened (consult MCP server documentation)

### Integration with CI/CD

Add to your validation pipeline:

```bash
# Exit code 0 = all tools valid
# Exit code 1 = one or more tools exceed limit
python3 scripts/validate-mcp-tool-names.py my-plugin my-server tool1 tool2
if [ $? -ne 0 ]; then
    echo "❌ MCP tool name validation failed!"
    exit 1
fi
```
