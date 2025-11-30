---
name: techdocs
description: This skill should be used when creating technical documentation for software projects. Trigger phrases include "write technical documentation", "create a one-pager", "document a proposal", "write an RFC", "create design document", "document this decision", or "help me write a proposal". Guides users interactively through template-based document creation with structured questioning, research assistance, and diagram generation. Currently supports one-pager proposals with RFC, TSD, and ADR templates coming soon.
---

# Technical Documentation Skill

Create professional technical documentation using structured templates with interactive guidance. This skill helps users articulate their ideas clearly, producing well-organized documents.

**Key principle**: All information comes from the user through interactive prompts. Do NOT read the user's codebase or files.

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
| **One-Pager** | [templates/one-pager/](templates/one-pager/) | ✅ Active | Proposals, feature briefs, quick decisions |
| RFC | *templates/rfc/* | 🚧 Coming | Request for Comments, cross-team design proposals |
| TSD | *templates/tsd/* | 🚧 Coming | Technical Specification Documents |
| ADR | *templates/adr/* | 🚧 Coming | Architecture Decision Records |

## Workflow Overview

> **IMPORTANT**: You MUST follow the workflow gates below. Do NOT skip to content generation without completing mandatory steps.

### Workflow Gates (Mandatory Checkpoints)

| Gate | Checkpoint | Required? | Blocked Until |
|------|------------|-----------|---------------|
| 1 | Document type confirmed | ✅ Yes | Cannot proceed without selection |
| 2 | User readiness assessed | ✅ Yes | Cannot generate content until assessed |
| 3 | Research offered (if Exploratory/Research-first) | Conditional | Must offer before content if user is uncertain |
| 4 | Quality validation | ✅ Yes | Cannot present final output without validation |

### Phase 1: Discovery

**Goal**: Understand what the user needs before writing anything.

#### Step 1: Select Document Type
Ask user to choose document type. See [question-bank.md](question-bank.md) for the `AskUserQuestion` pattern.

#### Step 2: Assess User Readiness (MANDATORY)

> **GATE 2**: You MUST ask this question before generating ANY content. Even if the user provides a topic, ask about their readiness level first.

Determine how much help the user needs:

| Readiness | Description | Workflow |
|-----------|-------------|----------|
| **Quick Start** | User has all details ready | 3 questions → draft |
| **Guided** | User has basics, needs help | Section-by-section prompts |
| **Exploratory** | Just an idea | Research + full discovery |
| **Research-first** | Needs to gather information | Offer research → then discovery |

**If user seems uncertain or provides vague input**: Default to asking "Would you like me to help research context first?" before proceeding.

#### Step 3: Gather Core Information
Based on readiness, collect:
- Title/topic
- Problem summary
- Target audience
- Stakeholders
- Output preferences (format, diagrams)

See [question-bank.md](question-bank.md) for reusable question patterns.

### Phase 2: Research (Conditional)

> **GATE 3**: If user selected "Exploratory" or "Research-first" in Step 2, you MUST offer research assistance before proceeding to content generation.

If user needs research assistance, invoke `agent:web-research-specialist` for:
- Industry best practices
- Technical context
- Competitor analysis
- Cost/pricing information

### Phase 3: Content Generation

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

1. **Load template guidance**: Read the appropriate `templates/{type}/guidance.md`
2. **Work section-by-section**: For each template section:
   - Explain what the section needs
   - Ask targeted questions from guidance.md (use choices where possible)
   - Generate draft content WITHOUT any checkboxes or quality criteria
   - Get feedback before moving on
3. **Reference examples**: Use `templates/{type}/examples.md` for quality benchmarks

### Phase 4: Visual Aids (Optional)

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
   - Read `templates/{type}/quality-checklist.md`
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

1. **Read the validation file**: `templates/{type}/quality-checklist.md`
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

Each document type has detailed validation criteria in `templates/{type}/quality-checklist.md`. Read this file during Phase 5 but NEVER show it to users.

## Reference Files

| File | Purpose | Use In |
|------|---------|--------|
| [writing-guidelines.md](writing-guidelines.md) | Technical writing best practices | All phases |
| [question-bank.md](question-bank.md) | Reusable `AskUserQuestion` patterns | Phase 1, 3 |
| templates/{type}/template.md | Clean document structure (headings only) | Phase 3 (structure) |
| templates/{type}/guidance.md | Section-specific guidance with questions and quality criteria (DO NOT copy to output) | Phase 3 (read for context) |
| templates/{type}/quality-checklist.md | Validation criteria (DO NOT show to user) | Phase 5 (internal validation) |
| templates/{type}/examples.md | Completed example documents | Phase 3 (quality reference) |

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

To add a new document type (e.g., RFC):

1. Create `templates/rfc/` directory
2. Add `template.md` - Document structure with guidance comments
3. Add `guidance.md` - Section-by-section guidance for the agent
4. Add `examples.md` - 2-3 completed examples
5. Update the document types table above
6. Add any type-specific questions to `question-bank.md`

The core workflow in this skill handles all document types generically. Document-specific logic lives in the template files.

## Adaptive Modes

### Quick Start Mode
For users with "I have everything ready":
```
1. Ask: Title, problem summary, solution summary
2. Generate complete draft using template
3. Review and refine
4. Output
```

### Guided Mode
For users with "I have the basics":
```
1. Ask core questions (purpose, audience, stakeholders)
2. For each section: prompt → draft → feedback
3. Review complete document
4. Output
```

### Exploratory Mode
For users with "Just an idea":
```
1. Offer research assistance
2. Help define the problem through questions
3. Brainstorm solutions and alternatives together
4. Full guided mode for content generation
5. Output
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
