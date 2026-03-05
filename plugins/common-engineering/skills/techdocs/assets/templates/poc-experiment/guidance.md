# POC/Technical Experiment Section Guidance

This file provides detailed guidance for each section of a POC/Technical Experiment document. Use this when helping users write their POC documentation.

## Document Overview

A POC/Technical Experiment document is used to validate hypotheses through controlled experimentation. Unlike RFCs (which design production solutions) or One-Pagers (which propose features), POCs focus on learning and Go/No-Go decision-making.

**When to use a POC/Experiment:**
- Validating whether a technology or approach is feasible
- Comparing multiple technical alternatives with measurable criteria
- Testing performance characteristics of a system or component
- Reducing uncertainty before committing to a full implementation
- Exploring new technologies with unknown production viability

## Quick Reference: Essential Questions by Section

For quick access during document creation:

- **Executive Summary**: What did you investigate? How? What did you learn? Go/No-Go?
- **Problem Statement**: What prompted this? What are the pain points? What does success look like?
- **Approach & Solution Design**: Why this approach? What's the architecture? What technologies?
- **Implementation Details**: How was it built? What steps? Any deviations?
- **Results & Findings**: Did you meet success criteria? What were the metrics? What evidence supports this?
- **Trade-offs & Limitations**: What compromises were made? What are the limitations? Any technical debt?
- **Recommendation & Next Steps**: Go/No-Go decision with rationale. What's needed for production?
- **Appendix**: Repos, branches, raw data, detailed logs, references

---

## Universal Discovery Integration

> **IMPORTANT**: POC/Experiment documents are created AFTER completing Phase 1 (Universal Discovery) and Phase 2 (Document Type Selection). The Problem Validation Gate must be completed before writing this POC.

### Universal Discovery Output → POC/Experiment Section Mapping

| Universal Discovery Output | Used In POC Section | How It's Used |
|----------------------------|---------------------|---------------|
| Current State description | Problem Statement | Current pain points and limitations |
| Evidence of Problem | Problem Statement | Quantifying the problem to define success criteria |
| Who Has This Problem | Problem Statement | Who is affected, prioritizing criteria |
| Desired State description | Problem Statement | Target outcomes for success criteria |
| State Gap | Problem Statement | Measurable improvement targets |
| Pain Point (worst thing) | Problem Statement | Priority framing for what to test |
| Impact Urgency | Problem Statement | Why this matters now |
| Technical Context | Approach & Solution Design | System landscape, constraints, technology choices |
| Team Context | Implementation Details | Team capacity, expertise for implementation |
| Related Documents | Appendix | References to previous work |
| Historical Context | Approach & Solution Design | What was tried before, what to avoid |

### Before Starting the POC/Experiment Document

**Prerequisites:**
1. ✅ Problem Validation Gate completed (current state, evidence, who's affected, gap analysis)
2. ✅ Document type selection confirmed (AI recommended POC/Experiment, user accepted)
3. ✅ POC/Experiment specific questions answered (hypothesis, success criteria, measurement approach)

### Key Benefits of Universal Discovery for POC/Experiments

**Better Hypothesis Definition:**
- Problem Validation Gate ensures the problem is real and worth investigating
- Evidence of Problem helps quantify what "success" means

**Better Success Criteria:**
- Desired State from Universal Discovery directly informs target outcomes
- Gap analysis provides measurable improvement targets

**Better Approach Design:**
- Technical Context ensures the approach fits the system landscape
- Historical Context helps avoid repeating failed experiments

**Better Decision Quality:**
- Team Context helps assess whether results are actionable
- Rich Context Input (related docs) ensures results build on previous work

### How to Use Universal Discovery Output

**When writing Problem Statement:**
1. Start with **Current State Deep Dive** output for pain points
2. Add **Evidence of Problem** to quantify the issue
3. Use **Desired State** to define success criteria
4. Use **Who Has This Problem** to prioritize criteria

**When writing Approach & Solution Design:**
1. Reference **Technical Context**: System landscape, constraints
2. Reference **Historical Context**: What was tried before?

**When writing Implementation Details:**
1. Use **Team Context**: Who can execute? What expertise exists?

**When writing Recommendation & Next Steps:**
1. Reference **Impact Urgency**: What's the cost of delaying?

---

## Section-by-Section Guidance

### Executive Summary

**Purpose**: A brief paragraph (3-5 sentences) covering the key points of the experiment.

**This section must answer**:
1. What problem did you investigate?
2. What approach did you take?
3. What were the key findings?
4. What is your recommendation (Go/No-Go/Conditional Go)?

**Questions to ask**:
- What was the main hypothesis you tested?
- What did you actually do?
- What did you learn?
- Should we proceed or not?

**Quality criteria**:
- ✅ Complete in 3-5 sentences
- ✅ Includes the decision (Go/No-Go)
- ✅ Quantified findings if applicable
- ✅ Stands alone (reader understands the conclusion)

**Example**:
```
We conducted a POC to validate whether Apache Pulsar could replace Kafka for our
high-throughput event streaming use case. The experiment tested message throughput
(max 1M msg/sec), latency (p99 < 10ms), and operational complexity over a 2-week
period. Key findings: Pulsar met throughput and latency targets but required 3x
the operational effort compared to Kafka. Our recommendation: No-Go for migration,
but consider Pulsar for net-new multi-region use cases.
```

---

### Problem Statement

**Purpose**: Clearly articulate what problem or question prompted this POC, and define success criteria.

**This section has three subsections**:

#### What Prompted This Experiment

**Questions to ask**:
- What specific problem or question are you trying to answer?
- Why is this experiment necessary now?
- What happens if you don't do this experiment?

**Quality criteria**:
- ✅ Clear problem or question stated
- ✅ Rationale for why experiment is needed
- ✅ Not jumping to solution

#### Current Pain Points or Limitations

**Questions to ask**:
- What are the current pain points?
- Who is affected by these pain points?
- What are the limitations of the current approach?

**Quality criteria**:
- ✅ Specific pain points identified
- ✅ Impact on users or systems described
- ✅ Connection to business or technical goals

#### Success Criteria

**Questions to ask**:
- What does success look like?
- How will you measure it?
- What are the target values?

**Quality criteria**:
- ✅ Each criterion is measurable
- ✅ Target values are defined
- ✅ Criteria map to the original problem
- ✅ Include at least 2-3 criteria

**Example**:
```
Success Criteria:

| Criterion | How Measured | Target | Status |
|-----------|--------------|--------|--------|
| Message throughput | Messages per second sustained | 1M msg/sec | ✅ Met |
| Latency (p99) | 99th percentile latency | < 10ms | ✅ Met |
| Setup time | Hours to get cluster running | < 4 hours | ❌ Not Met (16 hours) |
| Operational overhead | Hours/week for maintenance | < 2 hours | ❌ Not Met (6 hours) |
```

---

### Approach & Solution Design

**Purpose**: Explain why you chose this particular approach and provide the high-level design.

**This section has four subsections**:

#### Why This Approach

**Questions to ask**:
- Why this particular experimental approach?
- What alternatives were considered?
- Why were the alternatives rejected?

**Quality criteria**:
- ✅ Clear rationale for approach choice
- ✅ Alternatives considered and addressed
- ✅ Methodology explained

#### High-Level Architecture

**Questions to ask**:
- What is the high-level architecture?
- What are the key components?
- How do they interact?

**Quality criteria**:
- ✅ Architecture is clear
- ✅ Key components identified
- ✅ Diagram if complex (use `common-engineering:mermaid`)

#### Key Technologies, Tools, and Rationale

**Questions to ask**:
- What technologies or tools are used?
- Why was each chosen?

**Quality criteria**:
- ✅ Each technology has a clear purpose
- ✅ Rationale explains why this choice
- ✅ Trade-offs acknowledged

#### Scope Boundaries

**Questions to ask**:
- What is explicitly in scope?
- What is explicitly out of scope?

**Quality criteria**:
- ✅ Clear in-scope items
- ✅ Explicit out-of-scope items (manages expectations)
- ✅ Scope is realistic for a POC

---

### Implementation Details

**Purpose**: Document how the experiment was built, including step-by-step setup and any deviations from plan.

**This section has two subsections**:

#### Step-by-Step Setup or Configuration

**Questions to ask**:
- How was the experiment set up?
- What commands or configurations were used?
- What code snippets are worth highlighting?

**Quality criteria**:
- ✅ Steps are clear and reproducible
- ✅ Commands/configurations are included
- ✅ Code snippets where helpful
- ✅ Sufficient detail to reproduce results

#### Deviations from Original Plan

**Questions to ask**:
- What changed during implementation?
- Why did you deviate from the plan?

**Quality criteria**:
- ✅ All deviations documented
- ✅ Rationale provided for each deviation
- ✅ Honest about what changed

---

### Results & Findings

**Purpose**: Present the results of the experiment, including whether success criteria were met and any unexpected discoveries.

**This section has four subsections**:

#### Did It Meet the Success Criteria?

**Questions to ask**:
- Overall, did the experiment meet its success criteria?
- Which criteria were met? Which were not?

**Quality criteria**:
- ✅ Clear overall assessment
- ✅ References the success criteria table
- ✅ Honest about failures

#### Performance Metrics, Benchmarks, or Observations

**Questions to ask**:
- What metrics did you measure?
- What were the baseline and results?
- What was the percent change?

**Quality criteria**:
- ✅ Metrics are quantified
- ✅ Baseline provided for comparison
- ✅ Percent change calculated
- ✅ Notes provide context

#### Screenshots, Logs, or Evidence

**Questions to ask**:
- What evidence supports your conclusions?
- Can you include screenshots, logs, or charts?

**Quality criteria**:
- ✅ Evidence included where possible
- ✅ Screenshots/logs/charts support conclusions
- ✅ Data is readable and interpretable

#### Unexpected Discoveries

**Questions to ask**:
- What surprised you?
- What did you learn that wasn't part of the original plan?

**Quality criteria**:
- ✅ Both positive and negative surprises
- ✅ Insights that could inform future work
- ✅ Honest about what went wrong

---

### Trade-offs & Limitations

**Purpose**: Acknowledge the trade-offs made, known limitations, and any technical debt introduced.

**This section has three subsections**:

#### Trade-offs Made

**Questions to ask**:
- What compromises were made?
- What did you give up? What did you gain?
- Was it worth it?

**Quality criteria**:
- ✅ Honest about trade-offs
- ✅ Clear assessment of whether worth it
- ✅ Balanced view

#### Known Limitations

**Questions to ask**:
- What doesn't this POC prove?
- What's still unknown?
- What are the limitations of this approach?

**Quality criteria**:
- ✅ Honest about limitations
- ✅ Clear about what wasn't tested
- ✅ Manages expectations

#### Technical Debt or Shortcuts Taken

**Questions to ask**:
- What shortcuts were taken for the POC?
- What technical debt was introduced?
- What would need cleanup in production?

**Quality criteria**:
- ✅ Honest about shortcuts
- ✅ Production implications documented
- ✅ Cleanup effort estimated

---

### Recommendation & Next Steps

**Purpose**: Make a clear Go/No-Go decision supported by evidence, and outline next steps.

**This section has three subsections**:

#### Go/No-Go Decision

**Questions to ask**:
- Should we proceed (Go), not proceed (No-Go), or proceed with conditions (Conditional Go)?
- What evidence supports this decision?

**Quality criteria**:
- ✅ Clear decision stated upfront
- ✅ Rationale connects to results
- ✅ Evidence-based decision
- ✅ Honest recommendation

#### If Proceeding: Production Readiness Needs

**Questions to ask**:
- What's needed for production readiness?
- What's the current state vs. required state?
- What's the estimated effort?

**Quality criteria**:
- ✅ Areas clearly identified
- ✅ Current state vs. required state documented
- ✅ Effort estimates provided
- ✅ Total effort estimate included

#### If Not Proceeding: What Alternative Should Be Explored

**Questions to ask**:
- Why shouldn't we proceed?
- What alternative should be explored instead?

**Quality criteria**:
- ✅ Clear reasons for not proceeding
- ✅ Specific alternative suggested
- ✅ Rationale explained

#### Next Steps

**Questions to ask**:
- What are the immediate next steps?
- What needs to happen regardless of the decision?

**Quality criteria**:
- ✅ Actionable next steps
- ✅ Clear ownership (who does what)
- ✅ Timeline if applicable

---

### Appendix

**Purpose**: Provide links to repos, branches, raw data, detailed logs, and references.

**This section has three subsections**:

#### Links to Repos, Branches, or Environments

**Questions to ask**:
- What repos or branches contain the code?
- What environments were used?

**Quality criteria**:
- ✅ Links are provided
- ✅ Each link has a description
- ✅ Accessible to intended audience

#### Raw Data or Detailed Logs

**Questions to ask**:
- Is there raw data or detailed logs to reference?
- Where are they stored?

**Quality criteria**:
- ✅ Links to data/logs provided
- ✅ Descriptions explain what they contain
- ✅ Sufficient for reproducibility

#### References and Related Documentation

**Questions to ask**:
- What references or related docs should be included?
- What documents informed this work?

**Quality criteria**:
- ✅ References are relevant
- ✅ Each reference has a description
- ✅ Proper attribution if applicable

---

## Quality Validation

⚠️ **For internal validation only**: Quality criteria and checklists are used internally to validate document quality. They should NEVER appear in the user-facing document.

**See**: [quality-checklist.md](quality-checklist.md) for the complete validation checklist to use during Phase 5 (Review & Output).

**Important**: The quality checklist is for AI validation only. Do not include checkboxes or quality criteria in the document you present to users.
