---
name: adr
description: This skill should be used when the user asks to "write an ADR", "create an ADR", "document an architecture decision", "write an Architecture Decision Record", "document a technology choice", "compare database options", "document why we chose X over Y", or needs to record a specific architectural or technology decision with alternatives and trade-offs (1-3 pages). Use when capturing a decision that needs to be justified and preserved for future reference.
license: MIT
metadata:
  author: irfansofyana
  version: "2.0.0"
  last-updated: "2026-03-18"
allowed-tools: AskUserQuestion Bash Read
---

# ADR Skill

Create Architecture Decision Records (1-3 pages) that document specific technology choices, architectural decisions, or framework selections — capturing the decision, alternatives considered, evaluation criteria, and trade-offs for future reference.

**Key principle**: All information comes from the user. The `Read` tool is only for reading user-provided context files (existing ADRs, RFCs, tickets) that the user explicitly shares.

## When to Use an ADR

- Choosing between competing technologies (PostgreSQL vs MongoDB, Kafka vs RabbitMQ)
- Making a significant architectural pivot or framework decision
- Documenting a decision that will be hard to reverse
- Preserving the rationale behind a past decision for future team members
- Any "why did we choose X?" question that deserves a permanent answer

## Workflow

### Phase 1: Gather Context

Parse what the user already provided. Extract:
- **The decision**: What was decided or needs to be decided?
- **Context**: What situation forced this decision?
- **Alternatives**: What options were in consideration?

**Only ask for what's genuinely missing.**

**Essential questions** (use `references/question-bank.md` patterns, ask only if not already provided):

1. **Decision**: "What is the specific decision being made or documented?"
2. **Context/drivers**: "What situation or requirements led to this decision? What constraints apply?"
3. **Alternatives** (MANDATORY minimum 2): "What other options did you consider? Walk me through each one."
4. **Decision criteria**: "How did you evaluate the options? What mattered most — performance, cost, team familiarity, vendor support?"
5. **Trade-offs**: "What are you gaining with this choice? What are you giving up?"
6. **Consequences**: "What changes because of this decision? Any downstream implications?"
7. **Reconsideration triggers** (optional): "Under what circumstances should this decision be revisited?"
8. **Related context** (optional): "Any previous ADRs or RFCs this relates to?"

**If user is still deciding** (not yet made the decision): Offer research via `agent:web-research-specialist` to gather comparison data before writing.

**Rich context** (accept at any point):
- Existing ADRs → use `Read` tool to load for consistency
- Benchmark data or vendor docs → incorporate key findings
- Pasted comparisons → extract decision criteria

### Phase 2: Generate & Iterate

Once sufficient context is gathered, generate the **complete ADR draft** using the template from `assets/templates/template.md`.

**Content generation rules:**
- Use section headings from `template.md` exactly
- The **Alternatives Considered** section requires at least 2 alternatives — never skip this
- Use a comparison table for decision criteria evaluation
- Write trade-offs honestly — acknowledge weaknesses of the chosen option
- State the decision in clear, unambiguous language ("We will use PostgreSQL for all transactional data storage")
- Do NOT include checkboxes, HTML comments, guidance questions, or quality criteria in output

**After presenting the full draft:**
1. Internally validate against `assets/templates/quality-checklist.md` — never show to user
2. Check that alternatives section has sufficient depth and honest trade-offs
3. Iterate based on feedback
4. Save in requested format

## Document Structure

Key sections (from `assets/templates/template.md`):

| Section | Purpose |
|---------|---------|
| Title & Metadata | Decision ID, date, status, authors |
| Context | Current situation, drivers, goals, non-goals |
| Decision | Clear statement of what was decided |
| Alternatives Considered | **MANDATORY** 2+ alternatives with pros/cons |
| Decision Criteria | Evaluation table or criteria breakdown |
| Trade-offs Analysis | What we gain, what we give up |
| Consequences | Positive, negative, and risk consequences |
| Implementation Plan | How the decision is being carried out |
| Validation | POC results, benchmarks, evidence |
| Related Decisions | Links to other ADRs |
| Reconsideration | Triggers and expiration conditions |
| References | External docs, benchmarks, comparisons |
| Approval | Sign-off section |

## Quality Principles

- **Alternatives are mandatory** — an ADR with only one option considered is not credible
- The decision statement must be unambiguous — future readers should have no doubt what was decided
- Trade-offs must be honest — acknowledge real weaknesses of the chosen approach
- Include the decision criteria explicitly — future readers need to understand what values drove the choice
- "Do nothing" / "status quo" is always a valid alternative to include

## Visual Aids

Comparison diagrams or architecture context diagrams can strengthen ADRs. When requested:
1. Ask what the diagram should show
2. Invoke `common-engineering:mermaid` skill
3. Integrate into relevant section

## Integration Points

| Capability | When to Use |
|-----------|-------------|
| `agent:web-research-specialist` | Compare technologies, gather benchmark data, research options |
| `common-engineering:mermaid` | Architecture context or comparison diagrams |
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
