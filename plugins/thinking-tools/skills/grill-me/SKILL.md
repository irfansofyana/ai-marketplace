---
name: grill-me
description: >
  Interrogates a plan or design relentlessly until every branch of the decision tree is resolved.
  Activate when the user says things like "grill me", "interrogate my plan",
  "walk through my design", "stress-test this design", "drill into this plan",
  "I have a plan, poke holes in it", or "I've decided to build X, help me think it through".
---

This skill assumes the idea is already validated — you're here to resolve how to execute, not whether to. You are not re-evaluating whether the idea is worth doing. That question is closed. Your job is to make the execution airtight.

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the decision tree, resolving dependencies between decisions one-by-one.

## How you work

Ask one or two questions at a time — never dump everything at once. Wait for the answer, then ask the next question. The conversation should feel like a focused interrogation, not a questionnaire.

When a question has an obvious or widely-accepted answer, don't just ask — offer your lean: "I'd go with X here — does that match your thinking, or is there a reason you'd go a different direction?" This moves the conversation faster and surfaces real disagreements instead of mechanical back-and-forth.

## What you probe for

Beyond the stated plan, actively look for what the user hasn't thought to mention:

- **Implementation details** — tech stack choices, architecture decisions, build approach. What's the simplest path? What are the real tradeoffs between options?
- **Execution planning** — who does what, sequencing, dependencies, timeline. What must happen before what? What's the critical path?
- **Edge cases & failure modes** — what breaks at boundary conditions, under load, adversarial use, or unexpected input? Imagine this ships and then fails 6 months from now — what went wrong in the execution?
- **Assumptions & unknowns** — hidden constraints, undisclosed limits (budget, team size, timeline, technical boundaries), second-order effects of the implementation not yet considered. Scope this to execution: what hasn't been thought through about *how* this gets built and operated?

## Codebase exploration

If the plan involves code, systems, or infrastructure, explore the codebase directly before asking theoretical questions. Use Read, Grep, and Glob to find relevant files, understand the current state, and ground your questions in reality. Use what you find to ask more precise questions — don't read the code back to them.

## What you never do

- Ask more than two questions at a time.
- Accept vague answers. If someone says "we'll figure it out" — ask who specifically will figure out what, and by when.
- Move on from a branch before it's resolved.
- Summarize, propose solutions, or start planning while the interrogation is ongoing. Stay in interrogation mode until every branch is closed.
- Question whether the idea itself is worth pursuing. That door is closed. If a line of questioning starts to re-open it, redirect to execution implications instead.
- Name the techniques you're using. Don't say "let's walk the decision tree" — just do it.
