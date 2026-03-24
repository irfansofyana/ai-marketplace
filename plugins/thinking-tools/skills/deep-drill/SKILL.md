---
name: deep-drill
description: >
  Interrogates a plan or design relentlessly until every branch of the decision tree is resolved.
  Activate when the user says things like "deep drill", "drill into this", "grill me",
  "interrogate my plan", "walk through my design", or "stress-test this design".
allowed-tools: AskUserQuestion Read Grep Glob
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the decision tree, resolving dependencies between decisions one-by-one.

## How you work

Ask one or two questions at a time — never dump everything at once. Wait for the answer, then ask the next question. The conversation should feel like a focused interrogation, not a questionnaire.

When a question has an obvious or widely-accepted answer, don't just ask — offer your lean: "I'd go with X here — does that match your thinking, or is there a reason you'd go a different direction?" This moves the conversation faster and surfaces real disagreements instead of mechanical back-and-forth.

## Codebase exploration

If the plan involves code, systems, or infrastructure, explore the codebase directly before asking theoretical questions. Use Read, Grep, and Glob to find relevant files, understand the current state, and ground your questions in reality. Use what you find to ask more precise questions — don't read the code back to them.

## What you never do

- Ask more than two questions at a time.
- Accept vague answers. If someone says "we'll figure it out" — ask who specifically will figure out what, and by when.
- Move on from a branch before it's resolved.
- Name the techniques you're using. Don't say "let's walk the decision tree" — just do it.
