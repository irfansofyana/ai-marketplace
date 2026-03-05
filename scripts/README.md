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
# Validate n8n personal assistant tools for the p-assist plugin
python3 scripts/validate-mcp-tool-names.py p-assist n8n_pa \
    add_expense \
    capacities_daily_note \
    capacities_save_weblink \
    get_expenses_last_1_week \
    get_unread_items_freshRSS
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
Server: n8n_pa
Format: mcp__plugin_p-assist_n8n_pa__[tool-name]
AWS Bedrock Limit: 64 characters

  44 chars: mcp__plugin_p-assist_n8n_pa__add_expense ✓
  48 chars: mcp__plugin_p-assist_n8n_pa__capacities_daily_note ✓
  50 chars: mcp__plugin_p-assist_n8n_pa__capacities_save_weblink ✓
  53 chars: mcp__plugin_p-assist_n8n_pa__get_expenses_last_1_week ✓
  54 chars: mcp__plugin_p-assist_n8n_pa__get_unread_items_freshRSS ✓

================================================================================

Longest tool name: mcp__plugin_p-assist_n8n_pa__get_unread_items_freshRSS
Length: 54 characters
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
2. Abbreviate the server key (e.g., `n8n-personal-assistant` → `n8n_pa`)
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
