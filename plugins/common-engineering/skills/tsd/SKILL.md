---
name: tsd
description: This skill should be used when the user asks to "write a TSD", "create a TSD", "write a Technical Specification Document", "document an API", "spec out an API", "write an API spec", "document a data model", "write a technical spec", "create interface documentation", or needs a comprehensive technical specification covering API endpoints, data models, interface contracts, error handling, and versioning (5-20 pages).
license: MIT
metadata:
  author: irfansofyana
  version: "2.0.0"
  last-updated: "2026-03-18"
allowed-tools: AskUserQuestion Bash Read
---

# TSD Skill

Create Technical Specification Documents (5-20 pages) that comprehensively define APIs, data models, interface contracts, error handling, versioning strategies, and technical implementation details.

**Key principle**: All information comes from the user. Do NOT scan the codebase to discover APIs or schemas. The `Read` tool is only for reading user-provided context files (existing specs, API definitions, tickets) that the user explicitly shares.

## When to Use a TSD

- Defining new API endpoints or modifying existing ones
- Documenting data models and database schemas
- Specifying interface contracts between services
- Documenting integration points with external systems
- Capturing technical implementation details before or after development

## Workflow

### Phase 1: Gather Context

Parse what the user already provided in their initial request. Extract:
- **Scope**: What API, service, or data model is being specified?
- **Purpose**: What does this system do?
- **Consumers**: Who/what will use this API?
- **Constraints**: Auth, versioning, backward compatibility

**Only ask for what's genuinely missing.**

**Essential questions** (use `references/question-bank.md` patterns, ask only if not already provided):

1. **System overview**: "What does this service/API do? What problem does it solve?"
2. **API endpoints** (for APIs): "Walk me through the endpoints — what operations does it support? (e.g., CRUD, streaming, webhooks)"
3. **Data models**: "Describe the main data entities and their key fields. Any relationships between them?"
4. **Authentication/Authorization**: "How do clients authenticate? Are there different permission levels?"
5. **Error handling**: "What errors can occur? How should errors be communicated to consumers?"
6. **Versioning**: "How will this API be versioned? How will breaking changes be handled?"
7. **Performance requirements**: "Any latency, throughput, or SLA requirements?"
8. **Related context** (optional): "Existing specs, OpenAPI definitions, or service contracts I should reference?"

**If user seems uncertain about design choices**: Offer research assistance via `agent:web-research-specialist` for industry patterns (REST vs GraphQL, pagination approaches, etc.).

**Rich context** (accept at any point):
- OpenAPI/Swagger specs → use `Read` tool to load
- Existing service code → user should paste key interfaces
- Pasted schema definitions → incorporate directly

### Phase 2: Generate & Iterate

Once sufficient context is gathered, generate the **complete TSD draft** using the template from `assets/templates/template.md`.

**Content generation rules:**
- Use section headings from `template.md` exactly
- Format API endpoints consistently: `METHOD /path` with request/response examples
- Use code blocks for JSON schemas, request/response bodies
- Use tables for field definitions (field, type, required, description)
- Use italicized placeholders for missing info: *Define error codes*
- Do NOT include checkboxes, HTML comments, guidance questions, or quality criteria in output

**After presenting the full draft:**
1. Internally validate against `assets/templates/quality-checklist.md` — never show to user
2. Ask targeted follow-ups for gaps (e.g., "Should I add example requests and responses for each endpoint?")
3. Iterate based on feedback
4. Save in requested format

## Document Structure

Key sections (from `assets/templates/template.md`):

| Section | Purpose |
|---------|---------|
| Abstract | Executive summary |
| Overview | Purpose, scope, system context |
| API Endpoints/Methods | Detailed specs per endpoint |
| Data Models/Schemas | Entity definitions and relationships |
| Interface Contracts | Inputs, outputs, preconditions, postconditions |
| Error Handling | Error types, codes, formats, retry logic |
| Versioning Strategy | Version scheme and backward compatibility |
| Security Considerations | Auth, encryption, data protection |
| Performance Requirements | Latency, throughput, SLAs |
| Testing Requirements | Unit, integration, contract testing |
| Examples | Complete request/response examples |
| References | Related docs and standards |
| Change Log | Version history |

## Quality Principles

- Every endpoint needs: method, path, description, request schema, response schema, error codes
- Field definitions must include: name, type, required/optional, description, validation rules
- Use concrete examples — abstract specs are hard to implement against
- Document what happens on errors, not just the happy path
- Be explicit about backward compatibility guarantees

## Visual Aids

System context and data flow diagrams help consumers understand integration. When requested:
1. Ask what the diagram should show (system context, entity relationships, sequence flows)
2. Invoke `common-engineering:mermaid` skill
3. Integrate into Overview or relevant section

## Integration Points

| Capability | When to Use |
|-----------|-------------|
| `agent:web-research-specialist` | Research API design patterns, industry standards |
| `common-engineering:mermaid` | System context, ER diagrams, sequence diagrams |
| `document-skills:docx` | Export to Word format |
| `document-skills:pdf` | Export to PDF format |

## Reference Files

| File | Purpose |
|------|---------|
| `references/writing-guidelines.md` | Technical writing best practices |
| `references/question-bank.md` | AskUserQuestion patterns for this skill |
| `assets/templates/template.md` | Document structure (use for output) |
| `assets/templates/guidance.md` | Section-by-section guidance (read, never copy to output) |
| `assets/templates/quality-checklist.md` | Internal validation (never show to user) |
| `assets/templates/examples.md` | Completed examples for quality reference |
