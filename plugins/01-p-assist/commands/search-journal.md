---
description: Search your Logseq journals for specific topics or keywords
argument-hint: [search query]
---

# Search Journal

Search your Logseq journals for: "$ARGUMENTS"

**Instructions:**

1. Use `mcp__logseq__search` with the query: $ARGUMENTS
2. Set search parameters:
   - `include_pages: true` - to search page names
   - `include_blocks: true` - to search block content
   - `limit: 20` - to get top 20 results
3. Analyze and organize the results by:
   - Relevance to the search query
   - Date/chronological order if available
   - Context and related information
4. Present results in a clear, scannable format

**Output Format:**

```
# Search Results: "$ARGUMENTS"

Found X relevant entries:

## [Entry Title / Date]
**Source:** [page name]
**Content:**
[excerpt or full content]

---

## [Entry Title / Date]
**Source:** [page name]
**Content:**
[excerpt or full content]

---

## Summary
[Brief overview of patterns or insights across results]
```

**Additional Notes:**
- Highlight the most relevant excerpts
- If no results found, suggest alternative search terms
- Group related entries when possible
