---
name: poc-experiment
description: This skill should be used when the user asks to "write a POC document", "document a proof of concept", "write a POC report", "document an experiment", "write an experiment report", "document technical evaluation results", "write a Go/No-Go recommendation", "capture POC findings", or needs to document hypothesis validation, technology evaluation, or feasibility study results with a clear Go/No-Go decision (3-8 pages).
license: MIT
metadata:
  author: irfansofyana
  version: "2.0.0"
  last-updated: "2026-03-18"
allowed-tools: AskUserQuestion Bash Read
---

# POC/Experiment Skill

Create Proof of Concept and Experiment documents (3-8 pages) that capture hypothesis validation, technology evaluations, or feasibility studies — culminating in a clear Go/No-Go recommendation backed by evidence.

**Key principle**: All information comes from the user. Do NOT scan the codebase. The `Read` tool is only for reading user-provided context files that the user explicitly shares.

## When to Use a POC/Experiment Document

- Validating a technical hypothesis before committing to full implementation
- Evaluating a new technology or framework for adoption
- Assessing feasibility of an uncertain approach
- Documenting the results of a time-boxed technical spike
- Capturing evidence for a Go/No-Go decision on a risky approach

## Workflow

### Phase 1: Gather Context

Parse what the user already provided. Determine whether the POC is:
- **Planned** (writing before conducting): Help define hypothesis, success criteria, and approach
- **Completed** (documenting results): Capture findings and formulate recommendation

**Only ask for what's genuinely missing.**

**Essential questions** (use `references/question-bank.md` patterns, ask only if not already provided):

1. **Hypothesis**: "What specific hypothesis are you testing? (e.g., 'We believe X can achieve Y performance under Z conditions')"
2. **Motivation**: "What problem or decision is this POC trying to resolve?"
3. **Approach**: "How did you (or will you) conduct the experiment? What did you build or test?"
4. **Success criteria**: "How do you define success? What results would lead to Go vs No-Go?"
5. **Results/Findings** (if completed): "What did you find? Share key metrics, observations, or outcomes."
6. **Limitations**: "What are the limitations of this POC? What did it NOT test?"
7. **Recommendation**: "Based on the findings, what's your recommendation: Go, No-Go, or needs more investigation?"
8. **Next steps**: "If Go, what's the path to production? If No-Go, what alternatives exist?"
9. **Related context** (optional): "Any existing ADRs, RFCs, or tickets this informs?"

**If the user is planning (not yet run) the POC**: Focus on defining a rigorous hypothesis and measurable success criteria before the experiment begins.

**If user needs research on technology options**: Offer `agent:web-research-specialist` before or during the context gathering phase.

**Rich context** (accept at any point):
- Benchmark results or logs → use `Read` tool or accept pasted data
- Experiment code → capture key findings without scanning codebase
- Performance charts → incorporate key numbers into narrative

### Phase 2: Generate & Iterate

Once sufficient context is gathered, generate the **complete POC/Experiment document** using the template from `assets/templates/template.md`.

**Content generation rules:**
- Use section headings from `template.md` exactly
- The **Go/No-Go Decision** section is MANDATORY — be explicit and unambiguous
- Support the recommendation with concrete evidence from the findings
- Document limitations honestly — a POC that overstates its conclusions is dangerous
- Use tables or lists for metrics and comparative results
- Do NOT include checkboxes, HTML comments, guidance questions, or quality criteria in output

**After presenting the full draft:**
1. Internally validate against `assets/templates/quality-checklist.md` — never show to user
2. Check that the recommendation is backed by the findings
3. Ensure limitations are clearly stated
4. Iterate based on feedback
5. Save in requested format

## Document Structure

Key sections (from `assets/templates/template.md`):

| Section | Purpose |
|---------|---------|
| Executive Summary | TL;DR of hypothesis, approach, and Go/No-Go |
| Problem Statement | What prompted the POC, current pain, success criteria |
| Approach & Solution Design | How the experiment was designed and conducted |
| Implementation Details | What was built, technologies used, time-boxed scope |
| Results & Findings | Quantitative and qualitative outcomes |
| Trade-offs & Limitations | What the POC does NOT prove, scope constraints |
| Recommendation & Next Steps | **MANDATORY** Go/No-Go decision with rationale |
| Appendix | Raw data, code snippets, detailed logs |

## Quality Principles

- **Go/No-Go must be explicit** — "maybe" or "it depends" without further qualification is not a recommendation
- Results must be supported by evidence — don't let subjective impressions outweigh data
- Limitations must be honest — future readers will use this to make real decisions
- Success criteria should have been defined before the POC (if planning), or explicitly stated before results
- A No-Go with clear learnings is more valuable than an inconclusive Go

## Visual Aids

Graphs, comparison tables, and architecture diagrams strengthen POC documents. When requested:
1. Ask what the diagram should show (test setup, performance comparison, architecture)
2. Invoke `common-engineering:mermaid` skill for flowcharts and diagrams
3. For data charts, format results as tables in markdown

## Integration Points

| Capability | When to Use |
|-----------|-------------|
| `agent:web-research-specialist` | Research technology options, find comparable benchmarks |
| `common-engineering:mermaid` | Experiment setup diagrams, architecture comparisons |
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
