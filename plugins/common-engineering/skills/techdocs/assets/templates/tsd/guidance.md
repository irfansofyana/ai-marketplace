# TSD (Technical Specification Document) Guidance

> **Purpose**: This guide provides section-by-section instructions for writing high-quality TSDs. It explains how to use Universal Discovery output and what questions to ask for each section.

---

## Universal Discovery Integration

> **CRITICAL**: TSDs are created AFTER completing Phase 1 (Universal Discovery) and Phase 2 (Document Type Selection). The Problem Validation Gate must be completed before writing this TSD.

### Universal Discovery Output → TSD Section Mapping

| Universal Discovery Output | Used In TSD Section | How It's Used |
|----------------------------|---------------------|---------------|
| Current State description | Overview → Purpose | Technical context for "why this spec is needed" |
| Technical Context | Overview → System Context | System landscape and dependencies |
| Desired State description | Overview → Purpose | Technical goals |
| State Gap | Performance Requirements | Performance targets from gap analysis |
| Team Context | Testing Requirements | Team capacity and testing approach |

### Before Starting the TSD

**Prerequisites:**
1. ✅ Problem Validation Gate completed (current state, evidence, who's affected, gap analysis)
2. ✅ Document type selection confirmed (AI recommended TSD, user accepted)
3. ✅ Template-specific discovery questions answered (TSD-specific questions from agent)

### TSD vs RFC vs ADR

| Document Type | Focus | When to Use |
|---------------|-------|-------------|
| **TSD** | Technical "how" - API specs, data models, interfaces | When you need detailed technical implementation specs |
| **RFC** | Architectural "what and why" - design decisions | When proposing significant architectural changes |
| **ADR** | Decision "which option" - technology choices | When evaluating and selecting between alternatives |

**TSDs are appropriate when:**
- You need to specify API endpoints, request/response formats
- You need to define data models and schemas
- You need to document interface contracts between components
- The technical approach is already decided (via RFC or ADR)
- You need implementation-level details

**TSDs are NOT appropriate when:**
- The problem is not yet validated → Use Universal Discovery first
- The architectural approach is undecided → Write an RFC
- Technology selection is needed → Write an ADR
- The document is primarily for business stakeholders → Use a One-Pager

---

## Section-by-Section Guidance

### 1. Abstract

**Purpose**: Quick summary for technical readers to understand what this TSD specifies.

**Length**: 2-3 sentences

**Key Elements**:
- What is being specified
- Technical scope (APIs, data models, interfaces)
- Target audience (implementers, API consumers)

**TSD-Specific Questions**:
- "What does this TSD specify at a high level?"
- "Who is the primary audience for this spec?"
- "What type of technical specification is this?" (API, data model, interface contract)

**Quality Criteria**:
- States the technical scope clearly
- Identifies the target audience
- Under 100 words

**Example**:
> This TSD specifies the User Profile API endpoints, data models, and authentication requirements for the Profile Service. It defines RESTful endpoints for user CRUD operations, profile data schema, and error handling conventions. This specification is intended for frontend developers consuming the API and backend engineers implementing the service.

---

### 2. Overview

**Purpose**: Establish technical context and scope for the specification.

**Uses Universal Discovery Output**: Uses technical context and system understanding.

#### Purpose

**What to Include**:
- What this TSD specifies
- Problem it addresses (technical, not business)
- High-level technical approach

**Uses Universal Discovery**:
- **Current State** → Technical context (current system limitations)
- **Desired State** → Technical goals

**TSD-Specific Questions**:
- "What technical problem does this spec address?"
- "What are we building/specifying?"
- "What's the high-level technical approach?"

**Quality Criteria**:
- Technical focus (not business problem)
- Clear scope statement
- Links to related RFC/ADR if applicable

**Example**:
> This TSD specifies the technical implementation of the User Profile API. It addresses the problem identified in RFC-001: the current Profile service lacks a RESTful API, causing tight coupling between frontend and backend. The technical solution is a set of RESTful endpoints with JSON request/response formats, JWT authentication, and OpenAPI documentation.

#### Scope

**What to Include**:
- What is covered (list specific areas)
- What is NOT covered (explicitly exclude)

**TSD-Specific Questions**:
- "What's in scope for this spec?"
- "What's explicitly out of scope?"
- "Are there edge cases not covered?"

**Quality Criteria**:
- Scope is clear and specific
- Out-of-scope items are explicitly listed
- No ambiguity about what the spec covers

**Example**:
> **What is covered:**
> - RESTful API for user profile CRUD operations
> - JSON request/response schemas
> - JWT-based authentication
> - Error response formats
> - Rate limiting specification
>
> **What is NOT covered:**
> - Profile image upload (covered in separate TSD for Media Service)
> - User authentication flow (covered in Auth Service spec)
> - Admin operations (covered in Admin API spec)

#### System Context

**What to Include**:
- What system/service this spec applies to
- Interactions with other systems, APIs, databases
- Dependencies

**Uses Universal Discovery**:
- **Technical Context** → System landscape and dependencies

**TSD-Specific Questions**:
- "What system does this spec apply to?"
- "What other systems does it interact with?"
- "What are the dependencies?"

**Quality Criteria**:
- System boundaries are clear
- Dependencies are listed
- Interactions with other systems are documented

**Example**:
> This specification applies to the Profile Service (Node.js microservice). It interacts with:
> - **PostgreSQL**: User profile data storage
> - **Auth Service**: JWT token validation
> - **Redis**: Session data caching
>
> **Dependencies:**
> - PostgreSQL 15+ for data persistence
> - Auth Service for authentication (must be available)
> - Redis for caching (optional, graceful degradation if unavailable)

---

### 3. API Endpoints / Methods

**Purpose**: Detailed specification of all API endpoints or methods.

> **NOTE**: This section is ONLY for API specifications. For other types of TSDs (data models, interface contracts), adapt or skip this section.

**TSD-Specific Questions**:
- "What endpoints does this API provide?"
- "What are the request/response formats for each endpoint?"
- "What are the authentication requirements?"
- "What are the error codes for each endpoint?"

**Quality Criteria**:
- All endpoints are documented
- Request/response formats are complete
- Parameters are fully specified with types and validation
- Error codes are documented
- Rate limiting is specified
- Examples are provided for each endpoint

**Endpoint Structure**:
For each endpoint, document:
1. **Purpose**: What it does
2. **HTTP Method and Path**: GET / POST / PUT / PATCH / DELETE
3. **Request**: Headers, body, parameters
4. **Response**: Success format, error format
5. **Parameters**: Table with name, type, required/optional, description, validation
6. **Error Codes**: Specific to this endpoint
7. **Rate Limiting**: If different from global limits
8. **Examples**: Request/response examples

**Example (Complete Endpoint Spec)**:

> ### GET /api/v1/users/{user_id}
>
> **Purpose:** Retrieve a user profile by ID
>
> **Request:**
> ```http
> GET /api/v1/users/123 HTTP/1.1
> Host: api.example.com
> Authorization: Bearer {jwt_token}
> ```
>
> **Parameters:**
>
> | Name | Type | Required | Description | Validation |
> |------|------|----------|-------------|------------|
> | `user_id` | string | Yes | User ID (UUID format) | UUID v4 |
> | `fields` | string | No | Comma-separated fields to return | Alphanumeric, comma |
>
> **Response (Success):**
> ```http
> HTTP/1.1 200 OK
> Content-Type: application/json
>
> {
>   "id": "123e4567-e89b-12d3-a456-426614174000",
>   "name": "John Doe",
>   "email": "john@example.com",
>   "created_at": "2024-01-01T00:00:00Z"
> }
> ```
>
> **Response (Error):**
> ```http
> HTTP/1.1 404 Not Found
> Content-Type: application/json
>
> {
>   "error": "USER_NOT_FOUND",
>   "message": "User with ID 123... not found",
>   "request_id": "req_abc123"
> }
> ```
>
> **Error Codes:**
>
> | Code | HTTP Status | Description |
> |------|-------------|-------------|
> | `USER_NOT_FOUND` | 404 | User does not exist |
> | `INVALID_USER_ID` | 400 | Invalid UUID format |
> | `UNAUTHORIZED` | 401 | Missing or invalid token |

**Best Practices**:
- Use OpenAPI/Swagger format for consistency
- Provide examples for all major code paths (success and errors)
- Document parameter validation rules (regex, min/max, format)
- Specify idempotency (e.g., PUT is idempotent, POST is not)
- Document pagination for list endpoints

---

### 4. Data Models / Schemas

**Purpose**: Define all data structures used by the system.

**TSD-Specific Questions**:
- "What data models are used?"
- "What are the fields for each model?"
- "What are the validation rules for each field?"
- "Are there any relationships between models?"

**Quality Criteria**:
- All fields are documented with types
- Required vs optional is clear
- Validation rules are specified
- Examples are provided
- Relationships are documented

**Model Structure**:
For each model, document:
1. **Purpose**: What this model represents
2. **Fields**: Table with name, type, required/optional, description, constraints
3. **Example**: JSON example of the model
4. **Validation Rules**: Any additional validation

**Example**:

> ### Model: User
>
> **Purpose:** Represents a user profile in the system
>
> **Fields:**
>
> | Field | Type | Required | Description | Constraints |
> |-------|------|----------|-------------|-------------|
> | `id` | UUID | Yes | Unique user identifier | UUID v4 |
> | `name` | string | Yes | User's full name | 1-100 chars |
> | `email` | string | Yes | User's email address | Valid email, unique |
> | `role` | enum | Yes | User role | Values: `user`, `admin` |
> | `created_at` | timestamp | Yes | Account creation time | ISO 8601 |
> | `updated_at` | timestamp | No | Last update time | ISO 8601 |
>
> **Example:**
> ```json
> {
>   "id": "123e4567-e89b-12d3-a456-426614174000",
>   "name": "John Doe",
>   "email": "john@example.com",
>   "role": "user",
>   "created_at": "2024-01-01T00:00:00Z",
>   "updated_at": "2024-01-15T00:00:00Z"
> }
> ```
>
> **Validation Rules:**
> - `email` must be unique across all users
> - `name` cannot contain special characters (alphanumeric + spaces only)
> - `role` defaults to `user` if not specified

**Best Practices**:
- Use standard types (string, integer, boolean, enum, timestamp, UUID)
- Specify timestamp formats (ISO 8601, Unix epoch)
- Document field-level validation (regex, min/max length, ranges)
- Use consistent naming conventions (camelCase for JSON)
- Document read-only vs writable fields

---

### 5. Interface Contracts

**Purpose**: Define interfaces between components, services, or modules.

> **NOTE**: This section is for defining programming interfaces, not HTTP APIs (use API Endpoints section for HTTP APIs).

**TSD-Specific Questions**:
- "What interfaces are being defined?"
- "What are the method signatures?"
- "What are the input/output contracts?"
- "What are the implementation requirements?"

**Quality Criteria**:
- All methods are documented
- Input/output types are specified
- Contracts are unambiguous
- Implementation requirements are clear

**Interface Structure**:
For each interface, document:
1. **Purpose**: What this interface does
2. **Methods**: Table with method name, input, output, description
3. **Contract Specification**: Type definition (TypeScript, Go interface, etc.)
4. **Implementation Requirements**: What implementers must do

**Example**:

> ### Interface: CacheProvider
>
> **Purpose:** Defines the contract for cache storage implementations
>
> **Methods:**
>
> | Method | Input | Output | Description |
> |--------|-------|--------|-------------|
> | `get` | `key: string` | `Promise<Value | null>` | Retrieve value from cache |
> | `set` | `key: string, value: Value, ttl?: number` | `Promise<void>` | Store value in cache |
> | `delete` | `key: string` | `Promise<boolean>` | Delete value from cache |
> | `clear` | - | `Promise<void>` | Clear all cache entries |
>
> **Contract Specification:**
> ```typescript
> interface CacheProvider {
>   /**
>    * Retrieve a value from cache
>    * @param key - Cache key (max 256 chars)
>    * @returns Cached value or null if not found
>    */
>   get(key: string): Promise<Value | null>;
>
>   /**
>    * Store a value in cache
>    * @param key - Cache key (max 256 chars)
>    * @param value - Value to cache (must be serializable)
>    * @param ttl - Time to live in seconds (optional, default: 3600)
>    */
>   set(key: string, value: Value, ttl?: number): Promise<void>;
>
>   /**
>    * Delete a value from cache
>    * @param key - Cache key to delete
>    * @returns true if deleted, false if not found
>    */
>   delete(key: string): Promise<boolean>;
>
>   /**
>    * Clear all cache entries
>    */
>   clear(): Promise<void>;
> }
>
> type Value = string | number | object | boolean;
> ```
>
> **Implementation Requirements:**
> - All methods must return Promise (async interface)
> - `get` must return `null` for cache miss (not undefined)
> - `set` must serialize value before storage
> - `delete` must return false if key doesn't exist
> - Implementations must handle connection errors gracefully

**Best Practices**:
- Use appropriate language for target audience (TypeScript for JS/TS, Go interfaces for Go, etc.)
- Document behavior for edge cases (null inputs, empty strings, etc.)
- Specify error handling behavior (throw exceptions vs return error values)
- Define type aliases for complex types

---

### 6. Error Handling

**Purpose**: Define how errors are handled across the system.

**TSD-Specific Questions**:
- "What are the error categories?"
- "What is the error response format?"
- "What error codes exist?"
- "What is the retry policy for each error type?"

**Quality Criteria**:
- Error format is consistent
- All error codes are documented
- Retry policy is specified
- Error categories are clear

**Content Structure**:
1. **Error Categories**: Group errors by type (client, server, rate limit)
2. **Error Response Format**: Standard error structure
3. **Error Codes**: Complete list of codes with HTTP status and description
4. **Retry Policy**: When to retry, when not to retry

**Example**:

> ### Error Categories
>
> | Category | Description | HTTP Status Range |
> |----------|-------------|-------------------|
> | Client Errors | Invalid input, validation failures | 400-499 |
> | Server Errors | System failures, bugs | 500-599 |
> | Rate Limiting | Too many requests | 429 |
>
> ### Error Response Format
>
> **All errors follow this format:**
> ```json
> {
>   "error": "ERROR_CODE",
>   "message": "Human-readable description",
>   "request_id": "req_abc123",
>   "details": {
>     "field": "Additional context"
>   }
> }
> ```
>
> ### Error Codes
>
> | Error Code | HTTP Status | Message | Retry Policy |
> |------------|-------------|---------|--------------|
> | `VALIDATION_ERROR` | 400 | Invalid input | Do not retry |
> | `NOT_FOUND` | 404 | Resource not found | Do not retry |
> | `UNAUTHORIZED` | 401 | Missing or invalid auth | Do not retry |
> | `RATE_LIMITED` | 429 | Too many requests | Retry after `Retry-After` seconds |
> | `INTERNAL_ERROR` | 500 | System error | Retry with exponential backoff |
> | `SERVICE_UNAVAILABLE` | 503 | Service temporarily unavailable | Retry with exponential backoff |
>
> ### Retry Policy
>
> **Client-side retry behavior:**
> - **4xx errors**: Do not retry (except 429)
> - **429 Rate Limited**: Retry after `Retry-After` header value
> - **5xx errors**: Retry with exponential backoff (1s, 2s, 4s max 3 retries)
> - **Network errors**: Retry with exponential backoff (1s, 2s, 4s, 8s, 16s max 5 retries)

**Best Practices**:
- Use consistent error codes (SCREAMING_SNAKE_CASE)
- Provide human-readable messages (not just codes)
- Include `request_id` for tracing
- Specify which errors are retryable
- Document backoff strategy for retries

---

### 7. Versioning Strategy

**Purpose**: Define how the API/interface is versioned.

**TSD-Specific Questions**:
- "What versioning approach is used?"
- "What is the current version?"
- "How are breaking changes handled?"
- "What is the deprecation policy?"

**Quality Criteria**:
- Versioning approach is specified
- Current version is documented
- Version history is maintained
- Breaking changes are clearly marked
- Deprecation policy is defined

**Versioning Approaches**:

| Approach | Example | Pros | Cons | When to Use |
|----------|---------|------|------|-------------|
| URL path versioning | `/v1/users`, `/v2/users` | Clear, explicit | URL changes | Public APIs |
| Header versioning | `Accept: application/vnd.api.v1+json` | URL stable | Less discoverable | Internal APIs |
| Query param versioning | `?version=1` | Easy to test | Not recommended | Legacy support |
| No versioning | `/users` | Simple | Breaking changes painful | Internal only |

**Example**:

> ### Versioning Approach
>
> We use **URL path versioning** for this API.
>
> **Example:**
> - Version 1: `https://api.example.com/v1/users`
> - Version 2: `https://api.example.com/v2/users`
>
> ### Current Version
>
> **Version:** 1.2.0
> **Released:** 2024-01-15
> **Deprecation:** N/A (not deprecated)
>
> ### Version History
>
> | Version | Date | Changes | Breaking? |
> |---------|------|---------|-----------|
> | 1.2.0 | 2024-01-15 | Added `email_verified` field to User model | No |
> | 1.1.0 | 2023-12-01 | Added `PATCH /users/{id}` endpoint | No |
> | 1.0.0 | 2023-10-01 | Initial release | - |
>
> ### Backwards Compatibility
>
> **Breaking changes require:**
> - New major version (2.0.0)
> - Minimum 6 months notice before deprecation
> - Migration guide provided to API consumers
> - Existing versions supported during grace period (6 months after new version release)

**Best Practices**:
- Use semantic versioning (MAJOR.MINOR.PATCH)
- MAJOR: Breaking changes
- MINOR: New features, backwards compatible
- PATCH: Bug fixes, backwards compatible
- Provide migration guides for breaking changes
- Deprecate old versions gracefully (support overlap period)

---

### 8. Security Considerations

**Purpose**: Define authentication, authorization, and data security requirements.

**TSD-Specific Questions**:
- "How is authentication handled?"
- "How is authorization handled?"
> "What data security measures are required?"
- "What are the rate limiting rules?"

**Quality Criteria**:
- Authentication method is specified
- Authorization model is defined
- Data encryption requirements are stated
- Rate limiting is specified
- PII/sensitive data handling is documented

**Content Structure**:
1. **Authentication**: How clients authenticate
2. **Authorization**: How permissions are enforced
3. **Data Security**: Encryption requirements, sensitive data handling
4. **Rate Limiting**: Request limits per tier/client

**Example**:

> ### Authentication
>
> **Method: JWT Bearer Tokens**
>
> Clients must include a JWT token in the `Authorization` header:
> ```http
> Authorization: Bearer {jwt_token}
> ```
>
> **Token format:**
> - Issuer: `https://auth.example.com`
> - Audience: `https://api.example.com`
> - Expiration: 1 hour
> - Algorithm: RS256
>
> ### Authorization
>
> **Method: Role-Based Access Control (RBAC)**
>
> **Permissions:**
>
> | Role | Permissions |
> |------------|-------------|
> | `user` | Read own profile, update own profile |
> | `admin` | Read any profile, update any profile, delete profiles |
> | `service` | Full access (service-to-service) |
>
> ### Data Security
>
> **Encryption:**
> - **In transit:** TLS 1.3 required (HTTPS only)
> - **At rest:** AES-256 encryption for database
>
> **Sensitive data:**
> - PII (email, name) is encrypted at rest in database
> - Passwords are never logged or returned in responses
> - Audit logging for all write operations
>
> ### Rate Limiting
>
> | Tier | Limit | Time Window |
> |------|-------|-------------|
> | Free | 100 requests | 1 hour |
> | Pro | 1000 requests | 1 hour |
> | Enterprise | Unlimited | - |
>
> **Headers:** `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`

**Best Practices**:
- Use industry-standard authentication (OAuth 2.0, JWT)
- Define permission model clearly (RBAC, scopes)
- Specify encryption requirements (TLS version, cipher suites)
- Document PII/sensitive data handling
- Rate limit to prevent abuse

---

### 9. Performance Requirements

**Purpose**: Define performance targets for the system.

**Uses Universal Discovery**:
- **State Gap** → Performance targets from gap analysis

**TSD-Specific Questions**:
- "What are the latency targets?"
- "What is the target throughput?"
- "What are the resource limits?"
- "How is performance measured?"

**Quality Criteria**:
- Latency targets are specified (p50, p95, p99)
- Throughput targets are defined
- Resource limits are documented
- Performance is measurable

**Content Structure**:
1. **Latency**: Target latencies for different operations
2. **Throughput**: Target requests/second
3. **Resource Limits**: Max request size, response size, timeout

**Example**:

> ### Latency
>
> | Operation | Target (p50) | Target (p95) | Target (p99) |
> |-----------|-------------|-------------|-------------|
> | GET /users/{id} | 50ms | 100ms | 200ms |
> | POST /users | 100ms | 200ms | 500ms |
> | GET /users (list) | 200ms | 500ms | 1000ms |
>
> ### Throughput
>
> | Metric | Target | Notes |
> |--------|--------|-------|
> | Requests per second | 10,000 | Per instance (horizontal scalable) |
> | Concurrent connections | 1,000 | Max concurrent connections |
>
> ### Resource Limits
>
> | Resource | Limit | Notes |
> |----------|-------|-------|
> | Request size | 1 MB | Max request body |
> | Response size | 10 MB | Max response body |
> | Request timeout | 30s | Max duration for any request |

**Best Practices**:
- Specify percentiles (p50, p95, p99) not just "average"
- Include both happy path and edge case operations
- Document assumptions (e.g., "assuming cache hit rate 70%")
- Make performance measurable (define metrics)

---

### 10. Testing Requirements

**Purpose**: Define testing requirements for the specification.

**Uses Universal Discovery**:
- **Team Context** → Team capacity and testing approach

**TSD-Specific Questions**:
- "What is the unit test coverage requirement?"
- "What integration tests are needed?"
- "Are contract tests required?"
- "What performance tests are needed?"

**Quality Criteria**:
- Unit test coverage target is specified
- Integration test scenarios are listed
- Contract tests are defined (if applicable)
- Performance test criteria are defined

**Content Structure**:
1. **Unit Tests**: Coverage requirement, key scenarios
2. **Integration Tests**: Test coverage areas
3. **Contract Tests**: Compatibility verification
4. **Performance Tests**: Load testing criteria

**Example**:

> ### Unit Tests
>
> **Coverage requirement:** 85%
>
> **Key test scenarios:**
> - [ ] All endpoint handlers (success path)
> - [ ] All validation errors (4xx responses)
> - [ ] Database error handling (5xx responses)
> - [ ] Authentication/authorization enforcement
> - [ ] Rate limiting enforcement
> - [ ] Data model serialization/deserialization
>
> ### Integration Tests
>
> **Test coverage:**
> - [ ] API endpoint testing with real database
> - [ ] Authentication flow with real Auth Service
> - [ ] Cache integration with real Redis
> - [ ] Error handling with external service failures
>
> ### Contract Tests
>
> **Purpose:** Verify API compatibility with consumers
>
> **Test scenarios:**
> - [ ] Request/response format validation
> - [ ] Error response format validation
> - [ ] Required fields presence check
> - [ ] Data type validation
> - [ ] Version compatibility (test against v1 and v2)
>
> ### Performance Tests
>
> **Load testing:**
> - **Target load:** 10,000 requests/second
> - **Duration:** 1 hour
> - **Success criteria:**
>   - p95 latency < 500ms
>   - Error rate < 0.1%
>   - No memory leaks

**Best Practices**:
- Specify coverage target (percentage)
- Test both happy path and error cases
- Include contract tests for API integrations
- Performance tests should match production load patterns
- Document test environment (staging vs production-like)

---

### 11. Examples

**Purpose**: Provide concrete examples of how to use the API/interface.

**TSD-Specific Questions**:
- "What are the common use cases?"
- "What examples would be most helpful?"
- "Are there edge cases that should be demonstrated?"

**Quality Criteria**:
- Examples cover major use cases
- Examples are complete and runnable
- Both success and error examples are provided
- cURL/HTTP examples for APIs
- Code examples for libraries

**Content Structure**:
For each example:
1. **Scenario**: Description of the use case
2. **Request**: Complete request example
3. **Response**: Complete response example

**Example**:

> ### Example 1: Create User
>
> **Scenario:** Create a new user account
>
> **Request:**
> ```bash
> curl -X POST https://api.example.com/v1/users \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer eyJhbGc..." \
>   -d '{
>     "name": "John Doe",
>     "email": "john@example.com",
>     "role": "user"
>   }'
> ```
>
> **Response (Success):**
> ```http
> HTTP/1.1 201 Created
> Content-Type: application/json
> Location: /v1/users/123e4567-e89b-12d3-a456-426614174000
>
> {
>   "id": "123e4567-e89b-12d3-a456-426614174000",
>   "name": "John Doe",
>   "email": "john@example.com",
>   "role": "user",
>   "created_at": "2024-01-15T10:30:00Z"
> }
> ```
>
> **Response (Error - Duplicate Email):**
> ```http
> HTTP/1.1 409 Conflict
> Content-Type: application/json
>
> {
>   "error": "EMAIL_ALREADY_EXISTS",
>   "message": "A user with email john@example.com already exists",
>   "request_id": "req_abc123"
> }
> ```
>
> ### Example 2: Get User with Field Selection
>
> **Scenario:** Retrieve user profile, requesting only specific fields
>
> **Request:**
> ```bash
> curl -X GET "https://api.example.com/v1/users/123?fields=name,email" \
>   -H "Authorization: Bearer eyJhbGc..."
> ```
>
> **Response:**
> ```http
> HTTP/1.1 200 OK
> Content-Type: application/json
>
> {
>   "name": "John Doe",
>   "email": "john@example.com"
> }
> ```

**Best Practices**:
- Provide realistic examples (not placeholder data)
- Include both success and error cases
- Show complete HTTP requests (method, URL, headers, body)
- Use cURL for HTTP API examples
- Include comments for complex examples

---

### 12. References

**Purpose**: Link to related documents and external resources.

**Uses Universal Discovery**:
- **Related Documents** → Reference any attached docs

**TSD-Specific Questions**:
- "What related documents should readers review?"
- "What external standards/specifications apply?"
- "What implementation guides exist?"

**Quality Criteria**:
- Related documents are linked
- External references are relevant
- Links are accurate

**Example**:

> ### Related Documents
>
> - [RFC-001: Profile Service Architecture](/docs/rfc/rfc-001-profile-service.md) - Architectural design for Profile Service
> - [ADR-003: PostgreSQL vs MongoDB](/docs/adr/003-database-choice.md) - Database selection decision
> - [TSD-002: Authentication Service](/docs/tsd/002-auth-service.md) - Auth service API specification
>
> ### External References
>
> - [OpenAPI 3.0 Specification](https://spec.openapis.org/oas/v3.0.0) - API documentation standard
> - [RFC 7231: HTTP/1.1](https://tools.ietf.org/html/rfc7231) - HTTP semantics and status codes
> - [JWT Handbook](https://jwt.io/introduction) - JWT best practices

---

### 13. Appendix

**Purpose**: Additional context that doesn't fit in main sections.

**TSD-Specific Questions**:
- "What terms need definitions?"
- "What implementation details are useful?"

**Quality Criteria**:
- Glossary defines technical terms
- Implementation details are accurate
- Appendix is truly optional

**Content Structure**:
1. **Glossary**: Define technical terms
2. **Implementation Notes**: Additional technical context

**Example**:

> ### Glossary
>
> | Term | Definition |
> |------|------------|
> | UUID | Universally Unique Identifier, 128-bit identifier used to uniquely identify information in computer systems |
> | JWT | JSON Web Token, a compact URL-safe means of representing claims to be transferred between two parties |
> | RBAC | Role-Based Access Control, an approach to restricting system access to authorized users |
>
> ### Implementation Notes
>
> **Database Schema:**
> - Users table: `users` (PostgreSQL)
> - Indexes: `users_email_key` (unique), `users_id_idx` (primary key)
>
> **Cache Key Format:**
> - User profile: `user:profile:{user_id}`
> - User list: `user:list:{page}:{limit}`
>
> **Monitoring:**
> - Metrics exported to Prometheus on `/metrics` endpoint
> - Key metrics: `api_request_duration_seconds`, `api_requests_total`, `api_errors_total`

---

### 14. Change Log

**Purpose**: Track changes to the specification over time.

**TSD-Specific Questions**:
- "What changed in this version?"
> "Who made the changes?"
- "Why were the changes made?"

**Quality Criteria**:
- All changes are documented
- Version numbers follow semantic versioning
- Breaking changes are clearly marked

**Example**:

> ### Change Log
>
> | Version | Date | Author | Changes | Breaking? |
> |---------|------|--------|---------|-----------|
> | 1.2.0 | 2024-01-15 | Jane Smith | Added `email_verified` field to User model; added `PATCH /users/{id}` endpoint | No |
> | 1.1.0 | 2023-12-01 | John Doe | Added field selection parameter to GET endpoints; added rate limiting headers | No |
> | 1.0.0 | 2023-10-01 | Jane Smith | Initial release | - |

---

## Quality Checklist for TSDs

Before submitting a TSD for review, verify:

### Completeness
- [ ] All sections are complete
- [ ] All endpoints/methods are documented (for API specs)
- [ ] All data models are fully specified
- [ ] All error codes are documented

### Technical Accuracy
- [ ] Request/response formats are correct
- [ ] Data types are accurate
- [ ] Validation rules are complete
- [ ] Error codes cover all scenarios

### Clarity
- [ ] Technical terms are defined (in glossary)
- [ ] Examples are complete and runnable
- [ ] Scope is clear (what's in vs out)
- [ ] Dependencies are listed

### Testability
- [ ] Performance requirements are measurable
- [ ] Testing requirements are specified
- [ ] Success criteria are defined

### Security
- [ ] Authentication is specified
- [ ] Authorization is defined
- [ ] Data security requirements are stated
- [ ] Rate limiting is specified

---

## Common TSD Mistakes to Avoid

1. **Incomplete endpoint documentation**: Missing request/response formats → Document all fields
2. **Vague error codes**: "ERROR" without specificity → Use descriptive codes like `USER_NOT_FOUND`
3. **Missing validation rules**: Field is "string" with no constraints → Specify min/max, regex, format
4. **No examples**: Hard to understand how to use the API → Provide complete examples
5. **Inconsistent naming**: Mix of camelCase, snake_case → Choose one and stick to it
6. **Missing security**: No auth/authorization specified → Always document security
7. **No performance targets**: "Should be fast" → Specify p95 latency < X ms
8. **Breaking changes without version bump**: Changed API but stayed at v1.0 → Use semantic versioning
