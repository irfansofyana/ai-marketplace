---
description: Summarize an article from URL with optional Linkwarden save
argument-hint: [url] [save]
---

# Summarize Article

Fetch and summarize the article at: $1

**Instructions:**

1. Use `mcp__exa__web_search_exa` to fetch the content from the URL
2. Analyze and create a comprehensive summary including:
   - Main topic and key points (3-5 bullet points)
   - Key insights or takeaways
   - Target audience or use case
3. Present the summary in clear, readable markdown format

**Optional Linkwarden Save:**

If $2 equals "save":
- Use `mcp__linkwarden__create_link` to save the article to Linkwarden
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
