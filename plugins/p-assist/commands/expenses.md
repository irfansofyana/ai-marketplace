---
description: Query expenses by date range (interactive)
argument-hint: [optional: pre-select range like "today", "week", "month"]
---

# Query Expenses

Query your expenses from a specific time period.

**Instructions:**

1. If the user provided a range in $ARGUMENTS, use that. Otherwise, ask the user to select a date range:

**Ask the user:**
"What date range would you like to view expenses for?"

Options:
- Today
- Last 7 days
- Last 2 weeks
- Last 1 month
- Custom range (specify dates)

2. Based on the user's selection, call the appropriate n8n tool:
   - **Today**: `mcp__plugin_p-assist_n8n_pa__get_today_expense`
   - **Last 7 days**: `mcp__plugin_p-assist_n8n_pa__get_expenses_last_1_week`
   - **Last 2 weeks**: `mcp__plugin_p-assist_n8n_pa__get_expenses_last_2_weeks`
   - **Last 1 month**: `mcp__plugin_p-assist_n8n_pa__get_expenses_last_1_month`

3. If custom range is requested, verify it's within 1 month and inform user of the limitation if exceeded.

4. Format and present the results in a clear table format

**Output Format:**

```
Expenses for: [Selected Date Range]

| Date | Amount | Currency | Source | Description |
|------|--------|----------|--------|-------------|
| ... | ... | ... | ... | ... |

**Total:** [Sum of all amounts]
```

**Notes:**
- Always return the data in table format to the end user
- If no expenses found, inform the user
- Sort by date (most recent first)
