---
description: Add a new expense record
argument-hint: [amount] [currency] [description]
---

# Add Expense

Add a new expense to your tracking sheet.

**Arguments:**
- **Amount:** $1
- **Currency:** $2 (e.g., USD, EUR, IDR)
- **Description:** $3

**Instructions:**

1. Parse the arguments or ask user for missing values:
   - Amount: required
   - Currency: required (default to user's preferred currency)
   - Description: required
   - Date: optional (defaults to today)

2. Use `mcp__plugin_p-assist_n8n_pa__add_expense` to add the expense:
   - `amount`: The expense amount ($1)
   - `currency`: The currency code ($2)
   - `description`: Description of the expense ($3)
   - `date`: Today's date (or user-specified date)

3. Confirm the expense was added successfully

**Output Format:**

```
Expense added successfully

**Amount:** $1 $2
**Description:** $3
**Date:** [Today's date]

**Quick Actions:**
- View expenses: /p-assist:expenses
```

**Error Handling:**
- If amount is invalid, notify user
- If currency code is invalid, notify user
- If description is empty, prompt user for it
