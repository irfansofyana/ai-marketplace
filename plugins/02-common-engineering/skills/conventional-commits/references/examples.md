# Commit Message Examples

This document provides examples of good and bad commit messages to help you write effective conventional commits.

## Good vs Bad Examples

### Example 1: Feature Addition

#### ❌ Bad
```
Added new feature for authentication

I added OAuth2 support which was requested by the team.
Users can now login with Google and GitHub.
The implementation took 3 days.
```

**Problems:**
- Subject not in imperative mood ("Added" instead of "Add")
- Subject ends with a period
- Subject doesn't describe what type of change
- Body includes irrelevant information (time taken)

#### ✅ Good
```
feat(auth): implement OAuth2 authentication

Users can now authenticate using OAuth2 providers (Google, GitHub).
The implementation supports access tokens and refresh token rotation.

Closes #123
```

**Why it's good:**
- Clear type (`feat`) and scope (`auth`)
- Imperative mood ("implement")
- No period at end of subject
- Body explains what was added and why
- Includes reference to related issue

---

### Example 2: Bug Fix

#### ❌ Bad
```
fixing the bug where the api crashes

changed the if statement to check for null
```

**Problems:**
- Subject not in imperative mood ("fixing" instead of "fix")
- Missing colon and space after type
- No scope
- Doesn't explain the impact of the bug

#### ✅ Good
```
fix(api): handle null response from user service

The application crashed when the user service returned null.
Added null check to prevent the crash and return a 404 response instead.

Fixes #456
```

**Why it's good:**
- Clear type (`fix`) and scope (`api`)
- Explains what the bug was
- Explains how it was fixed
- References the issue

---

### Example 3: Breaking Change

#### ❌ Bad
```
feat: remove user endpoint

This endpoint is no longer needed.
```

**Problems:**
- Doesn't indicate breaking change
- No `!` after type
- No `BREAKING CHANGE` footer
- Doesn't explain migration path

#### ✅ Good
```
feat(api)!: remove deprecated user endpoint

BREAKING CHANGE: The /users/:id endpoint has been removed.
Consumers should migrate to the /profile/:id endpoint instead.

Migration guide:
- Replace /users/:id with /profile/:id
- Update response parsing to use new schema
- See migration.md for detailed examples
```

**Why it's good:**
- Clear breaking change indicator (`!`)
- `BREAKING CHANGE` footer with details
- Includes migration instructions
- References migration guide

---

### Example 4: Documentation

#### ❌ Bad
```
docs(readme): updated the readme.md file with new stuff

- added new section
- fixed typos
- updated links
```

**Problems:**
- Subject is vague ("new stuff")
- Bullet points in subject (should be in body)
- Scope uses uppercase (should be lowercase)

#### ✅ Good
```
docs: update README with new installation steps

Added prerequisites for Node.js 18 and updated the installation
commands for the latest package manager versions. Also added
troubleshooting section for common setup issues.
```

**Why it's good:**
- No scope (docs are typically project-wide)
- Subject clearly states what changed
- Body provides specific details
- No list in subject line

---

## Real-World Examples

### Simple Feature
```
feat(api): add rate limiting endpoint

Added a new endpoint /api/rate-limits that allows administrators
to configure rate limiting rules for API consumers.
```

### Bug Fix with Context
```
fix(auth): prevent token reuse in concurrent requests

When multiple requests were made concurrently with the same
refresh token, the token could be refreshed multiple times
causing race conditions. Added a distributed lock to ensure
only one refresh can happen at a time per token.
```

### Refactoring
```
refactor(user): extract validation logic into shared module

The validation logic was duplicated across user creation and
update endpoints. Extracted it into a shared module to reduce
duplication and improve maintainability.
```

### Performance Improvement
```
perf(database): add composite index on user_email and status

Query performance for the user list endpoint was degrading
as the user count grew. Added a composite index to improve
query time from 500ms to 50ms.
```

### Breaking Change with Migration
```
feat(api)!: redesign user response format

BREAKING CHANGE: The user response format has changed to
match the new API design guidelines.

Old format:
{
  "id": "123",
  "name": "John",
  "email": "john@example.com"
}

New format:
{
  "userId": "123",
  "profile": {
    "fullName": "John Doe",
    "contactEmail": "john@example.com"
  }
}

Migration: Update client code to use new field names.
See api-migration.md for detailed examples.
```

### Documentation Update
```
docs(auth): add OAuth2 integration guide

Added step-by-step guide for integrating OAuth2 authentication
with common providers (Google, GitHub, Azure AD). Includes
code examples in JavaScript, Python, and Go.
```

### Dependency Update
```
chore: upgrade dependencies to latest versions

Updated all npm packages to their latest stable versions.
Notable updates:
- express: 4.18.0 → 4.19.0
- lodash: 4.17.21 → 4.17.21 (security patch)
- typescript: 5.0.0 → 5.3.0
```

### Test Addition
```
test(api): add integration tests for authentication endpoints

Added comprehensive integration tests for login, logout,
and token refresh endpoints. Covers success cases and
common error scenarios.
```

### CI/CD Change
```
ci: add automated security scanning to GitHub Actions

Added Snyk security scanning to the CI pipeline. The scan
runs on every pull request and blocks merges if high-severity
vulnerabilities are detected.
```

### Revert
```
revert: feat(api): add rate limiting endpoint

This reverts commit a1b2c3d. The rate limiting implementation
caused performance issues and needs to be redesigned before
being reintroduced.
```

---

## Anti-Patterns to Avoid

### Don't include "why" in the subject

#### ❌ Bad
```
fix(api): handle null to prevent crashes
```
The "to prevent crashes" part explains why, which belongs in the body.

#### ✅ Good
```
fix(api): handle null response

The application was crashing when the API returned null.
Added null check to return appropriate error response.
```

### Don't use conversational language

#### ❌ Bad
```
feat: I added a cool new feature for logging in
```

#### ✅ Good
```
feat(auth): implement OAuth2 authentication
```

### Don't combine multiple unrelated changes

#### ❌ Bad
```
fix: handle null responses and update dependencies
```
These are two separate changes and should be separate commits.

#### ✅ Good (Commit 1)
```
fix(api): handle null response from user service
```

#### ✅ Good (Commit 2)
```
chore: update dependencies to latest versions
```

### Don't include implementation details in subject

#### ❌ Bad
```
feat: add user endpoint using express router
```
The "using express router" part is implementation detail.

#### ✅ Good
```
feat(api): add user CRUD endpoints
```

---

## Checklist for Good Commits

Before committing, verify:

- [ ] Type is one of: feat, fix, docs, style, refactor, test, chore, perf, ci, build, revert
- [ ] Subject starts with type and optional scope: `type(scope):`
- [ ] Subject is in imperative mood ("add" not "added" or "adding")
- [ ] Subject does NOT end with a period
- [ ] Subject is 72 characters or less
- [ ] Body explains WHAT and WHY (not HOW)
- [ ] Breaking changes are marked with `!` or `BREAKING CHANGE:` footer
- [ ] Each commit is for one logical change
- [ ] No AI-generated footers included

---

## Subject Length Examples

### Too long (>72 chars)
```
feat(auth): implement comprehensive OAuth2 authentication flow with refresh token rotation and session management for all supported providers
```
(128 characters - way too long)

### Just right (≤72 chars)
```
feat(auth): implement OAuth2 with refresh token rotation
```
(55 characters - perfect)

### Also good (short but descriptive)
```
feat(auth): implement OAuth2 authentication
```
(42 characters - clear and concise)
