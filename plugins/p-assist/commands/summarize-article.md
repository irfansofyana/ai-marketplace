---
description: Summarize an article from URL with optional Capacities save
argument-hint: [url] [save]
---

# Summarize Article

Fetch and summarize the article at: $1

**Instructions:**

1. Extract content from the URL using `mcp__plugin_shared-mcp_tavily__tavily_extract`
   - If extraction fails or exceeds token limits, inform the user that the URL could not be processed
   - Suggest they either provide the article text directly or use a browser extension to copy the content
2. Analyze and create a comprehensive summary including:
   - Main topic and key points (3-5 bullet points)
   - Key insights or takeaways
   - Target audience or use case
3. Present the summary in clear, readable markdown format

**Optional Capacities Save:**

If $2 equals "save":
- Use `mcp__plugin_p-assist_n8n_pa__capacities_save_weblink` to save the article to Capacities
- Use the article title as the weblink title
- Include the summary in the description field
- Add relevant tags based on the content

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

[If saved to Capacities: "✓ Saved to Capacities as a weblink"]
```
