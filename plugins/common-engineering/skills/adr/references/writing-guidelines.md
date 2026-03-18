# Technical Writing Guidelines

Best practices for creating effective technical documentation. These guidelines apply to all document types (One-Pager, RFC, TSD, ADR).

## Core Principles

### 1. Lead with the Problem
Always start by clearly articulating the problem before proposing solutions. Readers need to understand *why* before they care about *what*.

**Good**: "Our authentication system doesn't support SSO, causing enterprise customers to maintain separate credentials."
**Bad**: "We should implement OAuth 2.0 for our authentication system."

### 2. Know Your Audience
Adjust technical depth based on who will read the document:
- **Executives**: Focus on business impact, costs, timelines
- **Technical leads**: Balance business context with technical approach
- **Engineers**: Include implementation details, trade-offs, constraints

### 3. Be Concise but Complete
- Use bullet points for lists of 3+ items
- Keep paragraphs to 3-4 sentences max
- Remove filler words ("very", "really", "basically")
- Every sentence should add value

### 4. Use Concrete Examples
Abstract concepts are hard to evaluate. Ground your arguments in specifics:
- Quantify impact: "5 hours/week" not "significant time"
- Name specific systems: "PostgreSQL" not "our database"
- Reference real incidents: "The outage on Oct 15" not "recent issues"

## Structure Guidelines

### Document Metadata
Every document should start with:
- **Title**: Clear, descriptive (include document type prefix)
- **Status**: Draft, Under Review, Approved, Implemented
- **Author(s)**: Who wrote this
- **Date**: When created/last updated
- **Reviewers/Approvers**: Who needs to sign off

### Section Organization
Follow the template structure exactly. Readers expect consistent organization across documents.

**Do**:
- Use the exact section headings from the template
- Keep sections in the prescribed order
- Include all required sections (even if brief)

**Don't**:
- Invent new section names
- Reorder sections based on preference
- Skip required sections

### Linking and References
- Link to related documents, tickets, or external resources
- Use relative links for internal documents
- Include version numbers for external dependencies

## Writing Style

### Voice and Tone
- Use active voice: "We recommend X" not "X is recommended"
- Be direct: "This will fail" not "This might potentially have issues"
- Stay objective: Present facts, acknowledge uncertainties

### Technical Terminology
- Define acronyms on first use: "Single Sign-On (SSO)"
- Use consistent terminology throughout
- Avoid jargon when simpler terms work

### Formatting
- **Bold** for emphasis on key terms
- `code formatting` for technical names, commands, file paths
- Use tables for comparing options
- Use diagrams for architecture and flows (see mermaid skill)

## Section-Specific Guidance

### Problem Statement
- State the problem in 2-3 sentences max
- Identify who is affected
- Quantify impact where possible
- Explain current workaround (if any)

### Goals / Objectives
- Make goals specific and measurable
- Distinguish between must-have and nice-to-have
- Include success criteria

### Proposed Solution
- Lead with the recommendation
- Explain *why* this approach (not just *what*)
- Include high-level implementation approach
- Note key dependencies

### Alternatives Considered
- Include at least 2 alternatives
- Be honest about pros/cons (even for rejected options)
- Explain why the proposed solution is preferred
- "Do nothing" is a valid alternative to include

### Risks and Mitigations
- Be realistic, not alarmist
- Pair each risk with a mitigation strategy
- Include likelihood and impact assessment
- Don't hide uncomfortable truths

## Quality Checklist

Before submitting any document, verify:

### Completeness
- [ ] All required sections are filled out
- [ ] Metadata (authors, status, date) is current
- [ ] All reviewers are listed

### Clarity
- [ ] Problem is stated in first paragraph
- [ ] A non-expert could understand the summary
- [ ] Technical terms are defined
- [ ] No ambiguous pronouns ("it", "this", "that")

### Accuracy
- [ ] Numbers and dates are verified
- [ ] Links work and point to correct resources
- [ ] Technical details are accurate

### Persuasiveness
- [ ] Clear recommendation is made
- [ ] Trade-offs are acknowledged
- [ ] Risks are addressed with mitigations

## Common Mistakes to Avoid

1. **Solutioning before problem definition**: Don't propose solutions until the problem is crystal clear
2. **Missing alternatives**: Always show you considered other approaches
3. **Hidden assumptions**: State your assumptions explicitly
4. **Vague timelines**: "Soon" and "later" are not timelines
5. **Ignored risks**: Every approach has risks; acknowledge them
6. **Wall of text**: Use formatting to aid readability
7. **Missing context**: Don't assume readers know the backstory

## Visual Aids

Use diagrams when they clarify complex concepts:
- **Architecture diagrams**: System components and relationships
- **Sequence diagrams**: Request/response flows, process steps
- **Flowcharts**: Decision logic, workflows

Use the `common-engineering:mermaid` skill to create validated diagrams.

**When to use diagrams**:
- Explaining system architecture
- Showing data flow between components
- Illustrating process steps
- Comparing before/after states

**When NOT to use diagrams**:
- Simple concepts that text explains better
- When it would duplicate text content
- For aesthetic purposes only
