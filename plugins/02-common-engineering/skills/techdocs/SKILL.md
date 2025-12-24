---
name: techdocs
description: Interactive technical documentation writer using template-based creation with guided questioning. Use when users request technical documentation, one-pagers, proposals, RFCs, TSDs, ADRs, POCs, experiments, design documents, or need help documenting decisions. Supports One-Pager, RFC, TSD, ADR, and POC/Experiment document types with automatic AI recommendation. Integrates with web-research-specialist agent for research and mermaid skill for diagrams.
license: MIT
metadata:
  author: irfansofyana
  version: "1.1.0"
  last-updated: "2024-12-24"
allowed-tools: AskUserQuestion Bash Read
---

# Technical Documentation Skill

Create professional technical documentation using structured templates with interactive guidance. This skill helps users articulate their ideas clearly, producing well-organized documents.

**Key principle**: All information comes from the user through interactive prompts. Do NOT read the user's codebase.

## Skill Philosophy

This skill follows a **guided discovery approach** rather than automatic generation:
- Information comes from the user, not the codebase
- Progressive questioning reveals user's thinking
- Templates structure the thought process
- Research assistance when needed, not automatic
- Quality validation ensures completeness

This approach produces better documentation because it forces users to think through their proposals systematically.

## Supported Document Types

| Type | Template | Status | Use Case |
|------|----------|--------|----------|
| **One-Pager** | [assets/templates/one-pager/](assets/templates/one-pager/) | ✅ Active | Proposals, feature briefs, quick decisions |
| **RFC** | [assets/templates/rfc/](assets/templates/rfc/) | ✅ Active | Request for Comments, cross-team design proposals |
| **TSD** | [assets/templates/tsd/](assets/templates/tsd/) | ✅ Active | Technical Specification Documents (APIs, data models) |
| **ADR** | [assets/templates/adr/](assets/templates/adr/) | ✅ Active | Architecture Decision Records (technology choices) |
| **POC/Experiment** | [assets/templates/poc-experiment/](assets/templates/poc-experiment/) | ✅ Active | Proof of concepts, technical experiments, technology validation |

## Three-Phase Architecture

> **IMPORTANT**: This skill now follows a unified three-phase architecture that applies to ALL document types:
> 1. **Phase 1: Universal Discovery** (Problem Validation + Context Input) - SAME FOR ALL DOCUMENT TYPES
> 2. **Phase 2: Document Type Selection** (AI recommends, user decides)
> 3. **Phase 3: Template-Specific Discovery** (Questions unique to chosen document type)

**Key Benefits:**
- Problem clarity BEFORE committing to document format
- AI can recommend the most appropriate format based on the situation
- Single unified requirements gathering works for all document types
- Template-specific questions are more focused (problem already understood)

## Workflow Overview

> **IMPORTANT**: You MUST follow the workflow gates below. Do NOT skip to content generation without completing mandatory steps.

### Workflow Gates (Mandatory Checkpoints)

| Gate | Checkpoint | Required? | Blocked Until |
|------|------------|-----------|---------------|
| 1 | Problem Validation Gate complete | ✅ Yes | Cannot proceed without validated problem |
| 2 | Document type selected | ✅ Yes | Cannot proceed without type selection |
| 3 | Research offered (if Exploratory/Research-first) | Conditional | Must offer before content if user is uncertain |
| 4 | Quality validation | ✅ Yes | Cannot present final output without validation |

### Phase 1: Universal Discovery (ALL Document Types)

> **CRITICAL**: Phase 1 is MANDATORY for ALL document types. The Problem Validation Gate must be completed BEFORE selecting a document type.

**Goal**: Validate the problem and gather rich context BEFORE deciding on document format.

#### Step 1: Readiness Check

Ask user to choose their readiness level. See [references/question-bank.md](references/question-bank.md) for the `AskUserQuestion` pattern.

| Readiness | Description | Workflow |
|-----------|-------------|----------|
| **Quick Start** | User has all details ready | Skip to Phase 2 (Document Type Selection) |
| **Guided** | User has basics, needs help | Complete Problem Validation Gate → Phase 2 |
| **Exploratory** | Just an idea | Problem Validation Gate → Research (to fill gaps) → Phase 2 |
| **Research-first** | Needs to gather information | Problem Validation Gate → Research (to gather context) → Phase 2 |

#### Step 2: Problem Validation Gate (MANDATORY)

> **GATE 1**: You MUST complete the Problem Validation Gate BEFORE selecting a document type or discussing solutions.

For Guided, Exploratory, and Research-first modes, complete the **Universal Discovery** questions:

**Mandatory Problem Validation (4 questions):**
1. **Current State Deep Dive**: "Walk me through what happens now step by step."
2. **Evidence of Problem**: "How do we know this is a problem? What evidence exists?"
3. **Who Has This Problem** (conditional): If business-facing → "Who specifically experiences this?"; If technical-only → "Which teams/services are affected?"
4. **Current vs Desired State**: "Complete these sentences: 'Today, ________ happens.' and 'After we fix this, ________ should happen.'"

**Enhanced Problem Questions (optional):**
5. **Pain Point Specificity**: "What's the SINGLE WORST thing about the current situation?"
6. **Impact Urgency**: "What's the cost of NOT fixing this?"

**Solution Challenge Flow**:
If user jumps to solution before completing Problem Validation Gate:
- Acknowledge the solution idea
- Ask: "What PROBLEM does this solve?"
- Complete Problem Validation Gate
- Then proceed to Phase 2

#### Step 3: Rich Context Input (Optional)

**These can be asked at ANY point** to enrich the proposal:

- **Related Documents**: "Are there related documents we should reference? (ADRs, RFCs, TSDs, tickets)"
- **Document Attachment Flow**: "You can provide context in three ways: File paths (I'll read them), Paste content, Verbal description. Which do you prefer?"
- **Historical Context**: "Has this been proposed or attempted before?"
- **Technical Context**: "What technologies/systems are involved? Any constraints?"
- **Team Context**: "Who will implement this? Any organizational constraints?"

See [references/question-bank.md](references/question-bank.md) for Universal Discovery question patterns (lines 138-350).

### Phase 2: Document Type Selection (NEW)

> **GATE 2**: You MUST select a document type AFTER completing Universal Discovery (or after Quick Start users have all information).

**Goal**: Recommend and select the most appropriate document type based on the validated problem.

#### Step 1: AI Analysis

Analyze the problem to recommend a document type:

**Decision Logic:**

| Indicators | Recommended Type | Rationale |
|------------|------------------|-----------|
| Simple problem, single solution, quick decision | **One-Pager** | Concise proposal for fast approval |
| Complex architecture, multiple services, implementation phases | **RFC** | Detailed design requires thorough analysis |
| API specification, data model, interface definition | **TSD** | Technical implementation details |
| Technology choice, framework decision, architectural pivot | **ADR** | Decision-focused with alternatives analysis |
| User unsure, unclear scope | **Ask User** | Present options with descriptions |

#### Step 2: Present Recommendation

**Example:**
```
Based on what you've described, I recommend an **RFC** because:
- This involves multiple services and implementation phases
- There are significant migration and rollback considerations
- The architectural approach needs thorough review

Does that sound right?
```

#### Step 3: User Decision

**Options:**
- Accept AI recommendation
- Choose different type (with explanation)
- See all options with descriptions
- Ask for help deciding

### Phase 3: Template-Specific Discovery

**Goal**: Ask questions unique to the chosen document type AFTER the problem is understood and type is selected.

**Process:**
1. Load the appropriate template guidance: `assets/templates/{type}/guidance.md`
2. For each section, ask template-specific questions from guidance.md
3. Use Universal Discovery output in applicable sections (see guidance.md for mapping)
4. Generate content using template structure

**Template-Specific Questions Examples:**
- **One-Pager**: Sign-offs required, timeline urgency, high-level risks
- **RFC**: Architecture overview, implementation phases, migration strategy, rollback plan
- **TSD**: API endpoints, data models, interface contracts, error handling
- **ADR**: Alternatives considered (mandatory 2+), decision criteria, trade-offs analysis

### Research Integration (within Phases)

**When to offer research:**
- During **Phase 1 (Universal Discovery)**: AFTER Problem Validation Gate, if user selects "Exploratory" or "Research-first" mode
  - Research fills gaps identified during Problem Validation (e.g., "we don't have metrics on X", "we need to know what competitors do")
- During **Phase 3 (Template-Specific)**: If template-specific questions reveal information gaps

**How to invoke research:**
- Invoke `agent:web-research-specialist` for industry best practices, technical context, competitor analysis
- Use research findings to enrich Universal Discovery output or answer Template-Specific questions

**Key Principle**: Problem Validation Gate ALWAYS comes first. Research is targeted based on what gaps are identified during validation.

### Phase 4: Content Generation

**CRITICAL: Output Rules**

⚠️ **What to INCLUDE in user-facing documents:**
- ✅ Section headings from template.md (e.g., ## Problem, ## High level goal)
- ✅ User-provided content and information
- ✅ Diagrams (if requested and generated via mermaid skill)
- ✅ Placeholder text in italics (e.g., *Describe the problem*)
- ✅ Tables, lists, and formatting for user content

⚠️ **What to EXCLUDE from user-facing documents:**
- ❌ Checkboxes (✅ or - [ ]) of any kind
- ❌ HTML comments (<!--- ... --->)
- ❌ Quality criteria statements
- ❌ "GUIDANCE QUESTIONS" sections
- ❌ References to quality-checklist.md
- ❌ Any validation or assessment language

**Template Files Purpose:**
- `template.md` - Clean structure with section headings (use for document structure)
- `guidance.md` - Section-specific guidance with questions and quality criteria (read for context, never copy to output)
- `quality-checklist.md` - Validation criteria (use in Phase 5 only, never show to user)

**Content Generation Process:**

1. **Load template guidance**: Read the appropriate `assets/templates/{type}/guidance.md`
2. **Work section-by-section**: For each template section:
   - Explain what the section needs
   - Ask targeted questions from guidance.md (use choices where possible)
   - Generate draft content WITHOUT any checkboxes or quality criteria
   - Get feedback before moving on
3. **Reference examples**: Use `assets/templates/{type}/examples.md` for quality benchmarks

### Visual Aids (Optional)

**Only if user requested diagrams**:
1. Ask what the diagram should show
2. Use `common-engineering:mermaid` skill to generate validated diagrams
3. Integrate into document

Do NOT proactively suggest diagrams unless user requested them.

### Phase 5: Review & Output

**MANDATORY: Pre-Output Self-Check**

Before presenting ANY draft to the user, you MUST verify:

- [ ] ❌ NO checkboxes (✅ or - [ ]) anywhere in the document
- [ ] ❌ NO HTML comments in the document
- [ ] ❌ NO quality criteria text in the document
- [ ] ❌ NO "GUIDANCE QUESTIONS" sections in the document
- [ ] ❌ NO references to quality-checklist.md in the document
- [ ] ✅ ONLY section headings and user-provided content included

**If ANY prohibited content found**: Remove it immediately before presenting to user.

**Phase 5 Workflow:**

1. **Present Draft** (WITHOUT validation criteria):
   - Show the complete document to the user
   - Do NOT include any checkboxes, quality criteria, or validation language
   - The draft should contain ONLY section headings and user content

2. **Internal Validation** (Using quality-checklist.md):
   - Read `assets/templates/{type}/quality-checklist.md`
   - INTERNALLY validate the document against quality criteria
   - Do NOT show the checklist to the user
   - Do NOT include checkboxes in any response

3. **Offer Improvements** (Without showing checklist):
   - If gaps identified during validation, ask targeted questions
   - Suggest enhancements based on quality criteria (but don't show the criteria)
   - Example: "Would you like to add more specific metrics to the goal section?" (NOT "The checklist says...")

4. **User Refinements**:
   - Let user request changes
   - Make updates as requested
   - Continue to ensure no prohibited content appears

5. **Final Output**:
   - Run Pre-Output Self-Check one more time
   - Save using `document-skills:docx` or `document-skills:pdf`
   - Confirm no prohibited content in final document

## How to Invoke This Skill

This skill activates automatically when users request technical documentation. It works through interactive prompts:

1. **User trigger**: User says "write a one-pager" or similar phrase
2. **Skill activation**: techdocs skill loads and begins workflow
3. **Interactive prompting**: Skill asks questions using AskUserQuestion
4. **Research integration**: If needed, invoke `agent:web-research-specialist` using Task tool
5. **Diagram generation**: If needed, invoke `common-engineering:mermaid` skill

### Integration Examples

**Research assistance:**
```
When user selects "Research-first" or input is vague:
1. Use Task tool with subagent_type="common-engineering:web-research-specialist"
2. Pass research query (e.g., "industry best practices for OAuth implementation")
3. Incorporate findings into document sections
```

**Diagram creation:**
```
When user requests diagrams:
1. Invoke common-engineering:mermaid skill
2. Provide diagram type and content requirements
3. Mermaid skill validates and generates PNG
4. Include diagram in document output
```

## Quality Validation

⚠️ **CRITICAL**: Quality validation is for INTERNAL use only. Never show checkboxes or validation criteria to users.

**How to validate:**

1. **Read the validation file**: `assets/templates/{type}/quality-checklist.md`
2. **Validate internally**: Check the document against criteria WITHOUT showing the checklist
3. **Address gaps**: If issues found, ask targeted questions to improve content
4. **Never show criteria**: Offer improvements without mentioning the validation checklist

**Example - CORRECT approach:**
- ✅ "Would you like to add specific metrics to measure success?"
- ✅ "I notice the risks section could use mitigation strategies. Shall I help with that?"

**Example - WRONG approach:**
- ❌ "The quality checklist says we need metrics"
- ❌ "Let me check if this passes validation: - [ ] Metrics included"

### Universal Validation Criteria (Internal Use Only)

These criteria are checked internally during Phase 5:

- All required sections complete
- Metadata filled (authors, date, status)
- Problem clearly stated with impact
- Clear recommendation made
- Risks identified with mitigations

### Document-Specific Validation

Each document type has detailed validation criteria in `assets/templates/{type}/quality-checklist.md`. Read this file during Phase 5 but NEVER show it to users.

## Reference Files

| File | Purpose | Use In |
|------|---------|--------|
| [writing-guidelines.md](references/writing-guidelines.md) | Technical writing best practices | All phases |
| [question-bank.md](references/question-bank.md) | Reusable `AskUserQuestion` patterns | Phase 1, 3 |
| assets/templates/{type}/template.md | Clean document structure (headings only) | Phase 3 (structure) |
| assets/templates/{type}/guidance.md | Section-specific guidance with questions and quality criteria (DO NOT copy to output) | Phase 3 (read for context) |
| assets/templates/{type}/quality-checklist.md | Validation criteria (DO NOT show to user) | Phase 5 (internal validation) |
| assets/templates/{type}/examples.md | Completed example documents | Phase 3 (quality reference) |

**File Usage Rules:**
- ✅ USE template.md for document structure
- ✅ READ guidance.md for understanding
- ✅ READ quality-checklist.md for internal validation
- ❌ DO NOT copy content from guidance files to user output
- ❌ DO NOT show checkboxes or quality criteria to users

## Integration Points

### Required Skills/Agents

- **`agent:web-research-specialist`** (common-engineering plugin)
  - Purpose: Research industry best practices, technical context, competitors
  - When to use: User selects "Research-first" or "Exploratory" mode
  - Invocation: `Task(subagent_type="common-engineering:web-research-specialist", ...)`

- **`common-engineering:mermaid`** (common-engineering plugin)
  - Purpose: Generate validated Mermaid diagrams with automatic syntax checking
  - When to use: User requests diagrams or you recommend them for complex flows
  - Invocation: Invoke skill via "create a [diagram-type] diagram showing [content]"

### Optional Skills (Output)

- **`document-skills:docx`** (document-skills plugin)
  - Purpose: Export document to Microsoft Word format
  - Invocation: Use when user selects "Word" output format

- **`document-skills:pdf`** (document-skills plugin)
  - Purpose: Export document to PDF format
  - Invocation: Use when user selects "PDF" output format

### Dependencies

⚠️ **Required plugins:**
- common-engineering (for web-research-specialist agent and mermaid skill)
- document-skills (for docx/pdf export - optional, can output markdown without this)

## Adding New Document Types

To add a new document type (e.g., POC/Experiment):

1. Create `assets/templates/poc-experiment/` directory
2. Add `template.md` - Document structure with guidance comments
3. Add `guidance.md` - Section-by-section guidance for the agent
4. Add `quality-checklist.md` - Validation criteria (internal use only)
5. Add `examples.md` - 2-3 completed examples
6. Update the document types table above (line 29-37)
7. Update `techdocs-writer.md` agent Decision Logic table
8. Update `techdocs-writer.md` agent Template-Specific Questions Examples
9. Add any type-specific questions to `references/question-bank.md`

The core workflow in this skill handles all document types generically. Document-specific logic lives in the template files.

## Adaptive Modes

The three-phase architecture supports different user readiness levels:

### Quick Start Mode
For users with "I have everything ready":
```
1. Skip to Phase 2 (Document Type Selection)
2. User provides problem context directly
3. AI recommends document type based on user input
4. Complete Phase 3 (Template-Specific Discovery)
5. Generate content using template
6. Review and output
```

### Guided Mode
For users with "I have the basics":
```
1. Phase 1: Complete Problem Validation Gate
2. Phase 2: AI recommends document type
3. Phase 3: Template-specific questions for each section
4. Generate content section-by-section with feedback
5. Review complete document
6. Output
```

### Exploratory Mode
For users with "Just an idea":
```
1. Phase 1: Problem Validation Gate → Research (to fill gaps)
2. Phase 2: AI recommends document type based on validated problem + research findings
3. Phase 3: Template-specific discovery
4. Content generation with research findings integrated
5. Review and output
```

### Research-First Mode
For users who need to gather information:
```
1. Phase 1: Problem Validation Gate → Research (to gather context) → Context Input
2. Phase 2: AI recommends document type
3. Phase 3: Template-specific discovery
4. Content generation with research findings
5. Review and output
```

## Best Practices

1. **Always assess readiness first**: Before generating ANY content, ask how much information the user has ready
2. **Offer research proactively**: If user input is vague or they seem uncertain, offer research assistance
3. **Ask before assuming**: Confirm understanding before generating content
4. **Use choices**: Prefer multiple-choice questions over open-ended when possible
5. **Skip what's known**: Don't re-ask information user already provided
6. **Show progress**: Let user know which section you're working on
7. **Validate quality**: Use the checklist before presenting final output
8. **Reference examples**: Point users to examples.md when they're unsure of format
