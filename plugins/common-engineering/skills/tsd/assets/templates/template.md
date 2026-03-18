# TSD Template: Technical Specification Document

> **Purpose**: TSDs (Technical Specification Documents) provide detailed technical specifications for APIs, data models, interfaces, and implementation details. They focus on "how" something is built at a technical level.

---

## [TSD Title]

**Author:** [Name, Team]
**Status:** [Draft | In Review | Approved | Implemented | Deprecated]
**Created:** [YYYY-MM-DD]
**Last Updated:** [YYYY-MM-DD]

---

## Abstract

> A concise summary (2-3 sentences) of what this TSD specifies and its technical scope.

**Template:**
> This TSD specifies the technical implementation of [brief description]. It covers [key technical areas: APIs, data models, interfaces]. This specification is intended for [target audience: implementers, API consumers, integration partners].

---

## Overview

> **Uses Universal Discovery Output**: This section uses validated problem information to establish technical context.

### Purpose

**Template:**
> This TSD specifies the technical implementation of [what]. It addresses the problem identified in the RFC/ADR: [brief problem summary]. The technical solution is [high-level approach].

### Scope

**What is covered:**
- [ ] [Scope item 1]
- [ ] [Scope item 2]
- [ ] [Scope item 3]

**What is NOT covered:**
- [ ] [Out of scope item 1]
- [ ] [Out of scope item 2]

### System Context

**Template:**
> This specification applies to [system/service/component]. It interacts with [related systems, APIs, databases].

**Dependencies:**
- [Dependency 1]: [Description]
- [Dependency 2]: [Description]

---

## API Endpoints / Methods

> **If this is an API specification, detail all endpoints here.**

### Endpoint Group: [Group Name]

#### [METHOD] /path/to/resource

**Purpose:** [What this endpoint does]

**Request:**

```http
METHOD /path/to/resource HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer {token}

# Request body
{
  "field1": "value1",
  "field2": "value2"
}
```

**Parameters:**

| Name | Type | Required | Description | Validation |
|------|------|----------|-------------|------------|
| `param1` | string | Yes | Description | Regex/Format |
| `param2` | integer | No | Description | Min/Max |

**Response (Success):**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "field1": "value1",
  "field2": "value2
}
```

**Response (Error):**

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "error": "error_code",
  "message": "Human-readable error message",
  "details": {}
}
```

**Error Codes:**

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `ERROR_CODE_1` | 400 | Description |
| `ERROR_CODE_2` | 404 | Description |

**Rate Limiting:**
- **Limit:** [X] requests per [time period]
- **Headers:** `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`

---

## Data Models / Schemas

> **Define all data structures used by the system.**

### Model: [Model Name]

**Purpose:** [What this model represents]

**Fields:**

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| `field1` | string | Yes | Description | Max length, format |
| `field2` | integer | No | Description | Min, max |
| `field3` | enum | Yes | Description | Values: [a, b, c] |

**Example:**

```json
{
  "field1": "example value",
  "field2": 123,
  "field3": "a"
}
```

**Validation Rules:**
- [Rule 1]: [Description]
- [Rule 2]: [Description]

---

## Interface Contracts

> **Define interfaces between components, services, or modules.**

### Interface: [Interface Name]

**Purpose:** [What this interface does]

**Methods:**

| Method | Input | Output | Description |
|--------|-------|--------|-------------|
| `method1` | Type | Type | Description |
| `method2` | Type | Type | Description |

**Contract Specification:**

```typescript
// TypeScript example (or use your language)
interface InterfaceName {
  method1(input: InputType): Promise<OutputType>;
  method2(input: InputType): OutputType;
}
```

**Implementation Requirements:**
- [Requirement 1]
- [Requirement 2]

---

## Error Handling

> **Define how errors are handled across the system.**

### Error Categories

| Category | Description | HTTP Status Range |
|----------|-------------|-------------------|
| Client Errors | Invalid input, validation failures | 4xx |
| Server Errors | System failures, bugs | 5xx |
| Rate Limiting | Too many requests | 429 |

### Error Response Format

**All errors follow this format:**

```json
{
  "error": "ERROR_CODE",
  "message": "Human-readable message",
  "request_id": "unique-request-id",
  "details": {
    "field": "Additional context"
  }
}
```

### Error Codes

| Error Code | HTTP Status | Message | Retry Policy |
|------------|-------------|---------|--------------|
| `VALIDATION_ERROR` | 400 | Invalid input | Do not retry |
| `NOT_FOUND` | 404 | Resource not found | Do not retry |
| `RATE_LIMITED` | 429 | Too many requests | Retry after X seconds |
| `INTERNAL_ERROR` | 500 | System error | Retry with exponential backoff |

### Retry Policy

**Client-side retry behavior:**
- **4xx errors**: Do not retry (except 429)
- **429 Rate Limited**: Retry after `Retry-After` header
- **5xx errors**: Retry with exponential backoff (max 3 retries)
- **Network errors**: Retry with exponential backoff (max 5 retries)

---

## Versioning Strategy

> **Define how the API/interface is versioned.**

### Versioning Approach

- [ ] URL path versioning: `/v1/resource`, `/v2/resource`
- [ ] Header versioning: `Accept: application/vnd.api.v1+json`
- [ ] Query parameter versioning: `?version=1`
- [ ] No versioning (internal API)

### Current Version

**Version:** [X.X.X]
**Released:** [YYYY-MM-DD]
**Deprecation:** [YYYY-MM-DD or N/A]

### Version History

| Version | Date | Changes | Breaking? |
|---------|------|---------|-----------|
| 2.0.0 | YYYY-MM-DD | Description of changes | Yes |
| 1.1.0 | YYYY-MM-DD | Description of changes | No |

### Backwards Compatibility

**Breaking changes require:**
- [ ] New major version
- [ ] Minimum [X] months notice before deprecation
- [ ] Migration guide provided
- [ ] Existing clients supported during grace period

---

## Security Considerations

### Authentication

**Method:**
- [ ] API Keys
- [ ] JWT Tokens
- [ ] OAuth 2.0
- [ ] Mutual TLS
- [ ] No authentication (internal)

**Specification:**
- [How authentication works]

### Authorization

**Method:**
- [ ] Role-Based Access Control (RBAC)
- [ ] Scope-based permissions
- [ ] Resource-based permissions
- [ ] No authorization (all access)

**Permissions:**

| Scope/Role | Permissions |
|------------|-------------|
| `read` | Read-only access |
| `write` | Read and write access |
| `admin` | Full access |

### Data Security

**Encryption:**
- **In transit:** TLS 1.3 required
- **At rest:** AES-256 encryption

**Sensitive data:**
- [ ] PII is encrypted at rest
- [ ] Credentials are never logged
- [ ] Audit logging for sensitive operations

### Rate Limiting

| Tier | Limit | Time Window |
|------|-------|-------------|
| Free | 100 requests | 1 hour |
| Pro | 1000 requests | 1 hour |
| Enterprise | Unlimited | - |

---

## Performance Requirements

### Latency

| Operation | Target (p50) | Target (p95) | Target (p99) |
|-----------|-------------|-------------|-------------|
| Read operation | 50ms | 100ms | 200ms |
| Write operation | 100ms | 200ms | 500ms |
| List operation | 200ms | 500ms | 1000ms |

### Throughput

| Metric | Target | Notes |
|--------|--------|-------|
| Requests per second | 10,000 | Per instance |
| Concurrent connections | 1,000 | Max concurrent |

### Resource Limits

| Resource | Limit | Notes |
|----------|-------|-------|
| Request size | 1 MB | Max payload |
| Response size | 10 MB | Max response |
| Request timeout | 30s | Max duration |

---

## Testing Requirements

### Unit Tests

**Coverage requirement:** [X]%

**Key test scenarios:**
- [ ] [Scenario 1]
- [ ] [Scenario 2]

### Integration Tests

**Test coverage:**
- [ ] API endpoint testing
- [ ] Database integration
- [ ] External service integration

### Contract Tests

**Purpose:** Verify compatibility between services

**Test scenarios:**
- [ ] Request/response format validation
- [ ] Error handling validation
- [ ] Version compatibility

### Performance Tests

**Load testing:**
- **Target load:** [X] requests/second
- **Duration:** [X] hours
- **Success criteria:** [p95 latency < X, error rate < Y%]

---

## Examples

### Example 1: [Use Case Name]

**Scenario:** [Description of the use case]

**Request:**

```bash
curl -X POST https://api.example.com/v1/resource \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {token}" \
  -d '{
    "field1": "value1",
    "field2": "value2"
  }'
```

**Response:**

```json
{
  "id": "123",
  "field1": "value1",
  "field2": "value2",
  "created_at": "2024-01-01T00:00:00Z"
}
```

### Example 2: [Use Case Name]

**Scenario:** [Description of the use case]

[Request/Response examples]

---

## References

### Related Documents

- [RFC: Related RFC Title](/path/to/rfc.md) - [Brief description]
- [ADR: Related ADR Title](/path/to/adr.md) - [Brief description]
- [TSD: Related TSD Title](/path/to/tsd.md) - [Brief description]

### External References

- [External Spec/Standard](https://example.com) - [What it provides]
- [Documentation](https://example.com) - [What it provides]

---

## Appendix

### Glossary

| Term | Definition |
|------|------------|
| [Term 1] | [Definition] |
| [Term 2] | [Definition] |

### Implementation Notes

> Additional technical details useful for implementers.

---

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | Name | Initial version |
