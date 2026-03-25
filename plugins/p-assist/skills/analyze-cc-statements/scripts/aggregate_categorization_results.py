#!/usr/bin/env python3
"""Aggregate categorization results from parallel subagents.

This script combines JSON outputs from multiple categorization subagents,
validates the results, and produces a single merged output.

Usage:
    python3 aggregate_categorization_results.py <results_json_array>

Input:
    JSON array containing results from each subagent, e.g.:
    [
      {...result from subagent 1...},
      {...result from subagent 2...},
      ...
    ]

Output:
    JSON object with:
    - all_transactions: combined array of all categorized transactions
    - total_count: total number of transactions
    - by_category: breakdown by category with counts and totals
    - by_sub_category: breakdown for Food & Drinks sub-categories
    - warnings: any issues detected (missing chunks, duplicates, etc.)
"""

import json
import sys
from collections import defaultdict


def aggregate_results(subagent_results):
    """Combine results from multiple subagents."""
    all_transactions = []
    seen_rows = set()
    warnings = []
    chunks_processed = set()

    for result in subagent_results:
        # Check for subagent errors
        if 'error' in result:
            warnings.append(f"Subagent error: {result['error']}")
            continue

        chunk_data = result.get('categorized_transactions', [])
        chunk_num = result.get('chunk_num', 'unknown')
        total_chunks = result.get('total_chunks', 'unknown')

        chunks_processed.add(chunk_num)

        for txn in chunk_data:
            row = txn.get('row')

            # Check for duplicates
            if row in seen_rows:
                warnings.append(f"Duplicate transaction row {row} from chunk {chunk_num}")
                continue

            seen_rows.add(row)
            all_transactions.append(txn)

    # Sort by row number for consistent output
    all_transactions.sort(key=lambda x: x.get('row', 0))

    return {
        "all_transactions": all_transactions,
        "total_count": len(all_transactions),
        "chunks_processed": sorted(chunks_processed),
        "warnings": warnings
    }


def compute_breakdown(transactions):
    """Compute spending breakdown by category."""
    by_category = defaultdict(lambda: {"count": 0, "total": 0.0, "transactions": []})
    by_sub_category = defaultdict(lambda: {"count": 0, "total": 0.0})

    for txn in transactions:
        category = txn.get('category', 'Other')
        sub_category = txn.get('sub_category')
        amount = txn.get('amount', 0)

        by_category[category]["count"] += 1
        by_category[category]["total"] += amount
        by_category[category]["transactions"].append(txn)

        # Handle sub-categories for Food & Drinks
        if category == "Food & Drinks" and sub_category:
            key = f"Food & Drinks - {sub_category}"
            by_sub_category[key]["count"] += 1
            by_sub_category[key]["total"] += amount

    # Convert to regular dict and sort transactions within each category
    result = {}
    for category, data in sorted(by_category.items()):
        result[category] = {
            "count": data["count"],
            "total": round(data["total"], 2),
            "transactions": sorted(data["transactions"], key=lambda x: -x.get('amount', 0))
        }

    return result, dict(by_sub_category)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 aggregate_categorization_results.py <results_json_file>")
        print("  results_json_file: JSON file containing array of subagent results")
        sys.exit(1)

    results_file = sys.argv[1]

    # Load results
    try:
        with open(results_file, 'r', encoding='utf-8') as f:
            subagent_results = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    if not isinstance(subagent_results, list):
        print(json.dumps({"error": "Input must be a JSON array of subagent results"}))
        sys.exit(1)

    # Aggregate results
    aggregated = aggregate_results(subagent_results)

    # Compute breakdown
    by_category, by_sub_category = compute_breakdown(aggregated["all_transactions"])

    # Final output
    output = {
        **aggregated,
        "by_category": by_category,
        "by_sub_category": by_sub_category
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
