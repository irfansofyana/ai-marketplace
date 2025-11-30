---
name: techdocs
description: Guide users through writing technical documentation using templates. Supports one-pager docs with interactive guidance. Extensible for RFC, TSD, ADR. Integrates with web research and mermaid diagrams.
---

# Technical Documentation Skill

Create professional technical documentation using structured templates with interactive guidance. This skill helps users articulate their ideas clearly, producing well-organized documents.

**Key principle**: All information comes from the user through interactive prompts. Do NOT read the user's codebase or files.

## Supported Document Types

| Type | Template | Status | Use Case |
|------|----------|--------|----------|
| **One-Pager** | [templates/one-pager/](templates/one-pager/) | ✅ Active | Proposals, feature briefs, quick decisions |
| RFC | *templates/rfc/* | 🚧 Coming | Request for Comments, cross-team design proposals |
| TSD | *templates/tsd/* | 🚧 Coming | Technical Specification Documents |
| ADR | *templates/adr/* | 🚧 Coming | Architecture Decision Records |

## Workflow Overview

### Phase 1: Discovery

**Goal**: Understand what the user needs before writing anything.

#### Step 1: Select Document Type
Ask user to choose document type. See [question-bank.md](question-bank.md) for the `AskUserQuestion` pattern.

#### Step 2: Assess User Readiness
Determine how much help the user needs:

| Readiness | Description | Workflow |
|-----------|-------------|----------|
| **Quick Start** | User has all details ready | 3 questions → draft |
| **Guided** | User has basics, needs help | Section-by-section prompts |
| **Exploratory** | Just an idea | Research + full discovery |

#### Step 3: Gather Core Information
Based on readiness, collect:
- Title/topic
- Problem summary
- Target audience
- Stakeholders
- Output preferences (format, diagrams)

See [question-bank.md](question-bank.md) for reusable question patterns.

### Phase 2: Research (Optional)

If user needs research assistance, invoke `agent:web-research-specialist` for:
- Industry best practices
- Technical context
- Competitor analysis
- Cost/pricing information

### Phase 3: Content Generation

1. **Load template guidance**: Read the appropriate `templates/{type}/guidance.md`
2. **Work section-by-section**: For each template section:
   - Explain what the section needs
   - Ask targeted questions (use choices where possible)
   - Generate draft content
   - Get feedback before moving on
3. **Reference examples**: Use `templates/{type}/examples.md` for quality benchmarks

### Phase 4: Visual Aids (Optional)

**Only if user requested diagrams**:
1. Ask what the diagram should show
2. Use `common-engineering:mermaid` skill to generate validated diagrams
3. Integrate into document

Do NOT proactively suggest diagrams unless user requested them.

### Phase 5: Review & Output

1. Present complete draft
2. Run quality validation (see below)
3. Ask for refinements
4. Save using `document-skills:docx` or `document-skills:pdf`

## Quality Validation

Before presenting the final document, validate against these criteria:

### Universal Checklist
- [ ] All required sections complete
- [ ] Metadata filled (authors, date, status)
- [ ] Problem clearly stated with impact
- [ ] Clear recommendation made
- [ ] Risks identified with mitigations

### Document-Specific Checklists
Each document type has additional criteria in its `guidance.md` file.

## Reference Files

| File | Purpose |
|------|---------||
| [writing-guidelines.md](writing-guidelines.md) | Technical writing best practices |
| [question-bank.md](question-bank.md) | Reusable `AskUserQuestion` patterns |
| templates/{type}/template.md | Document structure |
| templates/{type}/guidance.md | Section-specific guidance |
| templates/{type}/examples.md | Completed examples |

## Integration Points

- **`agent:web-research-specialist`** - Research, context gathering, prior art
- **`common-engineering:mermaid`** - Diagrams (only when user requests)
- **`document-skills:docx`** - Word document output
- **`document-skills:pdf`** - PDF output

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

1. **Ask before assuming**: Always confirm understanding before generating content
2. **Use choices**: Prefer multiple-choice questions over open-ended when possible
3. **Skip what's known**: Don't re-ask information user already provided
4. **Show progress**: Let user know which section you're working on
5. **Validate quality**: Use the checklist before presenting final output
6. **Reference examples**: Point users to examples.md when they're unsure of format
