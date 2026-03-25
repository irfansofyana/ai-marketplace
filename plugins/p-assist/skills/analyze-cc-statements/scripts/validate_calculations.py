#!/usr/bin/env python3
"""Validate credit card statement calculations to catch double-counting bugs.

This script verifies:
1. Waived debits are only subtracted once
2. Waiver credits are not double-counted
3. Net spend calculation is correct

Usage:
    python3 validate_calculations.py <json_output_from_parser> <waived_debits_total> <unmatched_credits_total> <expected_net_spend>

Or pass a JSON file with all values:
    python3 validate_calculations.py --file validation_input.json
"""

import json
import sys


def validate_calculations(total_debit_raw, waived_debits_total, unmatched_credits_total,
                          gross_spend, net_spend, categorized_sum=None):
    """
    Validate the calculation chain.

    Args:
        total_debit_raw: Total debit from parser (includes ALL debits)
        waived_debits_total: Sum of waived/refunded debit amounts
        unmatched_credits_total: Sum of unmatched miscellaneous credits
        gross_spend: Calculated gross spend
        net_spend: Calculated net spend
        categorized_sum: Sum of categorized transactions (optional verification)

    Returns:
        dict with validation results
    """
    result = {
        'valid': True,
        'errors': [],
        'warnings': [],
        'calculations': {}
    }

    # Expected calculations
    expected_gross = round(total_debit_raw - waived_debits_total, 2)
    expected_net = round(gross_spend - unmatched_credits_total, 2)

    result['calculations'] = {
        'total_debit_raw': total_debit_raw,
        'waived_debits_total': waived_debits_total,
        'gross_spend_expected': expected_gross,
        'gross_spend_provided': gross_spend,
        'unmatched_credits_total': unmatched_credits_total,
        'net_spend_expected': expected_net,
        'net_spend_provided': net_spend
    }

    # Check 1: Gross spend calculation
    if abs(gross_spend - expected_gross) > 0.01:
        result['valid'] = False
        result['errors'].append(
            f"Gross spend mismatch: expected {expected_gross}, got {gross_spend}. "
            f"Formula: total_debit ({total_debit_raw}) - waived_debits ({waived_debits_total}) = {expected_gross}"
        )

    # Check 2: Net spend calculation
    if abs(net_spend - expected_net) > 0.01:
        result['valid'] = False
        result['errors'].append(
            f"Net spend mismatch: expected {expected_net}, got {net_spend}. "
            f"Formula: gross_spend ({gross_spend}) - unmatched_credits ({unmatched_credits_total}) = {expected_net}"
        )

    # Check 3: Categorized sum verification (if provided)
    if categorized_sum is not None:
        if abs(categorized_sum - gross_spend) > 0.01:
            result['warnings'].append(
                f"Categorized sum ({categorized_sum}) doesn't match gross spend ({gross_spend}). "
                f"Difference: {round(abs(categorized_sum - gross_spend), 2)}"
            )

    # Check 4: Common bug detection - double-counting waiver
    # If someone did: gross = total_debit - waived_debits - waived_credits
    double_subtracted_gross = round(total_debit_raw - waived_debits_total - waived_debits_total, 2)
    if abs(gross_spend - double_subtracted_gross) < 0.01:
        result['valid'] = False
        result['errors'].append(
            "CRITICAL BUG DETECTED: Waived debits appear to be subtracted twice! "
            f"gross_spend ({gross_spend}) == total_debit ({total_debit_raw}) - waived_debits ({waived_debits_total}) * 2"
        )

    # Summary
    if result['valid']:
        result['summary'] = (
            f"VALIDATION PASSED\n"
            f"  Total debit (raw):    Rp {total_debit_raw:,.2f}\n"
            f"  Less waived fees:     Rp {waived_debits_total:,.2f}\n"
            f"  = Gross spend:        Rp {gross_spend:,.2f}\n"
            f"  Less unmatched cred:  Rp {unmatched_credits_total:,.2f}\n"
            f"  = Net spend:          Rp {net_spend:,.2f}"
        )
    else:
        result['summary'] = "VALIDATION FAILED\n\nErrors:\n" + "\n".join(f"  - {e}" for e in result['errors'])

    return result


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    # Check if using file input
    if '--file' in sys.argv:
        file_idx = sys.argv.index('--file')
        if file_idx + 1 >= len(sys.argv):
            print("Error: --file requires a filename argument")
            sys.exit(1)

        with open(sys.argv[file_idx + 1], 'r') as f:
            data = json.load(f)

        result = validate_calculations(
            total_debit_raw=data['total_debit_raw'],
            waived_debits_total=data.get('waived_debits_total', 0),
            unmatched_credits_total=data.get('unmatched_credits_total', 0),
            gross_spend=data['gross_spend'],
            net_spend=data['net_spend'],
            categorized_sum=data.get('categorized_sum')
        )
    else:
        # Command line arguments
        if len(sys.argv) < 6:
            print("Usage: python3 validate_calculations.py <total_debit_raw> <waived_debits> <unmatched_credits> <gross_spend> <net_spend> [categorized_sum]")
            sys.exit(1)

        result = validate_calculations(
            total_debit_raw=float(sys.argv[1]),
            waived_debits_total=float(sys.argv[2]),
            unmatched_credits_total=float(sys.argv[3]),
            gross_spend=float(sys.argv[4]),
            net_spend=float(sys.argv[5]),
            categorized_sum=float(sys.argv[6]) if len(sys.argv) > 6 else None
        )

    print(json.dumps(result, indent=2))

    if not result['valid']:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
