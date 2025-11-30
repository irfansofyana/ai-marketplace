# Question Bank

Reusable `AskUserQuestion` patterns for the techdocs skill. These patterns are designed to be used across all document types and can be adapted for specific templates.

## Discovery Questions

### Document Type Selection

```python
AskUserQuestion(
    questions=[{
        "question": "What type of document would you like to create?",
        "header": "📄 Document Type",
        "options": [
            {"label": "One-Pager", "description": "Concise proposal for features, changes, or decisions (1-3 pages)"},
            {"label": "RFC", "description": "Request for Comments - detailed design proposal for cross-team review (coming soon)"},
            {"label": "TSD", "description": "Technical Specification Document - comprehensive technical design (coming soon)"},
            {"label": "ADR", "description": "Architecture Decision Record - document a specific architectural decision (coming soon)"}
        ],
        "multiSelect": false
    }]
)
```

### User Readiness Assessment

```python
AskUserQuestion(
    questions=[{
        "question": "How much information do you have ready?",
        "header": "📋 Information Readiness",
        "options": [
            {"label": "I have everything ready", "description": "I know the problem, solution, alternatives, and risks - let's draft quickly"},
            {"label": "I have the basics", "description": "I know the problem and rough solution, need help with details"},
            {"label": "Just an idea", "description": "I have a concept but need help structuring and developing it"},
            {"label": "Need to research first", "description": "I need to gather more information before writing"}
        ],
        "multiSelect": false
    }]
)
```

### Document Purpose

```python
AskUserQuestion(
    questions=[{
        "question": "What is the main purpose of this document?",
        "header": "🎯 Document Purpose",
        "options": [
            {"label": "Get approval for a new project/feature", "description": "Seeking stakeholder sign-off to proceed"},
            {"label": "Propose a solution to an existing problem", "description": "Documenting a fix or improvement"},
            {"label": "Make a technical decision", "description": "Choosing between approaches or technologies"},
            {"label": "Request resources or budget", "description": "Justifying investment"},
            {"label": "Document a process change", "description": "Proposing workflow changes"},
            {"label": "Other", "description": "I'll describe the purpose"}
        ],
        "multiSelect": false
    }]
)
```

### Target Audience

```python
AskUserQuestion(
    questions=[{
        "question": "Who is the primary audience?",
        "header": "👥 Target Audience",
        "options": [
            {"label": "Engineering team", "description": "Technical peers"},
            {"label": "Engineering leadership", "description": "Tech leads, managers, directors"},
            {"label": "Product team", "description": "PMs or designers"},
            {"label": "Executive leadership", "description": "VPs, C-level"},
            {"label": "Cross-functional", "description": "Mix of technical and non-technical"},
            {"label": "External", "description": "Partners or clients"}
        ],
        "multiSelect": true
    }]
)
```

### Technical Depth

```python
AskUserQuestion(
    questions=[{
        "question": "What level of technical detail?",
        "header": "📊 Technical Depth",
        "options": [
            {"label": "High-level overview", "description": "Business impact focus, minimal technical details"},
            {"label": "Moderate depth", "description": "Balance of business context and technical approach"},
            {"label": "Deep technical detail", "description": "Comprehensive technical explanation"}
        ],
        "multiSelect": false
    }]
)
```

### Timeline

```python
AskUserQuestion(
    questions=[{
        "question": "What is your timeline?",
        "header": "⏰ Timeline",
        "options": [
            {"label": "Urgent - today", "description": "Need a quick draft ASAP"},
            {"label": "This week", "description": "Have a few days to refine"},
            {"label": "No rush", "description": "Quality over speed"}
        ],
        "multiSelect": false
    }]
)
```

## Content Gathering Questions

### Topic and Problem (Quick)

```python
AskUserQuestion(
    questions=[
        {
            "question": "What is the title/topic?",
            "header": "📝 Title",
            "placeholder": "e.g., Migrate authentication to OAuth 2.0"
        },
        {
            "question": "What problem are you solving? (1-2 sentences)",
            "header": "🔍 Problem Summary",
            "placeholder": "e.g., Current auth doesn't support SSO, causing friction for enterprise customers"
        }
    ]
)
```

### Problem Category

```python
AskUserQuestion(
    questions=[{
        "question": "What type of problem is this?",
        "header": "🔍 Problem Category",
        "options": [
            {"label": "Technical debt", "description": "Code is hard to maintain or scale"},
            {"label": "Performance issue", "description": "System is slow or unreliable"},
            {"label": "Missing functionality", "description": "Users need a feature that doesn't exist"},
            {"label": "Security/Compliance", "description": "Doesn't meet requirements"},
            {"label": "Developer experience", "description": "Tooling or process slows development"},
            {"label": "Cost optimization", "description": "Current approach is too expensive"},
            {"label": "Other", "description": "I'll describe it"}
        ],
        "multiSelect": false
    }]
)
```

### Impact Scope

```python
AskUserQuestion(
    questions=[{
        "question": "Who is affected?",
        "header": "👥 Impact Scope",
        "options": [
            {"label": "End users/Customers", "description": "People using the product"},
            {"label": "Engineering team", "description": "Developers working on the codebase"},
            {"label": "Operations/SRE", "description": "People maintaining production"},
            {"label": "Other internal teams", "description": "Product, support, sales, etc."},
            {"label": "Multiple groups", "description": "I'll specify"}
        ],
        "multiSelect": true
    }]
)
```

### Impact Metrics

```python
AskUserQuestion(
    questions=[{
        "question": "Can you quantify the impact?",
        "header": "📈 Impact Metrics",
        "options": [
            {"label": "Time lost", "description": "Hours/week spent on workarounds"},
            {"label": "Error rates", "description": "Incidents per month"},
            {"label": "Cost impact", "description": "Dollar amount"},
            {"label": "Customer impact", "description": "Churn, complaints, NPS"},
            {"label": "No metrics yet", "description": "Skip quantification"}
        ],
        "multiSelect": true
    }]
)
```

### Solution Type

```python
AskUserQuestion(
    questions=[{
        "question": "What type of solution?",
        "header": "💡 Solution Type",
        "options": [
            {"label": "Build new functionality", "description": "Create something new"},
            {"label": "Refactor existing code", "description": "Improve current implementation"},
            {"label": "Migrate to new system", "description": "Move to different platform"},
            {"label": "Adopt third-party", "description": "Use existing tool or service"},
            {"label": "Process change", "description": "Change how we work"},
            {"label": "Other", "description": "I'll describe it"}
        ],
        "multiSelect": false
    }]
)
```

### Alternatives Count

```python
AskUserQuestion(
    questions=[{
        "question": "How many alternatives did you consider?",
        "header": "🔀 Alternatives",
        "options": [
            {"label": "1 alternative", "description": "Considered one other option"},
            {"label": "2-3 alternatives", "description": "Evaluated a few approaches"},
            {"label": "4+ alternatives", "description": "Extensive evaluation"},
            {"label": "None yet", "description": "Help me think of some"}
        ],
        "multiSelect": false
    }]
)
```

### Risk Categories

```python
AskUserQuestion(
    questions=[{
        "question": "What risks concern you?",
        "header": "⚠️ Risks",
        "options": [
            {"label": "Technical complexity", "description": "Harder than expected"},
            {"label": "Timeline risk", "description": "Might take longer"},
            {"label": "Integration challenges", "description": "May not work with existing systems"},
            {"label": "Team capacity", "description": "Bandwidth or expertise gaps"},
            {"label": "Cost overruns", "description": "Might exceed budget"},
            {"label": "User adoption", "description": "Users might not adopt it"},
            {"label": "Security concerns", "description": "Potential vulnerabilities"},
            {"label": "Other", "description": "I'll describe specific risks"}
        ],
        "multiSelect": true
    }]
)
```

### Stakeholders

```python
AskUserQuestion(
    questions=[{
        "question": "Who needs to sign off?",
        "header": "✍️ Approvers",
        "options": [
            {"label": "Direct manager only", "description": "Single approver"},
            {"label": "Multiple engineering leads", "description": "Several tech decision-makers"},
            {"label": "Cross-functional group", "description": "Engineering, product, design, etc."},
            {"label": "Executive approval", "description": "Senior leadership required"},
            {"label": "I'll specify names", "description": "Let me list specific people"}
        ],
        "multiSelect": false
    }]
)
```

## Output Questions

### Diagrams (Optional)

```python
AskUserQuestion(
    questions=[{
        "question": "Do you need diagrams?",
        "header": "📊 Diagrams (Optional)",
        "options": [
            {"label": "Architecture diagram", "description": "System components and relationships"},
            {"label": "Flowchart", "description": "Process or decision flow"},
            {"label": "Sequence diagram", "description": "Component interactions over time"},
            {"label": "No diagrams", "description": "Text-only document"},
            {"label": "Suggest if helpful", "description": "You recommend"}
        ],
        "multiSelect": true
    }]
)
```

### Output Format

```python
AskUserQuestion(
    questions=[{
        "question": "What output format?",
        "header": "📁 Output Format",
        "options": [
            {"label": "Word (.docx)", "description": "Editable for collaboration"},
            {"label": "PDF (.pdf)", "description": "Fixed format for distribution"},
            {"label": "Markdown (.md)", "description": "For version control or wikis"},
            {"label": "Decide later", "description": "Choose after reviewing draft"}
        ],
        "multiSelect": false
    }]
)
```

### Research Assistance

```python
AskUserQuestion(
    questions=[{
        "question": "Would you like research assistance?",
        "header": "🔬 Research",
        "options": [
            {"label": "Industry best practices", "description": "How others solved similar problems"},
            {"label": "Technical context", "description": "Info about proposed technologies"},
            {"label": "Competitors/alternatives", "description": "Existing solutions in market"},
            {"label": "Costs/pricing", "description": "Pricing for technologies or services"},
            {"label": "No research needed", "description": "I have all the context"}
        ],
        "multiSelect": true
    }]
)
```

### Review and Refinement

```python
AskUserQuestion(
    questions=[{
        "question": "How would you like to proceed?",
        "header": "✅ Next Steps",
        "options": [
            {"label": "Review and refine", "description": "Go through sections for feedback"},
            {"label": "Save as Word", "description": "Create .docx file"},
            {"label": "Save as PDF", "description": "Create .pdf file"},
            {"label": "Save as Markdown", "description": "Create .md file"},
            {"label": "Review then save", "description": "Feedback first, then choose format"}
        ],
        "multiSelect": false
    }]
)
```

### Section Refinement

```python
AskUserQuestion(
    questions=[{
        "question": "Which sections to refine?",
        "header": "✏️ Refinement",
        "options": [
            {"label": "Problem statement", "description": "Refine problem articulation"},
            {"label": "Goals", "description": "Adjust outcomes or metrics"},
            {"label": "Proposed solution", "description": "Modify solution description"},
            {"label": "Alternatives", "description": "Add or modify alternatives"},
            {"label": "Risks", "description": "Update risk assessment"},
            {"label": "Tone/style", "description": "Adjust writing style"},
            {"label": "All good", "description": "Proceed to save"}
        ],
        "multiSelect": true
    }]
)
```

## Usage Notes

1. **Adaptive questioning**: Skip questions the user has already answered
2. **Context-aware**: Adjust follow-up questions based on previous answers
3. **Progressive disclosure**: Start with essential questions, ask details only when needed
4. **Batch related questions**: Group related questions to reduce back-and-forth
