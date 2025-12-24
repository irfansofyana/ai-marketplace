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

### User Readiness Assessment (MANDATORY - Gate 2)

> **This question MUST be asked before generating any content.** Do not skip this step.

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

### Proactive Research Offer (When User Seems Uncertain)

> Use this when user's input is vague, or they selected "Just an idea" or "Need to research first".

```python
AskUserQuestion(
    questions=[{
        "question": "Before we start writing, would you like me to help research context?",
        "header": "🔍 Research Assistance",
        "options": [
            {"label": "Yes, research first", "description": "Help me gather industry context, best practices, or technical information"},
            {"label": "No, I'll provide the context", "description": "I have the information I need, let's proceed with questions"},
            {"label": "Let me explain what I know", "description": "I'll share what I have, then we can decide if research is needed"}
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

## Universal Discovery Questions

> **IMPORTANT**: These questions are part of the NEW three-phase architecture.
> Phase 1 (Universal Discovery) applies to ALL document types.
> Phase 2 (Document Type Selection) comes AFTER Universal Discovery.
> Phase 3 (Template-Specific) comes AFTER document type is chosen.

### Problem Validation Gate (MANDATORY - Universal for All Document Types)

> **CRITICAL**: The Problem Validation Gate MUST be completed BEFORE selecting a document type or discussing solutions. This applies to ALL document types (One-Pager, RFC, TSD, ADR).

#### 1. Current State Deep Dive

```python
AskUserQuestion(
    questions=[{
        "question": "Let's start by understanding the current situation. Walk me through what happens now step by step.",
        "header": "🔍 Current State",
        "placeholder": "Describe the current workflow, process, or situation in detail..."
    }]
)
```

**Follow-up if needed:**
- "What does 'broken' or 'problematic' look like in practice? Be specific."
- "Describe the current workflow/process as if explaining to someone new."

#### 2. Evidence of Problem

```python
AskUserQuestion(
    questions=[{
        "question": "How do we know this is a problem? What evidence exists?",
        "header": "📊 Evidence",
        "options": [
            {"label": "User complaints", "description": "Direct feedback from users or customers"},
            {"label": "Performance metrics", "description": "Quantitative data (latency, errors, throughput)"},
            {"label": "Error logs", "description": "System errors, exceptions, failures"},
            {"label": "Customer feedback", "description": "Sales objections, churn, NPS, support tickets"},
            {"label": "Internal observations", "description": "Developer/team experience, pain points"}
        ],
        "multiSelect": true
    }]
)
```

**Follow-up quantification:**
- "Can you quantify the impact? (e.g., 50 errors/day, 2s slower, 100 users affected)"
- "How often does this happen?"

#### 3. Who Has This Problem? (Conditional)

> **Note**: Ask this based on the document purpose/audience. Skip if already clear from context.

```python
# If business-facing or audience includes end users:
AskUserQuestion(
    questions=[{
        "question": "Who specifically experiences this problem? Describe the user persona.",
        "header": "👤 Who's Affected",
        "placeholder": "e.g., Enterprise sales reps trying to close deals, Mobile users in poor network conditions..."
    }]
)

# If technical-only:
AskUserQuestion(
    questions=[{
        "question": "Which teams, services, or systems are affected?",
        "header": "👤 Who's Affected",
        "placeholder": "e.g., Payment service team, API consumers, Database cluster..."
    }]
)
```

**Follow-up:**
- "Who would notice if we fixed this?"

#### 4. Current vs Desired State (Gap Analysis)

```python
AskUserQuestion(
    questions=[
        {
            "question": "Complete this sentence: 'Today, ________ happens.'",
            "header": "📍 Current State",
            "placeholder": "e.g., Every API request queries the database directly..."
        },
        {
            "question": "Complete this sentence: 'After we fix this, ________ should happen.'",
            "header": "🎯 Desired State",
            "placeholder": "e.g., Frequently-accessed data should be served from cache..."
        }
    ]
)
```

**Follow-up:**
- "What's the gap between these two states?"

### Enhanced Problem Section Questions

> These questions are asked when working on the Problem section of any document type.

#### 5. Pain Point Specificity

```python
AskUserQuestion(
    questions=[
        {
            "question": "What's the SINGLE WORST thing about the current situation?",
            "header": "😩 Pain Point",
            "placeholder": "e.g., 2-second API latency causes 30% drop-off..."
        },
        {
            "question": "If you could fix ONE thing, what would it be?",
            "header": "🎯 Priority",
            "placeholder": "e.g., Reduce database query time..."
        }
    ]
)
```

#### 6. Impact Urgency

```python
AskUserQuestion(
    questions=[{
        "question": "What's the cost of NOT fixing this?",
        "header": "💸 Cost of Inaction",
        "options": [
            {"label": "Revenue impact", "description": "Lost sales, deals, customers"},
            {"label": "Time impact", "description": "Hours/week wasted on workarounds"},
            {"label": "Technical debt", "description": "Problem gets worse over time"},
            {"label": "Team morale", "description": "Frustration, burnout risk"},
            {"label": "Customer trust", "description": "Churn, complaints, bad reviews"}
        ],
        "multiSelect": true
    }]
)
```

**Follow-up:**
- "Is this getting worse over time, or stable?"

#### 7. Solution Challenge (When User Jumps to Solution)

> **Use this proactively**: If the user mentions a solution before the problem is validated, redirect them.

```python
# If user mentions solution early:
say("I see you're thinking about [solution]. Before we discuss solutions, let's validate the problem first.")
# Then proceed with Problem Validation Gate above

# Or as a question:
AskUserQuestion(
    questions=[{
        "question": "You mentioned [solution]. What PROBLEM does that solve?",
        "header": "🤔 Solution Challenge",
        "placeholder": "Help me understand what problem this solution addresses..."
    }]
)
```

### Rich Context Input (Optional)

> **These questions can be asked at ANY point** during or after Universal Discovery to enrich the proposal with existing information.

#### 8. Related Documents

```python
AskUserQuestion(
    questions=[{
        "question": "Are there related documents we should reference? (ADRs, RFCs, TSDs, tickets, design docs)",
        "header": "📚 Related Documents (Optional)",
        "options": [
            {"label": "Yes, ADRs exist", "description": "Previous architecture decisions"},
            {"label": "Yes, TSDs/RFCs exist", "description": "Related technical designs"},
            {"label": "Yes, tickets/issues", "description": "Jira, GitHub Issues, etc."},
            {"label": "Multiple types", "description": "Several kinds of documents"},
            {"label": "None", "description": "No related documents"},
            {"label": "Skip for now", "description": "May add later"}
        ],
        "multiSelect": true
    }]
)
```

**Follow-up (if yes):**
- See "Document Attachment Flow" below.

#### 9. Document Attachment Flow

```python
AskUserQuestion(
    questions=[{
        "question": "How would you like to provide the document context?",
        "header": "📎 Context Input Method",
        "options": [
            {"label": "File paths", "description": "I'll read the files directly"},
            {"label": "Paste content", "description": "Copy-paste from existing docs"},
            {"label": "Verbal description", "description": "I'll describe the key points"},
            {"label": "Skip", "description": "No additional context needed"}
        ],
        "multiSelect": false
    }]
)
```

**For file paths:**
- Use the `Read` tool to read the file contents
- Ask for file paths: "Please provide the file paths (one per line or comma-separated)"

**For paste content:**
- Ask user to paste relevant content from the documents

**For verbal:**
- Ask: "What are the key points from these documents I should know?"

#### 10. Historical Context

```python
AskUserQuestion(
    questions=[{
        "question": "Has this been proposed or attempted before?",
        "header": "📜 History (Optional)",
        "options": [
            {"label": "First time proposal", "description": "This is a new idea"},
            {"label": "Previously rejected", "description": "Similar proposal was declined"},
            {"label": "Partially completed", "description": "Some work was done but not finished"},
            {"label": "Ongoing effort", "description": "Currently in progress"},
            {"label": "Unknown", "description": "Not sure about history"},
            {"label": "Skip", "description": "Not relevant"}
        ],
        "multiSelect": false
    }]
)
```

**Follow-up (if not first time):**
- "What happened? Why did it fail/succeed?"
- "What's different this time?"

#### 11. Technical Context

```python
AskUserQuestion(
    questions=[
        {
            "question": "What technologies or systems are involved?",
            "header": "⚙️ Tech Stack (Optional)",
            "placeholder": "e.g., PostgreSQL, Redis, Node.js, Kubernetes..."
        },
        {
            "question": "Any relevant technical constraints or dependencies?",
            "header": "🔗 Constraints (Optional)",
            "placeholder": "e.g., Must maintain API compatibility, limited to AWS services,..."
        }
    ]
)
```

#### 12. Team/Organizational Context

```python
AskUserQuestion(
    questions=[
        {
            "question": "Who will implement this?",
            "header": "👥 Implementation Team (Optional)",
            "options": [
                {"label": "My team only", "description": "Single team can deliver independently"},
                {"label": "Multiple teams", "description": "Requires cross-team coordination"},
                {"label": "Not determined yet", "description": "Team assignment TBD"},
                {"label": "External dependency", "description": "Vendors or partners involved"},
                {"label": "Skip", "description": "Not relevant"}
            ],
            "multiSelect": false
        },
        {
            "question": "Any organizational constraints or priorities to consider?",
            "header": "🏢 Organizational Context (Optional)",
            "placeholder": "e.g., Q1 OKR alignment, budget approval needed, depends on X team's capacity..."
        }
    ]
)
```

### Document Type Selection (Phase 2)

> **IMPORTANT**: This section comes AFTER Universal Discovery is complete. The AI analyzes the gathered information and recommends a document type. The user can accept or override.

#### 13. Document Type Recommendation

> **AI Instructions**: Analyze the Universal Discovery outputs and recommend the most appropriate document type. Use the decision logic table in guidance.md.

```python
# AI analyzes:
# - Problem complexity (simple vs complex)
# - Scope (single service vs multi-service vs platform)
# - Evidence type and depth (clear metrics vs anecdotal)
# - Technical vs business focus
# - Previous attempts (historical context)

# Then recommends with rationale:
say("Based on what you've described, I recommend an **[TYPE]** because:")
say("- [Reason 1]")
say("- [Reason 2]")
say("Does that sound right?")

AskUserQuestion(
    questions=[{
        "question": "What document type would you like to create?",
        "header": "📄 Document Type",
        "options": [
            {"label": "Yes, let's do [TYPE]", "description": "Accept the recommendation"},
            {"label": "Choose different type", "description": "I'll explain why"},
            {"label": "Show all options", "description": "Compare One-Pager, RFC, TSD, ADR"},
            {"label": "Help me decide", "description": "I'm not sure which is right"}
        ],
        "multiSelect": false
    }]
)
```

**Decision Logic Table (for AI reference):**

| Indicators | Recommended Type | Rationale |
|------------|------------------|-----------|
| Simple problem, single solution, quick decision | **One-Pager** | Concise proposal for fast approval |
| Complex architecture, multiple services, implementation phases | **RFC** | Detailed design requires thorough analysis |
| API specification, data model, interface definition | **TSD** | Technical implementation details |
| Technology choice, framework decision, architectural pivot | **ADR** | Decision-focused with alternatives analysis |
| User unsure, unclear scope | **Ask User** | Present options with descriptions |

**Document Type Descriptions (for "Show all options"):**

- **One-Pager**: Concise proposal (1-3 pages) for features, changes, or decisions seeking quick approval
- **RFC (Request for Comments)**: Detailed design proposal (5-15 pages) for complex changes requiring cross-team review, architecture, implementation, migration, and rollback planning
- **TSD (Technical Specification)**: Comprehensive technical spec (5-20 pages) documenting APIs, data models, interfaces, error handling, and versioning
- **ADR (Architecture Decision Record)**: Decision record (1-3 pages) documenting a specific technology choice with alternatives considered, decision criteria, and trade-offs analysis

#### 14. User Chooses Different Type

```python
# If user selects "Choose different type":
AskUserQuestion(
    questions=[{
        "question": "Which document type would you prefer?",
        "header": "📄 Your Choice",
        "options": [
            {"label": "One-Pager", "description": "Concise proposal for quick approval"},
            {"label": "RFC", "description": "Detailed design with cross-team review"},
            {"label": "TSD", "description": "Technical specification for APIs/interfaces"},
            {"label": "ADR", "description": "Architecture decision record"}
        ],
        "multiSelect": false
    }]
)

# Follow up:
say("Why do you prefer [TYPE]? This helps me tailor the questions.")
```

#### 15. User Asks for Help Deciding

```python
# If user selects "Help me decide":
say("Let me help you choose. Here's a quick comparison:")
say("")
say("**One-Pager**: Best for simple problems, single solutions, quick decisions (1-3 pages)")
say("  Example: 'Add caching to improve API performance'")
say("")
say("**RFC**: Best for complex architecture, multiple services, implementation phases (5-15 pages)")
say("  Example: 'Migrate payment system to microservices with phased rollout'")
say("")
say("**TSD**: Best for API specs, data models, interface definitions (5-20 pages)")
say("  Example: 'User Authentication API v2 with OAuth 2.0'")
say("")
say("**ADR**: Best for technology choices, framework decisions, architecture pivots (1-3 pages)")
say("  Example: 'Choose between PostgreSQL and MongoDB for user data storage'")
say("")
say("Which one sounds right for your situation?")
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

1. **Readiness assessment is mandatory**: ALWAYS ask the readiness question (Gate 2) before generating content
2. **Proactively offer research**: If user selects "Just an idea" or "Need to research first", use the proactive research offer question
3. **Adaptive questioning**: Skip questions the user has already answered
4. **Context-aware**: Adjust follow-up questions based on previous answers
5. **Progressive disclosure**: Start with essential questions, ask details only when needed
6. **Batch related questions**: Group related questions to reduce back-and-forth
