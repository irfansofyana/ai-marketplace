# ADR Question Bank

Reusable `AskUserQuestion` patterns for the ADR skill.

## Context Gathering

### The Decision

```python
AskUserQuestion(
    questions=[{
        "question": "What is the specific decision being made or documented?",
        "header": "🎯 Decision",
        "placeholder": "e.g., Choose between PostgreSQL and MongoDB for storing user profile data..."
    }]
)
```

### Context & Drivers

```python
AskUserQuestion(
    questions=[{
        "question": "What situation or requirements led to this decision? What constraints apply?",
        "header": "📋 Context",
        "placeholder": "e.g., We're migrating from a legacy Oracle DB. Requirements: must support JSONB for flexible schema, team has strong SQL expertise, AWS deployment..."
    }]
)
```

### Alternatives (MANDATORY)

```python
AskUserQuestion(
    questions=[{
        "question": "What other options did you consider? Walk me through each alternative.",
        "header": "🔀 Alternatives (Required — min. 2)",
        "placeholder": "e.g., Option A: PostgreSQL — ACID transactions, strong team familiarity, JSONB support. Option B: MongoDB — flexible schema, but team has no experience. Option C: DynamoDB — managed but vendor lock-in..."
    }]
)
```

### Decision Criteria

```python
AskUserQuestion(
    questions=[{
        "question": "How did you evaluate the options? What mattered most?",
        "header": "⚖️ Decision Criteria",
        "options": [
            {"label": "Performance / throughput", "description": "Speed and scale requirements"},
            {"label": "Team familiarity", "description": "Existing expertise"},
            {"label": "Operational simplicity", "description": "Ease of running in production"},
            {"label": "Cost", "description": "Licensing, infrastructure, or operational costs"},
            {"label": "Vendor support / community", "description": "Maturity and ecosystem"},
            {"label": "Compliance / security", "description": "Regulatory requirements"},
            {"label": "Migration effort", "description": "Cost to adopt vs. current approach"},
            {"label": "Other", "description": "I'll describe"}
        ],
        "multiSelect": true
    }]
)
```

### Trade-offs

```python
AskUserQuestion(
    questions=[
        {
            "question": "What are you gaining with this choice?",
            "header": "✅ What We Gain",
            "placeholder": "e.g., Strong SQL tooling, JSONB for flexible schemas, ACID transactions, team confidence..."
        },
        {
            "question": "What are you giving up or accepting as a trade-off?",
            "header": "❌ What We Give Up",
            "placeholder": "e.g., Horizontal write scaling requires more work (partitioning), higher storage costs than NoSQL..."
        }
    ]
)
```

### Consequences

```python
AskUserQuestion(
    questions=[{
        "question": "What changes because of this decision? Any downstream implications?",
        "header": "🔄 Consequences",
        "placeholder": "e.g., All new services must use PostgreSQL. Migration from Oracle needed. ORM choice now constrained to SQL-compatible options..."
    }]
)
```

### Reconsideration Triggers

```python
AskUserQuestion(
    questions=[{
        "question": "Under what circumstances should this decision be revisited?",
        "header": "🔁 Reconsideration (Optional)",
        "options": [
            {"label": "If we need to scale writes beyond X RPS", "description": "Performance threshold"},
            {"label": "If team expertise changes", "description": "Skill set shift"},
            {"label": "If costs exceed threshold", "description": "Budget trigger"},
            {"label": "After X months / years", "description": "Time-based expiry"},
            {"label": "If regulatory requirements change", "description": "Compliance trigger"},
            {"label": "Skip — permanent decision", "description": "No reconsideration planned"}
        ],
        "multiSelect": true
    }]
)
```

### Related Context

```python
AskUserQuestion(
    questions=[{
        "question": "Any existing ADRs, RFCs, or benchmark data I should reference?",
        "header": "📚 Context (Optional)",
        "options": [
            {"label": "Yes — file paths", "description": "I'll read them"},
            {"label": "Yes — I'll paste content", "description": "Paste benchmarks or docs"},
            {"label": "Yes — I'll describe key points", "description": "Verbal summary"},
            {"label": "None", "description": "No additional context"}
        ],
        "multiSelect": false
    }]
)
```

## Research Offer

```python
AskUserQuestion(
    questions=[{
        "question": "Would you like research assistance comparing the options?",
        "header": "🔍 Research",
        "options": [
            {"label": "Yes — benchmarks and comparisons", "description": "Performance data on the options"},
            {"label": "Yes — community and support analysis", "description": "Ecosystem health comparison"},
            {"label": "Yes — case studies", "description": "How others made similar decisions"},
            {"label": "No, I have what I need", "description": "Proceed with drafting"}
        ],
        "multiSelect": false
    }]
)
```

## Output

### Format

```python
AskUserQuestion(
    questions=[{
        "question": "What output format?",
        "header": "📁 Output Format",
        "options": [
            {"label": "Word (.docx)", "description": "Editable for collaboration"},
            {"label": "PDF (.pdf)", "description": "Fixed format for distribution"},
            {"label": "Markdown (.md)", "description": "For wikis or version control"},
            {"label": "Decide later", "description": "Review draft first"}
        ],
        "multiSelect": false
    }]
)
```
