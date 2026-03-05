---
description: Get unread items from FreshRSS
---

# List Unread RSS Items

Get unread items from your FreshRSS feeds.

**Instructions:**

1. Use `mcp__plugin_p-assist_n8n_pa__get_unread_items_freshRSS` to fetch unread items

2. Format and present the results in a clear, scannable format

**Output Format:**

```
Unread RSS Items ([count])

## [Feed Name]
**[Article Title]**
Source: [Feed Name]
Date: [Published Date]
URL: [Article URL]

---

## [Feed Name]
**[Article Title]**
Source: [Feed Name]
Date: [Published Date]
URL: [Article URL]

---

**Summary:**
- Total unread items: [count]
- From [number] feeds
```

**Error Handling:**
- If no unread items found, inform user
- If API call fails, notify user

**Tips:**
- Consider saving interesting articles to Capacities using /p-assist:save-weblink
