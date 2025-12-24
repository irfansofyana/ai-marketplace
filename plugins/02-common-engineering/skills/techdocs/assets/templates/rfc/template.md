# RFC Template: Request for Comments

> **Purpose**: RFCs (Request for Comments) are detailed design documents for complex architectural changes, multi-service implementations, or significant system modifications requiring thorough analysis and team consensus.

---

## [RFC Title]

**Author:** [Name, Team]
**Status:** [Draft | In Review | Approved | Rejected | Deprecated]
**Created:** [YYYY-MM-DD]
**Last Updated:** [YYYY-MM-DD]

---

## Abstract

> A concise summary (2-3 sentences) of what this RFC proposes and why it matters.

**Template:**
> This RFC proposes [brief description of the change]. The current system [problem summary]. This change will [benefit/outcome]. Implementation affects [affected systems/teams].

---

## Motivation

> **Uses Universal Discovery Output**: This section uses validated problem information from Phase 1 Universal Discovery.

### Current State

**Template:**
> **What happens now:** [From Universal Discovery - Current State Deep Dive]
>
> **Evidence of problem:** [From Universal Discovery - Evidence of Problem]
>
> **Who is affected:** [From Universal Discovery - Who Has This Problem]

### Desired State

**Template:**
> **What should happen:** [From Universal Discovery - Desired State]
>
> **The gap:** [From Universal Discovery - Gap Analysis]

### Problem Statement

**Template:**
> Today, [one-sentence current state]. This causes [specific pain/impact]. We need [one-sentence desired state]. The cost of not fixing this is [from Universal Discovery - Impact Urgency].

---

## Proposed Design

### High-Level Overview

> Describe the proposed solution at a high level. What are we building and how does it solve the problem?

### Architecture Overview

> Include diagrams, system boundaries, data flow, and component relationships.

> **Tip**: Use `/common-engineering:mermaid` to create architecture diagrams.

### Key Components

| Component | Purpose | Technology |
|-----------|---------|------------|
| [Component 1] | [Purpose] | [Tech choice] |
| [Component 2] | [Purpose] | [Tech choice] |

### Data Flow

> Describe how data flows through the system. What are the key interactions?

---

## Implementation Plan

### Phase 1: [Phase Name]

- **Goals:** [What this phase accomplishes]
- **Tasks:**
  - [ ] [Task 1]
  - [ ] [Task 2]
- **Owner:** [Team/Person]
- **Estimated effort:** [Time estimate]

### Phase 2: [Phase Name]

- **Goals:** [What this phase accomplishes]
- **Tasks:**
  - [ ] [Task 1]
  - [ ] [Task 2]
- **Owner:** [Team/Person]
- **Estimated effort:** [Time estimate]

### Remaining Phases

> Continue with additional phases as needed...

---

## Migration Strategy

### Current System Decommissioning

- **What changes:** [Current system behavior being replaced]
- **When:** [Timeline for deprecation]
- **Migration method:** [Big bang | Phased | Parallel run | Blue-green]

### Data Migration

- **Data scope:** [What data needs migration]
- **Migration approach:** [How data will be migrated]
- **Rollback:** [How to revert if migration fails]

### Backwards Compatibility

- **API compatibility:** [Breaking vs non-breaking changes]
- **Grace period:** [How long old clients are supported]
- **Deprecation timeline:** [When old behavior is removed]

---

## Rollback Plan

> **CRITICAL**: Every RFC must include a rollback plan. What happens if this change fails in production?

### Rollback Triggers

> Under what conditions do we rollback?

- [ ] [Trigger condition 1]
- [ ] [Trigger condition 2]
- [ ] [Trigger condition 3]

### Rollback Procedure

1. **Step 1:** [First rollback action]
2. **Step 2:** [Second rollback action]
3. **Step 3:** [Third rollback action]

### Rollback Validation

> How do we confirm rollback was successful?

- [ ] [Validation check 1]
- [ ] [Validation check 2]

---

## Testing Strategy

### Unit Tests

- **Coverage target:** [% or specific areas]
- **Key test scenarios:**
  - [ ] [Scenario 1]
  - [ ] [Scenario 2]

### Integration Tests

- **What's tested:** [Service interactions, dependencies]
- **Test environment:** [How integration tests are run]

### Performance Tests

- **Metrics to validate:** [Latency, throughput, resource usage]
- **Performance targets:** [Specific benchmarks]
- **Load testing approach:** [How performance is validated]

### Rollback Testing

> **CRITICAL**: Rollback must be tested before production deployment.

- **Rollback test plan:** [How rollback is tested]
- **Rollback test results:** [Actual test outcomes - add after testing]

---

## Performance Considerations

### Expected Performance Impact

- **Latency:** [Expected change in response times]
- **Throughput:** [Expected change in request capacity]
- **Resource usage:** [CPU, memory, storage, network impact]

### Monitoring

- **Key metrics:** [What will be monitored]
- **Alerting thresholds:** [What triggers alerts]
- **Dashboard:** [Where metrics are visualized]

---

## Security Considerations

### Security Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [High/Med/Low] | [Impact] | [Mitigation] |
| [Risk 2] | [High/Med/Low] | [Impact] | [Mitigation] |

### Compliance

- **Data privacy:** [Any PII/sensitive data concerns]
- **Regulatory:** [Compliance requirements - GDPR, SOC2, etc.]
- **Audit requirements:** [Logging/auditing needs]

### Authentication/Authorization

- **Access control:** [Who can access what]
- **Permission changes:** [Any auth/authz changes required]

---

## Alternatives Considered

> **Uses Universal Discovery Output**: If historical context included previous attempts, reference them here.

### Alternative 1: [Alternative Name]

> **Description:** [What this alternative proposes]

**Pros:**
- [Pro 1]
- [Pro 2]

**Cons:**
- [Con 1]
- [Con 2]

**Why not chosen:** [Rationale for rejection]

### Alternative 2: [Alternative Name]

> **Description:** [What this alternative proposes]

**Pros:**
- [Pro 1]
- [Pro 2]

**Cons:**
- [Con 1]
- [Con 2]

**Why not chosen:** [Rationale for rejection]

### Chosen Alternative: [Proposed Design]

> **Why this is the best choice:** [Rationale for selection]

---

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation Plan | Owner |
|------|------------|--------|-----------------|-------|
| [Risk 1] | [High/Med/Low] | [Impact] | [Mitigation steps] | [Owner] |
| [Risk 2] | [High/Med/Low] | [Impact] | [Mitigation steps] | [Owner] |
| [Risk 3] | [High/Med/Low] | [Impact] | [Mitigation steps] | [Owner] |

### Risk Mitigation Summary

> Summarize the overall risk profile. Is this low-risk, medium-risk, or high-risk? Why?

---

## Open Questions

> Questions that need answers before or during implementation.

| Question | Asked To | Status | Answer |
|----------|----------|--------|--------|
| [Question 1] | [Person/Team] | [Open | Answered] | [Answer if known] |
| [Question 2] | [Person/Team] | [Open | Answered] | [Answer if known] |

---

## Success Metrics

> How do we know this implementation was successful?

### Functional Success Criteria

- [ ] [Success criterion 1 - what must work]
- [ ] [Success criterion 2 - what must work]
- [ ] [Success criterion 3 - what must work]

### Quantitative Metrics

| Metric | Baseline | Target | How Measured |
|--------|----------|--------|--------------|
| [Metric 1] | [Current value] | [Target value] | [Measurement method] |
| [Metric 2] | [Current value] | [Target value] | [Measurement method] |

### Success Timeline

> When will we evaluate success? [Time after implementation]

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

## Appendix

### Glossary

| Term | Definition |
|------|------------|
| [Term 1] | [Definition] |
| [Term 2] | [Definition] |

### Implementation Details

> Any additional technical details that don't fit in main sections but are useful for implementers.

---

## Approval

| Role | Name | Approval | Date |
|------|------|----------|------|
| [Role 1 - e.g., Tech Lead] | | [✓] | |
| [Role 2 - e.g., Product Manager] | | [✓] | |
| [Role 3 - e.g., Security Review] | | [✓] | |
| [Role 4 - e.g., SRE/Oncall] | | [✓] | |
