---
description: Summarize an article from URL
argument-hint: [url]
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
```
