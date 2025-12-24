# Scope Detection Reference

This document defines the scope detection patterns used by the conventional-commits skill. These patterns are analyzed from the changed file paths to suggest appropriate commit scopes.

## Scope Detection Algorithm

The skill analyzes staged files using these steps:

1. **Get staged files**: `git diff --cached --name-only`
2. **Match against patterns**: Find matching patterns for each file
3. **Count frequency**: Determine the most common scope
4. **Suggest scope**: Present the most frequent scope to user
5. **User confirmation**: User can accept, modify, or omit the scope

## Standard Scope Patterns

### Web Application (Frontend)

| File Pattern | Suggested Scope | Priority |
|--------------|-----------------|----------|
| `src/components/**/*`, `src/views/**/*`, `src/pages/**/*` | `ui` | High |
| `src/store/**/*`, `src/state/**/*`, `src/redux/**/*` | `state` | High |
| `src/api/**/*`, `src/services/**/*`, `src/http/**/*` | `api` | Medium |
| `src/router/**/*`, `src/routes/**/*` | `router` | Medium |
| `src/hooks/**/*` | `hooks` | Medium |
| `src/utils/**/*`, `src/helpers/**/*`, `src/lib/**/*` | `utils` | Low |
| `src/styles/**/*`, `src/assets/**/*` | `styles` | Low |
| `tests/**/*`, `**/*.test.ts`, `**/*.spec.ts` | `tests` | Medium |
| `*.config.*`, `.eslintrc*`, `tsconfig.json` | `config` | Low |

### Backend API

| File Pattern | Suggested Scope | Priority |
|--------------|-----------------|----------|
| `src/api/**/*`, `routes/**/*`, `controllers/**/*` | `api` | High |
| `src/auth/**/*`, `services/auth/**/*` | `auth` | Medium |
| `src/models/**/*`, `models/**/*`, `entities/**/*` | `models` | Medium |
| `src/services/**/*`, `services/**/*` | `services` | Medium |
| `src/middleware/**/*`, `middleware/**/*` | `middleware` | Medium |
| `src/db/**/*`, `src/database/**/*`, `db/**/*` | `database` | Medium |
| `src/utils/**/*`, `utils/**/*`, `lib/**/*` | `utils` | Low |
| `tests/**/*`, `**/*.test.js`, `**/*.spec.js` | `tests` | Medium |
| `migrations/**/*` | `migrations` | Medium |

### Full Stack / Monorepo

| File Pattern | Suggested Scope | Priority |
|--------------|-----------------|----------|
| `frontend/**/*`, `client/**/*`, `web/**/*` | `frontend` | High |
| `backend/**/*`, `server/**/*`, `api/**/*` | `backend` | High |
| `shared/**/*`, `common/**/*` | `shared` | Medium |
| `packages/**/*` | (package name) | High |
| `services/**/*` | (service name) | High |

### DevOps / Infrastructure

| File Pattern | Suggested Scope | Priority |
|--------------|-----------------|----------|
| `Dockerfile*`, `docker-compose*`, `.dockerignore` | `docker` | High |
| `.github/**/*`, `workflows/**/*`, `*.yml`, `*.yaml` | `ci` | High |
| `kubernetes/**/*`, `k8s/**/*`, `helm/**/*` | `kubernetes` | High |
| `terraform/**/*`, `*.tf` | `terraform` | High |
| `ansible/**/*`, `*.yml` (playbooks) | `ansible` | Medium |
| `scripts/**/*`, `bin/**/*` | `scripts` | Low |

### Documentation

| File Pattern | Suggested Scope | Priority |
|--------------|-----------------|----------|
| `docs/**/*`, `README.md`, `CHANGELOG.md` | (no scope for docs type) | - |
| `*.md` (in project root) | (no scope for docs type) | - |

### Configuration

| File Pattern | Suggested Scope | Priority |
|--------------|-----------------|----------|
| `*.config.js`, `*.config.ts` | `config` | Medium |
| `.eslintrc*`, `.prettierrc*`, `.babelrc*` | `lint` | Low |
| `tsconfig.json`, `jsconfig.json` | `typescript` | Low |
| `.env*`, `*.env` | `config` | Medium |
| `package.json`, `package-lock.json`, `yarn.lock` | `deps` | Medium |

## Scope Suggestion Examples

### Example 1: Frontend Feature
```
Changed files:
- src/components/UserProfile.tsx
- src/components/UserProfile.test.tsx
- src/services/userApi.ts

Analysis:
- UserProfile.tsx → ui (components)
- UserProfile.test.tsx → tests
- userApi.ts → api

Result: ui (most frequent)
```

### Example 2: Backend Bug Fix
```
Changed files:
- src/controllers/userController.ts
- src/services/userService.ts
- src/models/User.ts

Analysis:
- userController.ts → api (controllers)
- userService.ts → services
- User.ts → models

Result: api (highest priority)
```

### Example 3: Documentation Update
```
Changed files:
- README.md
- docs/api/authentication.md
- docs/api/authorization.md

Analysis:
- README.md → no scope (docs)
- authentication.md → no scope (docs)
- authorization.md → no scope (docs)

Result: no scope suggested (docs type typically omits scope)
```

### Example 4: Infrastructure Change
```
Changed files:
- .github/workflows/test.yml
- Dockerfile
- docker-compose.yml

Analysis:
- test.yml → ci
- Dockerfile → docker
- docker-compose.yml → docker

Result: docker (most frequent)
```

## Multi-Scope Handling

When files span multiple scopes with equal frequency:

1. **Prioritize by scope type**: API > Auth > UI > Utils
2. **Present options to user**: Let user choose the primary scope
3. **Use broader scope**: If no clear winner, suggest a broader scope

Example:
```
Changed files:
- src/components/Button.tsx (ui)
- src/services/authService.ts (auth)
- src/api/userApi.ts (api)

Analysis: Equal frequency (1 each)

Suggested approach: "This change spans multiple scopes (ui, auth, api).
Which scope best represents this change?"
```

## Project-Specific Customization

For projects with unique structures, you can define custom scope patterns in a `.commit-scopes.json` file at the project root:

```json
{
  "scopePatterns": [
    {
      "pattern": "microservices/auth/**/*",
      "scope": "auth-service",
      "priority": "high"
    },
    {
      "pattern": "microservices/payment/**/*",
      "scope": "payment-service",
      "priority": "high"
    },
    {
      "pattern": "packages/ui/**/*",
      "scope": "ui-package",
      "priority": "high"
    }
  ],
  "aliasMapping": {
    "frontend": "ui",
    "server": "backend",
    "db": "database"
  }
}
```

## Scope Naming Conventions

### Recommended Style

- **Lowercase**: `api`, not `API` or `Api`
- **Hyphens for multi-word**: `user-profile`, not `user_profile` or `userProfile`
- **Singular form**: `api`, not `apis` (unless multiple APIs are genuinely different)
- **Short but descriptive**: `auth`, not `authentication-service`

### Common Scope Names

| Scope | Usage |
|-------|-------|
| `api` | API endpoints, controllers, routes |
| `auth` | Authentication, authorization, sessions |
| `ui` | User interface components, views |
| `state` | State management, store, redux |
| `database` | Database models, migrations, queries |
| `config` | Configuration files, environment variables |
| `ci` | CI/CD, GitHub Actions, workflows |
| `docker` | Docker, containers |
| `tests` | Test files, test utilities |
| `deps` | Dependencies, package.json |
| `docs` | Documentation (often omitted with docs type) |

## When to Omit Scope

Omit the scope when:

1. **Multiple scopes affected** and no single scope is appropriate
   ```
   chore: update all dependencies to latest versions
   ```

2. **Project-wide changes** that don't fit a specific scope
   ```
   style: format code with prettier
   docs: update README with new installation steps
   ```

3. **Scope would not add meaningful context**
   ```
   test: increase test coverage to 80%
   ```

## Scope Detection Limitations

The auto-detection has limitations:

- **Cannot understand semantic meaning**: Only analyzes file paths
- **May suggest irrelevant scope**: Based on file location, not change intent
- **Requires user confirmation**: Always review and adjust the suggested scope

For complex changes, rely on user input rather than auto-detection.
