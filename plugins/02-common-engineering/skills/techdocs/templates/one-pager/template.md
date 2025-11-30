# One-Pager Template

One-pagers are concise proposal documents used to get sign-off before investing in a full technical design. They focus on the "what" and "why" rather than detailed implementation.

**When to use:**
- Proposing a new feature or capability
- Suggesting a process change
- Recommending a technology decision
- Requesting resources or budget approval
- Documenting a quick decision that needs stakeholder buy-in

**Best practices:**
- Keep it concise and scannable; save details for the TSD
- Lead with the problem to make readers understand why this matters
- Be honest about trade-offs and acknowledge weaknesses
- Use concrete examples rather than abstract concepts
- Think about your audience and adjust technical depth accordingly
- Include visuals - a good diagram can replace paragraphs of explanation

---

# Proposal: [Project name]

<!---
SECTION: About this doc
GUIDANCE QUESTIONS:
- What is this document proposing?
- Who are the key stakeholders that need to sign off?
- What's the deadline for getting approval?
- Who are the authors?
--->

## About this doc

*Metadata about this document. Describe the scope and current status.*

This doc is a proposal for [feature or change]. Upon approval, we will look to have this prioritized as a project and do a full Technical Design Document.

| Sign off deadline | *Date* |
|---|---|
| Status | *Draft* |
| Author(s) | *Name 1, Name 2* |

### Sign offs

- *Name 1*
- *Name 2*
- Add your name here to sign off

<!---
SECTION: Problem
GUIDANCE QUESTIONS:
- What specific problem are you trying to solve?
- Who is affected by this problem?
- What's the current state or workaround?
- Why is the current approach insufficient?
- Can you quantify the impact (time lost, errors, costs)?

QUALITY CRITERIA:
- ✅ Clearly articulates the pain point
- ✅ Explains who is affected
- ✅ Describes current state
- ✅ Justifies why change is needed
--->

## Problem

*What is the problem being solved? What are the pain points? What is the current solution and why is it not good enough?*

<!---
SECTION: High level goal
GUIDANCE QUESTIONS:
- What's the desired outcome?
- How will you measure success? (metrics if possible)
- What are the consequences of inaction?
- What opportunities will be missed?

QUALITY CRITERIA:
- ✅ States clear, measurable goal when possible
- ✅ Explains business value
- ✅ Articulates cost of inaction
--->

## High level goal

*Why should we do this? Answer this in metrics ideally but otherwise a sentence or two is okay.*

### What will happen if we don't solve this?

*Make it clear the downsides of what will happen if we don't invest the time into this.*

<!---
SECTION: Proposed solution
GUIDANCE QUESTIONS:
- What is your recommended approach?
- Why is this the best option?
- What are the key benefits?
- What's the high-level approach (without deep implementation details)?

QUALITY CRITERIA:
- ✅ Clear recommendation with rationale
- ✅ Explains key benefits
- ✅ Appropriate level of detail (not too deep)

VISUAL AIDS: Consider using `common-engineering:mermaid` for:
- Architecture diagram for system changes
- Flowchart for process changes
--->

### Proposed solution: [Option name]

*State the option you suggest and explain your reasoning. What benefits will we get from this approach? Time, money, risk, convenience, etc.*

<!---
SECTION: Alternatives
GUIDANCE QUESTIONS:
- What other approaches did you consider?
- Why were they not chosen?
- What are the trade-offs of each?

QUALITY CRITERIA:
- ✅ At least 2 alternatives considered
- ✅ Honest pros/cons for each
- ✅ Clear reasoning for why proposed solution is preferred
--->

### Alternatives

*A table or summary of the other options to achieve the goal. Also, consider adding this to an Appendix to keep the doc focused too.*

- Option 1: …
  - Pros: …
  - Cons: …
- Option 2: …
  - Pros: …
  - Cons: …
- …

<!---
SECTION: Risks
GUIDANCE QUESTIONS:
- What could go wrong?
- What are the technical risks?
- What are the business/organizational risks?
- How will you mitigate each risk?

QUALITY CRITERIA:
- ✅ Identifies realistic risks
- ✅ Includes mitigation strategies
- ✅ Shows thoughtful consideration of failure modes
--->

### Risks

*What can go wrong with the proposed approach? How are you mitigating that?*

- *Risk 1*
- *Risk 2*
- *…*

<!---
SECTION: Open Questions (Optional)
GUIDANCE QUESTIONS:
- What aspects are you uncertain about?
- Where do you need input from others?
- What dependencies need to be resolved?
--->

### Open Questions [optional]

*Anything still being figured out that you could use some additional eyes or thoughts on.*

---

<!---
QUALITY CHECKLIST - Before finalizing, verify:

Completeness:
- [ ] All required sections are filled out
- [ ] Metadata (authors, deadline, status) is complete
- [ ] Sign-off list includes all stakeholders

Clarity:
- [ ] Problem is clearly stated and justified
- [ ] Goal is specific and measurable
- [ ] Proposed solution is understandable without deep technical knowledge
- [ ] Alternatives show genuine consideration

Persuasiveness:
- [ ] Makes a compelling case for the proposal
- [ ] Addresses likely concerns proactively
- [ ] Risks are acknowledged with mitigations

Format:
- [ ] Follows template structure exactly
- [ ] Appropriate length (typically 1-3 pages)
- [ ] Diagrams enhance rather than clutter
--->
