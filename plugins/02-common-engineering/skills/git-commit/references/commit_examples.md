# Commit Examples by Type

Examples of well-formed Conventional Commits for each type.

## feat (New Feature)

```bash
git commit -m "feat(auth): add JWT authentication middleware"

git commit -m "feat(api): implement rate limiting per user

Add token-bucket rate limiting:
- 100 requests per minute per user
- Configurable limits via environment
- Redis-backed for distributed systems"
```

## fix (Bug Fix)

```bash
git commit -m "fix(validation): prevent SQL injection in user input"

git commit -m "fix(session): resolve cookie expiration edge case

Session cookies were expiring prematurely due to:
- Incorrect timezone handling in expiry calculation
- Missing refresh on activity

Fix: Store expiry as UTC timestamp, refresh on each request"
```

## refactor (Code Restructuring)

```bash
git commit -m "refactor(http): extract retry logic into separate module"

git commit -m "refactor(services): consolidate duplicate validation code

Merge validation logic from:
- UserService.validate()
- OrderService.validate()
- ProductService.validate()

Into shared ValidationService class"
```

## perf (Performance)

```bash
git commit -m "perf(database): add index to users.email column"

git commit -m "perf(cache): implement response caching for API endpoints

Cache GET requests for 5 minutes:
- Reduces database load by ~40%
- Improves median response time from 200ms to 50ms"
```

## test (Tests)

```bash
git commit -m "test(auth): add unit tests for password hashing"

git commit -m "test(integration): add E2E tests for checkout flow

Cover complete user journey:
- Cart management
- Payment processing
- Order confirmation
- Email notifications"
```

## ci (CI/CD)

```bash
git commit -m "ci(github): add automated release workflow"

git commit -m "ci(docker): optimize multi-stage build for smaller images

Reduce final image size from 500MB to 150MB by:
- Using alpine base image
- Removing build dependencies
- Cleaning up package caches"
```

## docs (Documentation)

```bash
git commit -m "docs(api): update authentication documentation"

git commit -m "docs(readme): add installation guide for macOS

Include step-by-step instructions for:
- Homebrew installation
- Environment configuration
- Troubleshooting common issues"
```

## chore (Maintenance)

```bash
git commit -m "chore(deps): upgrade node from 18 to 20"

git commit -m "chore(deps): update react to v18.2.0

Also update related dependencies:
- react-dom
- @types/react
- eslint-plugin-react"
```

## style (Code Formatting)

```bash
git commit -m "style(components): format with prettier

Run prettier on all component files with:
- 2 space indentation
- Single quotes
- No trailing commas"
```

## security (Security Fixes)

```bash
git commit -m "security(auth): enforce HTTPS for production"

git commit -m "security(upload): validate file types to prevent RCE

Add allowlist of permitted MIME types:
- image/jpeg
- image/png
- application/pdf

Reject all other uploads."
```

## Breaking Changes

```bash
git commit -m "feat(api)!: remove deprecated legacy endpoint

BREAKING CHANGE: The /api/v1/legacy endpoint has been removed.
Migrate to /api/v2/standard by 2024-01-01."

git commit -m "feat(db)!: change primary key type from int to uuid

BREAKING CHANGE: All tables now use UUID primary keys instead of
auto-incrementing integers. Update foreign keys accordingly."
```

## Multi-Paragraph Body

```bash
git commit -m "feat(cache): implement distributed caching layer

Add Redis-based caching with the following features:

- Automatic cache invalidation on data changes
- Configurable TTL per cache key
- Cache warming on application startup
- Fallback to in-memory cache if Redis unavailable

This reduces database load by approximately 60% for read-heavy
workloads and improves average response time from 150ms to 40ms.

Addresses performance requirement from Q3 planning."
```

## Tips for Writing Good Commits

1. **Be specific**: "fix authentication" is vague, "fix(auth): use hmac.compare_digest" is specific
2. **Explain why, not just what**: The body should explain the reasoning behind the change
3. **Keep it focused**: One logical change per commit
4. **Use imperative mood**: "Add feature" not "Added feature" or "Adding feature"
5. **Limit subject line**: Maximum 50 characters after the colon
