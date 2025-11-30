# One-Pager Examples

This file contains completed example one-pagers that demonstrate the expected quality and format. Use these as references when helping users create their own documents.

---

## Example 1: Authentication Migration

# Proposal: Migrate Authentication to OAuth 2.0

## About this doc

This doc is a proposal for migrating our authentication system from custom tokens to OAuth 2.0 with Auth0. Upon approval, we will prioritize this as a Q1 project and produce a full Technical Specification Document.

| Sign off deadline | December 15, 2024 |
|---|---|
| Status | Draft |
| Author(s) | Jane Smith, Alex Chen |

### Sign offs

- Sarah Kim (Engineering Manager) - Pending
- Mike Johnson (Platform Tech Lead) - Pending
- Lisa Park (Product Manager) - Pending
- David Lee (Security Lead) - Pending

## Problem

Our current authentication system uses a custom token-based approach built in 2019. This system has several critical limitations:

1. **No SSO support**: Enterprise customers must maintain separate credentials, causing friction and security concerns
2. **Maintenance burden**: The custom auth code requires ~5 hours/week of engineering maintenance
3. **Security debt**: The implementation predates current security best practices and lacks features like MFA enforcement

**Impact**:
- 40% of enterprise prospects cite "no SSO" as a deal blocker (per Sales)
- Support handles 15 password reset tickets/week from enterprise users
- 3 security audit findings related to auth in the last year

## High level goal

Enable modern authentication with SSO support, improving enterprise sales conversion and reducing maintenance overhead.

**Success metrics**:
- 100% of enterprise customers can configure SSO within 30 days of contract signing
- Reduce auth-related support tickets by 80%
- Zero security audit findings related to authentication
- Reduce auth maintenance to <1 hour/week

### What happens if we don't solve this

- Continue losing ~$2M ARR annually in enterprise deals blocked by SSO requirements
- Accumulate more security debt; risk of security incident increases
- Engineering continues spending 260 hours/year on maintenance
- Fall further behind competitors (Acme Corp launched SSO 6 months ago)

## Proposed solution: Auth0 Integration

We recommend implementing OAuth 2.0 with OpenID Connect using Auth0 as our identity provider.

**Why Auth0**:
- Industry-standard protocols (OAuth 2.0, OIDC, SAML)
- Native support for enterprise SSO providers (Okta, Azure AD, Google Workspace)
- Built-in MFA, anomaly detection, and compliance certifications (SOC 2, GDPR)
- Managed service reduces maintenance burden

**High-level approach**:
1. Integrate Auth0 SDK into web and mobile applications
2. Migrate existing users with zero-downtime parallel auth period
3. Enable self-service SSO configuration for enterprise customers
4. Deprecate legacy auth system after 90-day transition

**Estimated effort**: 6-8 weeks with 2 engineers

### Alternatives

#### Alternative 1: Build custom OAuth implementation

**Pros**:
- Full control over implementation
- No vendor dependency
- No licensing costs

**Cons**:
- 6+ months engineering effort
- Ongoing maintenance burden
- Security risk of custom implementation
- No enterprise SSO connectors out of the box

**Why not chosen**: Engineering effort and security risk outweigh benefits.

#### Alternative 2: Cognito (AWS)

**Pros**:
- Already in AWS ecosystem
- Lower cost than Auth0

**Cons**:
- More complex SSO configuration
- Weaker enterprise connector support
- Less intuitive admin experience

**Why not chosen**: Enterprise SSO support is critical; Auth0 has better connector ecosystem.

#### Alternative 3: Do nothing

**Pros**:
- No immediate investment required

**Cons**:
- Problems continue and compound
- Competitive disadvantage grows

**Why not chosen**: Cost of inaction exceeds cost of change.

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Auth0 pricing increases | Medium | Medium | Negotiate 3-year contract; abstract auth layer for portability |
| Migration disrupts users | Low | High | Parallel auth period; extensive testing; rollback plan |
| Integration complexity | Medium | Medium | POC with mobile app first; allocate buffer time |
| Team learning curve | Low | Low | Auth0 training; leverage their professional services |

### Open Questions

1. Should we support SAML in addition to OIDC for legacy enterprise systems?
2. What's the deprecation timeline for the legacy auth system?
3. Do we need to maintain session compatibility with mobile app v2.x?

---

## Example 2: Database Migration

# Proposal: Migrate from MongoDB to PostgreSQL

## About this doc

This doc proposes migrating our primary datastore from MongoDB to PostgreSQL. Upon approval, we will create a detailed migration plan and Technical Specification Document.

| Sign off deadline | January 30, 2025 |
|---|---|
| Status | Under Review |
| Author(s) | Carlos Rodriguez |

### Sign offs

- Emma Wilson (Engineering Director) - Pending
- James Brown (DBA Lead) - Pending
- Nina Patel (Backend Tech Lead) - Pending

## Problem

Our MongoDB deployment has become a bottleneck as we've scaled:

1. **Query performance**: Complex aggregations take 10-30 seconds; blocking product features
2. **Data integrity**: Lack of schema enforcement has led to inconsistent data across collections
3. **Operational cost**: MongoDB Atlas costs have grown 300% YoY as data volume increased
4. **Expertise gap**: Team has stronger SQL skills; MongoDB expertise limited to 2 engineers

**Impact**:
- P95 latency for dashboard queries is 8 seconds (target: <2s)
- 3 data quality incidents in last quarter required manual cleanup
- $45K/month in MongoDB Atlas costs
- Feature velocity slowed due to query complexity

## High level goal

Migrate to PostgreSQL to improve query performance, data integrity, and reduce operational costs.

**Success metrics**:
- P95 dashboard query latency <2 seconds
- Zero data integrity incidents
- 40% reduction in database costs
- All engineers can effectively work with the database

### What happens if we don't solve this

- Query performance will continue degrading as data grows
- Data quality issues will increase customer-facing bugs
- Database costs will reach $80K/month by end of year
- Feature development remains constrained by MongoDB limitations

## Proposed solution: PostgreSQL on AWS RDS

We recommend migrating to PostgreSQL 15 on AWS RDS with a phased approach.

**Why PostgreSQL**:
- Superior query performance for our access patterns (relational with complex joins)
- Strong schema enforcement prevents data integrity issues
- Team expertise (8 of 10 engineers have PostgreSQL experience)
- Better cost scaling with RDS vs MongoDB Atlas

**High-level approach**:
1. **Phase 1** (4 weeks): Set up PostgreSQL, migrate read-heavy reporting tables
2. **Phase 2** (6 weeks): Migrate core transactional tables with dual-write
3. **Phase 3** (2 weeks): Cutover remaining tables, decommission MongoDB

**Estimated effort**: 12 weeks with 2 engineers

### Alternatives

#### Alternative 1: Optimize MongoDB

**Pros**:
- No migration risk
- Faster to implement

**Cons**:
- Doesn't address fundamental schema issues
- Cost trajectory unchanged
- Limited performance improvement potential

**Why not chosen**: Addresses symptoms, not root causes.

#### Alternative 2: CockroachDB

**Pros**:
- Distributed SQL with horizontal scaling
- PostgreSQL wire-compatible

**Cons**:
- Higher operational complexity
- Limited team experience
- Higher cost than RDS PostgreSQL

**Why not chosen**: Our scale doesn't require distributed SQL; added complexity not justified.

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Data loss during migration | Low | Critical | Dual-write period; extensive validation; point-in-time recovery |
| Performance regression | Medium | High | Load testing before each phase; gradual traffic shift |
| Extended timeline | Medium | Medium | Phased approach limits blast radius; can pause between phases |
| Application bugs from schema changes | Medium | Medium | Comprehensive test coverage; staged rollout |

### Open Questions

1. Should we migrate all historical data or archive data older than 2 years?
2. What's the rollback plan if Phase 2 encounters critical issues?
3. Do we need read replicas from day one, or can we add later?

---

## Example 3: Process Change (Short One-Pager)

# Proposal: Adopt Trunk-Based Development

## About this doc

Proposal to shift from long-lived feature branches to trunk-based development with feature flags.

| Sign off deadline | November 15, 2024 |
|---|---|
| Status | Draft |
| Author(s) | Amy Zhang |

### Sign offs

- Tom Harris (Engineering Manager) - Pending
- Dev Team Leads (3) - Pending

## Problem

Our current branching strategy (long-lived feature branches) causes:
- Painful merge conflicts averaging 2 hours/week per engineer
- Delayed integration issues discovered late in development
- Slow release velocity (2-week average PR merge time)

## High level goal

Reduce merge conflicts and accelerate release velocity by adopting trunk-based development.

**Success metrics**:
- Average PR merge time <24 hours
- Merge conflict time reduced by 80%
- Deploy to production daily (vs weekly currently)

### What happens if we don't solve this

- Merge pain continues to frustrate engineers and slow delivery
- Integration issues continue being discovered late
- Release velocity remains a competitive disadvantage

## Proposed solution: Trunk-based development with feature flags

Adopt trunk-based development where all engineers commit to main daily, using feature flags to hide incomplete work.

**Key changes**:
1. PRs must be <400 lines and merge within 24 hours
2. Use LaunchDarkly for feature flags
3. Incomplete features hidden behind flags
4. CI/CD pipeline deploys main to production daily

### Alternatives

| Option | Why Not |
|--------|---------|
| Keep current process | Problems persist |
| GitFlow | More complex, doesn't solve core issues |
| Ship-show-ask | Partial solution, still has long branches |

### Risks

| Risk | Mitigation |
|------|------------|
| Incomplete code in production | Feature flags hide WIP; robust testing |
| Learning curve | Training sessions; pair programming during transition |
| Flag debt accumulation | Monthly flag cleanup review |

---

## Notes on These Examples

**Example 1** (Auth Migration) demonstrates:
- Full template usage with all sections
- Quantified problem statement
- Clear recommendation with rationale
- Multiple alternatives with honest trade-offs
- Risk table with mitigations

**Example 2** (Database Migration) demonstrates:
- Phased implementation approach
- Technical decision with cost analysis
- Clear success metrics

**Example 3** (Process Change) demonstrates:
- Shorter format for simpler proposals
- Works for non-technical changes
- Condensed alternatives and risks
