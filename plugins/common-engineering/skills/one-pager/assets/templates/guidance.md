# One-Pager Section Guidance

This file provides detailed guidance for each section of a one-pager document. Use this when helping users write their one-pager proposals.

## Document Overview

A one-pager is a concise proposal document (1-3 pages) used to get stakeholder sign-off before investing in detailed technical design. It focuses on the **what** and **why**, not detailed implementation.

**When to use a One-Pager:**
- Proposing a new feature or capability
- Suggesting a process change
- Recommending a technology decision
- Requesting resources or budget
- Quick decisions needing stakeholder buy-in

## Quick Reference: Essential Questions by Section

For quick access during document creation:

- **About This Doc**: When do you need approval by? Who wrote this? What's the current status?
- **Sign Offs**: Who has authority to approve this? Are there cross-functional stakeholders?
- **Problem**: What's broken? Who's affected? What's the current workaround? What's the cost?
- **High Level Goal**: What does done look like? How will you measure success? What business metric will improve?
- **What Happens If We Don't Solve This**: What's the cost of maintaining status quo? What opportunities will we miss?
- **Proposed Solution**: What do you recommend? Why this approach over alternatives? What are the key benefits?
- **Alternatives**: What other approaches did you consider? What are the trade-offs? Why is the proposed solution better?
- **Risks**: What could go wrong? What are the technical/business risks? How will you mitigate each risk?
- **Open Questions** (optional): What aspects are you uncertain about? Where do you need input from others?

---

## Context Gathered → Section Mapping

Use this to map context gathered during Phase 1 (Gather Context) to the appropriate one-pager sections:

| Context Gathered | Used In Section | How It's Used |
|-----------------|-----------------|---------------|
| Current state description | Problem | Core content - "What's broken now" |
| Evidence of problem | Problem | "How do we know" - quantifies impact |
| Who is affected | Problem | "Who experiences this" |
| Desired state | High Level Goal | "What does done look like" |
| Cost of inaction | What Happens If We Don't Solve This | Urgency framing |
| Related documents | Throughout | Cite for context, previous attempts |
| Historical context | Alternatives | Previous attempts inform options |
| Technical context | Proposed Solution | System landscape, constraints |
| Team context | Risks | Team capacity, expertise risks |

### Key Benefits of Universal Discovery for One-Pagers

**Better Problem Clarity:**
- Problem Validation Gate ensures the problem is real and quantified
- No more superficial problem statements ("performance is slow" → "API p95 latency increased from 100ms to 2800ms")

**Better Goal Definition:**
- Desired State from Universal Discovery directly informs High Level Goal
- Gap analysis provides measurable success criteria

**Better Solution Fit:**
- Rich Context Input (related docs, historical context) ensures solution builds on previous work
- Technical Context ensures solution fits system landscape

**Better Risk Assessment:**
- Team Context helps identify realistic team capacity and expertise risks
- Historical Context helps avoid repeating past mistakes

### How to Use Universal Discovery Output

**When writing the Problem section:**
1. Start with **Current State Deep Dive** output: "What happens now step by step?"
2. Add **Evidence of Problem**: Quantify the impact (metrics, complaints, errors)
3. Include **Who Has This Problem**: Specify affected users or teams
4. Use **State Gap**: Show the difference between current and desired states

**When writing the High Level Goal section:**
1. Use **Desired State** output: "What should happen after we fix this?"
2. Derive success metrics from **State Gap**: "What's the measurable improvement?"

**When writing "What Happens If We Don't Solve This":**
1. Use **Impact Urgency** output: "What's the cost of NOT fixing this?"
2. Quantify if possible (revenue, time, frustration, technical debt)

**When writing Proposed Solution:**
1. Reference **Technical Context**: System landscape, constraints, dependencies
2. Reference **Related Documents**: Previous attempts, existing RFCs/ADRs

**When writing Alternatives:**
1. Reference **Historical Context**: What was tried before? Why did it fail?
2. Reference **Related Documents**: Previous decisions that inform current options

**When writing Risks:**
1. Use **Team Context**: Team capacity, expertise gaps
2. Use **Technical Context**: Integration complexity, dependencies

---

## Section-by-Section Guidance

### About This Doc

**Purpose**: Provide metadata and context for the document.

**Required elements**:
- Sign-off deadline
- Status (Draft, Under Review, Approved)
- Author(s)

**Questions to ask**:
- When do you need approval by?
- Who wrote or contributed to this?

**Example**:
```
This doc is a proposal for migrating our authentication service to OAuth 2.0.
Upon approval, we will prioritize this as a project and create a full TSD.

| Sign off deadline | December 15, 2024 |
|---|---|
| Status | Draft |
| Author(s) | Jane Smith, John Doe |
```

---

### Sign Offs

**Purpose**: List all stakeholders who need to approve before proceeding.

**Questions to ask**:
- Who has authority to approve this?
- Are there cross-functional stakeholders?
- Does this need executive approval?

**Tips**:
- Include role/title, not just names
- Consider: direct manager, tech lead, affected team leads, product owner
- Keep the list focused (3-6 people typically)

**Example**:
```
- Sarah Chen (Engineering Manager) - ✅ Approved
- Mike Johnson (Platform Tech Lead) - Pending
- Lisa Park (Product Manager) - Pending
```

---

### Problem

**Purpose**: Clearly articulate the pain point that motivates this proposal.

**This section must answer**:
1. What specific problem exists?
2. Who is affected?
3. What's the current state or workaround?
4. Why is the current approach insufficient?
5. Can you quantify the impact?

**Questions to ask**:
- What exactly is broken or missing?
- Who experiences this problem?
- How are people dealing with it today?
- What's the cost of the current situation?

**Quality criteria**:
- ✅ Problem is specific, not vague
- ✅ Impact is quantified where possible
- ✅ Current state is described
- ✅ Reader understands why change is needed

**Good example**:
```
Our current authentication system uses a custom token-based approach that doesn't 
support Single Sign-On (SSO). This causes significant friction for enterprise 
customers who must maintain separate credentials for our platform.

**Impact**:
- 40% of enterprise prospects cite "no SSO" as a blocker in sales conversations
- Support handles ~15 password reset tickets/week from enterprise users
- Engineering spends 5 hours/week maintaining custom auth code
```

**Bad example**:
```
Authentication needs to be improved because it's outdated.
```

---

### High Level Goal

**Purpose**: State what success looks like and why it matters.

**This section must answer**:
1. What is the desired outcome?
2. How will you measure success?
3. What value does this create?

**Questions to ask**:
- What does "done" look like?
- How will you know if this succeeded?
- What business metric will improve?

**Quality criteria**:
- ✅ Goal is specific and measurable
- ✅ Connected to business value
- ✅ Timeframe is clear (if applicable)

**Good example**:
```
Enable SSO authentication for enterprise customers, reducing credential 
friction and improving enterprise conversion.

**Success metrics**:
- 100% of enterprise customers can use SSO within 30 days of contract signing
- Reduce auth-related support tickets by 80%
- Remove SSO as a sales blocker (0 mentions in lost deal analysis)
```

---

### What Happens If We Don't Solve This

**Purpose**: Make the cost of inaction crystal clear.

**This section should cover**:
- Ongoing costs that continue if we do nothing
- Opportunities missed
- Risks that grow over time
- Competitive disadvantage

**Questions to ask**:
- What's the cost of maintaining status quo for another year?
- What opportunities will we miss?
- How does this affect our competitive position?

**Tips**:
- Be specific about consequences
- Use timeline projections where helpful
- Connect to business goals

**Example**:
```
Without SSO support:
- We'll continue losing ~$2M ARR annually in enterprise deals blocked by SSO requirements
- Enterprise customer satisfaction will remain below target (currently 3.2/5 vs target 4.0)
- Auth code maintenance will consume 260 engineering hours/year
- We risk falling further behind competitors (Acme Corp launched SSO 6 months ago)
```

---

### Proposed Solution

**Purpose**: State your recommendation and explain why it's the best approach.

**This section must answer**:
1. What do you recommend?
2. Why this approach over alternatives?
3. What are the key benefits?
4. High-level implementation approach (not detailed design)

**Questions to ask**:
- What's your recommended approach?
- Why is this better than the alternatives?
- What dependencies or prerequisites exist?

**Quality criteria**:
- ✅ Clear recommendation stated upfront
- ✅ Rationale explains why this option
- ✅ Key benefits articulated
- ✅ Appropriate level of detail (not too deep)

**Tips**:
- Lead with the recommendation
- Keep implementation details high-level (save details for TSD)
- Focus on *why* this approach, not just *what*

**Example**:
```
### Proposed solution: Implement OAuth 2.0 with OIDC

We recommend implementing OAuth 2.0 with OpenID Connect using Auth0 as our 
identity provider.

**Why Auth0**:
- Industry-standard protocols (OAuth 2.0, OIDC, SAML)
- Native support for enterprise SSO providers (Okta, Azure AD, Google Workspace)
- Handles compliance requirements (SOC 2, GDPR)
- Reduces engineering maintenance burden

**High-level approach**:
1. Integrate Auth0 SDK into authentication flow
2. Migrate existing users with zero-downtime cutover
3. Enable enterprise SSO connections per customer
```

**Consider adding a diagram** for complex solutions (use `common-engineering:mermaid`).

---

### Alternatives

**Purpose**: Show that other approaches were considered and explain trade-offs.

**Must include**:
- At least 2 alternatives considered
- Honest pros/cons for each
- Clear reasoning for why proposed solution is preferred

**Questions to ask**:
- What other approaches did you consider?
- What are the trade-offs of each?
- Why is the proposed solution better?

**Good alternatives to consider**:
- "Do nothing" (status quo)
- Build vs. buy options
- Different technology choices
- Phased vs. big-bang approaches

**Format**:
```
#### Alternative 1: Build custom OAuth implementation

**Pros**:
- Full control over implementation
- No vendor dependency
- No ongoing licensing costs

**Cons**:
- 6+ months of engineering effort
- Ongoing maintenance burden
- Risk of security vulnerabilities
- No enterprise SSO out of the box

**Why not chosen**: The engineering effort and security risk outweigh the benefits 
of avoiding vendor dependency.
```

---

### Risks

**Purpose**: Identify what could go wrong and how you'll address it.

**This section must answer**:
1. What are the realistic risks?
2. What's the likelihood and impact of each?
3. How will you mitigate each risk?

**Common risk categories**:
- Technical complexity
- Timeline/schedule
- Integration challenges
- Team capacity/expertise
- Cost overruns
- User adoption
- Security
- Vendor dependency

**Questions to ask**:
- What could go wrong?
- What are you most worried about?
- How will you mitigate each risk?

**Format**:
```
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Auth0 pricing increases | Medium | Medium | Negotiate multi-year contract; design for provider portability |
| Migration causes user disruption | Low | High | Zero-downtime migration plan; extensive testing; rollback capability |
| Integration complexity with legacy systems | Medium | Medium | POC with hardest integration first; allocate buffer time |
```

---

### Open Questions (Optional)

**Purpose**: Flag areas of uncertainty that need more input or investigation.

**When to include**:
- Technical decisions still being evaluated
- Dependencies on other teams
- Information you need from stakeholders
- Areas where you want reviewer input

**Format**:
```
1. Should we support SAML in addition to OIDC? (Need input from enterprise sales)
2. What's the timeline for deprecating the legacy auth system?
3. Do we need to maintain backward compatibility for mobile app v2.x?
```

---

## Quality Validation

⚠️ **For internal validation only**: Quality criteria and checklists are used internally to validate document quality. They should NEVER appear in the user-facing document.

**See**: [quality-checklist.md](quality-checklist.md) for the complete validation checklist to use during Phase 5 (Review & Output).

**Important**: The quality checklist is for AI validation only. Do not include checkboxes or quality criteria in the document you present to users.
