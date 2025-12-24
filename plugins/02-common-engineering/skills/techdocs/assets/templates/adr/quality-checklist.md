# ADR Quality Checklist

> **Purpose**: Internal validation checklist for ADRs. Use this to self-review before submitting for review, and during peer review to provide structured feedback.

---

## Checklist Overview

This checklist is organized by ADR sections. Each section has:
- **Required elements** - Must-haves for this section
- **Quality indicators** - Signs of high-quality content
- **Common issues** - Problems to watch for

---

## 1. Title and Metadata

### Required Elements
- [ ] Title is specific and clear
- [ ] Status is accurate (Proposed, Accepted, Deprecated, Superseded)
- [ ] Decision type is identified
- [ ] Deciders are listed
- [ ] Related ADRs are linked (if any)

### Quality Indicators
- Title clearly states the decision
- Status reflects current state
- Decision type is appropriate

### Common Issues
- ❌ Vague title ("Database Decision" vs "Choose PostgreSQL as Primary Database")
- ❌ Missing status
- ❌ No decision type specified
- ❌ No deciders listed

---

## 2. Context

### 2.1 Current Situation

#### Required Elements
- [ ] Current state is described
- [ ] Problem being solved is specified
- [ ] Constraints are identified

#### Quality Indicators
- Current situation is clear
- Problem is specific
- Constraints are realistic

#### Common Issues
- ❌ No current state described
- ❌ Problem is vague ("we need a better X")
- ❌ No constraints identified

### 2.2 Drivers

#### Required Elements
- [ ] Drivers are specified
- [ ] Evidence is provided (from Universal Discovery)
- [ ] Drivers are prioritized

#### Quality Indicators
- Drivers are specific and measurable
- Evidence supports each driver
- Most important drivers first

#### Common Issues
- ❌ No evidence provided
- ❌ Drivers are vague ("performance")
- ❌ Too many drivers (focus on 3-5 key ones)

### 2.3 Goals and Non-Goals

#### Required Elements
- [ ] Goals are specified
- [ ] Non-goals are explicitly defined

#### Quality Indicators
- Goals are specific and measurable
- Non-goals exclude out-of-scope items
- Goals align with drivers

#### Common Issues
- ❌ No non-goals defined
- ❌ Goals are vague ("better performance")
- ❌ Goals don't align with drivers

---

## 3. Decision

### Required Elements
- [ ] Decision is clearly stated
- [ ] Key attributes are specified

### Quality Indicators
- Decision is unambiguous
- Key attributes are clear

### Common Issues
- ❌ Decision is vague ("we chose the best option")
- ❌ No key attributes specified

---

## 4. Alternatives Considered

> **CRITICAL**: At least 2 alternatives must be documented. This is non-negotiable.

### Required Elements
- [ ] At least 2 alternatives documented ← NON-NEGOTIABLE
- [ ] Each alternative has:
  - [ ] Description
  - [ ] Pros (at least 2)
  - [ ] Cons (at least 2)
  - [ ] Estimated impact (cost, effort, risk)

### Quality Indicators
- Alternatives are realistic (not strawmen)
- Pros and cons are balanced
- Estimated impact is provided

### Common Issues
- ❌ **CRITICAL**: Fewer than 2 alternatives documented
- ❌ Strawman alternatives (obviously bad options)
- ❌ Pros only or cons only (need both)
- ❌ No estimated impact

---

## 5. Decision Criteria

### Required Elements
- [ ] Criteria are specified
- [ ] Weights are assigned (High/Med/Low)
- [ ] Alternatives are compared on each criterion
- [ ] Criteria definitions are provided

### Quality Indicators
- Criteria align with drivers and goals
- Weights reflect priorities
- Comparison is clear

### Common Issues
- ❌ No weights assigned
- ❌ Criteria don't align with drivers/goals
- ❌ No comparison of alternatives

---

## 6. Trade-offs Analysis

### Required Elements
- [ ] Trade-offs are documented
- [ ] Impact of each trade-off is specified

### Quality Indicators
- Multiple trade-off dimensions are analyzed
- Impacts are specific

### Common Issues
- ❌ No trade-offs documented (decision presented as perfect)
- ❌ Trade-offs are vague
- ❌ Only positive trade-offs shown

---

## 7. Consequences

### 7.1 Positive Consequences

#### Required Elements
- [ ] Benefits are documented
- [ ] Who benefits is specified

#### Quality Indicators
- Benefits are specific
- Multiple stakeholders considered

#### Common Issues
- ❌ Benefits are vague
- ❌ No stakeholder identification

### 7.2 Negative Consequences

#### Required Elements
- [ ] Drawbacks are documented
- [ ] Who is affected is specified

#### Quality Indicators
- Drawbacks are specific
- Honest assessment of downsides

#### Common Issues
- ❌ No negative consequences (every decision has downsides)
- ❌ Drawbacks are minimized

### 7.3 Risks

#### Required Elements
- [ ] Risks introduced are identified
- [ ] Each risk has likelihood, impact, mitigation
- [ ] Risks eliminated are documented

#### Quality Indicators
- Risks are realistic
- Mitigation plans are actionable

#### Common Issues
- ❌ No risks identified
- ❌ No mitigation plans
- ❌ No risks eliminated documented

---

## 8. Implementation Plan

### Required Elements
- [ ] Implementation is broken into phases
- [ ] Each phase has:
  - [ ] Goals
  - [ ] Tasks
  - [ ] Owner
  - [ ] Timeline
- [ ] Rollout strategy is specified
- [ ] Success criteria are defined

### Quality Indicators
- Phases are logically ordered
- Timeline is realistic
- Success criteria are specific

### Common Issues
- ❌ No implementation plan ("we'll just do it")
- ❌ No phases (just a list of tasks)
- ❌ No success criteria
- ❌ Unrealistic timeline

---

## 9. Validation

### Required Elements
- [ ] Validation approach is documented
- [ ] Results are summarized (if done)
- [ ] References are provided

### Quality Indicators
- Validation is appropriate for decision type
- Results support the decision

### Common Issues
- ❌ No validation (decision based on gut feeling)
- ❌ No references

---

## 10. Related Decisions

### Required Elements
- [ ] Related ADRs are linked
- [ ] Relationships are explained
- [ ] Superseded ADRs are identified (if any)

### Quality Indicators
- Links are accurate
- Relationships are clear

#### Common Issues
- ❌ No related ADRs linked
- ❌ No explanation of relationships

---

## 11. Reconsideration

### Required Elements
- [ ] Triggers for reconsideration are specified
- [ ] Review date is specified
- [ ] Rationale for triggers is provided

### Quality Indicators
- Triggers are specific and measurable
- Review date is reasonable

#### Common Issues
- ❌ No reconsideration triggers
- ❌ Vague triggers ("if it doesn't work")
- ❌ No review date

---

## 12. References

### Required Elements
- [ ] Related documents are linked
- [ ] External references are relevant
- [ ] Links are accurate

### Quality Indicators
- Related documents are relevant
- External sources are credible

#### Common Issues
- ❌ No references
- ❌ Broken links

---

## 13. Approval

### Required Elements
- [ ] Required roles are listed
- [ ] Approval status is tracked
- [ ] Dates are recorded

### Quality Indicators
- Approval roles are appropriate
- No approvals are missing

#### Common Issues
- ❌ No approval section
- ❌ Missing approvals

---

## Universal Discovery Integration Check

> **CRITICAL**: ADRs must integrate Universal Discovery output from Phase 1.

### Required Integration Points
- [ ] **Context → Current Situation**: Uses Universal Discovery "Current State"
- [ ] **Context → Drivers**: Uses Universal Discovery "Evidence of Problem"
- [ ] **Context → Goals**: Uses Universal Discovery "Desired State"
- [ ] **Alternatives**: Uses Universal Discovery "Technical Context" for constraints
- [ ] **References**: Links to Universal Discovery "Related Documents"

### Quality Indicators
- Current situation matches Universal Discovery
- Evidence from Universal Discovery is used
- Related documents are referenced

### Common Issues
- ❌ Context doesn't use Universal Discovery output
- ❌ No evidence provided (decision not validated)
- ❌ Related documents not referenced

---

## Critical Go/No-Go Criteria

An ADR is **READY FOR REVIEW** when:

- ✅ All required sections are complete
- ✅ At least 2 alternatives are documented ← NON-NEGOTIABLE
- ✅ Decision criteria are specified
- ✅ Trade-offs are documented
- ✅ Consequences (positive and negative) are documented
- ✅ Implementation plan is specified
- ✅ Reconsideration triggers are defined
- ✅ Universal Discovery output is integrated

An ADR is **NOT READY** if any of these are true:

- ❌ Fewer than 2 alternatives documented ← CRITICAL ISSUE
- ❌ No trade-offs documented
- ❌ No negative consequences
- ❌ No implementation plan
- ❌ No reconsideration triggers
- ❌ Context doesn't use Universal Discovery output

---

## Reviewer Guidelines

### When Reviewing an ADR

1. **Check Universal Discovery integration first**: Is the problem validated? Is evidence provided?
2. **Count alternatives**: Are there at least 2? Are they real options or strawmen?
3. **Verify trade-offs**: Are both pros and cons documented for each alternative?
4. **Check decision criteria**: Are criteria defined? Do they align with drivers?
5. **Verify consequences**: Are both positive and negative consequences documented?
6. **Check implementation plan**: Is it specific? Are success criteria defined?
7. **Check reconsideration**: Are triggers specific? Is there a review date?

### Providing Feedback

- **Be specific**: Instead of "alternatives are weak", say "MongoDB alternative should mention lack of ACID compliance as a con"
- **Reference sections**: Cite the section number
- **Explain why**: Explain the reasoning behind feedback
- **Suggest improvements**: Offer concrete suggestions

---

## Common Review Comments

Here are common review comments organized by section:

### Title and Metadata
- "Title is vague - be specific about the decision"
- "Missing status - is this Proposed, Accepted, Deprecated, or Superseded?"
- "No decision type specified - what type of decision is this?"

### Context
- "No current state - describe what's happening now"
- "Problem is vague - be specific about what problem we're solving"
- "No constraints identified - what are the technical, time, budget constraints?"
- "Drivers lack evidence - add metrics or specific examples"
- "No non-goals defined - what are we explicitly NOT trying to achieve?"

### Decision
- "Decision is vague - clearly state what was chosen"

### Alternatives Considered
- **"CRITICAL": Fewer than 2 alternatives - add at least one more alternative**
- "Strawman alternatives - make alternatives more realistic"
- "Pros only or cons only - need both for each alternative"
- "No estimated impact - add cost, effort, risk for each alternative"

### Decision Criteria
- "No criteria defined - specify how alternatives were evaluated"
- "No weights assigned - specify which criteria are High/Med/Low priority"
- "No comparison - compare alternatives on each criterion"

### Trade-offs
- "No trade-offs documented - every decision has trade-offs"
- "Trade-offs are vague - be specific about what's being traded off"

### Consequences
- "No negative consequences - every decision has downsides"
- "No risks identified - what could go wrong?"
- "No mitigation plans - how will we address the risks?"

### Implementation Plan
- "No implementation plan - how will this be implemented?"
- "No phases - break down implementation into phases"
- "No success criteria - how do we know if implementation succeeded?"

### Validation
- "No validation - was this decision validated? Add proof of concept or benchmarks"

### Reconsideration
- "No reconsideration triggers - specify when to revisit this decision"
- "Triggers are vague - be specific and measurable"
- "No review date - specify when this should be re-evaluated"

### Universal Discovery Integration
- "Context doesn't use Universal Discovery - integrate current state, evidence, and goals"
- "No evidence provided - decision seems based on opinion, not validated problem"
- "Related documents not referenced - link to documents from Universal Discovery"
