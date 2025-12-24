---
name: conventional-commits
description: Create git commits following Conventional Commits v1.0.0 specification. Auto-detects scopes from changed files, validates commit format, and prevents non-compliant commits. NO AI-generated footers added to commits for clean audit trails. Use when user wants to commit, push, or create git commits, or mentions "commit", "git commit", "push changes", "stage and commit", "make a commit", "create commit".
license: MIT
metadata:
  author: irfansofyana
  version: "1.0.0"
  last-updated: "2025-12-24"
allowed-tools: AskUserQuestion Bash Grep
---

# Conventional Commits Skill

Create git commits that follow the [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) specification. This skill replaces the built-in commit command to ensure clean, audit-friendly commit messages without any AI-generated footers.

## Core Principle

**CRITICAL**: Commit messages contain ONLY user-provided content. Never add footers like:
- "Generated with Claude Code"
- "Co-Authored-By: Claude <noreply@anthropic.com>"
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
- `fix(api)!: remove deprecated user endpoint` (breaking change)

## Workflow

### Phase 1: Pre-commit Analysis

**Step 1: Check for staged changes**

```bash
git status --porcelain
```

If nothing is staged (`git diff --cached --name-only` returns empty), ask the user to stage files first:

```
No files are staged for commit. Please stage the files you want to commit first:
- Use `git add <files>` to stage specific files
- Use `git add -p` to interactively stage hunks
- Use `git add -u` to stage all modified files
```

**Step 2: Get list of changed files**

```bash
git diff --cached --name-only
```

Save this list for scope auto-detection in Phase 3.

### Phase 2: Commit Type Selection

Use `AskUserQuestion` to present commit type options. Include descriptions for clarity:

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature for the user | `feat(auth): add OAuth2 support` |
| `fix` | Bug fix for the user | `fix(api): handle null response correctly` |
| `docs` | Documentation only changes | `docs: update README with setup instructions` |
| `style` | Code style changes (formatting, semicolons) | `style: format code with prettier` |
| `refactor` | Code change that neither fixes bug nor adds feature | `refactor(auth): extract validation logic` |
| `test` | Adding or updating tests | `test(api): add integration tests for users endpoint` |
| `chore` | Maintenance tasks, dependency updates | `chore: update dependencies to latest versions` |
| `perf` | Performance improvement | `perf(api): add caching for user queries` |
| `ci` | CI/CD changes | `ci: add automated tests to github actions` |
| `build` | Build system changes | `build: upgrade webpack to v5` |
| `revert` | Revert a previous commit | `revert: feat(api)!: remove oauth support` |

**Ask the user:**
```
What type of change is this commit?
```

Proceed to Phase 3 after user selects a type.

### Phase 3: Scope Suggestion & Confirmation

**Step 1: Auto-detect scope from changed files**

Analyze the file paths from Phase 1 to suggest a scope. Use the patterns from [references/scopes.md](references/scopes.md).

**Step 2: Present suggested scope**

```
Based on the changed files, I suggest the scope: "<suggested-scope>"

The suggested scope is derived from: <file-patterns>
```

**Step 3: User confirmation**

Use `AskUserQuestion`:
- Accept suggested scope
- Provide custom scope
- No scope (omit scope entirely)

**Important rules:**
- Scopes should be lowercase
- Use hyphens for multi-word scopes: `user-profile`, not `user_profile` or `userProfile`
- For `docs` type, scope is usually omitted (docs are typically project-wide)
- For `chore` type, scope is often omitted unless it's a specific subsystem

### Phase 4: Subject & Body Drafting

**Step 1: Subject line**

Ask for the commit subject. Validate it meets these criteria:
- Maximum 72 characters
- Use imperative mood ("add" not "added" or "adding")
- No period at the end
- Describes WHAT changed, not WHY

**Ask the user:**
```
Write a brief subject line for this commit (max 72 chars, imperative mood, no period):

Examples:
- "add rate limiting to API endpoints"
- "fix authentication token validation"
- "update installation documentation"
```

**Step 2: Body (optional)**

Ask if the user wants to add a body. The body should explain:
- WHAT was changed (more detail than subject)
- WHY the change was made
- NOT how it was implemented (code shows that)

```
Do you want to add a body to this commit? The body explains WHAT and WHY.

Example body:
"The previous implementation did not handle edge cases where users had
multiple active sessions. This could lead to race conditions during
concurrent requests."
```

**Step 3: Breaking change check**

Ask if this is a breaking change:

```
Is this a BREAKING CHANGE?
A breaking change is a commit that introduces a change that breaks
existing API contracts or requires users to update their code.

Examples:
- Removing or renaming a public API endpoint
- Changing the type or structure of a return value
- Modifying required configuration parameters
- Removing support for a previously supported feature
```

If breaking change:
- Add `!` after the type/scope: `feat(api)!: remove deprecated endpoint`
- OR add `BREAKING CHANGE:` footer in the body

### Phase 5: Pre-commit Validation

**Step 1: Validate the commit message format**

Verify the commit message matches this regex:
```
^(feat|fix|docs|style|refactor|test|chore|perf|ci|build|revert)(\(.+\))?!?: .+
```

**Validation checklist:**
- [ ] Type is one of: feat, fix, docs, style, refactor, test, chore, perf, ci, build, revert
- [ ] Scope (if present) is wrapped in parentheses
- [ ] Subject starts with a space after the colon
- [ ] Subject is in imperative mood
- [ ] Subject does NOT end with a period
- [ ] Subject is 72 characters or less
- [ ] If breaking change, `!` is present OR `BREAKING CHANGE:` footer is present

**Step 2: Show final commit message for confirmation**

```
Ready to commit. Here's the commit message:

---
<type>(<scope>): <subject>

<body>
<BREAKING CHANGE: footer if applicable>
---

Confirm? (yes/no)
```

Use `AskUserQuestion` for confirmation:
- Yes - proceed to commit
- No - go back and edit

### Phase 6: Execute Commit

**Execute the commit using bash:**

```bash
git commit -m "<type>(<scope>): <subject>" -m "<body>" -m "<footer>"
```

**CRITICAL**: The commit message must contain ONLY the user-provided content. No AI-generated footers.

**Confirmation:**
```
Commit created successfully!

Commit hash: <hash>
Branch: <branch>
Files changed: <count>
```

## When Scope Should Be Omitted

Omit the scope when:
1. The change affects multiple scopes and no single scope is appropriate
2. The change is project-wide (docs, chore, style often omit scope)
3. The scope would not provide meaningful context to readers

**Examples:**
- `docs: update README with new installation steps` (no scope)
- `chore: upgrade all dependencies to latest versions` (no scope)
- `style: format code with prettier` (no scope)

## Breaking Changes

There are two ways to indicate a breaking change:

**Option 1: Exclamation mark**
```
feat(api)!: remove deprecated user endpoint
```

**Option 2: BREAKING CHANGE footer**
```
feat(api): remove deprecated user endpoint

BREAKING CHANGE: The user endpoint has been removed. Use the new
profile endpoint instead.
```

**For breaking changes, always:**
- Clearly explain what broke
- Provide migration instructions if applicable
- Update version number accordingly (semantic versioning)

## Common Mistakes

### ❌ Wrong: Imperative mood not used
```
feat(api): added rate limiting
feat(api): adding rate limiting
```
### ✅ Correct: Imperative mood
```
feat(api): add rate limiting
```

### ❌ Wrong: Period at end of subject
```
feat(api): add rate limiting.
```
### ✅ Correct: No period
```
feat(api): add rate limiting
```

### ❌ Wrong: Subject too long (>72 chars)
```
feat(auth): implement comprehensive OAuth2 authentication flow with refresh token rotation and session management
```
### ✅ Correct: Concise subject
```
feat(auth): implement OAuth2 with refresh token rotation
```

### ❌ Wrong: Subject explains HOW instead of WHAT
```
fix(api): change the if statement to handle null values correctly
```
### ✅ Correct: Subject explains WHAT
```
fix(api): handle null responses
```

## Commit Message Examples

See [references/examples.md](references/examples.md) for comprehensive examples of good and bad commit messages.

## Commit Type Reference

See [references/commit-types.md](references/commit-types.md) for detailed explanations of each commit type with extensive examples.

## Scope Detection Reference

See [references/scopes.md](references/scopes.md) for configurable scope detection patterns for different project structures.

## Troubleshooting

**No staged changes:**
- Use `git add <files>` to stage files
- Use `git add -p` for interactive staging
- Use `git status` to see what files are available

**Commit rejected by pre-commit hook:**
- Fix the issue identified by the hook
- Re-run the commit workflow
- The skill does not bypass pre-commit hooks

**Scope detection not working:**
- The skill suggests a scope but you can always override it
- For projects with unique structures, you may need to manually specify scope each time
- Consider customizing scope patterns in your project documentation

## Integration

This skill replaces the built-in `/commit` command for creating commits with semantic conventions. To use this skill, simply ask to create a commit:

```
"Create a commit for these changes"
"Commit my staged changes"
"Make a conventional commit"
```

The skill will guide you through the process interactively.

## References

- [Conventional Commits v1.0.0 Specification](https://www.conventionalcommits.org/en/v1.0.0/)
- [Semantic Versioning](https://semver.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
