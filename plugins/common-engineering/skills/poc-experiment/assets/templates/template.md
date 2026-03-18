# POC/Technical Experiment Template

POC/Technical Experiment documents validate hypotheses through controlled experimentation. Unlike RFCs (which design production solutions) or One-Pagers (which propose features), POCs focus on learning and Go/No-Go decision-making.

**When to use:**

- Validating whether a technology or approach is feasible
- Comparing multiple technical alternatives with measurable criteria
- Testing performance characteristics of a system or component
- Reducing uncertainty before committing to a full implementation
- Exploring new technologies with unknown production viability

**Best practices:**

- Define success criteria upfront before starting the experiment
- Be honest about what worked and what didn't
- Quantify results wherever possible (performance metrics, cost, effort)
- Document deviations from the original plan and why
- Make a clear Go/No-Go decision supported by evidence
- Include enough implementation detail that someone could reproduce your results

---

# POC: [Experiment Title]

**Author:** [Name, Team]
**Status:** [Draft | In Progress | Completed | Aborted]
**Created:** [YYYY-MM-DD]
**Last Updated:** [YYYY-MM-DD]

---

## Executive Summary

*3-5 sentences covering: what problem you investigated, the approach you took, key findings/outcome, and recommendation (proceed, pivot, or abandon).*

> **Template:** We conducted a POC to validate whether [brief hypothesis]. The experiment tested [what was tested] using [approach/methodology]. Key findings: [1-2 sentence results with metrics if applicable]. Our recommendation: [Go/No-Go/Conditional Go with conditions].

---

## Problem Statement

### What Prompted This Experiment

*What specific problem or question prompted this POC? What are you trying to learn?*

### Current Pain Points or Limitations

*What are the current pain points or limitations? Who is affected?*

### Success Criteria

*What does success look like? Define measurable criteria if possible.*

| Criterion | How Measured | Target | Status |
|-----------|--------------|--------|--------|
| *[Criterion 1]* | *[Measurement method]* | *[Target value]* | *[✅ Met / ❌ Not Met / Partial]* |
| *[Criterion 2]* | *[Measurement method]* | *[Target value]* | *[✅ Met / ❌ Not Met / Partial]* |
| *[Criterion 3]* | *[Measurement method]* | *[Target value]* | *[✅ Met / ❌ Not Met / Partial]* |

---

## Approach & Solution Design

### Why This Approach

*Why this particular approach over alternatives? What other options were considered and rejected?*

### High-Level Architecture

*High-level architecture or design. Diagrams help here.*

> **Tip:** Use `/common-engineering:mermaid` to create architecture diagrams.

### Key Technologies, Tools, and Rationale

| Technology/Tool | Purpose | Rationale |
|-----------------|---------|-----------|
| *[Technology 1]* | *[Purpose]* | *[Why this choice]* |
| *[Technology 2]* | *[Purpose]* | *[Why this choice]* |
| *[Technology 3]* | *[Purpose]* | *[Why this choice]* |

### Scope Boundaries

**In Scope:**
- [ ] *[Scope item 1]*
- [ ] *[Scope item 2]*
- [ ] *[Scope item 3]*

**Explicitly Out of Scope:**
- [ ] *[What's explicitly not covered]*
- [ ] *[What's explicitly not covered]*

---

## Implementation Details

### Step-by-Step Setup or Configuration

*Step-by-step setup or configuration. Include code snippets, commands, or configurations worth highlighting.*

#### Step 1: [Step Name]

*What was done, how it was done, any important details.*

```bash
# Example command or configuration
```

#### Step 2: [Step Name]

*Continue for each step...*

```bash
# Example command or configuration
```

#### Step 3: [Step Name]

*Continue as needed...*

### Deviations from Original Plan

*Any deviations from the original plan and why.*

---

## Results & Findings

### Did It Meet the Success Criteria?

*Overall assessment of whether success criteria were met.*

### Performance Metrics, Benchmarks, or Observations

| Metric | Baseline | Experiment Result | Change | Notes |
|--------|----------|-------------------|--------|-------|
| *[Metric 1]* | *[Value]* | *[Value]* | *[+/- %]* | *[Notes]* |
| *[Metric 2]* | *[Value]* | *[Value]* | *[+/- %]* | *[Notes]* |
| *[Metric 3]* | *[Value]* | *[Value]* | *[+/- %]* | *[Notes]* |

### Screenshots, Logs, or Evidence Supporting Conclusions

*Include evidence: screenshots, logs, benchmark output, charts, etc.*

```
# Example: Benchmark output or log data
```

### Unexpected Discoveries

*Any unexpected discoveries (both positive and negative).*

---

## Trade-offs & Limitations

### Trade-offs Made

| Trade-off | What We Gave Up | What We Gained | Assessment |
|-----------|-----------------|----------------|------------|
| *[Trade-off 1]* | *[Downside]* | *[Benefit]* | *[Worth it?]* |
| *[Trade-off 2]* | *[Downside]* | *[Benefit]* | *[Worth it?]* |

### Known Limitations

*Known limitations of this approach. What doesn't this POC prove?*

1. *[Limitation 1]*
2. *[Limitation 2]*
3. *[Limitation 3]*

### Technical Debt or Shortcuts Taken for the POC

*Any technical debt or shortcuts taken for the POC that would need to be addressed in production.*

---

## Recommendation & Next Steps

### Go/No-Go Decision

> **DECISION: [GO / NO-GO / CONDITIONAL GO]**

**Rationale:**
*Why this decision? What evidence supports it?*

### If Proceeding: Production Readiness Needs

*What's needed for production readiness?*

| Area | Current State | Required for Production | Estimated Effort |
|------|---------------|-------------------------|------------------|
| *[Area 1]* | *[What exists now]* | *[What's needed]* | *[Time estimate]* |
| *[Area 2]* | *[What exists now]* | *[What's needed]* | *[Time estimate]* |
| *[Area 3]* | *[What exists now]* | *[What's needed]* | *[Time estimate]* |

**Total Estimated Effort:** *[High-level estimate]*

### If Not Proceeding: What Alternative Should Be Explored

*Why shouldn't we proceed? What alternative should be explored instead?*

### Next Steps

- [ ] *[Next step 1]*
- [ ] *[Next step 2]*
- [ ] *[Next step 3]*

---

## Appendix

### Links to Repos, Branches, or Environments

- *[Repository or environment link]* - [Description]
- *[Repository or environment link]* - [Description]

### Raw Data or Detailed Logs

- *[Link to raw data or logs]* - [Description]
- *[Link to raw data or logs]* - [Description]

### References and Related Documentation

- *[Link/Reference]* - [Description]
- *[Link/Reference]* - [Description]

---
