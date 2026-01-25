---
name: project-management-plan
description: >-
  Generate project management plan Excel workbooks (.xlsx) with automated Gantt charts,
  team charters, budget tracking, and RAID logs. Use when users request a "project management plan",
  "PM plan", "program plan", "project tracker", "project plan excel", "project plan spreadsheet",
  or need to create a structured project planning workbook. Follows an interactive 3-phase workflow:
  brainstorm with the user, get plan approval, then generate the workbook.
license: MIT
metadata:
  author: irfansofyana
  version: "1.0.0"
  last-updated: "2026-01-25"
allowed-tools: AskUserQuestion Bash Read Write
---

# Project Management Plan Generator

Generate professional project management plan Excel workbooks through an interactive, AI-assisted workflow. The skill brainstorms with the user, proposes task breakdowns, iterates on the plan, and produces a polished `.xlsx` file with 4 tabs: Main Program Plan (with Gantt chart), Charters, Budget, and RAID Logs.

**Key principle**: This is a collaborative workflow. The AI proposes, the user approves, and only then does generation happen. Never generate the workbook without explicit user approval.

## Workflow Overview

This skill follows a **3-phase collaborative workflow**:

| Phase | Purpose | Gate |
|-------|---------|------|
| **Phase 1: Discovery & Brainstorming** | Understand the project, propose breakdown | Must complete before Phase 2 |
| **Phase 2: Approval & Refinement** | User reviews, modifies, approves | Must get explicit approval before Phase 3 |
| **Phase 3: Generation & Delivery** | Build JSON, generate Excel, deliver | Only after user says "looks good" / approves |

> **CRITICAL**: Do NOT skip to Phase 3 without completing Phases 1 and 2. The user MUST explicitly approve the plan before generation.

## Phase 1: Discovery & Brainstorming

**Goal**: Understand the project context and propose a comprehensive plan.

### Step 1: Gather Project Context

Ask the user these questions (use `AskUserQuestion` where appropriate):

1. **Project Name**: "What is the name of this project?"
2. **High-Level Goals**: "What are the main goals or deliverables for this project?"
3. **Timeline**: "What is the approximate start date and end date?"
4. **Team Size/Structure**: "Who are the key people or teams involved? (e.g., engineering, design, QA, PM)"
5. **Key Constraints**: "Are there any important deadlines, dependencies, or constraints?"

Optional follow-ups based on context:
- "Is there an existing JIRA board or project tracker I should know about?"
- "What is the approximate budget range? Any specific budget categories to track?"
- "Are there known risks or blockers?"

### Step 2: AI-Proposed Breakdown

Based on the user's answers, **propose a complete project plan** including:

1. **Milestones & Tasks**: Break down the project into milestones with specific tasks, suggested workstreams, PICs (persons in charge), and estimated timelines (start/due dates)
2. **Team Charter**: Map core team roles to the people mentioned
3. **Budget Categories**: Suggest relevant budget line items based on the project type
4. **RAID Items**: Identify potential risks, assumptions, issues, and dependencies

**Present the proposal in a clear, readable format** (use markdown tables). Example:

```
### Proposed Task Breakdown

| # | Milestone | Task | Workstream | PIC | Start | Due |
|---|-----------|------|------------|-----|-------|-----|
| 1 | Phase 1 - Discovery | Requirements gathering | Product | Alice | 2025-01-06 | 2025-01-17 |
| 2 | Phase 1 - Discovery | Technical architecture | Engineering | Bob | 2025-01-06 | 2025-01-17 |
| ... | ... | ... | ... | ... | ... | ... |

### Proposed Team Charter

| Core Team | PICs |
|-----------|------|
| Program Sponsor | [name] |
| Engineering Leads | Bob, Carol |
| ... | ... |

### Proposed Budget

| Category | Owner | Amount | Currency |
|----------|-------|--------|----------|
| Infrastructure | DevOps | 0 | IDR |
| ... | ... | ... | ... |

### Identified RAID Items

| Category | Description | Impact |
|----------|-------------|--------|
| Risk | Third-party API dependency | High |
| ... | ... | ... |
```

Then ask: **"Please review the proposed plan above. You can approve it, or let me know what to modify, add, or remove."**

## Phase 2: Approval & Refinement

**Goal**: Iterate until the user is satisfied with the plan.

### Refinement Loop

The user may:
- **Approve**: "Looks good", "Approve", "Let's generate it" → proceed to Phase 3
- **Modify tasks**: "Change task 3 to...", "Move the deadline for..." → update and re-present
- **Add items**: "Add a task for...", "Include a risk about..." → add and re-present
- **Remove items**: "Remove task 5", "We don't need the QA milestone" → remove and re-present
- **Change structure**: "Split Phase 1 into two milestones", "Merge these tasks" → restructure and re-present

**Rules:**
- After each modification, present the updated plan clearly
- Always ask for confirmation after changes: "Here's the updated plan. Ready to generate, or any more changes?"
- Do NOT proceed to Phase 3 until the user explicitly approves
- Keep track of all approved items across categories (tasks, charters, budget, RAID)

## Phase 3: Generation & Delivery

**Goal**: Generate the Excel workbook from the approved plan.

### Step 1: Build JSON Configuration

Construct a JSON configuration file from the approved plan following this schema:

```json
{
  "project_name": "Project Alpha",
  "start_date": "2025-01-06",
  "end_date": "2025-03-31",
  "output_path": "./project-plan.xlsx",
  "tasks": [
    {
      "no": 1,
      "milestone": "Phase 1",
      "task": "Requirements gathering",
      "workstream": "Product",
      "pic": "Alice",
      "status": "Not Started",
      "start_date": "2025-01-06",
      "due_date": "2025-01-17",
      "jira_link": "",
      "remarks": ""
    }
  ],
  "charters": {
    "program_sponsor": "",
    "business": "",
    "product_design": "",
    "tpm": "",
    "pmo": "",
    "ba": "",
    "engineering_leads": "",
    "qa": ""
  },
  "budget": [
    {
      "category": "Infrastructure",
      "owner": "DevOps",
      "amount": 0,
      "currency": "IDR",
      "notes": ""
    }
  ],
  "raid": [
    {
      "no": 1,
      "category": "Risk",
      "description": "Third-party API dependency",
      "impact": "High",
      "status": "Open",
      "pic": "Bob",
      "action_items": "Evaluate fallback options"
    }
  ]
}
```

**Field notes:**
- `start_date` / `end_date`: Project-level dates (YYYY-MM-DD). Used to calculate Gantt chart range. If omitted, derived from task dates.
- `output_path`: Where to save the file. Default: `./project-plan.xlsx`
- `tasks[].status`: One of "Not Started", "In Progress", "Completed", "Blocked", "On Hold"
- `budget[].amount`: Numeric value. Set to 0 if unknown.
- `raid[].category`: One of "Risk", "Assumption", "Issue", "Dependency"
- `raid[].impact`: One of "High", "Medium", "Low"

### Step 2: Write JSON and Generate Workbook

1. Write the JSON config to a temporary file
2. Run the generation script:

```bash
python3 "${SKILL_PATH}/scripts/generate_pm_plan.py" /path/to/config.json
```

Where `${SKILL_PATH}` is the directory containing this SKILL.md file. To find it:
- Read this SKILL.md's own path from the skill invocation context
- The scripts directory is at the same level: `scripts/generate_pm_plan.py`

### Step 3: Verify the Output

After generation:
1. Confirm the file was created successfully
2. Report the file location to the user
3. Summarize what was generated:
   - Number of tasks in Main Program Plan
   - Gantt chart date range
   - Number of charter roles filled
   - Number of budget items
   - Number of RAID log entries

### Step 4: Optional Formula Recalculation

If the xlsx skill's recalc utility is available, run it to verify formulas:

```bash
python3 /Users/irfanputra/.claude/plugins/cache/anthropic-agent-skills/document-skills/69c0b1a06741/skills/xlsx/recalc.py /path/to/output.xlsx
```

This step is optional — the workbook is fully functional without it. Skip if recalc.py is not found.

## Workbook Structure Reference

### Tab 1: Main Program Plan
- **Row 1**: Project name (merged, large font)
- **Row 2**: Column headers (No, Milestone, Task Item, Workstream, PIC, Status, Start Date, Due Date, JIRA Link, Remarks)
- **Row 3+**: Task data (pre-filled from approved plan, 30 rows minimum for template use)
- **Status column**: Dropdown validation (Not Started / In Progress / Completed / Blocked / On Hold)
- **Gantt chart** (Column K onward): Weekly intervals with conditional formatting that auto-fills when a task's date range overlaps the week. Updates automatically when Start Date or Due Date cells are modified.
- **Freeze panes**: Column A-B and Row 1-2 frozen

### Tab 2: Charters
- **Row 1**: Project name + "Team Charter"
- **Row 2**: Headers (Core Team, PICs)
- **Row 3+**: Roles: Program Sponsor, Business, Product & Design, TPM, PMO, BA, Engineering Leads, QA

### Tab 3: Budget
- **Row 1**: Project name + "Budget"
- **Row 2**: Headers (Budget Category, Budget Owner, Amount, Currency, Notes)
- **Row 3+**: Budget line items
- **Total row**: SUM formula for Amount column

### Tab 4: RAID Logs
- **Row 1**: Project name + "RAID Logs"
- **Row 2**: Headers (No, Category, Description, Impact, Status, PIC, Action Items)
- **Row 3+**: RAID entries (20 rows minimum for template use)
- **Dropdowns**: Category (Risk/Assumption/Issue/Dependency), Impact (High/Medium/Low), Status (Open/Mitigated/Closed)

## Dependencies

- **Python 3** with `openpyxl` library (`pip install openpyxl`)
- **Optional**: LibreOffice (for formula recalculation via recalc.py)

## Error Handling

- If `openpyxl` is not installed, the script exits with a clear error message and install instructions
- If the output directory doesn't exist, it is created automatically
- If no tasks are provided, 30 empty template rows are generated
- If no budget items are provided, default Infrastructure and Vendor rows are created
- If project start/end dates are missing, they are derived from the earliest/latest task dates
