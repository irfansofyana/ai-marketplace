---
name: git-commit
description: Creates git commits following Conventional Commits format with type/scope/subject. Use when user wants to commit changes, create commit, save work, or stage and commit. Always enforces semantic conventions regardless of project.
license: MIT
compatibility: Requires git, bash
metadata:
  author: irfansofyana
  version: "1.0.0"
  last-updated: "2025-12-24"
allowed-tools: Bash Read Grep Glob
---

# Git Commit

Creates git commits following Conventional Commits format with proper type, scope, and subject. This skill enforces semantic conventions for all commits.

## Quick Start

```bash
# 1. Stage changes
git add <files>  # or: git add -A

# 2. Create commit
git commit -m "type(scope): subject

Body explaining HOW and WHY."
```

## Commit Types

| Type | Purpose |
|------|---------|
| `feat` | New feature or functionality |
| `fix` | Bug fix or issue resolution |
| `refactor` | Code refactoring without behavior change |
| `perf` | Performance improvements |
| `test` | Test additions or modifications |
| `ci` | CI/CD configuration changes |
| `docs` | Documentation updates |
| `chore` | Maintenance, dependencies, tooling |
| `style` | Code formatting, linting (non-functional) |
| `security` | Security vulnerability fixes or hardening |

### Scope (Required, kebab-case)

Examples: `validation`, `auth`, `cookie-service`, `template`, `config`, `tests`, `api`

### Subject Line Rules

- Max 50 characters after colon
- Present tense imperative: add, implement, fix, improve, enhance, refactor, remove, prevent
- NO period at the end
- Specific and descriptive - state WHAT, not WHY

## Full Interactive Workflow

### 1. Review Changes

Always start by reviewing what changed:

```bash
git status
git diff           # unstaged changes
git diff --staged  # staged changes
```

### 2. Stage Files

Stage specific files or all changes:

```bash
git add <specific-files>  # preferred - selective staging
# or
git add -A  # all changes
```

**NEVER commit**:
- `.env`, `credentials.json`, secrets
- `node_modules/`, `__pycache__/`, `.venv/`
- Large binary files without explicit approval

### 3. Create Commit

**Simple change**:
```bash
git commit -m "fix(auth): use hmac.compare_digest for secure comparison"
```

**Complex change (with body)**:
```bash
git commit -m "$(cat <<'EOF'
feat(validation): add URLValidator with domain whitelist

Implement URLValidator class supporting:
- Domain whitelist enforcement (youtube.com, youtu.be)
- Dangerous scheme blocking (javascript, data, file)
- URL parsing with embedded credentials handling

Addresses Requirement 31: Input validation
Part of Task 5.1: Input Validation Utilities
EOF
)"
```

### 4. Verify Commit

```bash
git log -1 --format="%h %s"
git show --stat HEAD
```

## Body Format (Recommended for Complex Changes)

```
<blank line>
Explain HOW and WHY the change was made.
- Use bullet points for multiple items
- Wrap at 72 characters

Reference: Task X.Y
Addresses: Req N
```

## Breaking Changes

For incompatible API/behavior changes, use `!` after scope OR `BREAKING CHANGE:` footer:

```
feat(api)!: change response format to JSON:API

BREAKING CHANGE: Response envelope changed from `{ data }` to `{ data: { type, id, attributes } }`.
```

## Important Rules

- **ALWAYS** include scope in parentheses
- **ALWAYS** use present tense imperative verb
- **NEVER** end subject with period
- **NEVER** commit secrets or credentials
- **NEVER** use generic messages ("update code", "fix bug", "changes")
- **NEVER** exceed 50 chars in subject line
- **ALWAYS** use semantic convention - no project-specific overrides

## Examples

**Good**:
```
feat(validation): add URLValidator with domain whitelist
fix(auth): use hmac.compare_digest for secure key comparison
refactor(template): consolidate filename sanitization logic
test(security): add 102 path traversal prevention tests
```

**Bad**:
```
update validation code           # no type, no scope, vague
feat: add stuff                  # missing scope, too vague
fix(auth): fix bug               # circular, not specific
chore: make changes              # missing scope, vague
feat(security): improve things.  # has period, vague
```

## References

- `references/commit_examples.md` - Extended examples by type

---

This skill enforces Conventional Commits format for consistent, readable commit history across all projects.
