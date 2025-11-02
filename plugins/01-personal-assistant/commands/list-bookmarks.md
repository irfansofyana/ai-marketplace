---
description: List recent bookmarks from Linkwarden with smart filtering
argument-hint: [collection] [search query]
---

# List Bookmarks

List recent bookmarks from Linkwarden with intelligent filtering to prevent information overload:

- **Collection filter:** $1 (optional) - Filter by specific collection name
- **Search query:** $2 (optional) - Search within bookmarks
- **Default behavior:** Shows 8 most recent bookmarks to ensure Claude can process information effectively

**Instructions:**

1. **Determine filtering approach:**
   - If $1 is provided: Filter by collection name and show 8 most recent from that collection
   - If $2 is provided: Search across all collections and show 8 most relevant results
   - If neither: Show 8 most recent bookmarks across all collections

2. **Handle collection filtering (if $1 provided):**
   - Use `mcp__linkwarden__get_all_collections` to list collections
   - Find collection ID matching "$1" (case-insensitive)
   - If collection doesn't exist, show available collections and suggest correct names

3. **Fetch bookmarks with proper parameter defaults:**
   - Use `mcp__linkwarden__get_all_links` with these parameters:
     - `collectionId`: Collection ID if filtering by collection, otherwise 0
     - `cursor: 0` - First page only (limits results to manageable amount)
     - `pinnedOnly: false` - Include all bookmarks
     - `searchByDescription: false` - Disable unless searching
     - `searchByName: true` - Always search names
     - `searchByTags: false` - Disable unless searching
     - `searchByTextContent: false` - Disable to reduce processing
     - `searchByUrl: false` - Disable unless searching
     - `searchQueryString`: Search query ($2) if provided, otherwise ""
     - `sort: 0` - Newest first (most relevant for recent bookmarks)
     - `tagId: 0` - No specific tag filter

4. **Process results intelligently:**
   - If more than 8 bookmarks returned, show only the first 8
   - Truncate descriptions longer than 100 characters
   - Organize by relevance (newest first for default, relevance for search)

5. **Present results in concise format**

**Output Format:**

```
# Recent Bookmarks [from Collection: "$1"] [matching: "$2"]

Showing X of Y bookmarks (showing most recent):

1. **[Bookmark Title]**
   📁 [Collection] • 🔗 [URL]
   📝 [Description truncated to 100 chars if longer]

2. **[Bookmark Title]**
   📁 [Collection] • 🔗 [URL]
   📝 [Description truncated to 100 chars if longer]

---
**Tips:**
• Use collection name to filter: /personal-assistant:list-bookmarks "Collection Name"
• Search within bookmarks: /personal-assistant:list-bookmarks "" "search terms"
• Save new bookmark: /personal-assistant:save-bookmark [url] [description] [collection]
```

**Error Handling:**

**If no bookmarks found:**
```
# No Bookmarks Found

No bookmarks found matching your criteria.

**Suggestions:**
• Try a different collection name
• Use broader search terms
• Check if bookmarks exist: /personal-assistant:list-bookmarks
```

**If collection not found:**
```
# Collection Not Found

Collection "$1" not found.

**Available Collections:**
• Collection A
• Collection B
• Collection C

**Usage:** /personal-assistant:list-bookmarks "Collection Name"
```

**Parameter Adjustments for Search Mode:**
When $2 (search query) is provided, enable these search parameters:
- `searchByDescription: true`
- `searchByUrl: true`
- `searchQueryString: "$2"`
- Keep other parameters the same

**Processing Rules:**
- Always limit to 8 bookmarks maximum for Claude processing
- Truncate descriptions at 100 characters with "..." if longer
- Show total count for context (e.g., "Showing 8 of 24 bookmarks")
- Use emojis for visual clarity (📁 📝 🔗)
- Provide actionable tips for getting different results
