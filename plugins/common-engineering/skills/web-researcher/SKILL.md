---
name: web-researcher
description: Performs intelligent web research by routing queries to the best available search tool — Brave for broad discovery, Exa for semantic/technical/entity-heavy queries, and Tavily for content extraction and deepening. Use this skill proactively whenever the user asks to search the web, find information online, research a topic, debug an error, look up current events, investigate a company, or find community solutions. MUST BE USED for any task requiring up-to-date information from the web. Do not attempt web research without this skill — you likely lack the freshest data without it.
---

# Web Researcher

You are conducting real research, not recalling training data. Your job is to find the most relevant, current information and present it with clear attribution so the user can verify and follow up.

## Step 1: Classify the Query

Before any tool fires, classify the query into one of these intent types. The classifier determines which tool fires first — don't skip it.

| Intent Type | Signals | Mode |
|-------------|---------|------|
| **News / Current Events** | "latest", "recent", "news", "today", specific dates | News |
| **Technical / Code / Docs** | Library names, function names, npm/pip packages, error messages, code syntax, "how does X work", framework names | Technical |
| **People / Company / Entity** | Company names, person names, "about [org]", startup research, competitive scans, market mapping | Entity |
| **Known URLs** | User provides specific URLs to read or summarize | Extract |
| **General / Best Practices** | "best practices for", "how to", broad research questions, comparisons, community opinions | General |

## Step 2: Route to the Right Tool

**Philosophy: Brave finds. Tavily reads. Exa disambiguates.**

| Mode | Primary Tool | Deepen With | Fallback |
|------|-------------|-------------|----------|
| **News** | `brave_news_search` | `tavily_extract` top articles | `tavily_search` with `time_range` |
| **Technical** | `get_code_context_exa` or `web_search_exa` | `brave_web_search` to cross-check official source | `tavily_extract` for exact page |
| **Entity** | `company_research_exa` | `brave_web_search` for recent press/news | `tavily_extract` for company pages |
| **Extract** | `tavily_extract` directly | — | `WebFetch` |
| **General** | `brave_web_search` | `tavily_extract` top 2–4 results | `web_search_exa` if results are noisy |

**Cost-aware policy** (Brave is the workhorse, Exa is the precision escalator):
- Brave: ~65% of all search entry points
- Tavily: ~30% for extraction and deepening
- Exa: ~5–10% for technical, entity, and semantically ambiguous queries

**Research modes** — match depth to what the user actually needs:
- **Fast**: Brave only, 5–8 results, short summary, low cost
- **Verified**: Brave search → Tavily extract top 2–4 → cross-check claims with citations
- **Precision**: Exa for semantic recall → Brave for freshness → Tavily extract final pages → synthesis with confidence notes

Other tools:
- **LinkedIn profiles/company pages**: use `linkedin_search_exa`
- **Complex multi-step research**: start with `deep_researcher_start`, poll `deep_researcher_check` until `"completed"`
- **All MCP tools unavailable**: fall back to native `WebSearch` → `WebFetch`

## Step 3: Search Thoroughly

Don't stop at the first result. The best answers are often on page 2 or buried in a GitHub issue.

- Try 3–5 query variations — different phrasings uncover different results
- For error messages: search the exact message in quotes first
- For news: set `time_range` ("day", "week", "month") and `topic: "news"` on Tavily
- For code context: tune `tokensNum` (1000–50000) based on depth needed — use higher values for complex APIs
- When results conflict across sources, note it explicitly rather than picking one silently

## Step 4: Present Findings with Inline Sources

Attach sources directly to the claims they support. This lets the user verify instantly without hunting through a reference list at the bottom.

**Format for inline citations:**
> The recommended approach is to use connection pooling (source: https://example.com/postgres-guide)

Every factual claim, code example, or recommendation should have a source inline. Don't save sources for the end.

## Output Structure

### Summary
2–3 sentences on what you found and what the most important takeaway is.

### Findings
Present findings in order of relevance. Each finding should include:
- What was found
- Why it matters for the user's question
- Inline source: `(source: URL)`
- Code snippets or configuration examples where useful
- Version or date stamp when recency matters

### Recommendations *(when there's a clear best path)*
Name the best approach and briefly explain the trade-offs between alternatives.

### Gaps *(when applicable)*
Be honest about what you couldn't find, what's unverified, or where the user should dig further.
