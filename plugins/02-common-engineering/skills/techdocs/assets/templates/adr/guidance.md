# ADR (Architecture Decision Record) Guidance

> **Purpose**: This guide provides section-by-section instructions for writing high-quality ADRs. It explains how to use Universal Discovery output and what questions to ask for each section.

---

## Universal Discovery Integration

> **CRITICAL**: ADRs are created AFTER completing Phase 1 (Universal Discovery) and Phase 2 (Document Type Selection). The Problem Validation Gate must be completed before writing this ADR.

### Universal Discovery Output → ADR Section Mapping

| Universal Discovery Output | Used In ADR Section | How It's Used |
|----------------------------|---------------------|---------------|
| Current State description | Context → Current Situation | "Current state" for decision context |
| Evidence of Problem | Context → Drivers | Evidence supporting need for decision |
| Desired State description | Context → Goals | Technical goals for the decision |
| Technical Context | Alternatives Considered | Technical constraints inform options |
| Related Documents | References | Linked/attached context |
| Historical Context | Alternatives Considered | Previous attempts inform options |

### Before Starting the ADR

**Prerequisites:**
1. ✅ Problem Validation Gate completed (current state, evidence, who's affected, gap analysis)
2. ✅ Document type selection confirmed (AI recommended ADR, user accepted)
3. ✅ Template-specific discovery questions answered (ADR-specific questions from agent)

### ADR vs RFC vs TSD

| Document Type | Focus | When to Use |
|---------------|-------|-------------|
| **ADR** | Decision "which option" - technology choices | When evaluating and selecting between alternatives |
| **RFC** | Architectural "what and why" - design decisions | When proposing significant architectural changes |
| **TSD** | Technical "how" - API specs, data models | When you need detailed technical implementation specs |

**ADRs are appropriate when:**
- You need to choose between technology options (frameworks, databases, libraries)
- You need to decide on an architectural pattern (microservices vs monolith, SQL vs NoSQL)
- You need to document an important architectural decision
- The decision has trade-offs that need to be documented

**ADRs are NOT appropriate when:**
- The problem is not yet validated → Use Universal Discovery first
- The decision is trivial or obvious → Just make the decision
- You need to specify implementation details → Write a TSD
- You need to design a complex system → Write an RFC

---

## Section-by-Section Guidance

### 1. Title and Metadata

**Purpose**: Identify the decision and its status.

**TSD-Specific Questions**:
- "What is this decision about?"
- "What type of decision is this?" (technology choice, framework decision, architectural pivot)
- "What is the current status?" (Proposed, Accepted, Deprecated, Superseded)

**Quality Criteria**:
- Title is specific and clear
- Status is accurate
- Decision type is identified
- Deciders are listed
- Related ADRs are linked (if any)

**Example**:
> **Title:** ADR-005: Choose PostgreSQL as Primary Database
> **Status:** Accepted
> **Decision Type:** Data Storage
> **Deciders:** Backend Tech Lead, Platform Team Lead
> **Related ADRs:** ADR-002 (Database Strategy)

---

### 2. Context

**Purpose**: Establish the context for why a decision is needed.

**Uses Universal Discovery Output**: Uses current state, evidence, and desired state to frame the decision.

#### Current Situation

**What to Include**:
- Current state (what's happening now)
- Problem being solved
- Constraints (technical, organizational, time)

**Uses Universal Discovery**:
- **Current State Deep Dive** → Current situation description
- **Evidence of Problem** → Drivers for decision
- **Technical Context** → Constraints

**ADR-Specific Questions**:
- "What is the current situation?"
- "What problem are we trying to solve?"
- "What constraints do we have?" (technical, time, budget, team skills)

**Quality Criteria**:
- Current situation is clearly described
- Problem is specific
- Constraints are identified
- Context is sufficient to understand the decision

**Example**:
> **Current Situation:**
> Our application currently uses SQLite as its database. This was fine for development and small-scale testing, but we're now approaching production. SQLite doesn't support concurrent writes well and has limited horizontal scaling capabilities. Our traffic projections (5000 req/sec) exceed SQLite's capacity.
>
> **Constraints:**
> - Team has experience with SQL databases (PostgreSQL, MySQL)
> - Deployment timeline: 3 months to production
> - Budget: $5K/month for database hosting
> - Must support ACID transactions for payment processing

#### Drivers

**What to Include**:
- Specific factors driving the decision
- Evidence from Universal Discovery

**Uses Universal Discovery**:
- **Evidence of Problem** → Quantified drivers

**ADR-Specific Questions**:
- "What are the key drivers for this decision?"
- "What evidence supports these drivers?"
- "Are there external dependencies or deadlines?"

**Quality Criteria**:
- Drivers are specific and measurable
- Evidence is provided
- Drivers are prioritized (most important first)

**Example**:
> **Drivers:**
> - **Scalability:** Must support 5000 req/sec by Q4 2024 (current: 500 req/sec)
> - **Reliability:** Must support ACID transactions for payments (regulatory requirement)
> - **Team skills:** Team has PostgreSQL experience (3 engineers, 2+ years each)
> - **Timeline:** Production launch in 3 months (limited time for evaluation)
> - **Cost:** Budget limited to $5K/month for managed database

#### Goals and Non-Goals

**What to Include**:
- What we want to achieve (goals)
- What we're explicitly NOT trying to achieve (non-goals)

**Uses Universal Discovery**:
- **Desired State** → Goals

**ADR-Specific Questions**:
- "What are we trying to achieve with this decision?"
- "What are we NOT trying to achieve?" (explicitly exclude out-of-scope items)

**Quality Criteria**:
- Goals are specific
- Non-goals are clearly defined
- Goals align with drivers

**Example**:
> **Goals:**
> - Support horizontal scaling for read operations
> - Maintain ACID compliance for payment transactions
> - Enable high availability (99.9% uptime)
> - Stay within $5K/month budget
>
> **Non-Goals:**
> - Multi-region deployment (single region is sufficient)
> - NoSQL features (don't need flexible schemas)
> - Real-time analytics (can use separate data warehouse)

---

### 3. Decision

**Purpose**: Clearly state what was chosen.

**ADR-Specific Questions**:
- "What was chosen?"
- "What are the key attributes of the chosen option?"

**Quality Criteria**:
- Decision is clear and unambiguous
- Key attributes are specified
- Brief description of chosen option

**Example**:
> We have chosen **PostgreSQL** as our primary database.
>
> **Key Attributes:**
> - **ACID compliant:** Full transaction support for payments
> - **Horizontal scaling:** Read replicas for query scaling
> - **Managed service:** AWS RDS for reduced operational overhead
> - **Version:** PostgreSQL 15 (latest stable)
> - **Instance:** db.r6g.xlarge (2 vCPU, 16GB RAM) with read replicas

---

### 4. Alternatives Considered

> **MANDATORY**: At least 2 alternatives must be documented. This is non-negotiable.

**ADR-Specific Questions**:
- "What alternatives were considered?"
- "What are the pros and cons of each?"
- "What is the estimated impact (cost, effort, risk) of each?"

**Quality Criteria**:
- At least 2 alternatives documented
- Each alternative has balanced pros and cons
- Estimated impact is provided (cost, effort, risk)
- Alternatives are realistic (not strawmen)

**Alternative Structure**:
For each alternative:
1. **Description**: Brief description
2. **Pros**: Advantages
3. **Cons**: Disadvantages
4. **Estimated Impact**: Cost, effort, risk

**Example**:

> ### Alternative 1: PostgreSQL
>
> **Description:** Open-source relational database with ACID compliance and read replica support.
>
> **Pros:**
> - **ACID compliant:** Full transaction support for payments
> - **Team experience:** 3 engineers have 2+ years PostgreSQL experience
> - **Read replicas:** Built-in support for horizontal scaling
> - **Cost effective:** $3K/month for RDS PostgreSQL with replicas
> - **Mature ecosystem:** Extensive tooling and community support
>
> **Cons:**
> - **Vertical scaling:** Requires larger instances for write scaling
> - **Schema rigidity:** Migrations required for schema changes
> - **Operational overhead:** Requires DBA expertise for optimization
>
> **Estimated Impact:**
> - **Cost:** $3K/month (within budget)
> - **Effort:** 3 weeks (team has experience)
> - **Risk:** Low (mature technology)

---

### 5. Decision Criteria

**Purpose**: Document how alternatives were evaluated.

**ADR-Specific Questions**:
- "What criteria mattered for this decision?"
- "How do the alternatives compare on each criterion?"
- "Which criteria are most important?"

**Quality Criteria**:
- Criteria are clearly defined
- Weights are assigned (High/Med/Low)
- Alternatives are compared on each criterion
- Criteria align with drivers and goals

**Criteria Examples**:
- **Performance**: Latency, throughput, scalability
- **Cost:** Licensing, hosting, operational costs
- **Effort:** Implementation time, learning curve
- **Risk:** Technology maturity, team experience, vendor lock-in
- **Compatibility**: Integration with existing systems
- **Time to market**: Speed of implementation

**Example**:

> | Criterion | Weight | SQLite | MongoDB | PostgreSQL |
> |-----------|--------|---------|---------|------------|
> | Scalability | High | Poor (no replicas) | Good (sharding) | Good (read replicas) |
> | ACID Compliance | High | Full | Limited (document level) | Full |
> | Team Experience | High | High (everyone knows it) | Low (no experience) | Medium (2 engineers experienced) |
> | Cost | Medium | Very Low ($0) | Medium ($4K/month) | Medium ($3K/month) |
> | Operational Overhead | Medium | Low | High (sharding complex) | Medium (managed RDS) |
>
> **Criteria Definitions:**
> - **Scalability:** Ability to handle 5000 req/sec with horizontal scaling
> - **ACID Compliance:** Full transaction support for payment processing
> - **Team Experience:** Number of engineers with experience and years
> - **Cost:** Monthly hosting cost (including managed service fees)
> - **Operational Overhead:** Complexity of day-to-day operations

---

### 6. Trade-offs Analysis

**Purpose**: Document what trade-offs were made.

**ADR-Specific Questions**:
- "What are we trading off?"
- "What's the impact of each trade-off?"
- "Are there any deal-breakers?"

**Quality Criteria**:
- Trade-offs are explicitly documented
- Impact of each trade-off is clear
- No major trade-offs are hidden

**Trade-off Dimensions**:
1. **Performance vs Simplicity**: More performance often adds complexity
2. **Cost vs Capability**: More capable solutions often cost more
3. **Time to Market vs Long-term Viability**: Quick solutions may not scale
4. **Flexibility vs Constraints**: More flexibility often means less structure

**Example**:

> ### Performance vs Simplicity
>
> | Aspect | Trade-off | Impact |
> |--------|-----------|--------|
> | Write scaling | PostgreSQL requires vertical scaling for writes | May need larger instance in future (+$2K/month) |
> | Query simplicity | SQL is simpler than MongoDB query language | Faster development, easier debugging |
>
> ### Cost vs Capability
>
> | Aspect | Trade-off | Impact |
> |--------|-----------|--------|
> | Managed service cost | RDS costs more than self-hosted | +$1K/month but 24/7 support included |
> | Feature set | PostgreSQL has fewer features than MongoDB | Sufficient for current needs |
>
> ### Time to Market vs Long-term Viability
>
> | Aspect | Trade-off | Impact |
> |--------|-----------|--------|
> | Learning curve | Team knows PostgreSQL (low learning curve) | Faster implementation (3 weeks vs 8 weeks) |
> | Future scaling | Read replicas scale reads, not writes | May need sharding in 2+ years |

---

### 7. Consequences

**Purpose**: Document positive and negative consequences of the decision.

**ADR-Specific Questions**:
- "What are the benefits of this decision?"
- "What are the drawbacks?"
- "What risks are introduced?"
> "What risks are eliminated?"

**Quality Criteria**:
- Both positive and negative consequences are documented
- Consequences are specific (not vague)
- Risks are identified with mitigation plans

**Content Structure**:
1. **Positive Consequences**: Benefits and who benefits
2. **Negative Consequences**: Drawbacks and who is affected
3. **Risks Introduced**: New risks with likelihood, impact, mitigation
4. **Risks Eliminated**: Risks this decision removes

**Example**:

> ### Positive Consequences
>
> - **Scalability:** Can scale to 5000 req/sec via read replicas (benefits: all users, better performance)
> - **Reliability:** ACID compliance prevents payment errors (benefits: finance team, customers)
> - **Team velocity:** Familiar technology speeds development (benefits: engineering team, product team)
> - **Cost savings:** Within budget at $3K/month (benefits: finance team)
>
> ### Negative Consequences
>
> - **Vendor lock-in:** Migration off RDS PostgreSQL would be effortful (affects: platform team)
> - **Write scaling:** Limited vertical scaling for writes (affects: backend team)
> - **Schema rigidity:** Migrations required for schema changes (affects: backend team)
>
> ### Risks Introduced
>
> | Risk | Likelihood | Impact | Mitigation |
> |------|------------|--------|------------|
> | Write performance bottleneck | Medium | High | Monitor write latency; plan for sharding if needed |
> | RDS outage causes downtime | Low | High | Multi-AZ deployment; read replicas for failover |
> | Cost overruns with scaling | Low | Medium | Budget alerts at 80%; review scaling needs quarterly |
>
> ### Risks Eliminated
>
> - **Payment data inconsistency:** ACID compliance eliminates transaction inconsistencies
> - **Scalability blocking:** Read replicas eliminate horizontal scaling blockers
> - **NoSQL learning curve:** Using familiar technology eliminates project delays

---

### 8. Implementation Plan

**Purpose**: How the decision will be implemented.

**ADR-Specific Questions**:
- "How will this be implemented?"
- "What are the phases?"
- "What's the rollout strategy?"
- "When will this be done?"

**Quality Criteria**:
- Implementation is broken into phases
- Each phase has clear goals
- Rollout strategy is specified
- Success criteria are defined

**Example**:

> ### Phase 1: PostgreSQL Setup
>
> - **Goals:** Provision RDS PostgreSQL, configure read replicas
> - **Tasks:**
>   - [ ] Provision RDS PostgreSQL 15 (db.r6g.xlarge)
>   - [ ] Configure Multi-AZ deployment
>   - [ ] Create 2 read replicas
>   - [ ] Set up monitoring and alerting
> - **Owner:** Platform Team
> - **Timeline:** 1 week
>
> ### Phase 2: Migration
>
> - **Goals:** Migrate data from SQLite to PostgreSQL
> - **Tasks:**
>   - [ ] Write migration scripts (SQLite → PostgreSQL)
>   - [ ] Test migration on staging data
>   - [ ] Execute production migration (downtime: 1 hour)
>   - [ ] Verify data integrity
> - **Owner:** Backend Team
> - **Timeline:** 1 week
>
> ### Phase 3: Application Updates
>
> - **Goals:** Update application to use PostgreSQL
> - **Tasks:**
>   - [ ] Update database connection strings
>   - [ ] Deploy to staging, test thoroughly
>   - [ ] Deploy to production
> - **Owner:** Backend Team
> - **Timeline:** 1 week
>
> ### Rollout Strategy
>
> - **Approach:** Big bang (complete cutover after migration)
> - **Timeline:** 3 weeks total (Phase 1: week 1, Phase 2: week 2, Phase 3: week 3)
> - **Success Criteria:**
>   - [ ] All data migrated successfully (100% row count match)
>   - [ ] Application performance meets targets (p95 latency < 200ms)
>   - [ ] Zero data loss during migration
>   - [ ] Read replicas serving 80%+ of read traffic

---

### 9. Validation

**Purpose**: How the decision was validated.

**ADR-Specific Questions**:
- "Was a proof of concept done?"
- "What benchmarks were run?"
- "What external references were consulted?"

**Quality Criteria**:
- Validation approach is documented
- Results are summarized
- References are provided

**Example**:

> ### Proof of Concept
>
> - **What was tested:** PostgreSQL read replicas performance under load
> - **Results:** Successfully handled 5000 req/sec with p95 latency of 120ms
> - **Conclusion:** Validated that PostgreSQL can meet performance targets
>
> ### Benchmarking
>
> - **What was measured:** PostgreSQL vs MongoDB query performance for our workload
> - **Results:** PostgreSQL 30% faster for complex joins; MongoDB 20% faster for simple document reads
> - **Conclusion:** PostgreSQL better for our workload (heavy joins)
>
> ### References
>
> - [PostgreSQL vs MySQL Comparison](https://example.com) - Performance comparison
> - [RDS PostgreSQL Best Practices](https://example.com) - AWS guidance
> - [Team Discussion: Slack #backend-db](https://example.com) - Internal discussion

---

### 10. Related Decisions

**Purpose**: Link to related ADRs.

**ADR-Specific Questions**:
- "What related ADRs exist?"
- "Does this supersede any previous ADRs?"

**Quality Criteria**:
- Related ADRs are linked
- Relationship is explained
- Superseded ADRs are identified

**Example**:

> ### Related ADRs
>
> - [ADR-002: Database Strategy](/docs/adr/002-database-strategy.md) - Established need for scalable database
> - [ADR-004: Cloud Provider Selection](/docs/adr/004-cloud-provider.md) - Selected AWS, making RDS available
>
> ### Supersedes
>
> - [ADR-001: Use SQLite for MVP](/docs/adr/001-sqlite-mvp.md) - SQLite was for MVP only; PostgreSQL chosen for production

---

### 11. Reconsideration

**Purpose**: When and why this decision should be revisited.

**ADR-Specific Questions**:
- "What triggers would cause us to reconsider this decision?"
- "When should this be reviewed?"

**Quality Criteria**:
- Triggers are specific
- Review date is specified
- Rationale for triggers is provided

**Example**:

> ### Triggers for Reconsideration
>
> This decision should be revisited if:
> - **Write scaling becomes bottleneck:** PostgreSQL single-master becomes limiting factor (trigger: p95 write latency > 500ms sustained)
> - **Cost exceeds budget:** RDS costs exceed $7K/month for 3 consecutive months
> - **Team grows database expertise:** Team gains deep PostgreSQL internals knowledge (may consider self-hosting for cost savings)
> - **New PostgreSQL features:** Major version release with compelling new features (e.g., built-in sharding)
>
> ### Expiration
>
> **Review Date:** 2025-06-01 (1 year from implementation)
>
> **Reason:** Re-evaluate whether PostgreSQL still meets needs or if new requirements have emerged

---

### 12. References

**Purpose**: Link to related documents and sources.

**Uses Universal Discovery**:
- **Related Documents** → Reference any attached docs

**ADR-Specific Questions**:
- "What documents should readers review?"
- "What external sources informed this decision?"

**Quality Criteria**:
- Related documents are linked
- External references are relevant
- Links are accurate

**Example**:

> ### Related Documents
>
> - [RFC-003: Production Architecture](/docs/rfc/003-production-arch.md) - Overall architecture for production deployment
> - [TSD-001: Database Schema](/docs/tsd/001-db-schema.md) - PostgreSQL schema specification
>
> ### External References
>
> - [PostgreSQL Documentation](https://www.postgresql.org/docs/) - Official PostgreSQL docs
> - [AWS RDS PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) - AWS RDS guide
> - [PostgreSQL vs MySQL Benchmark](https://example.com) - Performance benchmark

---

### 13. Approval

**Purpose**: Document required approvals.

**ADR-Specific Questions**:
- "Who needs to approve this decision?"
- "Has everyone approved?"

**Quality Criteria**:
- Required roles are listed
- Approval status is tracked
- Dates are recorded

**Example**:

> | Role | Name | Approval | Date |
> |------|------|----------|------|
> | Backend Tech Lead | Jane Smith | ✅ | 2024-09-15 |
> | Platform Team Lead | Mike Johnson | ✅ | 2024-09-16 |
> | Engineering Manager | John Doe | Pending | |

---

## Quality Checklist for ADRs

Before submitting an ADR for review, verify:

### Completeness
- [ ] All sections are complete
- [ ] At least 2 alternatives documented ← NON-NEGOTIABLE
- [ ] Decision criteria are specified
- [ ] Trade-offs are documented
- [ ] Consequences (positive and negative) are documented
- [ ] Implementation plan is specified

### Decision Quality
- [ ] Decision is clear and unambiguous
- [ ] Alternatives are realistic (not strawmen)
- [ ] Pros and cons are balanced for each alternative
- [ ] Decision aligns with drivers and goals
- [ ] Trade-offs are explicitly acknowledged

### Validation
- [ ] Decision was validated (proof of concept, benchmarking, or references)
- [ ] Validation results are documented

### Risk Management
- [ ] Risks introduced are identified with mitigation
- [ ] Risks eliminated are documented

### Actionability
- [ ] Implementation plan is specific
- [ ] Success criteria are defined
- [ ] Reconsideration triggers are specified

---

## Common ADR Mistakes to Avoid

1. **Too few alternatives**: Only 1 alternative documented → **MANDATE**: At least 2 alternatives
2. **Strawman alternatives**: Alternatives are obviously bad → Make alternatives realistic
3. **No trade-offs**: Decision is presented as perfect → Document the downsides
4. **Vague context**: "We need a database" → Be specific: "We need to support 5000 req/sec with ACID compliance"
5. **No implementation plan**: Decision but no how-to → Add implementation phases
6. **No reconsideration criteria**: Decision is forever → Specify when to reconsider
7. **Hidden agenda**: Decision already made, alternatives are fake → Be genuine about options
8. **No validation**: Decision based on gut feeling → Add proof of concept or benchmarks
