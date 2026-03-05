# RFC Quality Checklist

> **Purpose**: Internal validation checklist for RFCs. Use this to self-review before submitting for review, and during peer review to provide structured feedback.

---

## Checklist Overview

This checklist is organized by RFC sections. Each section has:
- **Required elements** - Must-haves for this section
- **Quality indicators** - Signs of high-quality content
- **Common issues** - Problems to watch for

---

## 1. Abstract

### Required Elements
- [ ] States what is being proposed
- [ ] States why it matters (problem it solves)
- [ ] States expected outcome
- [ ] 2-3 sentences only (under 100 words)

### Quality Indicators
- Abstract can be understood without reading the rest of the document
- Clear connection between problem and solution
- No jargon or undefined terms

### Common Issues
- ❌ Too long (>100 words)
- ❌ Missing problem statement (just says "we're doing X")
- ❌ Missing outcome (just says "this is important")
- ❌ Uses jargon not defined until later

---

## 2. Motivation

### 2.1 Current State

#### Required Elements
- [ ] Describes what happens now in detail
- [ ] Provides evidence of problem (metrics, logs, complaints)
- [ ] States who is affected
- [ ] Uses Universal Discovery output

#### Quality Indicators
- Specific, not vague ("API takes 2-3 seconds" not "API is slow")
- Evidence is quantitative where possible
- Clear connection to affected parties

#### Common Issues
- ❌ Vague problem description ("performance is poor")
- ❌ No evidence provided ("we know it's a problem")
- ❌ No connection to Universal Discovery output

### 2.2 Desired State

#### Required Elements
- [ ] Describes what "fixed" looks like
- [ ] States how success will be measured
- [ ] Uses Universal Discovery output

#### Quality Indicators
- Success criteria are specific and measurable
- Clear "before vs after" comparison
- Realistic expectations

#### Common Issues
- ❌ Vague desired state ("better performance")
- ❌ No measurable success criteria
- ❌ Unrealistic promises

### 2.3 Problem Statement

#### Required Elements
- [ ] One-sentence current state
- [ ] Specific pain/impact
- [ ] One-sentence desired state
- [ ] Cost of inaction (urgency)
- [ ] Uses Universal Discovery output

#### Quality Indicators
- Problem statement is clear and specific
- Impact is quantified (not just "it's slow")
- Urgency is justified (why NOW?)
- One-sentence format for current and desired states

#### Common Issues
- ❌ Multi-sentence problem statement (should be one sentence)
- ❌ No urgency (why solve this now?)
- ❌ Missing cost of inaction

---

## 3. Proposed Design

### Required Elements
- [ ] High-level overview of solution
- [ ] Architecture diagram
- [ ] Key components table (purpose, technology)
- [ ] Data flow description

### Quality Indicators
- Clear connection between problem and solution
- Understandable by both technical and non-technical readers
- All major components covered
- Diagram is accurate and readable

### Common Issues
- ❌ No architecture diagram
- ❌ Diagram is unreadable or inaccurate
- [ ] Solution doesn't connect to problem stated in Motivation
- [ ] Missing key components

---

## 4. Architecture Overview

### Required Elements
- [ ] Architecture diagram (use mermaid)
- [ ] System boundaries labeled
- [ ] Data flow shown
- [ ] Dependencies identified

### Quality Indicators
- New vs existing components are labeled
- Error flows included
- All components have purposes
- External dependencies identified

### Common Issues
- ❌ No diagram
- ❌ Diagram doesn't match description
- ❌ Components not labeled
- ❌ No error flows

---

## 5. Implementation Plan

### Required Elements
- [ ] Phases are logically ordered
- [ ] Each phase has:
  - [ ] Clear goals
  - [ ] Task checklist
  - [ ] Owner assigned
  - [ ] Effort estimate
  - [ ] Dependencies identified
  - [ ] Deliverables specified

### Quality Indicators
- Dependencies between phases respected
- Riskiest work is done early
- Ownership is clear
- Effort estimates are realistic

### Common Issues
- ❌ No phase ordering (just a list of tasks)
- ❌ Missing ownership (who does what?)
- ❌ No effort estimates
- ❌ Dependencies not identified

---

## 6. Migration Strategy

### Required Elements
- [ ] Migration method specified (big bang, phased, parallel, blue-green)
- [ ] Current system changes documented
- [ ] Data migration plan (if applicable)
- [ ] Backwards compatibility addressed
- [ ] Rollback plan referenced (see Rollback Plan section)

### Quality Indicators
- Migration method is appropriate for risk level
- Client impact is minimized
- Backwards compatibility is addressed
- Data migration has rollback plan

### Common Issues
- ❌ No migration method specified
- ❌ No backwards compatibility consideration
- ❌ Data migration without rollback plan
- ❌ Client impact not addressed

---

## 7. Rollback Plan

> **CRITICAL**: This section is NON-NEGOTIABLE. Every RFC must have a rollback plan.

### Required Elements
- [ ] Rollback triggers are specific
- [ ] Rollback procedure is step-by-step
- [ ] Rollback validation is specified
- [ ] Rollback has been tested OR test plan is documented
- [ ] Rollback time is estimated

### Quality Indicators
- Rollback triggers are actionable (not "if something goes wrong")
- Rollback procedure is unambiguous
- Anyone can execute rollback (not just the author)
- Rollback can be executed in <5 minutes

### Common Issues
- ❌ **CRITICAL**: No rollback plan
- ❌ Vague triggers ("if it doesn't work")
- ❌ No rollback validation (how do we know rollback succeeded?)
- ❌ Rollback not tested
- ❌ Rollback takes too long (>15 minutes)

---

## 8. Testing Strategy

### Required Elements
- [ ] Unit tests specified with coverage target
- [ ] Integration tests specified
- [ ] Performance tests specified with metrics
- [ ] **Rollback tests specified** ← NON-NEGOTIABLE

### Quality Indicators
- All testing types covered
- Coverage targets are specified
- Performance testing matches production load patterns
- **Rollback testing is documented** ← NON-NEGOTIABLE

### Common Issues
- ❌ No rollback testing ← CRITICAL ISSUE
- ❌ No performance testing
- ❌ No coverage targets
- ❌ Integration tests not specified

---

## 9. Performance Considerations

### Required Elements
- [ ] Performance impact is quantified (latency, throughput, resources)
- [ ] Monitoring plan specified (key metrics, dashboard)
- [ ] Alerting thresholds defined

### Quality Indicators
- Performance impact is quantified (not "should be faster")
- Resource usage is estimated (CPU, memory, network)
- Metrics are actionable

### Common Issues
- ❌ Vague performance claims ("will improve performance")
- ❌ No monitoring plan
- ❌ No alerting thresholds
- ❌ Resource usage not estimated

---

## 10. Security Considerations

### Required Elements
- [ ] Security risks identified in a table
- [ ] Each risk has likelihood, impact, and mitigation
- [ ] Compliance requirements addressed (if applicable)
- [ ] Authentication/authorization changes documented (if any)

### Quality Indicators
- All security risks identified
- Risk table is complete
- Compliance requirements are addressed
- Access control changes are documented

### Common Issues
- ❌ No security risks identified
- ❌ Risk table incomplete
- ❌ No compliance considerations
- ❌ Access control changes not documented

---

## 11. Alternatives Considered

### Required Elements
- [ ] At least 2 alternatives documented ← NON-NEGOTIABLE
- [ ] Each alternative has:
  - [ ] Description
  - [ ] Pros
  - [ ] Cons
  - [ ] Why not chosen
- [ ] Chosen alternative has clear rationale

### Quality Indicators
- Alternatives are real options (not strawmen)
- Pros and cons are balanced
- Rationale is clear and convincing
- Previous attempts referenced (if applicable)

### Common Issues
- ❌ **CRITICAL**: Fewer than 2 alternatives
- ❌ Strawman alternatives (obviously bad options)
- [ ] No rationale for chosen alternative
- [ ] Previous attempts not referenced

---

## 12. Risks and Mitigations

### Required Elements
- [ ] Risks identified in a table
- [ ] Each risk has:
  - [ ] Likelihood (High/Med/Low)
  - [ ] Impact
  - [ ] Mitigation plan
  - [ ] Owner
- [ ] Overall risk profile summarized

### Quality Indicators
- All risks identified (technical, operational, security)
- Risk table is complete
- Mitigation plans are actionable
- Ownership is assigned

### Common Issues
- ❌ Risks not identified
- ❌ Risk table incomplete
- ❌ No ownership assigned
- ❌ No overall risk profile summary

---

## 13. Open Questions

### Required Elements
- [ ] Questions are specific and answerable
- [ ] Each question has an owner
- [ ] Status is tracked (Open, In Progress, Answered)
- [ ] Answers filled in as discovered

### Quality Indicators
- Questions are actionable
- Owners are assigned
- Status is current
- No blockers unanswered (or explicitly noted as blockers)

### Common Issues
- ❌ Vague questions ("how do we do this?")
- ❌ No owners assigned
- ❌ Status not tracked
- ❌ Blockers not identified

---

## 14. Success Metrics

### Required Elements
- [ ] Functional success criteria are specific
- [ ] Quantitative metrics have:
  - [ ] Baseline
  - [ ] Target
  - [ ] Measurement method
- [ ] Success timeline is specified
- [ ] Metrics tie back to problem statement

### Quality Indicators
- Success criteria are specific (not vague)
- Metrics are quantified
- Measurement method is specified
- Timeline is realistic

### Common Issues
- ❌ Vague success criteria ("performance improved")
- ❌ No baseline for metrics
- ❌ No measurement method
- ❌ No timeline for evaluation

---

## 15. References

### Required Elements
- [ ] Related documents are linked
- [ ] Each link has a brief description
- [ ] External references are relevant

### Quality Indicators
- Links are accurate and accessible
- Descriptions are helpful
- Previous attempts referenced (if any)
- External sources are current

### Common Issues
- ❌ No references
- ❌ Broken links
- ❌ No descriptions for links
- ❌ Previous attempts not referenced

---

## 16. Appendix

### Required Elements
- [ ] Glossary defines domain-specific terms (if needed)
- [ ] Implementation details are accurate (if included)

### Quality Indicators
- Terms are clearly defined
- Implementation details are helpful
- Appendix is truly optional (main doc stands alone)

### Common Issues
- ❌ Glossary missing when needed (jargon not defined)
- ❌ Implementation details are inaccurate
- ❌ Appendix contains essential content (should be in main sections)

---

## 17. Approval

### Required Elements
- [ ] All required roles are listed
- [ ] Approval status is tracked
- [ ] Dates are recorded when approvals received

### Quality Indicators
- Approval roles are appropriate for the RFC
- No approvals are missing before implementation

### Common Issues
- ❌ Required roles not listed
- ❌ Approvals not tracked
- ❌ Implementation starts before approvals

---

## Universal Discovery Integration Check

> **CRITICAL**: RFCs must integrate Universal Discovery output from Phase 1.

### Required Integration Points
- [ ] **Motivation → Current State**: Uses Universal Discovery "Current State Deep Dive" output
- [ ] **Motivation → Problem Statement**: Uses Universal Discovery "Evidence of Problem" output
- [ ] **Motivation → Who's Affected**: Uses Universal Discovery "Who Has This Problem" output
- [ ] **Motivation → Desired State**: Uses Universal Discovery "Desired State" output
- [ ] **Motivation → Problem Statement**: Uses Universal Discovery "State Gap" output
- [ ] **Alternatives Considered**: References Universal Discovery "Historical Context" (if previous attempts)
- [ ] **References**: Links to Universal Discovery "Related Documents" (if provided)

### Quality Indicators
- Universal Discovery output is clearly used in Motivation section
- Problem statement is validated (not superficial)
- Evidence is quantified (not anecdotal only)
- Previous attempts are referenced (if any)

### Common Issues
- ❌ Motivation section doesn't use Universal Discovery output
- ❌ Problem statement is superficial (skipped Problem Validation Gate)
- ❌ No evidence provided (anecdotal only)
- ❌ Previous attempts not referenced

---

## Critical Go/No-Go Criteria

An RFC is **READY FOR REVIEW** when:

- ✅ All required sections are complete
- ✅ Rollback plan is detailed and specific ← NON-NEGOTIABLE
- ✅ At least 2 alternatives are documented with rationale
- ✅ Testing strategy includes rollback testing ← NON-NEGOTIABLE
- ✅ Success metrics are quantified with baseline, target, measurement method
- ✅ Security risks are identified with mitigations
- ✅ Universal Discovery output is integrated in Motivation section

An RFC is **NOT READY** if any of these are true:

- ❌ No rollback plan (or rollback plan is vague)
- ❌ Fewer than 2 alternatives documented
- ❌ No rollback testing specified
- ❌ Success metrics are vague (no baseline, target, or measurement method)
- ❌ No security considerations
- ❌ Motivation section doesn't use Universal Discovery output

---

## Reviewer Guidelines

### When Reviewing an RFC

1. **Check Universal Discovery integration first**: Is the problem validated? Is evidence quantified?
2. **Verify rollback plan**: Is it specific? Can anyone execute it? Has it been tested?
3. **Count alternatives**: Are there at least 2? Are they real options or strawmen?
4. **Check testing**: Is rollback testing specified?
5. **Verify metrics**: Are success metrics quantified (baseline, target, measurement)?
6. **Check security**: Are security risks identified?
7. **Check architecture**: Is there a diagram? Is it accurate?

### Providing Feedback

- **Be specific**: Instead of "problem statement is weak", say "problem statement needs quantitative evidence (currently anecdotal only)"
- **Reference sections**: Cite the section number (e.g., "Section 7: Rollback Plan needs specific triggers")
- **Explain why**: Explain the reasoning behind feedback (e.g., "rollback triggers must be specific so oncall knows when to rollback")
- **Suggest improvements**: Offer concrete suggestions (e.g., "add rollback trigger: p95 latency > 500ms for 5 minutes")

---

## Common Review Comments

Here are common review comments organized by section:

### Abstract
- "Too long - aim for 2-3 sentences under 100 words"
- "Missing problem statement - what problem does this solve?"
- "Missing outcome - what's the expected benefit?"

### Motivation
- "Current state is vague - add specific details (what happens now step by step)"
- "No evidence provided - add metrics, logs, or complaints"
- "Who is affected? - add affected users/services"
- "Desired state is vague - add measurable success criteria"
- "Problem statement is multi-sentence - compress to one sentence"
- "Missing cost of inaction - why solve this now?"

### Proposed Design
- "No architecture diagram - add mermaid diagram showing components and data flow"
- "Key components not listed - add table with component purposes"

### Architecture Overview
- "Diagram missing - use /common-engineering:mermaid to create diagram"
- "Components not labeled - add labels with purposes"
- "No error flows - add error handling to diagram"

### Implementation Plan
- "No phase ordering - break down into phases with dependencies"
- "No ownership - assign owners for each phase"
- "No effort estimates - add time estimates for each phase"

### Migration Strategy
- "No migration method specified - choose big bang, phased, parallel, or blue-green"
- "No backwards compatibility consideration - address client impact"
- "Data migration without rollback - add rollback plan for data migration"

### Rollback Plan
- **"CRITICAL**: No rollback plan - add detailed rollback procedure"
- "Rollback triggers are vague - add specific triggers (e.g., p95 latency > 500ms for 5 minutes)"
- "No rollback validation - add how to confirm rollback succeeded"
- "Rollback not tested - add test plan or results"

### Testing Strategy
- **"CRITICAL": No rollback testing specified - add rollback test plan**
- "No performance testing - add load testing plan"
- "No coverage targets - add target coverage percentages"

### Performance Considerations
- "Performance impact is vague - quantify latency, throughput, resource changes"
- "No monitoring plan - add key metrics and dashboard location"
- "No alerting thresholds - add what triggers alerts"

### Security Considerations
- "No security risks identified - add security risk table"
- "No compliance considerations - address PII, regulatory requirements"
- "No access control changes - document any auth/authz changes"

### Alternatives Considered
- **"CRITICAL**: Fewer than 2 alternatives - add at least one more alternative"
- "Alternatives are strawmen - make alternatives more realistic"
- "No rationale for chosen alternative - add why this is best choice"

### Risks and Mitigations
- "No risks identified - add risk table with likelihood, impact, mitigation"
- "No ownership assigned - add owner for each risk"
- "No overall risk profile - add summary of risk level"

### Success Metrics
- "Success criteria are vague - add specific, measurable criteria"
- "No baseline for metrics - add current values"
- "No target for metrics - add desired values"
- "No measurement method - add how each metric is measured"
- "No timeline - add when success will be evaluated"

### Universal Discovery Integration
- "Motivation doesn't use Universal Discovery output - integrate current state, evidence, who's affected, desired state, and gap analysis"
- "Problem is superficial - was Problem Validation Gate completed?"
- "No evidence provided - add quantitative evidence (not just anecdotal)"
- "Previous attempts not referenced - add to Alternatives Considered if applicable"
