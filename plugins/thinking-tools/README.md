# thinking-tools

Thinking tools for pressure-testing ideas and sharpening decisions before you commit to them.

## Which tool to use?

| Question | Skill |
|---|---|
| Should I pursue this idea at all? | idea-refinery |
| What decisions must be resolved before I commit or execute? | decision-sparring |

Natural order: run **idea-refinery** first to validate the idea and produce an Idea Brief, then run **decision-sparring** to resolve the remaining decision branches.

## Skills

### idea-refinery

A sparring partner that challenges your raw ideas through natural conversation, then produces a concise **Idea Brief**.

**Trigger phrases:**
- "pressure-test my idea"
- "idea refinery"
- "sparring partner"
- "challenge this idea"
- "gut-check this idea"
- "I have an idea"
- "is this worth doing"
- "should I pursue this"
- "help me decide"

**What it does:**

1. You share a raw idea — any format, any length
2. The agent asks sharp questions one or two at a time, probing:
   - Is this solving the real problem, or a symptom?
   - Who *specifically* has this problem?
   - What assumptions would break the idea if false?
   - What kills this 9 months from now?
   - What's the smallest version that still has value?
3. Once the idea has been genuinely challenged, the agent produces an **Idea Brief**

**Idea Brief structure:**

| Section | What it contains |
|---------|-----------------|
| **Idea** | One sentence — if it can't be said in one sentence, it's not sharp enough |
| **Problem** | Who specifically has it and why it matters |
| **Success looks like** | 1-2 measurable outcomes you'd actually observe |
| **MVP** | What's in v1 and what's explicitly out |
| **Biggest risk** | The single most likely thing to kill this |
| **Next 3 actions** | Concrete P0/P1/P2 steps |

**Scope:** Viability only — problem-fit, assumptions, risks, and whether this is worth doing. Implementation details are out of scope; that's what decision-sparring is for.

**Works for any kind of idea:** product features, technical decisions, process changes, org changes, personal projects.

### decision-sparring

A direct sparring partner that drills into every branch of an idea or plan until nothing important is unresolved. Probes for hidden assumptions, failure modes, tradeoffs, and constraints the user has not stated.

**Trigger phrases:**
- "decision sparring"
- "spar with this decision"
- "interrogate my plan"
- "walk through my design"
- "stress-test this decision"
- "drill into this plan"
- "I have a plan, poke holes in it"
- "I've decided to build X, help me think it through"

**What it does:**

1. You share a plan — any type, any format
2. The agent asks sharp questions one at a time, walking every branch of the decision tree and resolving dependencies one-by-one
3. When a question has an obvious answer, it offers its lean: "I'd go with X here — does that match your thinking?"
4. Probes for what you haven't thought to mention: undisclosed constraints, hidden assumptions, overlooked stakeholders, failure modes, and second-order effects of the implementation
5. If the plan involves code or systems, it can explore the codebase to ground its questions in reality

**Scope:** Viability and execution — useful when a decision still has unresolved branches, whether they are about pursuing the idea, sequencing the work, handling edge cases, or committing to concrete next steps.

**Works for:** technical architecture, product plans, process changes, any decision with multiple moving parts.

## Installation

```bash
/plugin install thinking-tools@ai-marketplace
```

No API keys or external dependencies required.
