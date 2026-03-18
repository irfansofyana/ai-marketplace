# RFC Question Bank

Reusable `AskUserQuestion` patterns for the RFC skill.

## Context Gathering

### Current State

```python
AskUserQuestion(
    questions=[{
        "question": "Walk me through the current architecture or process step by step.",
        "header": "🔍 Current State",
        "placeholder": "e.g., All payment processing runs through a monolithic Rails app. The billing module handles subscription, invoicing, and payment gateway calls..."
    }]
)
```

### Evidence

```python
AskUserQuestion(
    questions=[{
        "question": "Why does this need to change? What's the evidence?",
        "header": "📊 Evidence",
        "options": [
            {"label": "Performance degradation", "description": "Latency, throughput, or reliability issues"},
            {"label": "Scalability limits", "description": "Current design can't handle growth"},
            {"label": "Technical debt blocking progress", "description": "Hard to add features or maintain"},
            {"label": "Security or compliance requirement", "description": "Must change for regulatory reasons"},
            {"label": "Cost reduction", "description": "Current approach is too expensive"},
            {"label": "Other", "description": "I'll describe"}
        ],
        "multiSelect": true
    }]
)
```

### Proposed Design

```python
AskUserQuestion(
    questions=[{
        "question": "Describe the target architecture at a high level — what changes?",
        "header": "🏗️ Proposed Design",
        "placeholder": "e.g., Extract billing into a standalone microservice with its own database. Use event-driven communication via Kafka for billing events..."
    }]
)
```

### Affected Services & Teams

```python
AskUserQuestion(
    questions=[{
        "question": "Which services and teams are involved?",
        "header": "👥 Scope",
        "placeholder": "e.g., Affects: billing-service, auth-service, notification-service. Teams: Platform, Payments, Notifications..."
    }]
)
```

### Implementation Approach

```python
AskUserQuestion(
    questions=[{
        "question": "Do you have a phased rollout in mind?",
        "header": "📋 Implementation Phases",
        "options": [
            {"label": "Yes — I'll describe the phases", "description": "Multi-phase with specific milestones"},
            {"label": "Big-bang migration", "description": "Single cutover with feature flags"},
            {"label": "Parallel run", "description": "Run old and new systems simultaneously"},
            {"label": "Not decided yet", "description": "Need help thinking through this"}
        ],
        "multiSelect": false
    }]
)
```

### Migration Strategy

```python
AskUserQuestion(
    questions=[{
        "question": "How do you move from the current state to the target state?",
        "header": "🔄 Migration Strategy",
        "placeholder": "e.g., Phase 1: Extract billing DB. Phase 2: Dual-write during transition. Phase 3: Cut over and decommission old tables..."
    }]
)
```

### Rollback Plan

```python
AskUserQuestion(
    questions=[{
        "question": "If this goes wrong after deployment, how do you revert?",
        "header": "↩️ Rollback Plan",
        "placeholder": "e.g., Feature flag to route back to monolith. DB rollback script. Keep old tables for 30 days post-cutover..."
    }]
)
```

### Alternatives

```python
AskUserQuestion(
    questions=[{
        "question": "What other approaches did you consider? Why is this preferred?",
        "header": "🔀 Alternatives",
        "placeholder": "e.g., Alt 1: Modular monolith — lower operational complexity but doesn't solve scaling. Alt 2: Service mesh — too much overhead for our scale..."
    }]
)
```

### Risks

```python
AskUserQuestion(
    questions=[{
        "question": "What are the biggest technical and operational risks?",
        "header": "⚠️ Risks",
        "options": [
            {"label": "Data consistency / correctness", "description": "Risk of data loss or inconsistency"},
            {"label": "Performance regression", "description": "New design might be slower"},
            {"label": "Operational complexity", "description": "Harder to operate and debug"},
            {"label": "Team capacity / expertise", "description": "Skills gap or bandwidth"},
            {"label": "Integration failures", "description": "Downstream consumers breaking"},
            {"label": "Migration duration", "description": "Takes longer than planned"},
            {"label": "Other", "description": "I'll describe"}
        ],
        "multiSelect": true
    }]
)
```

### Related Context

```python
AskUserQuestion(
    questions=[{
        "question": "Any existing ADRs, TSDs, or tickets I should reference?",
        "header": "📚 Context (Optional)",
        "options": [
            {"label": "Yes — file paths", "description": "I'll read them"},
            {"label": "Yes — I'll paste content", "description": "Copy-paste key sections"},
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
            {"label": "Yes — industry patterns", "description": "How others solved similar architectural problems"},
            {"label": "Yes — technology comparison", "description": "Compare specific tech options"},
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

### Diagrams

```python
AskUserQuestion(
    questions=[{
        "question": "Do you need architecture diagrams?",
        "header": "📊 Diagrams",
        "options": [
            {"label": "Architecture diagram", "description": "System components and relationships"},
            {"label": "Sequence diagram", "description": "Request/response flows"},
            {"label": "Data flow diagram", "description": "How data moves between components"},
            {"label": "No diagrams needed", "description": "Text-only"}
        ],
        "multiSelect": true
    }]
)
```
