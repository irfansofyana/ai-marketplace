# One-Pager Question Bank

Reusable `AskUserQuestion` patterns for the one-pager skill.

## Context Gathering

### Problem & Current State

```python
AskUserQuestion(
    questions=[{
        "question": "Walk me through what's happening now — what's broken or missing?",
        "header": "🔍 Problem",
        "placeholder": "e.g., Our auth system doesn't support SSO, requiring enterprise customers to manage separate credentials..."
    }]
)
```

### Evidence of Problem

```python
AskUserQuestion(
    questions=[{
        "question": "How do we know this is a problem? Any metrics, incidents, or complaints?",
        "header": "📊 Evidence",
        "options": [
            {"label": "User/customer complaints", "description": "Direct feedback"},
            {"label": "Performance metrics", "description": "Quantitative data"},
            {"label": "Error logs / incidents", "description": "System failures"},
            {"label": "Internal pain points", "description": "Developer/team experience"},
            {"label": "No hard data yet", "description": "Qualitative observation"}
        ],
        "multiSelect": true
    }]
)
```

### Desired Outcome

```python
AskUserQuestion(
    questions=[
        {
            "question": "What does success look like after this is solved?",
            "header": "🎯 Desired Outcome",
            "placeholder": "e.g., Enterprise customers can sign in with their existing SSO provider..."
        },
        {
            "question": "How will you measure success?",
            "header": "📈 Success Metrics",
            "placeholder": "e.g., Reduce auth-related support tickets by 80%, enable SSO for 10+ enterprise customers"
        }
    ]
)
```

### Sign-offs

```python
AskUserQuestion(
    questions=[{
        "question": "Who needs to approve this?",
        "header": "✍️ Approvers",
        "options": [
            {"label": "Direct manager only", "description": "Single approver"},
            {"label": "Multiple engineering leads", "description": "Tech decision-makers"},
            {"label": "Cross-functional group", "description": "Engineering, product, design, etc."},
            {"label": "Executive approval", "description": "Senior leadership required"},
            {"label": "I'll specify names", "description": "Let me list specific people"}
        ],
        "multiSelect": false
    }]
)
```

### Risks

```python
AskUserQuestion(
    questions=[{
        "question": "What risks concern you most?",
        "header": "⚠️ Risks",
        "options": [
            {"label": "Technical complexity", "description": "Harder than expected"},
            {"label": "Timeline risk", "description": "Might take longer"},
            {"label": "Integration challenges", "description": "May not fit existing systems"},
            {"label": "Team capacity", "description": "Bandwidth or expertise gaps"},
            {"label": "User adoption", "description": "Users might not adopt it"},
            {"label": "Other", "description": "I'll describe specific risks"}
        ],
        "multiSelect": true
    }]
)
```

### Related Context

```python
AskUserQuestion(
    questions=[{
        "question": "Any existing documents or tickets I should reference?",
        "header": "📚 Context (Optional)",
        "options": [
            {"label": "Yes — file paths", "description": "I'll read them"},
            {"label": "Yes — I'll paste content", "description": "Copy-paste from existing docs"},
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
        "question": "Would you like research assistance before drafting?",
        "header": "🔍 Research",
        "options": [
            {"label": "Yes — industry best practices", "description": "How others solved this"},
            {"label": "Yes — technical context", "description": "Info about proposed approach"},
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

### Refinement

```python
AskUserQuestion(
    questions=[{
        "question": "Which sections to refine?",
        "header": "✏️ Refinement",
        "options": [
            {"label": "Problem statement", "description": "Sharpen problem articulation"},
            {"label": "High level goal", "description": "Adjust success metrics"},
            {"label": "Proposed solution", "description": "Modify solution description"},
            {"label": "Alternatives", "description": "Add or modify alternatives"},
            {"label": "Risks", "description": "Update risk assessment"},
            {"label": "All good — save it", "description": "Proceed to output"}
        ],
        "multiSelect": true
    }]
)
```
