---
description: Get a curated news briefing from FreshRSS with full content extraction and summarization
argument-hint: [limit] [keywords] [save]
---

# Curated News Briefing

Create a personalized news briefing from your unread RSS items.

**Arguments:**
- **Limit:** $1 (number of items to process, default: 5)
- **Keywords:** $2 (optional keywords to filter items)
- **Save:** $3 (if "save", also save briefing to Capacities)

**Instructions:**

1. **Fetch RSS Items:**
   - Use `mcp__plugin_p-assist_n8n_pa__get_unread_items_freshRSS` to get unread items
   - If no items returned, inform user and exit

2. **Filter Items:**
   - If keywords ($2) are provided, filter items matching those keywords
   - Otherwise, take the first N items where N = $1 (default: 5)

3. **Process Each Item:**
   For each selected item:
   - Extract the URL from the RSS item
   - Use `mcp__plugin_shared-mcp_tavily__tavily_extract` with the URL to get full content
   - Summarize the content in 2-3 sentences
   - Extract 3-5 key takeaways

4. **Present Briefing:**

```
# Curated News Briefing ([Today's date])

## [Feed Name]
**[Article Title]**
[URL]

**Summary:**
[2-3 sentence overview of the article]

**Key Takeaways:**
- [Key point 1]
- [Key point 2]
- [Key point 3]

---

## [Feed Name]
**[Article Title]**
[URL]

**Summary:**
[2-3 sentence overview]

**Key Takeaways:**
- [Key point 1]
- [Key point 2]

---

**Briefing Summary:**
Processed [count] articles from [count] feeds.

[If $3 equals "save": ✓ Saved to Capacities daily note]
```

5. **Optional Save to Capacities:**
   - If $3 equals "save", compile the entire briefing into markdown
   - Use `mcp__plugin_p-assist_n8n_pa__capacities_daily_note` to save
   - Confirm save to user

**Error Handling:**
- If no unread RSS items, inform user
- If Tavily extraction fails for an item, skip and note which items failed
- If keywords provided but no matches, inform user and suggest alternatives

**Tips:**
- Use this daily to catch up on important news
- Add keywords to focus on specific topics (e.g., "AI", "startup", "security")
- Use "save" argument to archive briefings in Capacities
