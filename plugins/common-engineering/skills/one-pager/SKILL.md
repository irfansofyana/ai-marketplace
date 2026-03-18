---
name: one-pager
description: This skill should be used when the user asks to "write a one-pager", "create a one-pager proposal", "draft a one-pager", "write a proposal doc", "create a feature proposal", "write a proposal for sign-off", or needs a concise stakeholder approval document (1-3 pages). Produces focused proposal documents with problem statement, goal, proposed solution, alternatives, and risks.
license: MIT
metadata:
  author: irfansofyana
  version: "2.0.0"
  last-updated: "2026-03-18"
allowed-tools: AskUserQuestion Bash Read
---

# One-Pager Skill

Create concise proposal documents (1-3 pages) for getting stakeholder sign-off before investing in detailed technical design. One-pagers focus on the **what** and **why** — not implementation details.

**Key principle**: All information comes from the user. Do NOT scan the codebase to discover the problem. The `Read` tool is only for reading user-provided context files (existing docs, ADRs, RFCs) that the user explicitly shares.

## When to Use a One-Pager

- Proposing a new feature or capability
- Suggesting a process or workflow change
- Recommending a technology decision
- Requesting resources or budget approval
- Any decision needing stakeholder buy-in that doesn't require full TSD/RFC depth

## Workflow

### Phase 1: Gather Context

Parse what the user already provided in their initial request. Extract:
- **Problem**: What's broken or missing?
- **Proposed solution**: What do they want to do?
- **Stakeholders**: Who needs to approve?
- **Context**: Technologies, constraints, related work

**Only ask for what's genuinely missing.** If the user said "write a one-pager for adding SSO to our internal tools", the problem and solution are already known — don't ask them to re-explain.

**Essential questions** (use `references/question-bank.md` patterns, ask only if not already provided):

1. **Problem & current state**: "Walk me through what's happening now and what's broken."
2. **Evidence**: "How do we know this is a problem? Any metrics, complaints, or incidents?"
3. **Desired outcome**: "What does success look like after this is solved?"
4. **Sign-offs needed**: "Who needs to approve this? Any cross-functional stakeholders?"
5. **Risks** (optional): "What could go wrong? Any technical or business risks?"
6. **Related context** (optional): "Any existing docs, tickets, or previous attempts I should know about?"

**If user seems uncertain or exploratory**: Offer research assistance via `agent:web-research-specialist` before drafting.

**Rich context** (accept at any point):
- File paths → use `Read` tool to load
- Pasted content → incorporate directly
- Verbal description → capture key points

### Phase 2: Generate & Iterate

Once sufficient context is gathered, generate the **complete one-pager draft** using the template structure from `assets/templates/template.md`.

**Content generation rules:**
- Use section headings from `template.md` exactly
- Fill sections with user-provided content
- Use italicized placeholders for missing info: *Describe the problem*
- Do NOT include checkboxes, HTML comments, guidance questions, or quality criteria in output
- Tables and lists are encouraged for readability

**After presenting the full draft:**
1. Internally validate against `assets/templates/quality-checklist.md` — never show this to the user
2. Identify any gaps and ask targeted follow-up questions (e.g., "Would you like to add success metrics to the Goal section?")
3. Iterate based on user feedback
4. Save in requested format (`document-skills:docx`, `document-skills:pdf`, or markdown)

## Document Structure

Sections (from `assets/templates/template.md`):

| Section | Purpose |
|---------|---------|
| About this doc | Metadata: deadline, status, authors |
| Sign offs | List of approvers |
| Problem | Current state, evidence, who's affected |
| High level goal | Desired outcome and success metrics |
| What happens if we don't solve this | Cost of inaction |
| Proposed solution | Recommended approach and rationale |
| Alternatives | Other options considered and why rejected |
| Risks | Technical and business risks with mitigations |
| Open questions | (Optional) Unresolved uncertainties |

## Quality Principles

- Lead with the problem — readers need to understand **why** before they care about **what**
- Quantify impact wherever possible ("50 errors/day", "2-hour weekly manual effort")
- Be honest about trade-offs and weaknesses
- Keep it scannable: bullet points, short paragraphs
- Include at least 1 alternative with clear trade-off reasoning

## Visual Aids

Only generate diagrams if the user explicitly requests them. When requested:
1. Ask what the diagram should show
2. Invoke `common-engineering:mermaid` skill
3. Integrate into document

## Integration Points

| Capability | When to Use |
|-----------|-------------|
| `agent:web-research-specialist` | User needs research on industry context, best practices |
| `common-engineering:mermaid` | User explicitly requests diagrams |
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
