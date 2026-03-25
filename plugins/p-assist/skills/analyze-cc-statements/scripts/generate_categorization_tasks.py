#!/usr/bin/env python3
"""Generate categorization prompts for parallel processing.

This script helps the analyze-cc-statements skill by:
1. Determining optimal chunk size based on transaction count
2. Generating pre-chunked transaction data for each subagent
3. Providing the exact prompt template to use

Usage:
    python3 generate_categorization_tasks.py <transactions_json> <chunk_size>

Output:
    JSON object with:
    - num_subagents: number of subagents to launch
    - chunk_size: transactions per chunk
    - prompts: array of prompts, one per subagent
    - expected_total: total transactions to categorize
"""

import json
import sys
import math


def chunkify(transactions, chunk_size):
    """Split transactions into chunks of specified size."""
    chunks = []
    for i in range(0, len(transactions), chunk_size):
        chunks.append(transactions[i:i + chunk_size])
    return chunks


def get_optimal_chunk_size(num_transactions):
    """Determine optimal number of subagents based on transaction count.

    Returns (num_subagents, chunk_size)
    """
    if num_transactions <= 50:
        return 1, 50  # No parallelization needed
    elif num_transactions <= 150:
        return 2, math.ceil(num_transactions / 2)  # 2 subagents
    elif num_transactions <= 300:
        return 4, math.ceil(num_transactions / 4)  # 4 subagents
    else:
        return 6, math.ceil(num_transactions / 6)  # 6 subagents max


def generate_prompt(chunk_data, chunk_num, total_chunks, guidelines_path):
    """Generate the categorization prompt for a single chunk."""

    # Read categorization guidelines
    try:
        with open(guidelines_path, 'r', encoding='utf-8') as f:
            guidelines = f.read()
    except FileNotFoundError:
        guidelines = "Use standard categorization rules based on merchant names."

    transactions_json = json.dumps(chunk_data, indent=2)

    prompt = f"""Categorize these credit card transactions according to the guidelines.

TRANSACTIONS TO CATEGORIZE (Chunk {chunk_num}/{total_chunks}):
{transactions_json}

CATEGORIZATION GUIDELINES:
{guidelines}

Categories available:
- **Food & Drinks** — sub-categorize as **Essential** (groceries, supermarkets, daily necessities) or **Social** (restaurants, cafes, bars, food delivery)
- **Transport** — ride-hailing, fuel, parking, tolls, public transit, airlines
- **Shopping** — e-commerce, retail, fashion, electronics
- **Subscriptions** — streaming, software/SaaS, gaming, recurring memberships
- **Health** — pharmacies, clinics, hospitals, fitness, supplements
- **Bills & Utilities** — electricity, water, internet, insurance, phone bills
- **Other** — anything that genuinely doesn't fit above (use sparingly)

Disambiguation rules:
1. When uncertain between two categories, prefer the more specific one over "Other"
2. For Grab/Gojek: FOOD → Food & Drinks (Social), TRANSPORT/CAR/BIKE → Transport
3. Supermarkets (Indomaret, Alfamart, Superindo) → Food & Drinks Essential
4. Streaming services (Netflix, Spotify) → Subscriptions
5. PLN, IndiHome, water → Bills & Utilities

For EACH transaction, determine:
1. **category**: Primary category from the list above
2. **sub_category**: "Essential" or "Social" for Food & Drinks only, null for others
3. **confidence**: "high" (clear merchant), "medium" (inferred), "low" (ambiguous)
4. **reasoning**: Brief explanation (5-15 words)

OUTPUT FORMAT (strict JSON, no markdown, no extra text):
{{
  "categorized_transactions": [
    {{
      "row": <original row number>,
      "card": "<card last 4>",
      "date": "<transaction date>",
      "description": "<merchant description>",
      "amount": <amount>,
      "category": "<Primary Category>",
      "sub_category": "<Essential|Social|null>",
      "confidence": "<high|medium|low>",
      "reasoning": "<brief reasoning>"
    }}
  ],
  "chunk_num": {chunk_num},
  "total_chunks": {total_chunks}
}}

Process ALL {len(chunk_data)} transactions. Do not skip any. Return ONLY valid JSON."""

    return prompt


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_categorization_tasks.py <transactions_json_file> [skill_dir]")
        print("  transactions_json_file: JSON file containing transactions array")
        print("  skill_dir: Path to skill directory (for guidelines)")
        sys.exit(1)

    transactions_file = sys.argv[1]
    skill_dir = sys.argv[2] if len(sys.argv) > 2 else None

    # Load transactions
    try:
        with open(transactions_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    transactions = data.get('transactions', [])
    if not transactions:
        print(json.dumps({"error": "No transactions found in input file"}))
        sys.exit(1)

    # Determine chunking strategy
    num_transactions = len(transactions)
    num_subagents, chunk_size = get_optimal_chunk_size(num_transactions)

    # Split into chunks
    chunks = chunkify(transactions, chunk_size)

    # Generate prompts
    guidelines_path = f"{skill_dir}/references/categorization-guidelines.md" if skill_dir else None

    result = {
        "num_subagents": num_subagents,
        "chunk_size": chunk_size,
        "total_transactions": num_transactions,
        "chunks": []
    }

    for i, chunk in enumerate(chunks, 1):
        chunk_info = {
            "chunk_num": i,
            "total_chunks": len(chunks),
            "transaction_count": len(chunk),
            "transactions": chunk
        }

        if guidelines_path:
            chunk_info["prompt"] = generate_prompt(chunk, i, len(chunks), guidelines_path)

        result["chunks"].append(chunk_info)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
