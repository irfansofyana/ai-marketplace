---
description: Update an existing expense record
argument-hint: [expense_id] [new_amount] [new_currency]
---

# Update Expense

Update an existing expense record.

**Arguments:**
- **Expense ID/Email:** $1 (the identifier to match the expense)
- **New Amount:** $2
- **New Currency:** $3

**Instructions:**

1. Parse the arguments or ask user for missing values:
   - Expense ID/Email: required (used to match the expense record)
   - New Amount: required
   - New Currency: required

2. Use `mcp__plugin_p-assist_n8n_pa__update_expense` to update the expense:
   - `email_id__using_to_match_`: The expense identifier ($1)
   - `amount`: The new amount ($2)
   - `currency`: The new currency ($3)

3. Confirm the expense was updated successfully

**Output Format:**

```
Expense updated successfully

**Expense ID:** $1
**New Amount:** $2 $3

**Quick Actions:**
- View expenses: /p-assist:expenses
```

**Error Handling:**
- If expense ID is not found, notify user
- If amount is invalid, notify user
- If currency code is invalid, notify user
