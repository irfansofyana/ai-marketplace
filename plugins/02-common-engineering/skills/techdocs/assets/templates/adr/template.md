# ADR Template: Architecture Decision Record

> **Purpose**: ADRs (Architecture Decision Records) capture important architectural decisions, the context, and the consequences. They focus on technology choices, framework decisions, and architectural pivots.

---

## [ADR Title]

**Status:** [Proposed | Accepted | Deprecated | Superseded]
**Date:** [YYYY-MM-DD]
**Decision Type:** [Technology Choice | Framework Decision | Architectural Pivot | Data Storage | Integration Pattern]
**Deciders:** [Names/Roles]
**Related ADRs:** [Link to related ADRs if superseding or related]

---

## Context

> **Uses Universal Discovery Output**: This section uses validated problem information to establish decision context.

**Template:**
> We need to make a decision about [decision topic]. Currently, [current state - from Universal Discovery]. This is causing [problem/evidence - from Universal Discovery]. We need to [desired state - from Universal Discovery].

**Current Situation:**
- [Describe the current state in detail]
- [What problem are we trying to solve?]
- [What constraints do we have?]

**Drivers:**
- [Driver 1]: [Description]
- [Driver 2]: [Description]
- [Driver 3]: [Description]

**Goals:**
- [Goal 1]: [Description]
- [Goal 2]: [Description]
- [Goal 3]: [Description]

**Non-Goals:**
- [Non-goal 1]: [Description]
- [Non-goal 2]: [Description]

---

## Decision

> **What was chosen.**

We have chosen **[chosen alternative]** for [decision topic].

**Description:**
[Detailed description of the chosen option]

**Key Attributes:**
- [Attribute 1]: [Description]
- [Attribute 2]: [Description]
- [Attribute 3]: [Description]

---

## Alternatives Considered

> **MANDATORY**: At least 2 alternatives must be documented.

### Alternative 1: [Alternative Name]

**Description:**
[Brief description of this alternative]

**Pros:**
- [Pro 1]: [Description]
- [Pro 2]: [Description]

**Cons:**
- [Con 1]: [Description]
- [Con 2]: [Description]

**Estimated Impact:**
- **Cost:** [Description]
- **Effort:** [Description]
- **Risk:** [Low | Medium | High]

### Alternative 2: [Alternative Name]

**Description:**
[Brief description of this alternative]

**Pros:**
- [Pro 1]: [Description]
- [Pro 2]: [Description]

**Cons:**
- [Con 1]: [Description]
- [Con 2]: [Description]

**Estimated Impact:**
- **Cost:** [Description]
- **Effort:** [Description]
- **Risk:** [Low | Medium | High]

### (Optional) Alternative 3: [Alternative Name]

**Description:**
[Brief description of this alternative]

**Pros:**
- [Pro 1]: [Description]
- [Pro 2]: [Description]

**Cons:**
- [Con 1]: [Description]
- [Con 2]: [Description]

**Estimated Impact:**
- **Cost:** [Description]
- **Effort:** [Description]
- **Risk:** [Low | Medium | High]

---

## Decision Criteria

> **How we evaluated alternatives.**

| Criterion | Weight | Alternative 1 | Alternative 2 | Chosen Alternative |
|-----------|--------|---------------|---------------|-------------------|
| [Criterion 1] | [High/Med/Low] | [Score/Notes] | [Score/Notes] | [Score/Notes] |
| [Criterion 2] | [High/Med/Low] | [Score/Notes] | [Score/Notes] | [Score/Notes] |
| [Criterion 3] | [High/Med/Low] | [Score/Notes] | [Score/Notes] | [Score/Notes] |

**Criteria Definitions:**
- **[Criterion 1]**: [What this means and why it matters]
- **[Criterion 2]**: [What this means and why it matters]
- **[Criterion 3]**: [What this means and why it matters]

---

## Trade-offs Analysis

> **What we're trading off.**

### Performance vs Simplicity

| Aspect | Trade-off | Impact |
|--------|-----------|--------|
| [Aspect 1] | [Description] | [Impact] |
| [Aspect 2] | [Description] | [Impact] |

### Cost vs Capability

| Aspect | Trade-off | Impact |
|--------|-----------|--------|
| [Aspect 1] | [Description] | [Impact] |
| [Aspect 2] | [Description] | [Impact] |

### Time to Market vs Long-term Viability

| Aspect | Trade-off | Impact |
|--------|-----------|--------|
| [Aspect 1] | [Description] | [Impact] |
| [Aspect 2] | [Description] | [Impact] |

---

## Consequences

> **Positive and negative consequences of this decision.**

### Positive Consequences

- **[Benefit 1]**: [Description and who benefits]
- **[Benefit 2]**: [Description and who benefits]
- **[Benefit 3]**: [Description and who benefits]

### Negative Consequences

- **[Drawback 1]**: [Description and who is affected]
- **[Drawback 2]**: [Description and who is affected]
- **[Drawback 3]**: [Description and who is affected]

### Risks Introduced

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [High/Med/Low] | [Impact] | [Mitigation] |
| [Risk 2] | [High/Med/Low] | [Impact] | [Mitigation] |

### Risks Eliminated

- **[Risk 1]**: [Description of risk this decision eliminates]
- **[Risk 2]**: [Description of risk this decision eliminates]

---

## Implementation Plan

> **How we will implement this decision.**

### Phase 1: [Phase Name]

- **Goals:** [What this phase accomplishes]
- **Tasks:**
  - [ ] [Task 1]
  - [ ] [Task 2]
- **Owner:** [Team/Person]
- **Timeline:** [Time estimate]

### Phase 2: [Phase Name]

- **Goals:** [What this phase accomplishes]
- **Tasks:**
  - [ ] [Task 1]
  - [ ] [Task 2]
- **Owner:** [Team/Person]
- **Timeline:** [Time estimate]

### Rollout Strategy

- **Approach:** [Big bang | Phased | Parallel | Experimental]
- **Timeline:** [When this will be implemented]
- **Success Criteria:**
  - [ ] [Success criterion 1]
  - [ ] [Success criterion 2]

---

## Validation

> **How we validated this decision.**

### Proof of Concept

- **What was tested:** [Description]
- **Results:** [Description]
- **Conclusion:** [Did it validate the decision?]

### Benchmarking

- **What was measured:** [Description]
- **Results:** [Description]
- **Conclusion:** [Did it validate the decision?]

### References

- **[Reference 1]**: [URL/Source] - [What it provides]
- **[Reference 2]**: [URL/Source] - [What it provides]

---

## Related Decisions

### Related ADRs

- [ADR-XXX: Title](/path/to/adr.md) - [Relationship]
- [ADR-YYY: Title](/path/to/adr.md) - [Relationship]

### Supersedes

- [ADR-ZZZ: Title](/path/to/adr.md) - [Why it supersedes this ADR]

---

## Reconsideration

> **When and why this decision should be revisited.**

### Triggers for Reconsideration

This decision should be revisited if:
- [Trigger 1]: [Description]
- [Trigger 2]: [Description]
- [Trigger 3]: [Description]

### Expiration

**Review Date:** [YYYY-MM-DD or "This decision should be reviewed in X months"]

**Reason:** [Why this review date was chosen]

---

## References

> **Uses Universal Discovery Output**: Reference any attached documents from Rich Context Input.

### Related Documents

- [Document link/name] - [Brief description]
- [Document link/name] - [Brief description]

### External References

- [Link/Source] - [What it provides]
- [Link/Source] - [What it provides]

---

## Approval

| Role | Name | Approval | Date |
|------|------|----------|------|
| [Role 1] | | [✓] | |
| [Role 2] | | [✓] | |
