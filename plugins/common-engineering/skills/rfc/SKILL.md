---
name: rfc
description: This skill should be used when the user asks to "write an RFC", "create an RFC", "draft an RFC", "write a Request for Comments", "write a design proposal for cross-team review", "document a complex architecture change", or needs a detailed design document covering architecture, implementation phases, migration, and rollback planning (5-15 pages). Use for complex multi-service changes requiring thorough cross-team review.
license: MIT
metadata:
  author: irfansofyana
  version: "2.0.0"
  last-updated: "2026-03-18"
allowed-tools: AskUserQuestion Bash Read
---

# RFC Skill

Create detailed Request for Comments documents (5-15 pages) for complex architecture changes that require cross-team review, thorough design analysis, implementation planning, and rollback strategies.

**Key principle**: All information comes from the user. Do NOT scan the codebase to discover the problem. The `Read` tool is only for reading user-provided context files (existing ADRs, TSDs, tickets) that the user explicitly shares.

## When to Use an RFC

- Complex architecture changes spanning multiple services
- Changes requiring cross-team coordination and review
- Significant migrations with rollback requirements
- Proposals where implementation phases and sequencing matter
- Anything where a one-pager is too shallow but a TSD is too API-focused

## Workflow

### Phase 1: Gather Context

Parse what the user already provided in their initial request. Extract:
- **Problem**: What's the current pain point?
- **Proposed design**: High-level architecture approach
- **Scope**: Services and teams affected
- **Constraints**: Timeline, compatibility, budget

**Only ask for what's genuinely missing.** If the user described the migration in their request, capture it and move forward.

**Essential questions** (use `references/question-bank.md` patterns, ask only if not already provided):

1. **Current state**: "Walk me through the current architecture/process step by step."
2. **Evidence**: "How do we know this needs to change? What's the evidence?"
3. **Proposed design**: "Describe the target architecture at a high level — what changes?"
4. **Affected services/teams**: "Which services and teams are involved?"
5. **Implementation approach**: "Do you have a phased rollout in mind? Any ordering constraints?"
6. **Migration strategy**: "How do you move from current to target state? Any data migration?"
7. **Rollback plan**: "If this goes wrong after deployment, how do you revert?" (MANDATORY for RFCs)
8. **Alternatives**: "What other approaches did you consider? Why is this preferred?"
9. **Risk areas**: "What are the biggest technical and operational risks?"
10. **Related context** (optional): "Existing ADRs, TSDs, or tickets I should know about?"

**If user seems uncertain**: Offer research assistance via `agent:web-research-specialist`.

**Rich context** (accept at any point):
- File paths → use `Read` tool to load
- Architecture diagrams or descriptions → incorporate
- Pasted content → capture key points

### Phase 2: Generate & Iterate

Once sufficient context is gathered, generate the **complete RFC draft** using the template from `assets/templates/template.md`.

**Content generation rules:**
- Use section headings from `template.md` exactly
- Fill sections with user-provided content
- Use italicized placeholders for missing info: *Describe the migration strategy*
- Do NOT include checkboxes, HTML comments, guidance questions, or quality criteria in output
- The **Rollback Plan** section is MANDATORY — always include it, even if brief

**After presenting the full draft:**
1. Internally validate against `assets/templates/quality-checklist.md` — never show to user
2. Ask targeted follow-ups for gaps (e.g., "The rollback section could use more detail — what's the revert procedure?")
3. Offer diagram generation if architecture is complex
4. Iterate based on feedback
5. Save in requested format

## Document Structure

Key sections (from `assets/templates/template.md`):

| Section | Purpose |
|---------|---------|
| Abstract | Executive summary of the RFC |
| Motivation | Current state, desired state, problem statement |
| Proposed Design | Architecture overview, components, data flow |
| Implementation Plan | Phases, ownership, timeline |
| Migration Strategy | How to transition from current to target state |
| Rollback Plan | **MANDATORY** — how to revert if things go wrong |
| Testing Strategy | Including rollback testing |
| Performance Considerations | Benchmarks, SLAs, load expectations |
| Security Considerations | Auth, data protection, compliance |
| Alternatives Considered | Other approaches and why rejected |
| Risks and Mitigations | Technical and operational risks |
| Open Questions | Unresolved design decisions |
| Success Metrics | How to know the RFC succeeded |
| References | Related docs and external resources |
| Approval | Sign-off section |

## Quality Principles

- **Rollback Plan is non-negotiable** — every RFC must have one
- Require at least 2 alternatives with honest trade-off analysis
- Implementation phases should have clear ownership and sequencing
- Performance and security sections should have concrete numbers, not vague statements
- State your assumptions explicitly

## Visual Aids

Diagrams are highly valuable for RFCs. If the user requests them or if the architecture is complex:
1. Ask what the diagram should show (architecture, data flow, sequence)
2. Invoke `common-engineering:mermaid` skill
3. Integrate into the Proposed Design section

## Integration Points

| Capability | When to Use |
|-----------|-------------|
| `agent:web-research-specialist` | Research industry patterns, technology options |
| `common-engineering:mermaid` | Architecture and sequence diagrams |
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
