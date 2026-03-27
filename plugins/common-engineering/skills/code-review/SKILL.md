---
name: code-review
description: This skill should be used when the user asks to "review my code", "review this branch", "review my changes", "check my diff", "review before merge", "code review", or needs a structured code review analyzing correctness, security, maintainability, and scalability of git diff changes against a base branch. Use this proactively whenever the user is working on a feature branch and mentions wanting feedback on their changes before merging or opening a PR.
license: MIT
allowed-tools: AskUserQuestion Bash Read Glob Grep
---

# Code Review

Review code changes on the current branch against a base branch. Produce a structured report with findings classified by severity (Critical/Major/Minor/Nit) across four dimensions: correctness, security, maintainability, and scalability.

**This skill applies the Pareto principle (80/20 rule):** Focus on the ~20% of findings that catch ~80% of real issues. Don't try to be exhaustive — be precise. A review with 3 high-confidence findings that each describe a real harm scenario is far more valuable than 15 speculative observations. Prioritize depth on what matters over breadth across everything.

Everything comes from the codebase — git diffs and source files. Only ask the user about configuration (base branch, scope).

## Workflow

### 1. Get the diff

1. **Detect the base branch** using this priority order:
   - If the user specified a base branch, use that.
   - Run `git rev-parse --verify origin/main 2>/dev/null` — if it exists, use `origin/main`.
   - Run `git rev-parse --verify origin/master 2>/dev/null` — if it exists, use `origin/master`.
   - Run `git remote show origin 2>/dev/null | grep 'HEAD branch'` to detect the remote default branch, then use `origin/<that-branch>`.
   - If none of the above work (e.g., no remote, unusual setup), ask the user with `AskUserQuestion`.

   **Always diff against `origin/<branch>`** (not the local branch) to ensure you're comparing against the latest remote state, not a potentially stale local copy. Run `git fetch origin <branch>` first if needed.
2. Run `git diff <base>...HEAD --stat` for a summary, then `git diff <base>...HEAD` for the full diff.
3. Skip noise automatically — lockfiles (`package-lock.json`, `yarn.lock`, `go.sum`, etc.), generated code (`*.pb.go`, `*.min.js`, `dist/`, `build/`), binaries, and vendor dirs (`node_modules/`, `vendor/`). Log what was skipped. **Exception**: Always review dependency manifest files (`package.json`, `go.mod`, `Cargo.toml`, `pyproject.toml`, `requirements.txt`, `Gemfile`, `pom.xml`, `build.gradle`) — these are never skipped.
4. For large diffs (>30 files), triage automatically using the tiered reading strategy below. Only ask the user to scope if the diff is so large (>80 files) that even tiered reading won't produce a meaningful review.

### 2. Read context

Use `Glob` to detect the project type (`package.json`, `go.mod`, `Cargo.toml`, etc.) so you apply the right language-specific checks.

**Always apply tiered reading** — even for small diffs, not every file deserves the same depth. Use the `--stat` output and diff content to triage files into risk levels:

- **Deep read (full file):** Files that appear higher-risk based on signals in their path, imports, diff content, or change size. Use your judgment — security-sensitive paths, database-touching code, new endpoints, large rewrites, and new files with significant logic are typical candidates.
- **Medium read (diff hunks + ~50 lines surrounding context):** Standard business logic and service files where the diff hunks plus some surrounding context is enough to understand the change.
- **Light read (diff hunks only):** Tests, documentation, configuration, and UI components that rarely produce high-severity findings.

For small diffs (≤15 files), most files will naturally land in deep or medium. For large diffs, be more selective — deep-read only the highest-risk files and light-read the rest. The goal is to spend your context budget where it matters most. You don't need to be told exactly which files are high-risk — look at the filenames, the diff content, the change size, and the imports to make that call yourself. When in doubt, read more rather than less.

### 3. Analyze

Analyze files in proportion to their read tier — deep-read files get thorough multi-dimension analysis, medium-read files get focused analysis on what the diff reveals, light-read files only get flagged if something obviously wrong jumps out. Read `references/review-checklist.md` for detailed criteria. The checklist is a reference — not every item applies to every file.

**The confidence filter is the most important part of this skill.** For every potential finding, ask yourself: *can I describe a realistic scenario where this causes harm in 1-2 sentences?* If yes, include it with that scenario. If no, drop it — it's noise.

Why this matters: AI code reviews tend to produce ~80% noise. The value of this skill is in surfacing the findings that actually matter, not in cataloguing every imperfection. **Cap the total report at ~10 findings maximum** regardless of diff size. For a 5-file diff that might be 2-4 findings; for a 40-file diff it's still ~10, focused on the highest-severity issues across all files. A concise review gets read and acted on — a wall of 30+ findings gets ignored.

Additional confidence rules:
- If a finding depends on runtime behavior, state your assumption explicitly ("If `user.profile` can be null — likely, since profiles are created async — this will throw")
- If something is "possible but depends on context you can't see," lower it to Minor or drop it
- Respect established project patterns — if the codebase consistently does something, don't flag new code for following suit

### 4. Classify

| Severity | Meaning | Examples |
|----------|---------|----------|
| **Critical** | Blocks merge | Security vulns, data corruption, breaking API changes |
| **Major** | Fix before merge | Logic errors, missing error handling, perf regressions |
| **Minor** | Can defer | Non-critical optimizations, minor inconsistencies |
| **Nit** | Optional | Formatting, minor readability tweaks |

### 5. Generate the report

Use this exact structure:

```
# Code Review Report

**Branch:** [branch-name] **Base:** [base-branch] **Date:** [YYYY-MM-DD]
**Files Reviewed:** [N] | **Skipped:** [M] | **Diff:** +[X] / -[Y] lines

## Summary
[2-3 sentences. Lead with the most impactful finding.]

**Verdict:** [Ready to merge | Merge after fixes | Needs significant rework]

| Severity | Count |
|----------|-------|
| Critical | N |
| Major | N |
| Minor | N |
| Nit | N |

## Findings

### [CR-1] [Title]
- **File:** `path/to/file` (lines X-Y) | **Category:** Security
- **What:** [1-2 sentences]
- **Why it matters:** [The realistic harm scenario]
- **Suggestion:** [Concrete fix]

[Group by severity: Critical > Major > Minor > Nit. Use IDs: CR-N, MJ-N, MN-N, NT-N.
 Omit empty severity sections.]

## Files Reviewed
| File | Changes | Findings |
|------|---------|----------|
| `path` | +X / -Y | MJ-1, MN-1 or "Clean" |

## Dependency Changes
[Include this section whenever manifest files (package.json, go.mod, etc.) are in the diff. Omit if no dependency changes.]

| Package | Change | From | To | Risk |
|---------|--------|------|----|------|
| `example-lib` | Added | — | ^2.1.0 | Low — well-maintained, small footprint |
| `big-framework` | Major bump | 3.x | 4.0.0 | High — breaking changes, check migration guide |
| `unused-dep` | Removed | 1.5.0 | — | Low — no remaining imports |

## Skipped Files
| File | Reason |
|------|--------|
| `package-lock.json` | Lockfile |

## What went well
[1-3 genuine, specific things the author did well. Not generic praise.]
```

**Verdict rules** (mechanical, not subjective):
- No Critical and no Major = **Ready to merge**
- Has Major, no Critical = **Merge after fixes**
- Has any Critical = **Needs significant rework**

### What NOT to flag

These create noise and erode trust in the review:
- Style preferences (brace placement, tabs vs spaces) — leave these to linters
- Missing comments on clear code
- Import ordering
- Variable names that are "not ideal" but understandable
- Patterns the project already uses consistently
- Test file organization preferences

## Example

Here's what a good review looks like — notice how each finding has a concrete harm scenario:

---

# Code Review Report

**Branch:** feat/search-feature **Base:** main **Date:** 2026-03-20
**Files Reviewed:** 8 | **Skipped:** 4 | **Diff:** +847 / -23 lines

## Summary

The search feature has a critical SQL injection vulnerability in the query builder and an N+1 query pattern that will degrade at scale. Frontend implementation is solid.

**Verdict:** Needs significant rework

| Severity | Count |
|----------|-------|
| Critical | 1 |
| Major | 2 |
| Minor | 1 |

## Findings

### [CR-1] SQL injection via string interpolation in search query
- **File:** `src/services/search.ts` (lines 34-41) | **Category:** Security
- **What:** Query built with template literals: `` `SELECT * FROM products WHERE name LIKE '%${searchTerm}%'` ``. The `searchTerm` comes directly from the request query parameter.
- **Why it matters:** An attacker can inject `'; DROP TABLE products; --` as a search term. This is a public endpoint (no auth), so it's immediately exploitable.
- **Suggestion:** Use parameterized queries: `db.query('SELECT * FROM products WHERE name LIKE $1', [`%${searchTerm}%`])`.

### [MJ-1] N+1 query loading categories per search result
- **File:** `src/services/search.ts` (lines 52-58) | **Category:** Scalability
- **What:** Each search result calls `getCategoryById(result.category_id)` individually in a loop.
- **Why it matters:** With 50 results per page, this fires 51 DB queries per search. At 100 concurrent searches = 5,100 queries. Response time degrades from ~50ms to >2s.
- **Suggestion:** JOIN categories in the original query, or batch-fetch with `WHERE id IN (...)`.

### [MJ-2] Pagination returns duplicates at page boundaries
- **File:** `src/services/search.ts` (lines 44-48) | **Category:** Correctness
- **What:** `OFFSET/LIMIT` pagination without `ORDER BY`. The DB may return different row orders between requests.
- **Why it matters:** Users see duplicate items when paging, or miss items entirely. Worse when rows are inserted between requests.
- **Suggestion:** Add `ORDER BY id ASC`. Consider cursor-based pagination for deep offsets.

### [MN-1] Duplicated validation with inconsistent limits
- **File:** `src/components/SearchBar.tsx` (lines 22-28) and `src/services/search.ts` (lines 30-32) | **Category:** Maintainability
- **What:** Search term length validated in both frontend (100 char max) and backend (200 char max) with different limits.
- **Why it matters:** Frontend truncates at 100 but backend accepts up to 200 — confusing, and if rules change they need updating in two places.
- **Suggestion:** Backend validation is the security boundary. Align frontend limit or remove it.

## Files Reviewed
| File | Changes | Findings |
|------|---------|----------|
| `src/services/search.ts` | +186 / -0 | CR-1, MJ-1, MJ-2 |
| `src/components/SearchBar.tsx` | +89 / -3 | MN-1 |
| `src/routes/search.ts` | +24 / -0 | Clean |
| `src/components/SearchResults.tsx` | +156 / -0 | Clean |
| `src/components/SearchPagination.tsx` | +72 / -0 | Clean |
| `src/hooks/useSearch.ts` | +64 / -0 | Clean |
| `src/tests/search.test.ts` | +198 / -12 | Clean |
| `migrations/20260320_add_search.sql` | +18 / -0 | Clean |

## Skipped Files
| File | Reason |
|------|--------|
| `package-lock.json` | Lockfile |
| `generated/graphql-types.ts` | Generated |
| `public/images/search-icon.png` | Binary |
| `public/images/no-results.svg` | Binary |

## What went well
- **Error boundaries**: `SearchResults` gracefully handles API failures with user-friendly messages. The `useSearch` hook manages loading/error/empty states cleanly.
- **Migration quality**: The SQL migration adds indexes on `products.name`, which will help search performance.
- **Test coverage**: Tests cover search with results, empty results, pagination, and error scenarios.
