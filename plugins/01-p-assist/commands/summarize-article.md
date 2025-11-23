---
description: Summarize an article from URL with optional Linkwarden save
argument-hint: [url] [save]
---

# Summarize Article

Fetch and summarize the article at: $1

**Instructions:**

1. Extract content from the URL using a two-tier approach:
   - **Primary**: Try `mcp__plugin_shared-mcp_tavily__tavily_extract` first (faster, works for most articles)
   - **Fallback**: If Tavily fails with "exceeds maximum allowed tokens" error, use `mcp__plugin_shared-mcp_jina__read_url`
   - Jina handles large content better and stays within token limits
2. Analyze and create a comprehensive summary including:
   - Main topic and key points (3-5 bullet points)
   - Key insights or takeaways
   - Target audience or use case
3. Present the summary in clear, readable markdown format

**Optional Linkwarden Save:**

If $2 equals "save":
- Use `mcp__plugin_p-assist_linkwd__create_link` to save the article to Linkwarden
- Use a descriptive name based on the article title
- Add relevant tags based on the content
- Include the summary in the description field

**Output Format:**

```
# [Article Title]

**URL:** [url]

## Summary
[2-3 sentence overview]

## Key Points
- Point 1
- Point 2
- Point 3

## Takeaways
[Key insights or actionable items]

[If saved to Linkwarden: "✓ Saved to Linkwarden in [collection name]"]
```
