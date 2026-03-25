---
name: analyze-cc-statements
description: >
  Analyze credit card statement CSV files, categorize transactions, and produce
  a markdown spending report with month-over-month comparison. Activate when the
  user says "analyze my credit card statement", "analyze cc statement", "spending
  analysis for YYYY-MM", "categorize my transactions", "credit card report",
  "analyze-cc-statements", or provides a month argument like "2026-03" in the
  context of credit card or transaction analysis.
allowed-tools: Read Write Glob Bash
---

This skill reads a month's credit card transactions from a CSV file, categorizes each transaction, and writes a structured markdown analysis report with month-over-month comparison and savings recommendations.

## Input requirements

- **Argument:** `YYYY-MM` (e.g., `2026-03`). This is required — if missing or malformed, inform the user of the expected format and stop.
- **Working directory:** The user must invoke this skill from a directory containing `trxns/` and `analysis/` subdirectories.
- **CSV path:** `./trxns/{YYYY-MM}.csv`
- **Output path:** `./analysis/{YYYY-MM}.md`

### CSV schema

```
card_last4, transaction_date, posting_date, description, amount, type, installment_info
```

- `amount` — numeric, may contain commas or currency symbols (strip before parsing)
- `type` — `debit` (purchase) or `credit` (payment to card)
- `installment_info` — mostly empty; if present, contains installment status (e.g., "5/12", "Final Settlement")

**Filter rule:** Only analyze rows where `type = debit`. Ignore `credit` rows — those are payments back to the card.

## Workflow

Follow these steps in order:

### 1. Validate the argument

Extract the YYYY-MM from the user's input. Verify it matches the `YYYY-MM` pattern (4-digit year, dash, 2-digit month, month between 01-12). If invalid, tell the user the expected format and stop.

### 2. Verify CSV file exists

Use the Glob tool to check if `./trxns/{YYYY-MM}.csv` exists. If the file does not exist, inform the user and stop.

### 3. Parse CSV using the helper script

Execute the helper script to accurately parse the CSV and get structured transaction data:

```bash
python3 <script_path>/scripts/parse_transactions.py ./trxns/{YYYY-MM}.csv
```

Where `<script_path>` is the path to this skill directory (derive it from the path to this SKILL.md file — the scripts directory is at `scripts/parse_transactions.py` relative to it).

The script returns JSON with:
- `debit_count` — count of all rows where `type = debit`
- `credit_count` — count of all rows where `type = credit`
- `total_debit` — sum of all debit amounts (before any adjustments)
- `total_credit` — sum of all credit amounts
- `transactions` — array of all debit transactions with fields: row, card, date, description, amount, installment
- `credits` — array of all credit transactions with fields: row, card, date, description, amount
- `cards` — sorted list of unique card_last4 values
- `date_range` — min/max transaction dates in ISO format
- `skipped_rows` — any rows that couldn't be parsed (malformed)

**Handle script errors:**
- If the script returns an error (file not found, empty file, wrong column count), inform the user and stop
- If `debit_count` is 0, inform the user that no spending transactions were found and stop — do not write an output file

### 4. Analyze for refunds, waivers, and reversals

**IMPORTANT**: Do not use `total_debit` from the script directly as the final spend. First, identify credits that are refunds/waivers/reversals (not card payments).

Using AI judgment, analyze both `transactions` (debits) and `credits` arrays to identify:

1. **Card payments** — credits with descriptions like "PAYMENT", "PEMBAYARAN TAGIHAN", "Pembayaran Kartu Kredit" — these are payments TO the card, NOT spending adjustments. Exclude from analysis.

2. **Refunds/waivers/reversals** — credits that reverse a specific debit:
   - Look for description keywords: "REFUND", "WAIVER", "FEE REVERSAL", "PEMBEBASAN", "REVERSAL", "CREDIT" (when not a payment)
   - Match to debits by: similar description keywords, same card, similar amount, credit date after debit date
   - Examples:
     - Debit "IURAN TAHUNAN 500000" + Credit "PEMBEBASAN IURAN TAHUNAN 500000" = waiver pair
     - Debit "APPLE.COM/BILL" + Credit "Credit IRL CORK APPLE.COM/BILL" = refund pair

3. **Net spending calculation**:
   - For each matched refund/waiver pair: exclude BOTH the debit and credit from spending analysis
   - Report matched pairs in a "Refunds & Waivers" section (transparency)
   - Final spend = sum of debits MINUS excluded refund/waiver amounts
   - Transaction count = debit_count MINUS number of matched debits (waived/refunded transactions are excluded)

4. **Unmatched credits** — if a credit doesn't match any debit and isn't a card payment, treat as miscellaneous credit (note it, but don't reduce spending)

### 5. Categorize transactions

For each transaction in the `transactions` array, infer a category from the `description` field. Read `references/categorization-guidelines.md` for the full categorization rules and merchant pattern mappings.

The categories are:
- **Food & Drinks** — sub-categorized as **Essential** or **Social**
- **Transport**
- **Shopping**
- **Subscriptions**
- **Health**
- **Bills & Utilities**
- **Other**

### 6. Aggregate and flag

Compute total spend per category (and sub-category for Food & Drinks). Flag any category where the total exceeds 40% of the overall spend as potentially disproportionate. This flagging is at the aggregate level — do not flag individual transactions.

### 6. Check for previous month's analysis

Compute the previous month's YYYY-MM:
- For months 02-12: subtract 1 from the month
- For month 01 (January): roll back to 12 (December) of the previous year

Use the Glob tool to check if `./analysis/{previous-YYYY-MM}.md` exists. If it exists, read it with the Read tool. Extract the category totals from the "Spend by Category" section (it's a pipe-delimited markdown table) for month-over-month comparison.

If the previous month's file does not exist, or its format cannot be parsed, skip the MoM comparison and note it in the output.

### 7. Write the analysis

Use the Write tool to create `./analysis/{YYYY-MM}.md`. Follow the template structure defined in `assets/templates/template.md`.

Fill in all sections:
1. **Header metadata** — month, date range, cards, transaction count (excluding waived/refunded), total spend (net of waivers)
2. **Refunds & Waivers** — if any refund/waiver pairs were identified, list them here with amounts (for transparency)
3. **Spend by Category** — table with totals, percentages, and flags
4. **Transaction Details by Category** — all transactions listed per category, sorted descending by amount (exclude waived/refunded transactions)
5. **Month-over-Month Comparison** — delta and percentage change per category (or "No previous month data available")
6. **Savings Recommendations** — opinionated, specific recommendations

### 8. Present summary

After writing the file, present a concise summary to the user:
- Total spend and number of transactions analyzed
- Top 3 categories by spend
- Any flagged categories (>40% of total)
- Key MoM changes (if available)
- File path of the written analysis

## MoM comparison logic

When the previous month's analysis file exists and is parseable:

- Compare each category's total month-over-month
- Calculate absolute delta and percentage change
- Flag categories with >30% increase as "Notable increase"
- Flag categories with >30% decrease as "Notable decrease"
- If a category appears in the current month but not the previous, mark as "New"
- If a category appeared in the previous month but not the current, mark as "Gone"

## Savings recommendations

Write 3-5 opinionated, specific savings recommendations based on:

- Categories flagged as disproportionately high (>40% of total spend)
- Categories with notable MoM increases (>30%)
- Food & Drinks Social spend relative to Food & Drinks Essential spend — if Social exceeds Essential, call it out
- Subscription accumulation — if multiple subscription entries exist, suggest an audit
- Reference actual merchant names from the transactions to make recommendations concrete

Be direct and specific. "You spent Rp 890,000 at Tokopedia this month — that's 35% of your Shopping category" is useful. "Consider reducing discretionary spending" is not.

## Reference materials

- Categorization rules: `references/categorization-guidelines.md`
- Output template: `assets/templates/template.md`
