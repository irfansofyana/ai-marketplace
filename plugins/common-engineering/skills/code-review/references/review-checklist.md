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

## Reliability

**Error recovery**: Missing retries on transient failures (network, DB), no fallback when a downstream service is unavailable, crash-on-error instead of graceful degradation

**Timeouts**: External calls (HTTP, DB, RPC) without timeouts, unbounded blocking operations, missing circuit breakers on critical paths

**Resource cleanup**: Unclosed connections/streams/file handles in error paths, missing `finally`/`defer`/`with` for cleanup, connection pool exhaustion under load

**Idempotency**: Non-idempotent operations exposed to retries (duplicate payments, duplicate records), missing deduplication keys on write endpoints

**Concurrency**: Race conditions on shared state, TOCTOU bugs, deadlock-prone lock ordering, uncoordinated concurrent writes

**Observability**: Silent failures (swallowed errors with no logging), missing health checks on new services, no alerting hooks for new failure modes

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

## Dependencies

**Version bumps**: Major version bumps without migration notes, multiple unrelated deps upgraded in one PR (harder to bisect), downgrading a dependency without explanation

**New dependencies**: Adding a dep for something achievable with stdlib or existing deps, unmaintained packages (no commits in 12+ months, low download counts), packages with known CVEs, adding a heavy dep for a small utility (e.g., lodash for one function)

**Removals**: Removing a dep still imported elsewhere, removing without cleaning up its configuration files or types

**Version pinning**: Inconsistent strategy (mixing exact `1.2.3` and range `^1.2.3`), overly broad ranges (`*` or `>=`), pinning to a pre-release without justification

**Peer dependency conflicts**: New dep requiring a different major version of a shared peer dep (e.g., React 17 vs 18), missing peer deps

**Manifest files to watch**: `package.json`, `go.mod`, `Cargo.toml`, `pyproject.toml`, `requirements.txt`, `Gemfile`, `pom.xml`, `build.gradle`

## Language-Specific

**JS/TS**: `==` vs `===`, unhandled promise rejections, React `useEffect` cleanup leaks, `any` proliferation (only flag in new code)

**Go**: Ignored errors (`_ :=`), goroutine leaks (no cancellation context), concurrent map access, `defer` in loops

**Python**: Mutable default args (`def f(x=[])`), bare `except:`, `shell=True` with user input, missing `with` for resources

**Java**: Missing try-with-resources, `==` vs `.equals()`, mutable map keys, over-broad `synchronized`

**Rust**: `unwrap()`/`expect()` in production paths, unnecessary `clone()`, unjustified `unsafe`
