---
description: Save a bookmark to Linkwarden with metadata
argument-hint: [url] [description] [collection]
---

# Save Bookmark to Linkwarden

Save the following bookmark to Linkwarden:

- **URL:** $1
- **Description:** $2
- **Collection:** $3

**Instructions:**

1. First, check if the collection exists:
   - Use `mcp__plugin_p-assist_linkwd__get_all_collections` to list collections
   - Find the collection ID matching "$3" (case-insensitive)
   - If collection doesn't exist, list available collections and ask user to choose

2. Fetch the URL content briefly to generate a better name:
   - Try `mcp__plugin_shared-mcp_tavily__tavily_extract` to get page title and content
   - If Tavily fails, use a simple format based on the URL domain (e.g., "Content from example.com")
   - Extract the page title from the content for the bookmark name

3. Extract or generate relevant tags:
   - Based on the description "$2"
   - Based on the URL domain or content type
   - Keep tags concise and relevant (2-4 tags)

4. Save the bookmark using `mcp__plugin_p-assist_linkwd__create_link`:
   - `url`: $1
   - `name`: Generated from page title
   - `description`: $2
   - `collectionId`: Found collection ID
   - `tags`: Array of tag objects with `name` fields

5. Confirm successful save with details

**Output Format:**

```
✓ Bookmark saved to Linkwarden

**Name:** [Page Title]
**URL:** $1
**Collection:** $3
**Tags:** #tag1 #tag2 #tag3
**Description:** $2

**Quick Access:**
- View all bookmarks: /p-assist:list-bookmarks
```

**Error Handling:**
- If collection "$3" doesn't exist, show available collections
- If URL is invalid, notify user
- If tags can't be generated, use generic tags based on collection
