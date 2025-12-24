# TSD Example: User Profile API

> **Purpose**: This is a complete TSD example demonstrating how to specify a RESTful API with endpoints, data models, error handling, and examples.

---

## Universal Discovery Context

Before writing this TSD, the author completed Phase 1 (Universal Discovery) with the Problem Validation Gate, and the architectural approach was decided via RFC-001.

**Universal Discovery Output**:
- **Current State**: Frontend tightly coupled to backend via RPC; no RESTful API for user profiles; direct database access from frontend.
- **Evidence**: 3+ days to add simple profile fields; frontend team blocked on backend changes; tight coupling prevents independent deployments.
- **Who is Affected**: Frontend team (blocked on backend), Backend team (frequent profile schema change requests), Product team (slow feature iteration).
- **Desired State**: RESTful API for user profile CRUD operations; decoupled frontend and backend; independent deployments.
- **Technical Context**: Node.js backend, PostgreSQL database, React frontend.
- **Related Documents**: RFC-001: Profile Service Architecture

This TSD uses this Universal Discovery output to establish technical context.

---

# TSD: User Profile API Specification

**Author:** Jane Smith, Backend Team Lead
**Status:** In Review
**Created:** 2024-09-10
**Last Updated:** 2024-09-15

---

## Abstract

This TSD specifies the User Profile API endpoints, data models, and security requirements for the Profile Service. It defines RESTful endpoints for user profile CRUD operations, JSON request/response formats, JWT authentication, and error handling conventions. This specification is intended for frontend developers consuming the API and backend engineers implementing the service.

---

## Overview

### Purpose

This TSD specifies the technical implementation of the User Profile API. It addresses the problem identified in RFC-001: the current system lacks a RESTful API for user profiles, causing tight coupling between frontend and backend. The technical solution is a set of RESTful endpoints with JSON request/response formats, JWT-based authentication, and comprehensive error handling.

### Scope

**What is covered:**
- RESTful API for user profile CRUD operations (Create, Read, Update, Delete)
- JSON request/response schemas for User model
- JWT-based authentication and authorization
- Error response formats and error codes
- Rate limiting specification
- Field selection and pagination for list operations

**What is NOT covered:**
- Profile image upload (covered in TSD-002: Media Service API)
- User authentication flow (covered in TSD-003: Auth Service API)
- Admin operations (covered in TSD-004: Admin API)
- Password reset flow (covered in TSD-003: Auth Service API)

### System Context

This specification applies to the **Profile Service** (Node.js microservice). It interacts with:

- **PostgreSQL 15**: User profile data storage
- **Auth Service**: JWT token validation and user authentication
- **Redis**: Session data caching (optional, graceful degradation if unavailable)

**Dependencies:**
- **PostgreSQL 15+**: Required for data persistence
- **Auth Service**: Required for authentication (must be available)
- **Redis**: Optional for caching (graceful degradation if unavailable)

---

## API Endpoints

### Endpoint Group: User Profile Operations

#### GET /api/v1/users/{user_id}

**Purpose:** Retrieve a user profile by ID

**Request:**

```http
GET /api/v1/users/123e4567-e89b-12d3-a456-426614174000 HTTP/1.1
Host: api.example.com
Authorization: Bearer {jwt_token}
```

**Parameters:**

| Name | Type | Required | Description | Validation |
|------|------|----------|-------------|------------|
| `user_id` | string | Yes | User ID (UUID format) | UUID v4 format |
| `fields` | string | No | Comma-separated fields to return | Alphanumeric + comma, max 100 chars |

**Response (Success):**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "John Doe",
  "email": "john@example.com",
  "role": "user",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-15T00:00:00Z"
}
```

**Response (Error):**

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "error": "USER_NOT_FOUND",
  "message": "User with ID 123e4567-e89b-12d3-a456-426614174000 not found",
  "request_id": "req_abc123xyz"
}
```

**Error Codes:**

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `USER_NOT_FOUND` | 404 | User does not exist |
| `INVALID_USER_ID` | 400 | Invalid UUID format |
| `UNAUTHORIZED` | 401 | Missing or invalid JWT token |
| `FORBIDDEN` | 403 | Not authorized to access this user |

**Rate Limiting:**
- **Limit:** 100 requests per minute per user
- **Headers:** `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`

#### POST /api/v1/users

**Purpose:** Create a new user profile

**Request:**

```http
POST /api/v1/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer {jwt_token}

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword123",
  "role": "user"
}
```

**Parameters:**

| Name | Type | Required | Description | Validation |
|------|------|----------|-------------|------------|
| `name` | string | Yes | User's full name | 1-100 chars, alphanumeric + spaces |
| `email` | string | Yes | User's email address | Valid email format, unique |
| `password` | string | Yes | User's password | 8-100 chars, must contain letter + number |
| `role` | string | No | User role | Enum: `user`, `admin`, defaults to `user` |

**Response (Success):**

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/v1/users/123e4567-e89b-12d3-a456-426614174000

{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "John Doe",
  "email": "john@example.com",
  "role": "user",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

**Response (Error):**

```http
HTTP/1.1 409 Conflict
Content-Type: application/json

{
  "error": "EMAIL_ALREADY_EXISTS",
  "message": "A user with email john@example.com already exists",
  "request_id": "req_abc123xyz"
}
```

**Error Codes:**

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_REQUEST_BODY` | 400 | Request body validation failed |
| `INVALID_EMAIL` | 400 | Invalid email format |
| `INVALID_PASSWORD` | 400 | Password doesn't meet requirements |
| `INVALID_ROLE` | 400 | Invalid role value |
| `EMAIL_ALREADY_EXISTS` | 409 | Email already registered |
| `UNAUTHORIZED` | 401 | Missing or invalid JWT token |

#### PATCH /api/v1/users/{user_id}

**Purpose:** Partially update a user profile

**Request:**

```http
PATCH /api/v1/users/123e4567-e89b-12d3-a456-426614174000 HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer {jwt_token}

{
  "name": "Jane Doe"
}
```

**Parameters:**

| Name | Type | Required | Description | Validation |
|------|------|----------|-------------|------------|
| `name` | string | No | User's full name | 1-100 chars, alphanumeric + spaces |
| `email` | string | No | User's email address | Valid email format, unique |
| `role` | string | No | User role | Enum: `user`, `admin` |

**Response (Success):**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "Jane Doe",
  "email": "john@example.com",
  "role": "user",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-15T10:35:00Z"
}
```

**Error Codes:**

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `USER_NOT_FOUND` | 404 | User does not exist |
| `INVALID_REQUEST_BODY` | 400 | Request body validation failed |
| `EMAIL_ALREADY_EXISTS` | 409 | Email already registered |
| `UNAUTHORIZED` | 401 | Missing or invalid JWT token |
| `FORBIDDEN` | 403 | Not authorized to update this user |

#### DELETE /api/v1/users/{user_id}

**Purpose:** Delete a user profile

**Request:**

```http
DELETE /api/v1/users/123e4567-e89b-12d3-a456-426614174000 HTTP/1.1
Host: api.example.com
Authorization: Bearer {jwt_token}
```

**Response (Success):**

```http
HTTP/1.1 204 No Content
```

**Error Codes:**

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `USER_NOT_FOUND` | 404 | User does not exist |
| `UNAUTHORIZED` | 401 | Missing or invalid JWT token |
| `FORBIDDEN` | 403 | Not authorized to delete this user |
| `USER_LOCKED` | 403 | User is locked and cannot be deleted |

#### GET /api/v1/users

**Purpose:** List users with pagination and filtering

**Request:**

```http
GET /api/v1/users?page=1&limit=20&role=user&sort=created_at:desc HTTP/1.1
Host: api.example.com
Authorization: Bearer {jwt_token}
```

**Parameters:**

| Name | Type | Required | Description | Validation |
|------|------|----------|-------------|------------|
| `page` | integer | No | Page number (1-indexed) | Min 1, default 1 |
| `limit` | integer | No | Results per page | Min 1, max 100, default 20 |
| `role` | string | No | Filter by role | Enum: `user`, `admin` |
| `sort` | string | No | Sort field and direction | Format: `field:direction`, direction: `asc` or `desc` |
| `fields` | string | No | Comma-separated fields to return | Alphanumeric + comma |

**Response (Success):**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "data": [
    {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "name": "John Doe",
      "email": "john@example.com",
      "role": "user",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "total_pages": 8
  }
}
```

**Error Codes:**

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_PAGINATION` | 400 | Invalid page or limit value |
| `INVALID_SORT` | 400 | Invalid sort parameter |
| `UNAUTHORIZED` | 401 | Missing or invalid JWT token |

---

## Data Models

### Model: User

**Purpose:** Represents a user profile in the system

**Fields:**

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| `id` | UUID | Yes | Unique user identifier | UUID v4 format |
| `name` | string | Yes | User's full name | 1-100 chars, alphanumeric + spaces |
| `email` | string | Yes | User's email address | Valid email format, unique |
| `role` | enum | Yes | User role | Values: `user`, `admin` |
| `created_at` | timestamp | Yes | Account creation time | ISO 8601 format |
| `updated_at` | timestamp | No | Last update time | ISO 8601 format |

**Example:**

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "John Doe",
  "email": "john@example.com",
  "role": "user",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-15T00:00:00Z"
}
```

**Validation Rules:**
- `email` must be unique across all users
- `name` cannot contain special characters (alphanumeric + spaces only)
- `role` defaults to `user` if not specified
- `id` is auto-generated on creation (not client-provided)

### Model: Pagination

**Purpose:** Represents pagination metadata for list responses

**Fields:**

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| `page` | integer | Yes | Current page number (1-indexed) | Min 1 |
| `limit` | integer | Yes | Results per page | Min 1, max 100 |
| `total` | integer | Yes | Total number of results | Non-negative |
| `total_pages` | integer | Yes | Total number of pages | Non-negative |

**Example:**

```json
{
  "page": 1,
  "limit": 20,
  "total": 150,
  "total_pages": 8
}
```

---

## Error Handling

### Error Categories

| Category | Description | HTTP Status Range |
|----------|-------------|-------------------|
| Client Errors | Invalid input, validation failures | 400-499 |
| Server Errors | System failures, bugs | 500-599 |
| Rate Limiting | Too many requests | 429 |

### Error Response Format

**All errors follow this format:**

```json
{
  "error": "ERROR_CODE",
  "message": "Human-readable description",
  "request_id": "req_abc123xyz",
  "details": {
    "field": "Additional context"
  }
}
```

### Error Codes

| Error Code | HTTP Status | Message | Retry Policy |
|------------|-------------|---------|--------------|
| `INVALID_REQUEST_BODY` | 400 | Request body validation failed | Do not retry |
| `INVALID_EMAIL` | 400 | Invalid email format | Do not retry |
| `INVALID_PASSWORD` | 400 | Password doesn't meet requirements | Do not retry |
| `INVALID_ROLE` | 400 | Invalid role value | Do not retry |
| `INVALID_PAGINATION` | 400 | Invalid page or limit value | Do not retry |
| `INVALID_SORT` | 400 | Invalid sort parameter | Do not retry |
| `INVALID_USER_ID` | 400 | Invalid UUID format | Do not retry |
| `USER_NOT_FOUND` | 404 | User does not exist | Do not retry |
| `EMAIL_ALREADY_EXISTS` | 409 | Email already registered | Do not retry |
| `UNAUTHORIZED` | 401 | Missing or invalid JWT token | Do not retry |
| `FORBIDDEN` | 403 | Not authorized for this operation | Do not retry |
| `USER_LOCKED` | 403 | User is locked | Do not retry |
| `RATE_LIMITED` | 429 | Too many requests | Retry after `Retry-After` seconds |
| `INTERNAL_ERROR` | 500 | Internal server error | Retry with exponential backoff |
| `SERVICE_UNAVAILABLE` | 503 | Service temporarily unavailable | Retry with exponential backoff |

### Retry Policy

**Client-side retry behavior:**
- **4xx errors**: Do not retry (except 429)
- **429 Rate Limited**: Retry after `Retry-After` header value (in seconds)
- **5xx errors**: Retry with exponential backoff (1s, 2s, 4s max 3 retries)
- **Network errors**: Retry with exponential backoff (1s, 2s, 4s, 8s, 16s max 5 retries)

---

## Versioning Strategy

### Versioning Approach

We use **URL path versioning** for this API.

**Example:**
- Version 1: `https://api.example.com/v1/users`
- Version 2: `https://api.example.com/v2/users`

### Current Version

**Version:** 1.0.0
**Released:** 2024-01-15
**Deprecation:** N/A (not deprecated)

### Version History

| Version | Date | Changes | Breaking? |
|---------|------|---------|-----------|
| 1.0.0 | 2024-01-15 | Initial release | - |

### Backwards Compatibility

**Breaking changes require:**
- New major version (2.0.0)
- Minimum 6 months notice before deprecation
- Migration guide provided to API consumers
- Existing versions supported during grace period (6 months after new version release)

**Non-breaking changes:**
- Adding new optional fields to responses
- Adding new query parameters
- Adding new endpoints

---

## Security Considerations

### Authentication

**Method: JWT Bearer Tokens**

Clients must include a JWT token in the `Authorization` header:

```http
Authorization: Bearer {jwt_token}
```

**Token format:**
- **Issuer:** `https://auth.example.com`
- **Audience:** `https://api.example.com`
- **Expiration:** 1 hour
- **Algorithm:** RS256

**Token validation:**
- Token is validated by Profile Service via Auth Service
- Invalid or expired tokens result in `401 Unauthorized`

### Authorization

**Method: Role-Based Access Control (RBAC)**

**Permissions:**

| Role | Permissions |
|------------|-------------|
| `user` | Read own profile, update own profile |
| `admin` | Read any profile, update any profile, delete profiles |
| `service` | Full access (service-to-service communication) |

**Authorization rules:**
- Users can only read/update their own profile (unless they are `admin`)
- Only `admin` role can delete profiles
- Service accounts (identified by `role: service` in JWT) have full access

### Data Security

**Encryption:**
- **In transit:** TLS 1.3 required (HTTPS only, HTTP is rejected)
- **At rest:** AES-256 encryption for PostgreSQL database

**Sensitive data:**
- **Passwords** are hashed using bcrypt (cost factor 12) before storage
- **Passwords** are never returned in API responses
- **PII** (email, name) is encrypted at rest in PostgreSQL
- **Audit logging** for all write operations (create, update, delete)

**Logging restrictions:**
- Passwords are never logged
- JWT tokens are never logged (only token IDs for tracing)

### Rate Limiting

| Tier | Limit | Time Window |
|------|-------|-------------|
| Free | 100 requests | 1 hour |
| Pro | 1,000 requests | 1 hour |
| Enterprise | Unlimited | - |

**Headers:**
- `X-RateLimit-Limit`: Request limit per time window
- `X-RateLimit-Remaining`: Remaining requests in current window
- `X-RateLimit-Reset`: Unix timestamp when window resets

**Rate limit exceeded response:**

```http
HTTP/1.1 429 Too Many Requests
Content-Type: application/json
Retry-After: 3600

{
  "error": "RATE_LIMITED",
  "message": "Rate limit exceeded. Try again in 3600 seconds.",
  "request_id": "req_abc123xyz"
}
```

---

## Performance Requirements

### Latency

| Operation | Target (p50) | Target (p95) | Target (p99) |
|-----------|-------------|-------------|-------------|
| GET /users/{id} | 50ms | 100ms | 200ms |
| POST /users | 100ms | 200ms | 500ms |
| PATCH /users/{id} | 75ms | 150ms | 300ms |
| DELETE /users/{id} | 50ms | 100ms | 200ms |
| GET /users (list) | 200ms | 500ms | 1000ms |

**Assumptions:**
- Cache hit rate of 70% for GET /users/{id}
- Database queries are optimized (proper indexes)
- Network latency is <10ms within data center

### Throughput

| Metric | Target | Notes |
|--------|--------|-------|
| Requests per second | 5,000 | Per instance (horizontal scalable) |
| Concurrent connections | 1,000 | Max concurrent connections per instance |

### Resource Limits

| Resource | Limit | Notes |
|----------|-------|-------|
| Request size | 1 MB | Max request body size |
| Response size | 10 MB | Max response size |
| Request timeout | 30s | Max duration for any request |
| Page size (list) | 100 | Max results per page |

---

## Testing Requirements

### Unit Tests

**Coverage requirement:** 85%

**Key test scenarios:**
- [ ] All endpoint handlers (success path)
- [ ] All validation errors (4xx responses)
- [ ] Database error handling (5xx responses)
- [ ] Authentication/authorization enforcement
- [ ] Rate limiting enforcement
- [ ] Data model serialization/deserialization
- [ ] Pagination logic
- [ ] Field selection logic

### Integration Tests

**Test coverage:**
- [ ] API endpoint testing with real PostgreSQL
- [ ] Authentication flow with real Auth Service
- [ ] Cache integration with real Redis (if enabled)
- [ ] Error handling with external service failures

**Test environment:** Staging environment with production-like data

### Contract Tests

**Purpose:** Verify API compatibility with frontend consumers

**Test scenarios:**
- [ ] Request/response format validation
- [ ] Error response format validation
- [ ] Required fields presence check
- [ ] Data type validation
- [ ] Field selection functionality
- [ ] Pagination functionality

### Performance Tests

**Load testing:**
- **Target load:** 5,000 requests/second
- **Duration:** 1 hour
- **Success criteria:**
  - p95 latency < 500ms
  - Error rate < 0.1%
  - No memory leaks
  - Database CPU < 70%

---

## Examples

### Example 1: Create User

**Scenario:** Create a new user account

**Request:**

```bash
curl -X POST https://api.example.com/v1/users \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Il..." \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "SecurePass123",
    "role": "user"
  }'
```

**Response (Success):**

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/v1/users/123e4567-e89b-12d3-a456-426614174000

{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "John Doe",
  "email": "john@example.com",
  "role": "user",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

**Response (Error - Duplicate Email):**

```http
HTTP/1.1 409 Conflict
Content-Type: application/json

{
  "error": "EMAIL_ALREADY_EXISTS",
  "message": "A user with email john@example.com already exists",
  "request_id": "req_abc123xyz"
}
```

### Example 2: Get User with Field Selection

**Scenario:** Retrieve user profile, requesting only specific fields

**Request:**

```bash
curl -X GET "https://api.example.com/v1/users/123e4567-e89b-12d3-a456-426614174000?fields=name,email" \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Il..."
```

**Response (Success):**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com"
}
```

### Example 3: Update User

**Scenario:** Update user's name

**Request:**

```bash
curl -X PATCH https://api.example.com/v1/users/123e4567-e89b-12d3-a456-426614174000 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Il..." \
  -d '{
    "name": "Jane Doe"
  }'
```

**Response (Success):**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "Jane Doe",
  "email": "john@example.com",
  "role": "user",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-15T10:35:00Z"
}
```

### Example 4: List Users with Pagination

**Scenario:** List users with pagination and role filter

**Request:**

```bash
curl -X GET "https://api.example.com/v1/users?page=1&limit=20&role=user&sort=created_at:desc" \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Il..."
```

**Response (Success):**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "data": [
    {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "name": "John Doe",
      "email": "john@example.com",
      "role": "user",
      "created_at": "2024-01-01T00:00:00Z"
    },
    {
      "id": "987fcdeb-51a2-43f1-a456-426614174000",
      "name": "Jane Smith",
      "email": "jane@example.com",
      "role": "user",
      "created_at": "2023-12-15T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "total_pages": 8
  }
}
```

### Example 5: Delete User

**Scenario:** Delete a user profile

**Request:**

```bash
curl -X DELETE https://api.example.com/v1/users/123e4567-e89b-12d3-a456-426614174000 \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Il..."
```

**Response (Success):**

```http
HTTP/1.1 204 No Content
```

**Response (Error - User Not Found):**

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "error": "USER_NOT_FOUND",
  "message": "User with ID 123e4567-e89b-12d3-a456-426614174000 not found",
  "request_id": "req_xyz789abc"
}
```

---

## References

### Related Documents

- [RFC-001: Profile Service Architecture](/docs/rfc/rfc-001-profile-service.md) - Architectural design for Profile Service
- [ADR-003: PostgreSQL vs MongoDB](/docs/adr/003-database-choice.md) - Database selection decision
- [TSD-002: Media Service API](/docs/tsd/002-media-service.md) - Profile image upload API
- [TSD-003: Auth Service API](/docs/tsd/003-auth-service.md) - Authentication service specification

### External References

- [OpenAPI 3.0 Specification](https://spec.openapis.org/oas/v3.0.0) - API documentation standard
- [RFC 7231: HTTP/1.1](https://tools.ietf.org/html/rfc7231) - HTTP semantics and status codes
- [JWT Handbook](https://jwt.io/introduction) - JWT best practices
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) - API security guidelines

---

## Appendix

### Glossary

| Term | Definition |
|------|------------|
| UUID | Universally Unique Identifier, 128-bit identifier used to uniquely identify information in computer systems |
| JWT | JSON Web Token, a compact URL-safe means of representing claims to be transferred between two parties |
| RBAC | Role-Based Access Control, an approach to restricting system access to authorized users based on their role |
| bcrypt | A password hashing function based on the Blowfish cipher, designed for secure password storage |

### Implementation Notes

**Database Schema:**

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(20) NOT NULL DEFAULT 'user',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);
```

**Cache Key Format (Redis):**
- User profile: `user:profile:{user_id}`
- User list: `user:list:{page}:{limit}:{filters_hash}`

**Monitoring:**
- Metrics exported to Prometheus on `/metrics` endpoint
- Key metrics:
  - `api_request_duration_seconds` (histogram)
  - `api_requests_total` (counter)
  - `api_errors_total` (counter)
  - `api_cache_hits_total` (counter)
  - `api_cache_misses_total` (counter)

---

## Change Log

| Version | Date | Author | Changes | Breaking? |
|---------|------|--------|---------|-----------|
| 1.0.0 | 2024-01-15 | Jane Smith | Initial release | - |
