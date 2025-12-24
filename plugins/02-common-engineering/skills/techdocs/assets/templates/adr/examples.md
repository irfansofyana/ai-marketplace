# ADR Example: Choose PostgreSQL as Primary Database

> **Purpose**: This is a complete ADR example demonstrating how to document a technology choice decision with alternatives, criteria, trade-offs, and consequences.

---

## Universal Discovery Context

Before writing this ADR, the author completed Phase 1 (Universal Discovery) with the Problem Validation Gate.

**Universal Discovery Output**:
- **Current State**: Using SQLite for database; works for development but can't handle production load (5000 req/sec projected).
- **Evidence**: Load testing showed SQLite maxes out at 800 req/sec; write locks cause blocking; p95 latency increases from 50ms to 2000ms under load.
- **Who is Affected**: Backend team (blocked on scaling), Product team (can't launch production), Finance team (losing revenue due to performance issues).
- **Desired State**: Database that scales horizontally, supports ACID transactions for payments, and fits within $5K/month budget.
- **Technical Context**: Team has PostgreSQL experience; AWS infrastructure already selected; 3-month timeline to production.
- **Related Documents**: ADR-004 (Cloud Provider Selection - AWS), RFC-001 (Production Architecture)

This ADR uses this Universal Discovery output to establish decision context.

---

# ADR-005: Choose PostgreSQL as Primary Database

**Status:** Accepted
**Date:** 2024-09-10
**Decision Type:** Data Storage
**Deciders:** Jane Smith (Backend Tech Lead), Mike Johnson (Platform Team Lead), John Doe (Engineering Manager)
**Related ADRs:** ADR-002 (Database Strategy), ADR-004 (Cloud Provider Selection)

---

## Context

### Current Situation

Our application currently uses SQLite as its primary database. SQLite was chosen for MVP development because it required zero configuration and worked well for single-server deployments. However, we're now approaching production launch with projected traffic of 5000 requests/second. SQLite has several limitations that block our production readiness:

- **No concurrent write support**: SQLite uses database-level write locks, causing write operations to block each other
- **No horizontal scaling**: SQLite cannot be scaled horizontally (no read replicas)
- **Single-server limitation**: SQLite is a file-based database that requires direct file system access
- **Limited connection handling**: SQLite struggles with high connection counts

Load testing in August 2024 showed SQLite maxes out at approximately 800 req/sec with p95 latency degrading from 50ms to 2000ms. Our production projections require 5000 req/sec by Q4 2024.

### Drivers

- **Scalability requirement**: Must support 5000 req/sec by Q4 2024 (10x current capacity)
- **ACID compliance**: Payment processing requires full transaction support (regulatory requirement from finance team)
- **Team experience**: Backend team has strong PostgreSQL experience (3 engineers with 2+ years each)
- **Timeline constraint**: Production launch in 3 months (limited time for evaluating new technologies)
- **Budget constraint**: $5K/month maximum for database hosting (finance team approval)

Evidence from load testing:
- SQLite at 800 req/sec: p95 latency 2000ms, CPU 85%
- SQLite at 500 req/sec: p95 latency 120ms, CPU 45%
- Target: p95 latency < 200ms at 5000 req/sec

### Goals

- Support horizontal scaling for read operations via read replicas
- Maintain full ACID compliance for payment transactions
- Achieve 99.9% uptime (high availability requirement)
- Stay within $5K/month budget for database hosting
- Enable production launch within 3 months

### Non-Goals

- Multi-region deployment (single region is sufficient for current needs)
- NoSQL features (don't need flexible schemas)
- Real-time analytics (can use separate data warehouse for analytics)
- Global low-latency access (all users are in US region)

---

## Decision

We have chosen **PostgreSQL** (via AWS RDS) as our primary database.

**Description:**
PostgreSQL is an open-source relational database with full ACID compliance, read replica support, and a mature ecosystem. We will use AWS RDS PostgreSQL 15 with Multi-AZ deployment for high availability and 2 read replicas for horizontal scaling of read operations.

**Key Attributes:**
- **ACID compliant**: Full transaction support with serializable isolation level
- **Horizontal scaling**: Native read replica support (up to 15 replicas)
- **Managed service**: AWS RDS handles backups, patching, failover
- **Version**: PostgreSQL 15 (latest stable release with performance improvements)
- **Instance type**: db.r6g.xlarge (2 vCPU, 16GB RAM) for primary; db.r6g.large (2 vCPU, 8GB RAM) for replicas
- **Deployment**: Multi-AZ (primary in us-east-1a, standby in us-east-1b)
- **Read replicas**: 2 replicas (us-east-1a, us-east-1b) for read scaling

---

## Alternatives Considered

### Alternative 1: PostgreSQL (AWS RDS)

**Description:** Open-source relational database with ACID compliance and read replica support, hosted on AWS RDS managed service.

**Pros:**
- **ACID compliant**: Full transaction support for payment processing
- **Team experience**: 3 engineers have 2+ years PostgreSQL experience
- **Read replicas**: Native support for horizontal scaling (up to 15 replicas)
- **Cost effective**: $3K/month for Multi-AZ + 2 read replicas (within budget)
- **Mature ecosystem**: Extensive tooling, monitoring, and community support
- **AWS integration**: Seamless integration with our existing AWS infrastructure
- **Backup/restore**: Automated daily backups + point-in-time recovery (PITR)

**Cons:**
- **Vertical scaling for writes**: Single-master architecture requires larger instances for write scaling
- **Schema rigidity**: Migrations required for schema changes (vs NoSQL flexibility)
- **Operational overhead**: Requires DBA expertise for query optimization (though RDS reduces this)

**Estimated Impact:**
- **Cost:** $3K/month (db.r6g.xlarge + 2x db.r6g.large + backup storage)
- **Effort:** 3 weeks (team has experience, familiar with AWS RDS)
- **Risk:** Low (mature technology, team has experience)

### Alternative 2: MongoDB (AWS DocumentDB)

**Description:** NoSQL document database with flexible schema and horizontal sharding support, hosted on AWS DocumentDB.

**Pros:**
- **Horizontal scaling**: Native sharding support for both reads and writes
- **Flexible schema**: No migrations required for schema changes
- **Document model**: Natural fit for JSON data (our API uses JSON)
- **Managed service**: AWS DocumentDB handles operational tasks

**Cons:**
- **Limited ACID support**: ACID compliance at document level only, not across documents (problem for payment transactions)
- **No team experience**: Zero team members have MongoDB experience (learning curve)
- **Higher cost**: $4.5K/month for comparable performance (over budget)
- **Query complexity**: Aggregation framework is complex for relational-style queries
- **Transaction limitations**: Multi-document transactions have performance overhead

**Estimated Impact:**
- **Cost:** $4.5K/month (over $5K budget with buffer)
- **Effort:** 6-8 weeks (team needs to learn MongoDB, rewrite queries)
- **Risk:** Medium (new technology for team, ACID limitations for payments)

### Alternative 3: MySQL (AWS RDS)

**Description:** Open-source relational database similar to PostgreSQL, also ACID compliant with read replica support.

**Pros:**
- **ACID compliant**: Full transaction support
- **Team familiarity**: Team has basic MySQL experience (though less than PostgreSQL)
- **Read replicas**: Native support for horizontal scaling
- **Cost**: Similar to PostgreSQL at ~$2.8K/month

**Cons:**
- **Fewer features:** Lacks advanced PostgreSQL features (JSON support, extensions, advanced indexing)
- **Team preference:** Team prefers PostgreSQL for feature set and experience
- **Limited tooling:** Ecosystem and tooling less mature than PostgreSQL

**Estimated Impact:**
- **Cost:** $2.8K/month (slightly less than PostgreSQL)
- **Effort:** 3 weeks (similar to PostgreSQL)
- **Risk:** Low (mature technology)

---

## Decision Criteria

| Criterion | Weight | PostgreSQL | MongoDB | MySQL |
|-----------|--------|------------|---------|-------|
| Scalability (read/write) | High | Good (read replicas only) | Excellent (sharding) | Good (read replicas only) |
| ACID Compliance | High | Full | Limited (doc-level only) | Full |
| Team Experience | High | High (3 engineers, 2+ years) | None (learning curve) | Medium (basic experience) |
| Cost (monthly) | Medium | $3K (within budget) | $4.5K (over budget) | $2.8K (within budget) |
| Time to Implement | Medium | 3 weeks (familiar) | 6-8 weeks (learning) | 3 weeks (familiar) |
| Operational Overhead | Medium | Low (managed RDS) | Medium (sharding complex) | Low (managed RDS) |

**Criteria Definitions:**
- **Scalability:** Ability to handle 5000 req/sec with horizontal scaling for reads
- **ACID Compliance:** Full transaction support with serializable isolation for payment processing
- **Team Experience:** Number of engineers with experience and years of experience
- **Cost:** Monthly hosting cost including managed service fees
- **Time to Implement:** Estimated calendar weeks from start to production-ready
- **Operational Overhead:** Complexity of day-to-day operations (backups, patching, monitoring)

**Analysis:**
PostgreSQL scores highest on ACID Compliance (mandatory for payments) and Team Experience (reduces risk). MongoDB has the best scalability (sharding) but fails on ACID Compliance (critical blocker) and Cost (over budget). MySQL is a close second but lacks PostgreSQL's advanced features that the team values.

---

## Trade-offs Analysis

### Performance vs Simplicity

| Aspect | Trade-off | Impact |
|--------|-----------|--------|
| Write scaling | PostgreSQL requires vertical scaling for writes (larger instances) | May need to upgrade to db.r6g.2xlarge in 12-18 months (+$2K/month) |
| Query simplicity | SQL queries are simpler than MongoDB aggregations | Faster development, easier debugging, better maintainability |

### Cost vs Capability

| Aspect | Trade-off | Impact |
|--------|-----------|--------|
| Managed service cost | RDS costs more than self-hosted PostgreSQL (+$1K/month) | 24/7 AWS support, automated backups, patching included |
| Feature set | PostgreSQL has more features than MySQL | Better JSON support, extensions, advanced indexing (useful for future) |

### Time to Market vs Long-term Viability

| Aspect | Trade-off | Impact |
|--------|-----------|--------|
| Learning curve | Team knows PostgreSQL (no learning curve) vs MongoDB (6-8 week learning curve) | Faster time to production (3 weeks vs 6-8 weeks) |
| Future scaling | PostgreSQL read replicas scale reads, not writes | May need sharding in 2+ years (can migrate to distributed SQL then) |

---

## Consequences

### Positive Consequences

- **Scalability achieved:** Can scale to 5000 req/sec via read replicas (benefits: product team can launch, users get better performance)
- **ACID compliance maintained:** Full transaction support prevents payment errors (benefits: finance team, customers, regulatory compliance)
- **Team velocity:** Familiar technology speeds development (benefits: engineering team, product team - faster feature iteration)
- **Cost within budget:** $3K/month is under $5K budget (benefits: finance team)
- **Operational simplicity:** Managed RDS reduces operational overhead (benefits: platform team - less toil)
- **High availability:** Multi-AZ deployment provides 99.9% uptime SLA (benefits: all users)

### Negative Consequences

- **Write scaling limitation:** Single-master architecture limits write scaling (affects: backend team - may need larger instances in future)
- **Vendor lock-in:** Migration off RDS PostgreSQL would be effortful (affects: platform team - future flexibility)
- **Schema migration overhead:** Schema changes require migrations (affects: backend team - development overhead)
- **RDS cost increase:** RDS costs more than self-hosted (affects: finance team - higher ongoing cost)

### Risks Introduced

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Write performance becomes bottleneck | Medium | High | Monitor write latency; plan for sharding or distributed SQL in 2+ years |
| AWS RDS outage causes downtime | Low | High | Multi-AZ deployment provides 99.9% uptime; read replicas for failover |
| Cost overruns with scaling | Low | Medium | Budget alerts at 80%; review scaling needs quarterly; reserved instances for cost savings |
| Schema migrations cause downtime | Medium | Medium | Use zero-downtime migration tools (pgadmin, Sqitch); test migrations in staging |

### Risks Eliminated

- **SQLite blocking production:** PostgreSQL eliminates the "SQLite can't scale" blocker
- **Payment data inconsistency:** ACID compliance eliminates transaction inconsistency risks
- **Team learning curve delay:** Using familiar technology eliminates project delay risk

---

## Implementation Plan

### Phase 1: AWS RDS PostgreSQL Setup

**Goals:** Provision RDS PostgreSQL, configure Multi-AZ, set up read replicas

**Tasks:**
- [ ] Provision RDS PostgreSQL 15 (db.r6g.xlarge) in us-east-1a
- [ ] Configure Multi-AZ deployment with standby in us-east-1b
- [ ] Create 2 read replicas (db.r6g.large) in us-east-1a and us-east-1b
- [ ] Set up automated daily backups (retention: 30 days)
- [ ] Enable point-in-time recovery (PITR)
- [ ] Configure parameter groups (optimize for workload)
- [ ] Set up CloudWatch monitoring and alarms

**Owner:** Platform Team
**Timeline:** 1 week

### Phase 2: Database Migration

**Goals:** Migrate data from SQLite to PostgreSQL

**Tasks:**
- [ ] Install PostgreSQL client tools and libraries
- [ ] Write migration scripts (SQLite → PostgreSQL)
- [ ] Convert SQLite schema to PostgreSQL schema
- [ ] Test migration on staging data
- [ ] Execute production migration (planned downtime: 1 hour at 2AM Sunday)
- [ ] Verify data integrity (row count, checksums)
- [ ] Update application connection strings

**Owner:** Backend Team
**Timeline:** 1 week

### Phase 3: Application Deployment

**Goals:** Deploy application using PostgreSQL to production

**Tasks:**
- [ ] Update application configuration for PostgreSQL
- [ ] Deploy to staging, test thoroughly
- [ ] Load test staging with PostgreSQL (verify 5000 req/sec target)
- [ ] Deploy to production (blue-green deployment)
- [ ] Monitor metrics for 24 hours
- [ ] Enable read replica routing for read queries

**Owner:** Backend Team
**Timeline:** 1 week

### Rollout Strategy

- **Approach:** Big bang (complete cutover after migration)
- **Timeline:** 3 weeks total (Phase 1: week 1, Phase 2: week 2, Phase 3: week 3)
- **Success Criteria:**
  - [ ] All data migrated successfully (100% row count match, 0 data corruption)
  - [ ] Application performance meets targets (p95 latency < 200ms at 5000 req/sec)
  - [ ] Zero data loss during migration
  - [ ] Read replicas serving 80%+ of read traffic
  - [ ] Monitoring and alerting operational

---

## Validation

### Proof of Concept

- **What was tested:** PostgreSQL read replicas performance under load (5000 req/sec)
- **Results:** Successfully handled target load with p95 latency of 120ms (well under 200ms target)
- **Conclusion:** Validated that PostgreSQL can meet performance requirements

### Benchmarking

- **What was measured:** PostgreSQL vs MongoDB query performance for our workload (complex joins vs simple document reads)
- **Results:** PostgreSQL 30% faster for complex joins (our workload is 70% joins), MongoDB 20% faster for simple document reads (30% of our workload)
- **Conclusion:** PostgreSQL better overall for our workload

### References

- [PostgreSQL vs MySQL Comparison](https://www.enterprisedb.com/blog/postgresql-vs-mysql-a-comparison-for-enterprises/) - Feature comparison showing PostgreSQL advantages
- [AWS RDS PostgreSQL Best Practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) - AWS operational guidance
- [Team Slack Discussion: Database Selection](https://company.slack.com/archives/backend-db/p12345678) - Internal team consensus on PostgreSQL

---

## Related Decisions

### Related ADRs

- [ADR-002: Database Strategy](/docs/adr/002-database-strategy.md) - Established need for scalable ACID-compliant database
- [ADR-004: Cloud Provider Selection](/docs/adr/004-cloud-provider.md) - Selected AWS, making RDS available as an option

### Supersedes

- [ADR-001: Use SQLite for MVP](/docs/adr/001-sqlite-mvp.md) - SQLite was appropriate for MVP but PostgreSQL chosen for production scalability

---

## Reconsideration

### Triggers for Reconsideration

This decision should be revisited if:

- **Write scaling becomes bottleneck:** PostgreSQL single-master write performance becomes limiting factor
  - **Trigger:** Sustained p95 write latency > 500ms for 1 week despite optimization
- **Cost exceeds budget:** RDS PostgreSQL costs exceed $6K/month for 3 consecutive months
- **Team grows database expertise:** Team gains deep PostgreSQL internals knowledge (may consider self-hosting for cost savings)
- **New PostgreSQL features:** Major PostgreSQL version release with built-in sharding or write scaling
- **Workload change significant:** Application architecture changes to NoSQL-first (e.g., heavy document model)

### Expiration

**Review Date:** 2025-06-01 (9 months from implementation)

**Reason:** Re-evaluate whether PostgreSQL still meets needs or if new requirements have emerged. Also check if distributed SQL options (CockroachDB, YugabyteDB) have matured.

---

## References

### Related Documents

- [RFC-001: Production Architecture](/docs/rfc/001-production-arch.md) - Overall architecture for production deployment
- [TSD-001: Database Schema](/docs/tsd/001-db-schema.md) - PostgreSQL schema specification
- [Load Testing Results: August 2024](/docs/load-testing/sqlite-august-2024.pdf) - Evidence of SQLite limitations

### External References

- [PostgreSQL Documentation](https://www.postgresql.org/docs/) - Official PostgreSQL documentation
- [AWS RDS PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) - AWS RDS PostgreSQL user guide
- [PostgreSQL vs MongoDB for Payments](https://www.mongodb.com/postgresql-vs-mongodb) - Third-party comparison

---

## Approval

| Role | Name | Approval | Date |
|------|------|----------|------|
| Backend Tech Lead | Jane Smith | ✅ | 2024-09-12 |
| Platform Team Lead | Mike Johnson | ✅ | 2024-09-13 |
| Engineering Manager | John Doe | ✅ | 2024-09-14 |
| Finance Team | Sarah Williams | ✅ | 2024-09-14 |
