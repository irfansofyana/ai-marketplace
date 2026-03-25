---
name: analyze-cc-statements
description: >
  Analyze credit card statement CSV files, categorize transactions, and produce
  a markdown spending report with month-over-month comparison. Activate when the
  user says "analyze my credit card statement", "analyze cc statement", "spending
  analysis for YYYY-MM", "categorize my transactions", "credit card report",
  "analyze-cc-statements", or provides a month argument like "2026-03" in the
  context of credit card or transaction analysis.
allowed-tools: Read Write Glob Bash Agent
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

**Tell the user:** "Parsing CSV file to extract transaction data..."

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

3. **Build matched pairs list**:
   - Create `matched_waiver_pairs` array with objects: `{debit_row, debit_amount, debit_description, credit_row, credit_amount, credit_description}`
   - Calculate `waived_debits_total` = sum of all `debit_amount` in matched pairs
   - Calculate `waived_credits_total` = sum of all `credit_amount` in matched pairs
   - **GUARDRAIL CHECK**: Verify that `waived_debits_total` equals `waived_credits_total` (or document any discrepancy). These should match because each waiver credit reverses its corresponding debit.

4. **Net spending calculation** (CRITICAL - avoid double-counting):
   - `total_debit_raw` = `total_debit` from parser (includes ALL debits, including waived ones)
   - `gross_spend` = `total_debit_raw` - `waived_debits_total`
   - **GUARDRAIL CHECK**: Verify `gross_spend` equals the sum of all non-waived debits. If using categorized transactions sum, it should match.
   - Transaction count for report = `debit_count` - (number of matched waiver debits)
   - **IMPORTANT**: The waiver credit is NOT subtracted again — it simply cancels out the waived debit. Do NOT do: `gross_spend - waived_credits_total` — that would double-count the waiver.

5. **Unmatched credits** — if a credit doesn't match any debit and isn't a card payment, treat as miscellaneous credit:
   - Add to `unmatched_credits` array for reporting
   - Calculate `unmatched_credits_total` = sum of all unmatched credit amounts
   - These WILL reduce the final spend (see step 6)
   - **GUARDRAIL CHECK**: Ensure no credit is counted as both a waiver match AND an unmatched credit. Each credit should be classified exactly once: (1) card payment, (2) waiver/refund match, or (3) unmatched miscellaneous.

6. **Filter transactions for categorization**: Create a filtered list of transactions excluding those that were matched with refunds/waivers. These are the transactions to categorize.

### 5. Categorize transactions using parallel subagents

**Tell the user first:** "Starting parallel categorization of {N} transactions across {M} subagents..."

**Determine chunk size and number of subagents:**
- If ≤50 transactions: use 1 subagent (no parallelization needed)
- If 51-150 transactions: split into 2 chunks, launch 2 subagents in parallel
- If 151-300 transactions: split into 3-4 chunks, launch 3-4 subagents in parallel
- If >300 transactions: split into 5-6 chunks, launch 5-6 subagents in parallel
- Maximum chunk size: 60 transactions per subagent

**Chunking strategy:**
- Divide transactions array into roughly equal chunks
- Each chunk should have contiguous transactions (no randomization needed)
- Track chunk index for each subagent (0, 1, 2, ...)

**Launch all subagents in parallel** using the Agent tool. For each chunk, launch a subagent with this prompt:

```
Categorize these credit card transactions according to the guidelines.

TRANSACTIONS TO CATEGORIZE (Chunk {chunk_num}/{total_chunks}):
{JSON array of transactions for this chunk}

CATEGORIZATION GUIDELINES:
Read and follow: references/categorization-guidelines.md

Categories available:
- Food & Drinks — sub-categorize as Essential (groceries, supermarkets) or Social (restaurants, cafes, bars)
- Transport — ride-hailing, fuel, parking, tolls, public transit
- Shopping — e-commerce, retail, fashion, electronics
- Subscriptions — streaming, software, gaming, recurring memberships, CLOUD SERVICES
- Health — pharmacies, clinics, hospitals, fitness
- Bills & Utilities — electricity, water, internet, insurance, phone
- Other — anything that doesn't fit above

CRITICAL RULES (common errors to avoid):
1. CLOUD SERVICES → Subscriptions, NOT Transport:
   - "ALIBABA CLOUD", "ANYCLOUD", "AWS", "GOOGLE CLOUD", "AZURE" → Subscriptions
   - "PROTON" (ProtonVPN/Mail), "NANONOBLE" → Subscriptions
   - Any transaction with "CLOUD", "HOSTING", "SERVER" → Subscriptions
2. INSTALLMENTS → categorize by MERCHANT, NOT as "Other":
   - "CICILAN BCA SMARTPHONE", "CICILAN MATAHARI" → Shopping
   - Look at the merchant name to determine category
3. GRAB* entries:
   - "GRAB*FOOD" → Food & Drinks (Social)
   - "GRAB*TRANSPORT", "GRAB*CAR" → Transport
4. APPLE.COM/BILL, GOOGLE* → Subscriptions (if software/service), Shopping (if hardware)

For EACH transaction, determine:
1. Primary category
2. Sub-category (only for Food & Drinks: "Essential" or "Social", otherwise null)
3. Confidence (only for non-obvious cases): "low" if uncertain, omit otherwise

OUTPUT FORMAT (strict JSON):
{
  "categorized_transactions": [
    {
      "row": <original row number>,
      "card": "<card last 4>",
      "date": "<transaction date>",
      "description": "<merchant description>",
      "amount": <amount>,
      "category": "<Primary Category>",
      "sub_category": "<Essential|Social|null>",
      "confidence": "<low>"  // only include if uncertain
    }
  ],
  "chunk_num": <chunk number>,
  "total_chunks": <total chunks>
}

Rules:
- Process ALL transactions. Do not skip any.
- Return ONLY valid JSON.
- Do NOT include reasoning for individual transactions — categorization should be self-evident from the guidelines.
- Only include "confidence": "low" when genuinely uncertain (e.g., garbled description, ambiguous merchant).
```

**Wait for all subagents to complete** before proceeding.

**Aggregate results:**
- Combine all `categorized_transactions` arrays from each subagent
- Verify total count matches expected (should equal filtered transaction count)
- If any subagent failed or returned invalid JSON, retry that chunk with a single agent

### 8. Aggregate and flag

Compute total spend per category (and sub-category for Food & Drinks). Flag any category where the total exceeds 40% of the overall spend as potentially disproportionate. This flagging is at the aggregate level — do not flag individual transactions.

**Calculate final net spend** (CRITICAL - follow this exact formula to avoid double-counting):

```
# From parser
total_debit_raw = total_debit  # Includes ALL debits

# From waiver matching (step 4)
waived_debits_total = sum of debit amounts from matched waiver pairs

# From unmatched credits (step 4)
unmatched_credits_total = sum of unmatched miscellaneous credit amounts

# Final calculation
gross_spend = total_debit_raw - waived_debits_total
net_spend = gross_spend - unmatched_credits_total
```

**GUARDRAIL CHECKS** (perform these before finalizing):
1. `gross_spend` should equal the sum of all categorized transaction amounts. If using the filtered transactions from step 4, verify: `sum(categorized_transactions.amount) == gross_spend`
2. Verify waiver is only subtracted once: `gross_spend + waived_debits_total == total_debit_raw`
3. **COMMON BUG TO AVOID**: Do NOT subtract `waived_credits_total` from `gross_spend`. The waiver credit already cancelled out the debit — subtracting it again would be double-counting.
4. **COMMON BUG TO AVOID**: Do NOT add `waived_credits_total` to `unmatched_credits_total`. Waiver credits are matched pairs, not miscellaneous credits.

**Report breakdown** in the report header:
- "Rp X gross spend (Rp Y total_debit - Rp Z waived fees) - Rp W unmatched credits = Rp V net spend"

### 7. Check for previous month's analysis

**Tell the user:** "Checking for previous month's analysis for comparison..."

Compute the previous month's YYYY-MM:
- For months 02-12: subtract 1 from the month
- For month 01 (January): roll back to 12 (December) of the previous year

Use the Glob tool to check if `./analysis/{previous-YYYY-MM}.md` exists. If it exists, read it with the Read tool. Extract the category totals from the "Spend by Category" section (it's a pipe-delimited markdown table) for month-over-month comparison.

If the previous month's file does not exist, or its format cannot be parsed, skip the MoM comparison and note it in the output.

### 8. Write the analysis

**Before writing, VALIDATE CALCULATIONS** using the helper script:

```bash
python3 <script_path>/scripts/validate_calculations.py \
    <total_debit_raw> <waived_debits_total> <unmatched_credits_total> <gross_spend> <net_spend>
```

Where:
- `<total_debit_raw>` = `total_debit` from parser
- `<waived_debits_total>` = sum of matched waiver debit amounts
- `<unmatched_credits_total>` = sum of unmatched miscellaneous credits
- `<gross_spend>` = calculated gross spend
- `<net_spend>` = calculated net spend

**If validation fails**, do NOT write the report. Instead, debug the calculation discrepancy first.

Use the Write tool to create `./analysis/{YYYY-MM}.md`. Follow the template structure defined in `assets/templates/template.md`.

Fill in all sections:
1. **Header metadata** — month, date range, cards, transaction count (excluding waived/refunded), total spend with breakdown: "Rp X gross (Rp Y total_debit - Rp Z waived fees) - Rp W unmatched credits = Rp V net spend"
2. **Refunds & Waivers** — if any refund/waiver pairs were identified, list them here with amounts (for transparency). Show the matched pairs clearly.
3. **Spend by Category** — table with totals, percentages, and flags
4. **Transaction Details by Category** — all transactions listed per category, sorted descending by amount (exclude waived/refunded transactions)
5. **Month-over-Month Comparison** — delta and percentage change per category (or "No previous month data available")
6. **Savings Recommendations** — opinionated, specific recommendations

### 9. Present summary

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

## Performance notes

- **CSV parsing**: Usually fast (<5 seconds)
- **Refund/waiver analysis**: Quick AI operation (<10 seconds)
- **Categorization**: Longest step — parallel subagents reduce time significantly
  - Optimized: Removed per-transaction confidence and reasoning overhead
  - 1 subagent: ~10-20 seconds for 50 transactions
  - 4 subagents in parallel: ~10-20 seconds for 200 transactions (4x speedup)
- **Report generation**: Fast (<10 seconds)

**Always inform the user before starting long-running operations** (especially subagent launches).
