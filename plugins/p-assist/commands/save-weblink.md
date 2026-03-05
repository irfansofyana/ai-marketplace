---
description: Save a URL to Capacities as a weblink
argument-hint: [url] [title] [description]
---

# Save Weblink to Capacities

Save the following URL to Capacities:

- **URL:** $1
- **Title:** $2
- **Description:** $3

**Instructions:**

1. Fetch the URL content briefly to generate better metadata:
   - Use `mcp__plugin_shared-mcp_tavily__tavily_extract` to get page title and content
   - If Tavily fails, use the provided title or a simple format based on the URL domain

2. Save the weblink using `mcp__plugin_p-assist_n8n_pa__capacities_save_weblink`:
   - `parameters1_Value`: The URL ($1)
   - `parameters2_Value`: The title ($2 or extracted from page)
   - `parameters3_Value`: The description ($3 or generated from content)
   - `parameters5_Value`: Any additional context or notes in markdown format

3. Confirm successful save with details

**Output Format:**

```
Weblink saved to Capacities

**Title:** [Page Title]
**URL:** $1
**Description:** [Description]

**Quick Access:**
- View in Capacities to add more context or organize
```

**Error Handling:**
- If URL is invalid, notify user
- If fetching fails, proceed with provided title/description
- Generate sensible defaults if title/description not provided
