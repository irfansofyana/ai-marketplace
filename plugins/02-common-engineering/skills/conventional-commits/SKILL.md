---
name: conventional-commits
description: Create git commits following Conventional Commits v1.0.0 specification. Autonomous agent that analyzes changes, auto-detects type/scope, generates commit message, and only asks for final review. NO AI-generated footers for clean audit trails. Use when user wants to commit, push, or create git commits.
license: MIT
metadata:
  author: irfansofyana
  version: "2.0.0"
  last-updated: "2025-12-24"
allowed-tools: AskUserQuestion Bash Grep Read
---

# Conventional Commits Skill (Autonomous)

An autonomous agent that creates git commits following the [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) specification. The agent analyzes your changes, auto-detects the commit type and scope, generates a commit message, and only asks for your review before committing.

## Core Principle

**CRITICAL**: Commit messages contain ONLY user-approved content. Never add footers like:
- "Generated with Claude Code"
- "Co-Authored-By: Claude"
- Any other AI attribution

This ensures clean git history for audit processes and compliance requirements.

## Commit Format

```
<type>[optional scope][!]: <description>

[optional body]

[optional footer(s)]
```

**Examples:**
- `feat(api): add rate limiting endpoint`
- `fix(auth): prevent token reuse in concurrent requests`
- `docs: update installation guide with new prerequisites`
- `feat!: redesign authentication flow` (breaking change)

## Autonomous Workflow

### Phase 1: Gather Context (Autonomous)

**Step 1: Check for staged changes**

```bash
git diff --cached --name-only
```

If nothing is staged, inform the user:

```
No files are staged for commit. Please stage the files you want to commit:
- git add <files>     # Stage specific files
- git add -p          # Interactive staging
- git add -u          # Stage all modified files
```

**Step 2: Get the full diff for analysis**

```bash
git diff --cached
```

**Step 3: Get recent commit history for context**

```bash
git log --oneline -5
```

### Phase 2: Autonomous Analysis

Analyze the gathered context to determine:

1. **Commit Type** - Based on diff patterns
2. **Scope** - Based on file paths
3. **Subject** - Based on what changed
4. **Breaking Change** - Based on removal/signature patterns
5. **Body** - Optional, for complex changes

#### Commit Type Detection Rules

Analyze the diff content and file paths to determine the commit type:

| Priority | Condition | Type |
|----------|-----------|------|
| 1 | All changed files are `.md` files | `docs` |
| 2 | All changed files are test files (`*.test.*`, `*.spec.*`, `__tests__/*`) | `test` |
| 3 | All changed files are CI/workflow files (`.github/workflows/*`, `*.yml` in CI context) | `ci` |
| 4 | All changed files are Docker-related (`Dockerfile*`, `docker-compose*`) | `build` |
| 5 | Only `package.json`/`package-lock.json` with dependency changes | `chore` |
| 6 | Only whitespace/formatting changes (no logic changes) | `style` |
| 7 | Performance-related keywords in diff (`cache`, `optimize`, `performance`, `speed up`) | `perf` |
| 8 | Bug fix indicators in diff or context (`fix`, `bug`, `issue`, `error`, `crash`, `handle`) | `fix` |
| 9 | New functions/classes/components added | `feat` |
| 10 | Code restructuring without behavior change | `refactor` |
| 11 | Default fallback | `chore` |

#### Scope Detection Rules

Use file paths to determine scope (reference: [references/scopes.md](references/scopes.md)):

1. Extract the primary directory or component from changed files
2. Use the most specific common ancestor
3. Apply scope naming conventions:
   - Lowercase: `api`, not `API`
   - Hyphens for multi-word: `user-profile`, not `userProfile`
   - Short but descriptive: `auth`, not `authentication-service`

**Omit scope when:**
- Changes span multiple unrelated areas
- Type is `docs` (typically project-wide)
- Type is `chore` with project-wide changes
- Scope would not add meaningful context

#### Subject Generation Rules

Generate a concise subject line:

1. **Analyze the primary change** - What is the main thing being modified?
2. **Use imperative mood** - "add", "fix", "update" (not "added", "fixes", "updating")
3. **Keep under 72 characters**
4. **No period at the end**
5. **Focus on WHAT changed**, not HOW

**Subject patterns by type:**
- `feat`: "add [feature]", "implement [capability]", "support [functionality]"
- `fix`: "fix [issue]", "handle [edge case]", "prevent [problem]"
- `docs`: "update [document]", "add [documentation]", "clarify [section]"
- `refactor`: "extract [component]", "simplify [logic]", "reorganize [structure]"
- `test`: "add tests for [feature]", "increase coverage for [module]"
- `chore`: "update [dependency]", "configure [tool]", "clean up [area]"

#### Breaking Change Detection

Detect breaking changes by looking for:

1. **Removed exports** - `export` statements removed
2. **Removed public functions/methods** - Public API deletions
3. **Changed function signatures** - Parameters added/removed/reordered
4. **Removed configuration options** - Config keys deleted
5. **Major version bumps** - In package.json
6. **Renamed public APIs** - Function/class renames

If breaking change detected, add `!` after type/scope.

#### Body Generation (Optional)

Generate a body only when the change is complex:

- Multiple logical changes in one commit
- Non-obvious reasoning behind the change
- Important context for future readers

Keep the body concise and focused on WHAT and WHY, not HOW.

### Phase 3: User Review (Single Interaction)

Present the generated commit message for review:

```
Based on my analysis of your changes, here's the proposed commit:

---
<type>(<scope>): <subject>

<body if applicable>
---

Files changed:
- file1.ts
- file2.ts

Detected: <brief explanation of why this type/scope was chosen>
```

Use `AskUserQuestion` with options:
- **Commit** - Proceed with this message
- **Edit** - Let user provide modifications
- **Cancel** - Abort the commit

**If user chooses Edit:**
Ask what they want to change (type, scope, subject, or body) and incorporate their feedback. Then present the updated message for final confirmation.

### Phase 4: Execute Commit (Autonomous)

After user approval, execute the commit using one of these patterns:

#### Pattern 1: Simple commit (no body)

For commits with only type/scope and subject:

```bash
git commit -m "<type>(<scope>): <subject>"
```

#### Pattern 2: Commit with body

For commits with a body, use EITHER multiple `-m` flags OR a heredoc (not both):

**Option A: Multiple -m flags**
```bash
git commit -m "<type>(<scope>): <subject>" -m "<body>"
```

**Option B: Heredoc (for multi-line bodies)**
```bash
git commit -m "$(cat <<'EOF'
<type>(<scope>): <subject>

<body>
EOF
)"
```

**CRITICAL HEREDOC RULES:**
- The closing `EOF` must be on its own line
- `EOF` must be at the start of the line (no leading spaces)
- Do not add any text after the closing `EOF`
- The `$(cat <<'EOF'` pattern with single quotes prevents variable expansion

#### Pattern 3: Breaking change

For breaking changes, include `!` and a BREAKING CHANGE footer:

```bash
git commit -m "$(cat <<'EOF'
<type>(<scope>)!: <subject>

<body if applicable>

BREAKING CHANGE: <explanation>
EOF
)"
```

**CRITICAL**: The commit message must contain ONLY user-approved content. No AI-generated footers.

**Confirmation output:**

```
Commit created successfully!

Commit: <hash>
Branch: <branch>
Files: <count> changed
```

## Commit Type Reference

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature for the user | `feat(auth): add OAuth2 support` |
| `fix` | Bug fix for the user | `fix(api): handle null response` |
| `docs` | Documentation only changes | `docs: update README` |
| `style` | Code style changes (formatting) | `style: format with prettier` |
| `refactor` | Code restructuring | `refactor(auth): extract validator` |
| `test` | Adding or updating tests | `test(api): add user endpoint tests` |
| `chore` | Maintenance tasks | `chore: update dependencies` |
| `perf` | Performance improvement | `perf(api): add caching` |
| `ci` | CI/CD changes | `ci: add test workflow` |
| `build` | Build system changes | `build: upgrade webpack` |
| `revert` | Revert a previous commit | `revert: feat(api): remove endpoint` |

## Common Patterns

### New Feature Detection
```diff
+ export function newFeature() {
+   // implementation
+ }
```
Result: `feat(<scope>): add newFeature function`

### Bug Fix Detection
```diff
- if (value) {
+ if (value !== null && value !== undefined) {
    process(value);
  }
```
Result: `fix(<scope>): handle null/undefined values`

### Documentation Detection
```diff
# README.md
+ ## Installation
+ Run `npm install` to get started.
```
Result: `docs: add installation instructions`

### Refactoring Detection
```diff
- function validateUser(user) {
-   if (!user.email) return false;
-   if (!user.name) return false;
-   return true;
- }
+ function validateUser(user) {
+   return validateEmail(user.email) && validateName(user.name);
+ }
+ function validateEmail(email) { return !!email; }
+ function validateName(name) { return !!name; }
```
Result: `refactor(<scope>): extract validation functions`

## Breaking Changes

When a breaking change is detected:

```
feat(api)!: remove deprecated user endpoint

BREAKING CHANGE: The /api/v1/user endpoint has been removed.
Use /api/v2/users instead.
```

## Edge Cases

### Multiple File Types
When changes span different types (e.g., feature + tests):
- Prioritize the primary change (usually `feat` or `fix`)
- Tests accompanying a feature are part of `feat`

### Ambiguous Changes
When the type is unclear:
- Default to analyzing the intent from diff content
- Consider the most impactful change
- When truly ambiguous, include reasoning in the review for user to adjust

### Large Commits
For commits with many changes:
- Focus on the primary purpose
- Suggest splitting if changes are unrelated (but proceed if user confirms)

## References

- [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- [Commit Types Reference](references/commit-types.md)
- [Scope Detection Reference](references/scopes.md)
- [Examples Reference](references/examples.md)
