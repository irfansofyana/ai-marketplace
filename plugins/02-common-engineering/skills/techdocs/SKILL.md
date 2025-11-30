---
name: techdocs
description: Guide users through writing technical documentation using templates. Supports one-pager docs (proposals, feature briefs) with interactive section-by-section guidance. Extensible for RFC, TSD, API docs, and more. Integrates with web research for context gathering and mermaid diagrams for visualization.
---

# Technical Documentation Skill

Create professional technical documentation using structured templates with interactive guidance. This skill helps users think through and articulate their ideas clearly, producing well-organized documents that follow established patterns.

## Supported Document Types

| Type | Template | Status | Use Case |
|------|----------|--------|---------|
| **One-Pager** | [one-page-template.md](templates/one-page-template.md) | ✅ Active | Proposals, feature briefs, quick decisions |
| RFC | *Coming soon* | 🚧 Planned | Request for Comments, design proposals |
| TSD | *Coming soon* | 🚧 Planned | Technical Specification Documents |
| API Docs | *Coming soon* | 🚧 Planned | API reference documentation |

## 🚀 Workflow Overview

When helping users create documentation, follow this proactive workflow:

### Phase 1: Discovery & Context Gathering

1. **Identify document type** - Determine which template to use
2. **Read the template** - Load the appropriate template file for structure and guidance
3. **Understand the topic** - Ask clarifying questions about what they're proposing
4. **Conduct research** - Use `agent:web-research-specialist` to gather context (see Research Guidelines below)
5. **Collect key information** - Gather essential details before writing

### Phase 2: Content Generation

1. **Work section-by-section** - Follow the template's guidance questions for each section
2. **Generate draft content** - Produce content that matches template structure exactly
3. **Add visual aids** - Use `common-engineering:mermaid` skill for diagrams when helpful

### Phase 3: Review & Output

1. **Quality check** - Use the template's quality criteria to validate
2. **Iterate on feedback** - Refine sections based on user input
3. **Clean the document** - Remove all `<!--- ... --->` guidance comments from the output
4. **Produce final document** - Use `document-skills:docx` or `document-skills:pdf` to save the output

**IMPORTANT:** The template contains HTML comments (`<!--- ... --->`) with guidance questions and quality criteria. These are for YOUR reference while writing. You MUST remove all these comments from the final document output. The user should only see the actual content, not the guidance.

### Output Location

When saving the final document, ask the user where they want to save it. Suggest sensible defaults:

- **Default location**: Current working directory or a `docs/` folder if it exists
- **Filename format**: `[project-name]-one-pager.[ext]` (e.g., `auth-service-migration-one-pager.docx`)
- **Always confirm** the full path with the user before saving

---

## Research Guidelines

Use `agent:web-research-specialist` to gather context before and during content generation. Research is especially valuable for:

### When to Research

- **Unfamiliar terms** - When the user mentions technologies, frameworks, or concepts you're uncertain about
- **Technology references** - To understand capabilities, limitations, and best practices of proposed technologies
- **Industry context** - To find how others have solved similar problems
- **Competitor analysis** - To understand existing solutions in the market
- **Best practices** - To validate the proposed approach against industry standards
- **Prior art** - To find existing implementations or case studies

### Research Triggers

Proactively suggest research when the user's proposal involves:

1. **New or emerging technologies** - Research current state, adoption, and community sentiment
2. **Integration with external systems** - Research API capabilities, limitations, and gotchas
3. **Security or compliance considerations** - Research standards and requirements
4. **Performance claims** - Research benchmarks and real-world performance data
5. **Cost estimates** - Research pricing models and typical costs

### How to Research

Invoke `agent:web-research-specialist` with specific queries:

```
Research: [specific technology/term] best practices for [use case]
Research: [competitor/solution] approach to [problem]
Research: [technology] vs [alternative] comparison for [context]
```

Incorporate research findings into the relevant sections:
- **Problem section** - Use research to quantify impact or validate pain points
- **Proposed solution** - Reference industry best practices and successful implementations
- **Alternatives** - Include research-backed pros/cons for each option
- **Risks** - Cite known issues or failure cases from research

---

## Integration Points

This skill integrates with:

- **`agent:web-research-specialist`** - For gathering context, research, technology references, and prior art
- **`common-engineering:mermaid`** - For creating diagrams (architecture, flowchart, sequence)
- **`document-skills:docx`** - For producing the final document as a Word document (.docx)
- **`document-skills:pdf`** - For producing the final document as a PDF (.pdf)

---

## Future Extensions

This skill is designed to be extended with additional document types:

- **RFC Template** - For detailed design proposals requiring broader review
- **TSD Template** - For comprehensive technical specifications
- **API Documentation** - For API reference documentation
- **ADR Template** - For Architecture Decision Records
