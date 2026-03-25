# Credit Card Statement Analysis: {YYYY-MM}

<!-- Replace all {placeholders} with actual values -->

**Generated:** {current date}
**Period:** {earliest transaction_date} to {latest transaction_date}
**Cards analyzed:** {comma-separated list of unique card_last4 values}
**Total transactions:** {count of debit rows analyzed}
**Total spend:** Rp {total amount, formatted with thousand separators}
<!-- If any rows were skipped due to malformed data, note it here -->
<!-- If any refunds/waivers were identified, note them in the Refunds & Waivers section below -->

---

## Refunds & Waivers

<!-- If any refund/waiver pairs were identified, list them here. Otherwise write "None identified." -->

| Date | Card | Description | Amount | Note |
|------|:----:|-------------|-------:|------|
| {date} | {card} | {description} | Rp {amount} | {Waiver/Refund of original debit}

<!-- These transactions were excluded from spending analysis (both debit and credit sides net to zero) -->

---

---

## Spend by Category

<!-- This table must remain pipe-delimited and parseable — future runs read it for MoM comparison -->

| Category | Sub-category | Total | % of Total | Flag |
|----------|-------------|------:|:----------:|:----:|
| Food & Drinks | Essential | Rp {amount} | {pct}% | |
| Food & Drinks | Social | Rp {amount} | {pct}% | |
| Transport | - | Rp {amount} | {pct}% | |
| Shopping | - | Rp {amount} | {pct}% | |
| Subscriptions | - | Rp {amount} | {pct}% | |
| Health | - | Rp {amount} | {pct}% | |
| Bills & Utilities | - | Rp {amount} | {pct}% | |
| Other | - | Rp {amount} | {pct}% | |
| **Total** | | **Rp {total}** | **100%** | |

<!-- Flag column: mark with ⚠️ if category exceeds 40% of total spend -->
<!-- Omit rows for categories with zero transactions -->

---

## Transaction Details by Category

<!-- One section per category. Sort transactions descending by amount within each section. -->
<!-- Omit sections for categories with zero transactions. -->

### Food & Drinks — Essential (Rp {category total})

| # | Date | Card | Description | Amount |
|--:|------|:----:|-------------|-------:|
| 1 | {transaction_date} | {card_last4} | {description} | Rp {amount} |

### Food & Drinks — Social (Rp {category total})

| # | Date | Card | Description | Amount |
|--:|------|:----:|-------------|-------:|
| 1 | {transaction_date} | {card_last4} | {description} | Rp {amount} |

### Transport (Rp {category total})

| # | Date | Card | Description | Amount |
|--:|------|:----:|-------------|-------:|
| 1 | {transaction_date} | {card_last4} | {description} | Rp {amount} |

### Shopping (Rp {category total})

| # | Date | Card | Description | Amount |
|--:|------|:----:|-------------|-------:|
| 1 | {transaction_date} | {card_last4} | {description} | Rp {amount} |

### Subscriptions (Rp {category total})

| # | Date | Card | Description | Amount |
|--:|------|:----:|-------------|-------:|
| 1 | {transaction_date} | {card_last4} | {description} | Rp {amount} |

### Health (Rp {category total})

| # | Date | Card | Description | Amount |
|--:|------|:----:|-------------|-------:|
| 1 | {transaction_date} | {card_last4} | {description} | Rp {amount} |

### Bills & Utilities (Rp {category total})

| # | Date | Card | Description | Amount |
|--:|------|:----:|-------------|-------:|
| 1 | {transaction_date} | {card_last4} | {description} | Rp {amount} |

### Other (Rp {category total})

| # | Date | Card | Description | Amount |
|--:|------|:----:|-------------|-------:|
| 1 | {transaction_date} | {card_last4} | {description} | Rp {amount} |

---

## Month-over-Month Comparison

<!-- If previous month analysis exists, fill the comparison table below -->
<!-- If not, replace this entire section with: "No previous month data available — skipping comparison." -->

Compared with: **{previous-YYYY-MM}**

| Category | Previous | Current | Delta | % Change | Trend |
|----------|--------:|---------:|------:|---------:|:-----:|
| Food & Drinks (Essential) | Rp {prev} | Rp {curr} | Rp {delta} | {pct}% | {trend} |
| Food & Drinks (Social) | Rp {prev} | Rp {curr} | Rp {delta} | {pct}% | {trend} |
| Transport | Rp {prev} | Rp {curr} | Rp {delta} | {pct}% | {trend} |
| Shopping | Rp {prev} | Rp {curr} | Rp {delta} | {pct}% | {trend} |
| Subscriptions | Rp {prev} | Rp {curr} | Rp {delta} | {pct}% | {trend} |
| Health | Rp {prev} | Rp {curr} | Rp {delta} | {pct}% | {trend} |
| Bills & Utilities | Rp {prev} | Rp {curr} | Rp {delta} | {pct}% | {trend} |
| Other | Rp {prev} | Rp {curr} | Rp {delta} | {pct}% | {trend} |
| **Total** | **Rp {prev_total}** | **Rp {curr_total}** | **Rp {delta}** | **{pct}%** | |

<!-- Trend indicators: -->
<!-- ⬆️ Notable increase (>30%) -->
<!-- ⬇️ Notable decrease (>30%) -->
<!-- ➡️ Stable (within ±30%) -->
<!-- 🆕 New category (not in previous month) -->
<!-- ❌ Gone category (not in current month) -->

---

## Savings Recommendations

<!-- Write 3-5 opinionated, specific recommendations. Reference actual merchant names and amounts. -->

1. **{Recommendation title}**
   {Specific, actionable recommendation with actual numbers and merchant references}

2. **{Recommendation title}**
   {Specific, actionable recommendation}

3. **{Recommendation title}**
   {Specific, actionable recommendation}
