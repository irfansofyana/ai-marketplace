---
description: Create a new entry in your Logseq journal
argument-hint: [entry content]
---

# Create Journal Entry

Create a new Logseq journal entry with the following content:

"$ARGUMENTS"

**Instructions:**

1. Format the entry content appropriately:
   - Use proper markdown formatting
   - Add relevant tags using #hashtag format
   - Include timestamps if needed
   - Structure with bullet points or headings as appropriate

2. Generate a descriptive page title:
   - If the content is date-specific, use format: "Journal - YYYY-MM-DD"
   - If it's a topic note, use a descriptive title from the content
   - Keep titles concise and searchable

3. Use `mcp__plugin_p-assist_logseq__create_page` to create the entry:
   - `title`: Generated page title
   - `content`: Formatted entry content

4. Confirm the entry was created successfully

**Output Format:**

```
✓ Journal entry created successfully

**Title:** [page title]

**Content Preview:**
[First few lines of the entry]

**Tips:**
- Find this entry with: /p-assist:search-journal [keyword]
- View in Logseq to add more context or links
```

**Content Enhancement:**
- Automatically add today's date if not specified
- Suggest relevant tags based on content
- Format lists and structure for readability
