#!/usr/bin/env python3
"""Parse credit card statement CSV and return structured transaction data.

Usage:
    python3 parse_transactions.py <csv_file>

Output:
    JSON object with transactions, counts, totals, and metadata.
"""

import csv
import json
import sys
import re


def parse_amount(amount_str):
    """Parse amount string, handling various formats (Rp, commas, decimals)."""
    if not amount_str:
        return 0.0
    # Remove currency symbols, commas, whitespace
    cleaned = re.sub(r'[^\d.\-]', '', str(amount_str).strip())
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def parse_date(date_str):
    """Parse date, auto-detecting DD-MM-YYYY vs YYYY-MM-DD format.

    Returns ISO format (YYYY-MM-DD) for consistency.
    """
    if not date_str:
        return None
    date_str = str(date_str).strip()

    # Try DD-MM-YYYY first (common in Indonesia)
    match = re.match(r'(\d{2})-(\d{2})-(\d{4})', date_str)
    if match:
        return f"{match.group(3)}-{match.group(2)}-{match.group(1)}"

    # Try YYYY-MM-DD
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})', date_str)
    if match:
        return date_str

    return None


def analyze_csv(filepath):
    """Parse CSV and return structured transaction data."""
    result = {
        'transactions': [],
        'credits': [],
        'total_debit': 0.0,
        'total_credit': 0.0,
        'debit_count': 0,
        'credit_count': 0,
        'skipped_rows': [],
        'cards': set(),
        'date_range': {'min': None, 'max': None}
    }

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)

            # Read and validate header
            try:
                header = next(reader)
            except StopIteration:
                print(json.dumps({'error': 'Empty file'}))
                return

            if len(header) < 7:
                print(json.dumps({
                    'error': f'Expected 7 columns in header, got {len(header)}',
                    'header': header
                }))
                return

            # Process data rows
            for row_num, row in enumerate(reader, start=2):
                # Skip malformed rows
                if len(row) != 7:
                    result['skipped_rows'].append({
                        'row': row_num,
                        'reason': f'Expected 7 columns, got {len(row)}',
                        'content': row[:3] + ['...'] if len(row) > 3 else row
                    })
                    continue

                card_last4, txn_date, posting_date, description, amount, txn_type, installment = row

                # Validate transaction type
                txn_type = txn_type.strip().lower()
                if txn_type not in ['debit', 'credit']:
                    result['skipped_rows'].append({
                        'row': row_num,
                        'reason': f"Invalid type '{txn_type}'",
                        'content': [description[:30]] if description else ['(empty)']
                    })
                    continue

                # Parse amount and date
                amount_val = parse_amount(amount)
                parsed_date = parse_date(txn_date)

                # Track unique cards
                result['cards'].add(card_last4.strip())

                # Track date range
                if parsed_date:
                    if result['date_range']['min'] is None or parsed_date < result['date_range']['min']:
                        result['date_range']['min'] = parsed_date
                    if result['date_range']['max'] is None or parsed_date > result['date_range']['max']:
                        result['date_range']['max'] = parsed_date

                # Categorize by type
                if txn_type == 'debit':
                    result['debit_count'] += 1
                    result['total_debit'] += amount_val
                    result['transactions'].append({
                        'row': row_num,
                        'card': card_last4.strip(),
                        'date': parsed_date or txn_date,
                        'description': description.strip(),
                        'amount': amount_val,
                        'installment': installment.strip() if installment and installment.strip() else None
                    })
                else:
                    result['credit_count'] += 1
                    result['total_credit'] += amount_val
                    result['credits'].append({
                        'row': row_num,
                        'card': card_last4.strip(),
                        'date': parsed_date or txn_date,
                        'description': description.strip(),
                        'amount': amount_val
                    })

    except FileNotFoundError:
        print(json.dumps({'error': f'File not found: {filepath}'}))
        return
    except Exception as e:
        print(json.dumps({'error': str(e)}))
        return

    # Convert sets to lists for JSON serialization
    result['cards'] = sorted(result['cards'])

    # Round totals to avoid floating point issues
    result['total_debit'] = round(result['total_debit'], 2)
    result['total_credit'] = round(result['total_credit'], 2)

    print(json.dumps(result, indent=2))


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 parse_transactions.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    analyze_csv(csv_file)


if __name__ == "__main__":
    main()
