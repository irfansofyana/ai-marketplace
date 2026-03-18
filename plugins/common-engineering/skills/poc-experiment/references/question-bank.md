# POC/Experiment Question Bank

Reusable `AskUserQuestion` patterns for the POC/Experiment skill.

## Context Gathering

### POC Status

```python
AskUserQuestion(
    questions=[{
        "question": "Are you writing this before or after the POC?",
        "header": "📋 POC Status",
        "options": [
            {"label": "Before — planning the experiment", "description": "Define hypothesis and approach"},
            {"label": "After — documenting results", "description": "Capture findings and recommendation"},
            {"label": "During — in progress", "description": "Capture what we know so far"}
        ],
        "multiSelect": false
    }]
)
```

### Hypothesis

```python
AskUserQuestion(
    questions=[{
        "question": "What specific hypothesis are you testing?",
        "header": "🧪 Hypothesis",
        "placeholder": "e.g., 'We believe that switching from REST to gRPC will reduce inter-service latency below 10ms at p99 for our data ingestion pipeline under 5000 RPS load.'"
    }]
)
```

### Motivation

```python
AskUserQuestion(
    questions=[{
        "question": "What problem or decision is this POC trying to resolve?",
        "header": "❓ Motivation",
        "placeholder": "e.g., We need to decide whether WebAssembly is viable for running user-defined code sandboxes before committing 3 months of engineering..."
    }]
)
```

### Approach

```python
AskUserQuestion(
    questions=[{
        "question": "How was the experiment designed and conducted? What did you build or test?",
        "header": "🔬 Approach",
        "placeholder": "e.g., Built a minimal prototype using Rust compiled to WASM. Tested execution of 50 user-defined transform functions with simulated production data..."
    }]
)
```

### Success Criteria

```python
AskUserQuestion(
    questions=[{
        "question": "How do you define success? What results lead to Go vs No-Go?",
        "header": "✅ Success Criteria",
        "placeholder": "e.g., Go if: execution latency < 5ms p99, memory overhead < 50MB per sandbox, no security escapes in 1000 fuzz test runs. No-Go if any criterion fails..."
    }]
)
```

### Results & Findings (if completed)

```python
AskUserQuestion(
    questions=[{
        "question": "What did you find? Share key metrics and observations.",
        "header": "📊 Results",
        "placeholder": "e.g., Latency: 3.2ms p99 ✓. Memory: 38MB avg ✓. Fuzz testing: 0 escapes in 2000 runs ✓. But cold start: 450ms — unexpected and potentially blocking for our use case..."
    }]
)
```

### Limitations

```python
AskUserQuestion(
    questions=[{
        "question": "What are the limitations of this POC? What didn't it test?",
        "header": "⚠️ Limitations",
        "options": [
            {"label": "Limited scale — didn't test at production load", "description": "Synthetic or small-scale testing only"},
            {"label": "Limited scope — tested only part of the problem", "description": "Not end-to-end"},
            {"label": "Time-boxed — may have missed edge cases", "description": "Known gaps from time constraints"},
            {"label": "Environment differences — not production-like", "description": "Local or staging only"},
            {"label": "I'll describe specific limitations", "description": "Custom limitations"}
        ],
        "multiSelect": true
    }]
)
```

### Recommendation

```python
AskUserQuestion(
    questions=[{
        "question": "Based on the findings, what's your recommendation?",
        "header": "🚦 Recommendation",
        "options": [
            {"label": "Go — proceed to full implementation", "description": "Hypothesis validated, move forward"},
            {"label": "Conditional Go — proceed with caveats", "description": "Validated with known limitations to address"},
            {"label": "No-Go — do not proceed", "description": "Hypothesis rejected or risks too high"},
            {"label": "Inconclusive — need more investigation", "description": "Results mixed, specific questions remain"}
        ],
        "multiSelect": false
    }]
)
```

### Next Steps

```python
AskUserQuestion(
    questions=[{
        "question": "What are the next steps based on this recommendation?",
        "header": "➡️ Next Steps",
        "placeholder": "e.g., If Go: start RFC for full implementation, allocate 2 engineers for Q2. If No-Go: evaluate alternative X, return to decision in 6 months..."
    }]
)
```

### Related Context

```python
AskUserQuestion(
    questions=[{
        "question": "Any ADRs, RFCs, or tickets this POC informs?",
        "header": "📚 Context (Optional)",
        "options": [
            {"label": "Yes — file paths", "description": "I'll read them"},
            {"label": "Yes — I'll paste content", "description": "Paste relevant sections"},
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
        "question": "Would you like research assistance?",
        "header": "🔍 Research",
        "options": [
            {"label": "Yes — comparable benchmarks", "description": "Find real-world data on the technology"},
            {"label": "Yes — known limitations", "description": "What others discovered in similar POCs"},
            {"label": "Yes — alternative approaches", "description": "Other ways to solve the same problem"},
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
