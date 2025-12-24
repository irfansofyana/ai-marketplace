# Commit Types Reference

This document provides detailed explanations of each Conventional Commits type with examples and usage guidelines.

## feat: New Feature

Introduces a new feature to the application. A `feat` commit represents a user-facing change that adds new functionality.

### When to use
- Adding a new API endpoint
- Implementing a new user interface component
- Adding support for a new feature flag
- Introducing new configuration options

### Examples

```
feat(api): add rate limiting endpoint

Added a new endpoint that allows administrators to configure
rate limiting rules for API consumers.
```

```
feat(auth): implement OAuth2 authentication

Users can now authenticate using OAuth2 providers (Google, GitHub).
The implementation supports access tokens and refresh token rotation.
```

```
feat(ui)!: redesign navigation menu

BREAKING CHANGE: The navigation menu API has changed. Components
importing NavigationMenu will need to update their props.

The new design includes:
- Collapsible sidebar
- Breadcrumb navigation
- Quick search
```

### Common mistakes
- ❌ Using for internal refactorings (use `refactor` instead)
- ❌ Using for bug fixes (use `fix` instead)
- ❌ Not marking breaking changes with `!`

---

## fix: Bug Fix

Fixes a bug in the codebase. A `fix` commit represents a change that addresses incorrect behavior.

### When to use
- Fixing a crash or error
- Correcting incorrect output
- Fixing edge cases
- Resolving security vulnerabilities

### Examples

```
fix(api): handle null response from user service

The application crashed when the user service returned null.
Added null check to prevent the crash.
```

```
fix(auth): prevent token reuse in concurrent requests

When multiple requests were made concurrently with the same token,
the token could be refreshed multiple times causing race conditions.
Added a lock mechanism to prevent this.
```

```
fix(database): resolve connection leak in retry logic

The retry logic was not properly closing connections on failure.
Fixed by using a connection pool with proper cleanup.
```

### Common mistakes
- ❌ Using for new features (use `feat` instead)
- ❌ Not explaining the impact of the bug
- ❌ Not explaining how the fix works

---

## docs: Documentation Only

Changes to documentation only. No code functionality is changed.

### When to use
- Updating README files
- Adding or modifying inline code comments
- Updating API documentation
- Adding contributing guidelines

### Examples

```
docs: update README with new installation steps

Added prerequisites for Node.js 18 and updated the installation
commands for the latest package manager versions.
```

```
docs(api): add authentication documentation

Documented the OAuth2 flow with code examples for common
programming languages.
```

```
docs: fix typo in contributing guide

Corrected the email address for submitting pull requests.
```

### Common mistakes
- ❌ Including code changes (use a separate commit or combine with another type)
- ❌ Using for refactoring (use `refactor` instead)

---

## style: Code Style Changes

Changes that don't affect the meaning of the code (white-space, formatting, missing semi-colons, etc).

### When to use
- Running code formatters (prettier, black, gofmt)
- Fixing linting errors
- Reordering imports
- Changing indentation

### Examples

```
style: format code with prettier

Ran prettier on all JavaScript files to ensure consistent formatting.
```

```
style: sort imports alphabetically

Organized imports according to the project's style guide.
```

```
style(docs): fix trailing whitespace in comments

Cleaned up trailing whitespace in inline documentation.
```

### Common mistakes
- ❌ Including logic changes (separate the formatting from logic changes)
- ❌ Using for refactoring (use `refactor` instead)

---

## refactor: Code Refactoring

A code change that neither fixes a bug nor adds a feature. The code is changed to improve structure, readability, or performance while maintaining the same behavior.

### When to use
- Extracting functions or classes
- Renaming variables for clarity
- Reorganizing code structure
- Simplifying complex logic
- Removing duplicated code

### Examples

```
refactor(auth): extract validation logic into separate module

The validation logic was duplicated across multiple files.
Extracted it into a shared module to improve maintainability.
```

```
refactor(api): replace callback pattern with async/await

Modernized the codebase by replacing callback-based code with
async/await for improved readability.
```

```
refactor(ui): simplify state management

Reduced the complexity of the state management by consolidating
redundant state objects.
```

### Common mistakes
- ❌ Changing behavior (use `feat` or `fix` instead)
- ❌ Not being clear about what was refactored and why

---

## test: Adding or Updating Tests

Adding or updating tests. No production code is changed.

### When to use
- Adding new unit tests
- Adding integration tests
- Updating test fixtures
- Increasing test coverage

### Examples

```
test(api): add integration tests for user endpoints

Added tests for create, read, update, and delete operations on the
user API endpoints.
```

```
test(auth): increase coverage for token validation

Added edge case tests for expired tokens and malformed tokens.
```

```
test: fix failing tests after API changes

Updated test assertions to match the new API response format.
```

### Common mistakes
- ❌ Including production code changes (use a separate commit)
- ❌ Using for bug fixes (use `fix` instead)

---

## chore: Maintenance Tasks

Routine tasks that don't fit into other categories. Typically maintenance or dependency updates.

### When to use
- Updating dependencies
- Adding build configuration
- Updating tooling
- Adding or updating CI/CD scripts (use `ci` for that)

### Examples

```
chore: update dependencies to latest versions

Updated all npm packages to their latest stable versions.
```

```
chore: add .editorconfig file

Added editor configuration to ensure consistent formatting
across different editors.
```

```
chore: upgrade to TypeScript 5.0

Migrated the codebase to TypeScript 5.0 and updated type definitions.
```

### Common mistakes
- ❌ Using for user-facing features (use `feat` instead)
- ❌ Using for bug fixes (use `fix` instead)

---

## perf: Performance Improvement

A code change that improves performance. No functionality is changed.

### When to use
- Optimizing algorithms
- Adding caching
- Reducing memory usage
- Improving database query performance

### Examples

```
perf(api): add caching for user queries

Added Redis caching for frequently accessed user data.
Response time improved from 200ms to 20ms.
```

```
perf(database): optimize slow query with indexes

Added indexes on the user_email and created_at columns.
Query time reduced from 500ms to 50ms.
```

```
perf(ui): implement virtual scrolling for large lists

Replaced standard scrolling with virtual scrolling for lists
containing more than 1000 items. Render time improved by 80%.
```

### Common mistakes
- ❌ Changing behavior (use `feat` or `fix` instead)
- ❌ Not including before/after metrics when possible

---

## ci: CI/CD Changes

Changes to CI/CD configuration files and scripts.

### When to use
- Adding GitHub Actions workflows
- Modifying Jenkins pipelines
- Updating Docker images
- Adding deployment scripts

### Examples

```
ci: add automated tests to GitHub Actions

Added a workflow that runs tests on every pull request.
```

```
ci(docker): optimize Docker image size

Reduced image size from 500MB to 200MB by using multi-stage builds.
```

```
ci: enable Dependabot for dependency updates

Configured Dependabot to automatically create pull requests for
dependency updates.
```

### Common mistakes
- ❌ Using for build configuration (use `build` instead)
- ❌ Including production code changes

---

## build: Build System Changes

Changes that affect the build system or external dependencies.

### When to use
- Updating webpack configuration
- Changing build scripts
- Modifying package.json build commands
- Updating build tools

### Examples

```
build: upgrade webpack to v5

Migrated from webpack v4 to v5 and updated all related plugins.
```

```
build: add production environment variable support

Added support for environment-specific builds using NODE_ENV.
```

```
build: enable tree shaking in production build

Configured the build to eliminate dead code from the production bundle.
```

### Common mistakes
- ❌ Using for CI/CD changes (use `ci` instead)
- ❌ Using for dependency updates (use `chore` instead)

---

## revert: Revert a Previous Commit

Reverts a previous commit. The commit message should reference the original commit.

### When to use
- Reverting a breaking change
- Rolling back a problematic feature
- Undoing a bug fix that introduced new issues

### Examples

```
revert: feat(api)!: remove deprecated user endpoint

This reverts commit 8f5a3b2 which removed the user endpoint.
The removal broke existing clients that depend on this endpoint.
```

```
revert: fix(auth): prevent token reuse

This reverts commit 3c7d9e1. The fix introduced a performance
regression that outweighed the benefits.
```

### Common mistakes
- ❌ Not including the original commit hash
- ❌ Not explaining why the revert was necessary

---

## Quick Reference

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(api): add rate limiting` |
| `fix` | Bug fix | `fix(auth): prevent token reuse` |
| `docs` | Documentation only | `docs: update README` |
| `style` | Code style changes | `style: format with prettier` |
| `refactor` | Code restructuring | `refactor(api): extract validator` |
| `test` | Adding tests | `test(api): add user endpoint tests` |
| `chore` | Maintenance tasks | `chore: update dependencies` |
| `perf` | Performance improvement | `perf(api): add caching` |
| `ci` | CI/CD changes | `ci: add test workflow` |
| `build` | Build system changes | `build: upgrade webpack` |
| `revert` | Revert commit | `revert: feat(api): remove endpoint` |
