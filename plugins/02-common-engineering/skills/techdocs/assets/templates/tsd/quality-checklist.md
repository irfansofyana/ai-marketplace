# TSD Quality Checklist

> **Purpose**: Internal validation checklist for TSDs. Use this to self-review before submitting for review, and during peer review to provide structured feedback.

---

## Checklist Overview

This checklist is organized by TSD sections. Each section has:
- **Required elements** - Must-haves for this section
- **Quality indicators** - Signs of high-quality content
- **Common issues** - Problems to watch for

---

## 1. Abstract

### Required Elements
- [ ] States what is being specified
- [ ] States technical scope (APIs, data models, interfaces)
- [ ] States target audience
- [ ] 2-3 sentences only (under 100 words)

### Quality Indicators
- Technical scope is clear
- Target audience is identified
- No ambiguity about what the spec covers

### Common Issues
- ❌ Too long (>100 words)
- ❌ Missing technical scope
- ❌ Missing target audience
- ❌ Vague ("specifies an API" vs "specifies User Profile API endpoints")

---

## 2. Overview

### 2.1 Purpose

#### Required Elements
- [ ] States what TSD specifies
- [ ] References related RFC/ADR (if applicable)
- [ ] States high-level technical approach

#### Quality Indicators
- Technical focus (not business problem)
- Links to related RFC/ADR
- Clear scope statement

#### Common Issues
- ❌ Business problem instead of technical problem
- ❌ No reference to related RFC/ADR
- ❌ Vague technical approach

### 2.2 Scope

#### Required Elements
- [ ] In-scope items listed
- [ ] Out-of-scope items listed
- [ ] Scope is specific and clear

#### Quality Indicators
- Scope boundaries are clear
- Out-of-scope items are explicit
- No ambiguity

#### Common Issues
- ❌ No out-of-scope items listed
- ❌ Scope is too vague
- ❌ Scope creep (includes too much)

### 2.3 System Context

#### Required Elements
- [ ] System/service identified
- [ ] Interactions with other systems documented
- [ ] Dependencies listed

#### Quality Indicators
- System boundaries are clear
- All dependencies listed
- Interactions are documented

#### Common Issues
- ❌ No system context
- ❌ Dependencies not listed
- ❌ Interactions with other systems missing

---

## 3. API Endpoints / Methods

> **Skip this section if TSD is not an API specification**

### Required Elements
- [ ] All endpoints are documented
- [ ] Each endpoint has:
  - [ ] Purpose statement
  - [ ] HTTP method and path
  - [ ] Request format (headers, body, parameters)
  - [ ] Response format (success and error)
  - [ ] Parameters table (name, type, required, description, validation)
  - [ ] Error codes table
  - [ ] Examples (request and response)

### Quality Indicators
- Request/response formats are complete
- Parameters are fully specified with validation
- Error codes are specific (not generic)
- Examples are runnable
- Rate limiting is specified

### Common Issues
- ❌ Missing endpoints
- ❌ Incomplete parameter tables (missing validation)
- ❌ Generic error codes (just "ERROR")
- ❌ No examples
- ❌ Examples don't match specification
- ❌ No rate limiting specified

---

## 4. Data Models / Schemas

### Required Elements
- [ ] All models are documented
- [ ] Each model has:
  - [ ] Purpose statement
  - [ ] Fields table (name, type, required, description, constraints)
  - [ ] Example JSON
  - [ ] Validation rules

### Quality Indicators
- All fields are documented with types
- Required vs optional is clear
- Validation rules are specified
- Examples are valid JSON
- Relationships are documented

### Common Issues
- ❌ Missing fields in documentation
- ❌ No validation rules
- ❌ Required vs optional not specified
- ❌ Examples are invalid JSON
- ❌ Relationships not documented

---

## 5. Interface Contracts

> **Skip this section if TSD is not defining programming interfaces**

### Required Elements
- [ ] All interfaces are documented
- [ ] Each interface has:
  - [ ] Purpose statement
  - [ ] Methods table (name, input, output, description)
  - [ ] Contract specification (type definition)
  - [ ] Implementation requirements

### Quality Indicators
- All methods are documented
- Input/output types are specified
- Contract is unambiguous
- Implementation requirements are clear

### Common Issues
- ❌ Missing methods
- ❌ Input/output types not specified
- ❌ Contract is vague
- ❌ No implementation requirements

---

## 6. Error Handling

### Required Elements
- [ ] Error categories are defined
- [ ] Error response format is specified
- [ ] All error codes are documented
- [ ] Retry policy is specified

### Quality Indicators
- Error format is consistent
- Error codes are specific
- Retry policy is clear
- Error categories are logical

### Common Issues
- ❌ No error response format
- ❌ Generic error codes
- ❌ No retry policy
- ❌ Error categories not defined

---

## 7. Versioning Strategy

### Required Elements
- [ ] Versioning approach is specified
- [ ] Current version is documented
- [ ] Version history is maintained
- [ ] Breaking changes are marked
- [ ] Deprecation policy is defined

### Quality Indicators
- Versioning approach is clear
- Semantic versioning is used
- Breaking changes are clearly marked
- Deprecation policy is reasonable

### Common Issues
- ❌ No versioning approach specified
- ❌ No version history
- ❌ Breaking changes not marked
- ❌ No deprecation policy

---

## 8. Security Considerations

### Required Elements
- [ ] Authentication method is specified
- [ ] Authorization model is defined
- [ ] Data encryption requirements are stated
- [ ] Rate limiting is specified
- [ ] PII/sensitive data handling is documented

### Quality Indicators
- Authentication is industry-standard
- Authorization model is clear
- Encryption requirements are specific (TLS version, cipher)
- Rate limiting tiers are defined
- Sensitive data handling is addressed

### Common Issues
- ❌ No authentication specified
- ❌ No authorization model
- ❌ Vague encryption ("encrypted" vs "TLS 1.3, AES-256")
- ❌ No rate limiting
- ❌ PII/sensitive data not addressed

---

## 9. Performance Requirements

### Required Elements
- [ ] Latency targets are specified (p50, p95, p99)
- [ ] Throughput targets are defined
- [ ] Resource limits are documented

### Quality Indicators
- Percentiles are specified (not just "average")
- Latency targets are specific
- Throughput is measurable
- Resource limits are defined

### Common Issues
- ❌ No latency targets
- ❌ "Average" latency only (need percentiles)
- ❌ No throughput target
- ❌ No resource limits

---

## 10. Testing Requirements

### Required Elements
- [ ] Unit test coverage target is specified
- [ ] Integration test scenarios are listed
- [ ] Contract tests are defined (if applicable)
- [ ] Performance test criteria are defined

### Quality Indicators
- Coverage target is specified (percentage)
- Test scenarios are specific
- Performance tests have success criteria
- Contract tests verify compatibility

### Common Issues
- ❌ No coverage target
- ❌ Vague test scenarios ("test endpoints")
- ❌ No performance tests
- ❌ No contract tests (for APIs)

---

## 11. Examples

### Required Elements
- [ ] Examples cover major use cases
- [ ] Each example has:
  - [ ] Scenario description
  - [ ] Complete request
  - [ ] Complete response
  - [ ] Both success and error cases (where applicable)

### Quality Indicators
- Examples are complete and runnable
- Examples use realistic data
- Both success and error cases shown
- cURL/HTTP examples for APIs

### Common Issues
- ❌ No examples
- ❌ Incomplete examples (missing headers, body)
- ❌ Placeholder data only
- ❌ Only success cases shown

---

## 12. References

### Required Elements
- [ ] Related documents are linked
- [ ] External references are relevant
- [ ] Links are accurate

### Quality Indicators
- Related RFC/ADR are referenced
- External standards are linked
- Links work

### Common Issues
- ❌ No references
- ❌ Broken links
- ❌ No descriptions for links

---

## 13. Appendix

### Required Elements
- [ ] Glossary defines technical terms (if needed)
- [ ] Implementation details are accurate (if included)

### Quality Indicators
- Terms are clearly defined
- Implementation details are helpful
- Appendix is truly optional

### Common Issues
- ❌ Glossary missing when jargon used
- ❌ Implementation details are inaccurate
- ❌ Appendix contains essential content

---

## 14. Change Log

### Required Elements
- [ ] All changes are documented
- [ ] Version numbers follow semantic versioning
- [ ] Breaking changes are clearly marked
- [ ] Dates and authors are recorded

### Quality Indicators
- Semantic versioning is used
- Breaking changes are flagged
- Change descriptions are clear

### Common Issues
- ❌ No change log
- ❌ Not following semantic versioning
- ❌ Breaking changes not marked

---

## Universal Discovery Integration Check

> **CRITICAL**: TSDs must integrate Universal Discovery output from Phase 1.

### Required Integration Points
- [ ] **Overview → Purpose**: References technical context from Universal Discovery
- [ ] **Overview → System Context**: Uses Universal Discovery "Technical Context"
- [ ] **Performance Requirements**: Uses Universal Discovery "State Gap" for targets
- [ ] **Testing Requirements**: Uses Universal Discovery "Team Context" for capacity
- [ ] **References**: Links to Universal Discovery "Related Documents" (if provided)

### Quality Indicators
- System context is accurate (from Universal Discovery)
- Performance targets are quantified (from gap analysis)
- Related documents are referenced
- Technical approach is validated

### Common Issues
- ❌ Overview doesn't reference technical context
- ❌ Performance targets are vague (no specific numbers)
- ❌ No system context
- ❌ Related documents not referenced

---

## Critical Go/No-Go Criteria

A TSD is **READY FOR REVIEW** when:

- ✅ All required sections are complete
- ✅ All endpoints/methods are fully documented (for API specs)
- ✅ All data models are fully specified
- ✅ All error codes are documented
- ✅ Examples are complete and runnable
- ✅ Performance requirements are quantified
- ✅ Security considerations are addressed
- ✅ Universal Discovery output is integrated

A TSD is **NOT READY** if any of these are true:

- ❌ Missing endpoint/method documentation
- ❌ Incomplete data model specifications
- ❌ Generic error codes (not specific)
- ❌ No examples or incomplete examples
- ❌ Vague performance requirements (no specific numbers)
- ❌ No security considerations
- ❌ No system context

---

## Reviewer Guidelines

### When Reviewing a TSD

1. **Check Universal Discovery integration first**: Is the technical context accurate?
2. **Verify API endpoint completeness**: Are all endpoints fully documented with request/response?
3. **Check data model completeness**: Are all fields specified with validation?
4. **Verify error codes**: Are error codes specific and comprehensive?
5. **Check examples**: Are examples complete and runnable?
6. **Verify performance requirements**: Are targets quantified (p50, p95, p99)?
7. **Check security**: Is authentication, authorization, and data security addressed?

### Providing Feedback

- **Be specific**: Instead of "endpoint docs are incomplete", say "GET /users/{id} is missing the `fields` parameter in the documentation"
- **Reference sections**: Cite the section number (e.g., "Section 3: API Endpoints, GET /users/{id}")
- **Explain why**: Explain the reasoning behind feedback
- **Suggest improvements**: Offer concrete suggestions

---

## Common Review Comments

Here are common review comments organized by section:

### Abstract
- "Too long - aim for 2-3 sentences under 100 words"
- "Missing technical scope - what specifically does this TSD specify?"
- "Missing target audience - who is this for?"

### Overview
- "No technical context - what system does this apply to?"
- "Missing dependencies - what other systems does this interact with?"
- "Scope is vague - be specific about what's in/out of scope"

### API Endpoints
- "Missing endpoint documentation - [endpoint name] has no request/response format"
- "Parameters incomplete - [parameter] is missing validation rules"
- "Generic error codes - use specific codes like USER_NOT_FOUND instead of just ERROR"
- "No examples provided - add complete request/response examples"
- "Examples don't match spec - example shows field not in parameter table"

### Data Models
- "Missing field documentation - [field] is not documented"
- "No validation rules - specify constraints for [field]"
- "Required vs optional not clear - mark which fields are required"
- "Example invalid JSON - fix JSON syntax"

### Error Handling
- "No error response format - specify standard error structure"
- "Generic error codes - use descriptive codes"
- "No retry policy - specify which errors are retryable"

### Versioning
- "No versioning approach - specify URL path, header, or other approach"
- "No version history - maintain a change log"
- "Breaking changes not marked - flag breaking changes clearly"

### Security
- "No authentication specified - how do clients authenticate?"
- "No authorization model - what permissions exist?"
- "Vague encryption - specify TLS version and cipher suite"
- "No rate limiting - specify request limits"

### Performance
- "No latency targets - specify p50, p95, p99 targets"
- "Average latency only - need percentiles, not just average"
- "No throughput target - specify requests/second"

### Testing
- "No coverage target - specify unit test coverage percentage"
- "Vague test scenarios - be specific about what to test"
- "No performance tests - add load testing criteria"

### Examples
- "No examples - add complete request/response examples"
- "Incomplete examples - missing headers or body"
- "Placeholder data only - use realistic data"
- "Only success cases - add error examples"

### Universal Discovery Integration
- "No technical context - system context from Universal Discovery not used"
- "Performance targets vague - use quantified targets from gap analysis"
- "Related documents not referenced - link to documents from Universal Discovery"
