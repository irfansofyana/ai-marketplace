# Review Checklist

Use this as a reference when analyzing changed files. Not every item applies to every file — use judgment based on the language and context.

## Correctness

**Logic errors**: Off-by-one, wrong operators (`<` vs `<=`, `==` vs `===`), inverted conditions, short-circuit bugs, type coercion surprises

**Edge cases**: Null/undefined access, empty collections (`.first()` on empty array), boundary values (zero, negative, max int), Unicode

**Race conditions**: Shared mutable state without locks, TOCTOU, async gaps between `await` points, concurrent map access (Go)

**API contracts**: Changed signatures without updating callers, return type changes, semantic changes (compiles but behaves differently)

**Error handling**: Swallowed exceptions (`catch {}`), missing error propagation, unhandled promise rejections, wrong HTTP status codes

**Test gaps**: New code paths without tests, modified behavior with stale tests, deleted tests without replacement

## Security

**Injection**: SQL (string concat in queries), XSS (`dangerouslySetInnerHTML`, `v-html`), command injection (`exec()`/`os.system()` with user input), path traversal (`../`), SSRF

**Auth**: Missing auth on new endpoints, privilege escalation / IDOR, broken role checks, JWT issues (no validation, no expiry, hardcoded secret)

**Secrets**: Hardcoded API keys/tokens/passwords, PII or secrets in log output, `.env` files committed

**Crypto**: MD5/SHA1 for security, ECB mode, static IVs, custom crypto, `Math.random()` for security

## Maintainability

**Complexity**: Deep nesting (>3 levels), overly clever one-liners, premature abstraction (factory pattern for 2 cases), functions with 5+ boolean flags

**Naming**: Misleading names, inconsistent naming within the PR (`userId` vs `user_id`), opaque abbreviations beyond convention

**Duplication**: Copy-pasted logic blocks, repeated error handling that should be a helper, duplicated validation across frontend/backend

**Organization**: God functions (>50 LOC doing multiple things), mixed concerns (HTTP + business logic + DB in one function), circular dependencies

## Scalability

**N+1 queries**: DB calls in loops, missing joins/eager loading, ORM lazy-loading traps

**Unbounded operations**: `SELECT *` without LIMIT, unbounded in-memory collections, API endpoints returning all records, unbounded regex on user input

**Resource leaks**: Unclosed connections/streams/cursors, caches without eviction/TTL, event listeners without cleanup, connection pool exhaustion

**Missing indexes**: New WHERE/ORDER BY on unindexed columns (only flag when schema changes are in the diff)

## Language-Specific

**JS/TS**: `==` vs `===`, unhandled promise rejections, React `useEffect` cleanup leaks, `any` proliferation (only flag in new code)

**Go**: Ignored errors (`_ :=`), goroutine leaks (no cancellation context), concurrent map access, `defer` in loops

**Python**: Mutable default args (`def f(x=[])`), bare `except:`, `shell=True` with user input, missing `with` for resources

**Java**: Missing try-with-resources, `==` vs `.equals()`, mutable map keys, over-broad `synchronized`

**Rust**: `unwrap()`/`expect()` in production paths, unnecessary `clone()`, unjustified `unsafe`
