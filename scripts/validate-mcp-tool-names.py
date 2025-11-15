#!/usr/bin/env python3
"""
Validate MCP tool names for AWS Bedrock compatibility.

AWS Bedrock has a 64-character maximum for tool names.
This script validates that all MCP tool names in a plugin stay within this limit.

Usage:
    python3 scripts/validate-mcp-tool-names.py <plugin-name> <server-key> <tool-names...>

Example:
    python3 scripts/validate-mcp-tool-names.py p-assist linkwd \
        archive_link create_link get_public_collections_links
"""

import sys


def validate_tool_names(plugin_name: str, server_key: str, tools: list[str]) -> bool:
    """
    Validate that all MCP tool names are within AWS Bedrock's 64-character limit.

    Args:
        plugin_name: The plugin name (e.g., 'p-assist')
        server_key: The MCP server key (e.g., 'linkwd')
        tools: List of tool names from the MCP server

    Returns:
        True if all tool names are valid, False otherwise
    """
    print("=" * 80)
    print("MCP Tool Name Validation for AWS Bedrock")
    print("=" * 80)
    print(f"\nPlugin: {plugin_name}")
    print(f"Server: {server_key}")
    print(f"Format: mcp__plugin_{plugin_name}_{server_key}__[tool-name]")
    print(f"AWS Bedrock Limit: 64 characters\n")

    max_length = 0
    longest_tool = ""
    over_limit = []

    for tool in tools:
        full_name = f"mcp__plugin_{plugin_name}_{server_key}__{tool}"
        length = len(full_name)
        status = "✓" if length <= 64 else "✗ EXCEEDS LIMIT"

        print(f"  {length:2d} chars: {full_name} {status}")

        if length > max_length:
            max_length = length
            longest_tool = full_name

        if length > 64:
            over_limit.append((full_name, length))

    print("\n" + "=" * 80)
    print(f"\nLongest tool name: {longest_tool}")
    print(f"Length: {max_length} characters")
    print(f"Status: {'✓ PASS - All tools within limit' if max_length <= 64 else '✗ FAIL - Some tools exceed limit'}")

    if over_limit:
        print(f"\n⚠️  WARNING: {len(over_limit)} tool(s) exceed the 64-character limit:")
        for tool, length in over_limit:
            print(f"  - {tool} ({length} chars)")
        print("\nSuggestions:")
        print("  1. Shorten the plugin name")
        print("  2. Abbreviate the server key")
        print("  3. Both of the above")
        return False
    else:
        print("\n✓ All tool names are AWS Bedrock compatible!")
        return True


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    plugin_name = sys.argv[1]
    server_key = sys.argv[2]
    tools = sys.argv[3:]

    is_valid = validate_tool_names(plugin_name, server_key, tools)
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
