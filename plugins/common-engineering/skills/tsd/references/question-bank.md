# TSD Question Bank

Reusable `AskUserQuestion` patterns for the TSD skill.

## Context Gathering

### System Overview

```python
AskUserQuestion(
    questions=[{
        "question": "What does this service or API do? What problem does it solve?",
        "header": "📋 System Overview",
        "placeholder": "e.g., User Authentication Service — handles login, token issuance, and session management for all internal services..."
    }]
)
```

### API Endpoints

```python
AskUserQuestion(
    questions=[{
        "question": "What operations does this API support? Walk me through the endpoints.",
        "header": "🔌 API Endpoints",
        "placeholder": "e.g., POST /auth/login, POST /auth/refresh, DELETE /auth/logout, GET /auth/me..."
    }]
)
```

### Data Models

```python
AskUserQuestion(
    questions=[{
        "question": "Describe the main data entities and their key fields.",
        "header": "📦 Data Models",
        "placeholder": "e.g., User: {id, email, created_at, role}. Session: {token, user_id, expires_at, ip_address}..."
    }]
)
```

### Authentication & Authorization

```python
AskUserQuestion(
    questions=[{
        "question": "How do clients authenticate? Are there different permission levels?",
        "header": "🔐 Auth",
        "options": [
            {"label": "API key", "description": "Static key per client"},
            {"label": "OAuth 2.0", "description": "Token-based with scopes"},
            {"label": "JWT", "description": "Self-contained tokens"},
            {"label": "mTLS", "description": "Client certificate authentication"},
            {"label": "No auth required", "description": "Internal service only"},
            {"label": "I'll describe", "description": "Custom approach"}
        ],
        "multiSelect": false
    }]
)
```

### Error Handling

```python
AskUserQuestion(
    questions=[{
        "question": "What errors can occur and how should they be communicated?",
        "header": "❌ Error Handling",
        "placeholder": "e.g., 400 for invalid input, 401 for expired token, 429 for rate limiting. Error body: {code, message, details}..."
    }]
)
```

### Versioning

```python
AskUserQuestion(
    questions=[{
        "question": "How will this API be versioned? How are breaking changes handled?",
        "header": "🔖 Versioning",
        "options": [
            {"label": "URL versioning (/v1/, /v2/)", "description": "Version in the path"},
            {"label": "Header versioning", "description": "API-Version header"},
            {"label": "No versioning", "description": "Internal service, breakage acceptable"},
            {"label": "Semantic versioning", "description": "SemVer with deprecation policy"},
            {"label": "I'll describe", "description": "Custom approach"}
        ],
        "multiSelect": false
    }]
)
```

### Performance Requirements

```python
AskUserQuestion(
    questions=[{
        "question": "Any latency, throughput, or SLA requirements?",
        "header": "⚡ Performance",
        "placeholder": "e.g., p99 < 200ms, 1000 RPS sustained, 99.9% availability SLA..."
    }]
)
```

### Related Context

```python
AskUserQuestion(
    questions=[{
        "question": "Any existing specs, OpenAPI definitions, or service contracts I should reference?",
        "header": "📚 Context (Optional)",
        "options": [
            {"label": "Yes — file paths", "description": "I'll read them"},
            {"label": "Yes — I'll paste content", "description": "Paste OpenAPI, schema, etc."},
            {"label": "Yes — I'll describe key points", "description": "Verbal summary"},
            {"label": "None", "description": "Starting fresh"}
        ],
        "multiSelect": false
    }]
)
```

## Research Offer

```python
AskUserQuestion(
    questions=[{
        "question": "Would you like research assistance on API design patterns?",
        "header": "🔍 Research",
        "options": [
            {"label": "Yes — REST vs GraphQL patterns", "description": "Compare API paradigms"},
            {"label": "Yes — pagination approaches", "description": "Cursor, offset, keyset"},
            {"label": "Yes — error handling standards", "description": "RFC 7807, Problem Details"},
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
        "question": "Do you need technical diagrams?",
        "header": "📊 Diagrams",
        "options": [
            {"label": "System context diagram", "description": "Show where this service fits"},
            {"label": "Entity-relationship diagram", "description": "Data model relationships"},
            {"label": "Sequence diagram", "description": "Request/response flows"},
            {"label": "No diagrams needed", "description": "Text-only"}
        ],
        "multiSelect": true
    }]
)
```
