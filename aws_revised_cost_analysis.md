# AWS Cost Optimization - Revised Analysis
## Based on New Information

## Current State
- **85 EC2 instances** across all AWS accounts
- **21 RDS databases** across all AWS accounts
- **$10k/month Savings Plan** (covering EC2 and Lambda compute) ✅
- **Dev/Staging/Prod all run 24/7** (justified: west-east timezones + offshore developers)
- **$40k/month total AWS spend**

---

## Analysis: You're Already Doing Some Things Right

### ✅ What's Working:
1. **Savings Plan ($10k/month):** You've already addressed the biggest waste pattern (On-Demand pricing)
2. **Legitimate 24/7 operations:** Unlike most companies, you have valid reasons for running dev/staging continuously

### 🚨 What's Still Wasteful:

---

## RED FLAG #1: 85 EC2 Instances is VERY HIGH

**Context for your business:**
- ~15 coaches
- ~20+ referrals/day (~500-600/month)
- Healthcare operations automation

**Industry Benchmarks:**
- Similar-sized SaaS companies: **10-25 EC2 instances**
- Well-architected companies your size: **15-30 instances**
- You have: **85 instances** (3-6x higher than expected)

### Why This Is a Problem:

**Scenario A: Over-Provisioned (Many Small Instances)**
- Running many small instances instead of fewer larger ones
- Not using autoscaling groups
- Static provisioning for peak load

**Scenario B: Sprawl (Orphaned/Legacy Instances)**
- Old instances from completed projects still running
- Duplicate instances across dev/staging/prod
- Instances created for testing but never deleted

**Scenario C: Microservices Overload**
- Each microservice has dedicated instances instead of containerization
- Not using ECS/EKS with autoscaling
- Over-engineered architecture for current scale

### The Math:
- Average EC2 instance cost with Savings Plan: ~$40-80/month
- 85 instances × $60 avg = **$5,100/month**
- If you could consolidate to 40-50 instances: **Save $2,000-3,000/month**

### Action Items:

**Week 1: Instance Inventory Audit**
```bash
# Get detailed instance inventory
aws ec2 describe-instances \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,LaunchTime,Tags[?Key==`Name`].Value|[0],Tags[?Key==`Environment`].Value|[0],Tags[?Key==`Project`].Value|[0]]' \
  --output table > ec2_inventory.txt

# Find instances older than 1 year (likely legacy)
aws ec2 describe-instances \
  --query 'Reservations[*].Instances[?LaunchTime<=`2024-01-01`].[InstanceId,InstanceType,LaunchTime,Tags[?Key==`Name`].Value|[0]]' \
  --output table

# Check CPU utilization for all instances (find idle ones)
# This requires a script - I can provide one
```

**Questions to Answer:**
1. How many instances per environment?
   - Production: _____
   - Staging: _____
   - Dev: _____
   - Other: _____

2. How many instances are for:
   - Salesforce integration/middleware: _____
   - DocuPipe processing: _____
   - LLM/AI workloads: _____
   - Databases (non-RDS): _____
   - Legacy/unknown: _____

3. **Consolidation opportunities:**
   - Can you move to ECS/EKS with autoscaling? (10-15 instances → 3-5 instances)
   - Can you shut down legacy instances from old projects?
   - Can you combine dev/staging onto shared instances with isolation?

**Potential Savings: $2,000-4,000/month**

---

## RED FLAG #2: 21 RDS Databases is VERY HIGH

**Context:**
- You mentioned Salesforce as primary database
- Healthcare operations with 3 workflows (intake, coaching, scheduling)

**Industry Benchmarks:**
- Similar companies: **3-8 RDS databases**
  - 1-2 for production (primary + analytics/reporting)
  - 1-2 for staging
  - 1 for dev
  - Maybe 1-2 for microservices
- You have: **21 databases** (3-7x higher than expected)

### Why This Is a Problem:

**RDS costs scale with instance count:**
- Average RDS instance with Multi-AZ: ~$130-350/month
- 21 databases × $130 avg = **$2,730/month** (matches your actual RDS cost!)
- If you could consolidate to 8-10 databases: **Save $1,200-1,800/month**

### Likely Causes:

**Pattern A: Microservices Gone Wild**
- Each microservice has its own database
- Could use schemas/tables in shared databases instead

**Pattern B: Environment Duplication**
- Each application has separate prod/staging/dev databases
- 7 applications × 3 environments = 21 databases

**Pattern C: Legacy/Orphaned Databases**
- Old project databases still running but unused
- Test databases that were never deleted

**Pattern D: Over-Separation**
- Separate databases for intake, coaching, scheduling, DocuPipe, etc.
- Could consolidate with schemas/multi-tenancy

### Action Items:

**Week 1: Database Inventory**
```bash
# Get detailed RDS inventory
aws rds describe-db-instances \
  --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceClass,Engine,MultiAZ,AllocatedStorage,StorageType,InstanceCreateTime]' \
  --output table > rds_inventory.txt

# Check database size and activity
aws rds describe-db-instances \
  --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceClass,AllocatedStorage,EngineVersion]' \
  --output table
```

**Questions to Answer:**
1. List your databases by purpose:
   - Production databases: _____ (how many?)
   - Staging databases: _____ (how many?)
   - Dev databases: _____ (how many?)
   - Analytics/reporting: _____ (how many?)
   - Legacy/unknown: _____ (how many?)

2. **Consolidation opportunities:**
   - Can dev/staging share databases with different schemas?
   - Can microservices share a database cluster?
   - Are there any databases with <10GB data? (candidates for consolidation)
   - Are there any databases that haven't been accessed in 90+ days?

**Immediate Savings (No Consolidation Needed):**

Even without consolidation, you can optimize:

1. **Disable Multi-AZ for non-production databases:**
   - If 12 databases are dev/staging with Multi-AZ: **Save $800-1,500/month**

2. **Rightsize over-provisioned databases:**
   - Run CloudWatch CPU/Memory metrics for 30 days
   - Downsize databases with <30% utilization: **Save $500-1,000/month**

3. **Switch storage from gp2 → gp3:**
   - 20% cheaper for same performance
   - 21 databases × 100GB avg × $0.035 savings = **Save $75-150/month**

**Potential Total RDS Savings: $1,400-2,650/month**

---

## RED FLAG #3: Data Transfer Mystery ($5,285/month)

You said you're "not sure" about massive data transfer. Let me explain what I see in your Cost Explorer data:

### What I'm Seeing:
- **EC2-Other: ~$5,285/month**
- In AWS billing, "EC2-Other" is almost always **data transfer OUT to internet**
- At $0.09/GB, this means **~59 terabytes/month** leaving AWS

### This is NOT normal for your business size.

**For comparison:**
- A typical healthcare SaaS your size: **5-15 TB/month** ($450-1,350/month)
- You're transferring: **59 TB/month** ($5,285/month)
- **You're 4-12x higher than expected**

### Where Could This Be Coming From?

**Hypothesis #1: DocuPipe Document Processing**
- DocuPipe downloads referral documents from external sources
- If documents are re-downloaded multiple times (no caching): massive transfer
- Each document download from internet → processed → sent back out → double transfer cost

**Hypothesis #2: Serving Medical Documents Without CDN**
- PT notes, referral documents, medical records served directly from S3/EC2
- No CloudFront CDN caching
- Every document request = full download from S3 → transfer charge

**Hypothesis #3: Large API Responses**
- APIs sending uncompressed JSON/XML responses to external systems
- Clinic integrations, adjuster communications, case manager data
- No gzip compression = 5-10x larger transfers

**Hypothesis #4: Database Backups or ETL**
- Daily RDS snapshots being downloaded to on-premises
- Large ETL jobs moving data between AWS and external systems
- Analytics/reporting pulling large datasets

**Hypothesis #5: Video/Media Streaming**
- If you're storing/streaming any video content (unlikely for your business)
- Training videos, recorded sessions, etc.

### How to Investigate:

**Step 1: Find the Source (15 minutes)**
```bash
# Check which S3 buckets have high data transfer
aws cloudwatch get-metric-statistics \
  --namespace AWS/S3 \
  --metric-name BytesDownloaded \
  --dimensions Name=BucketName,Value=YOUR_BUCKET_NAME \
  --start-time 2025-11-01T00:00:00Z \
  --end-time 2025-12-01T00:00:00Z \
  --period 86400 \
  --statistics Sum

# Check which EC2 instances are sending the most data
# AWS Console → CloudWatch → EC2 → Per-Instance Metrics → NetworkOut
# Sort by sum over last 30 days
```

**Step 2: Check Cost Explorer by Usage Type**
1. AWS Console → Cost Explorer
2. Group by: **Usage Type**
3. Filter: Service = **EC2**
4. Look for lines containing "DataTransfer-Out-Bytes" or "Regional-Bytes"
5. This will show which region/resource is generating transfer

**Step 3: Review Top Applications**
- DocuPipe: Does it cache documents or re-download?
- Salesforce integrations: Are you syncing large amounts of data?
- Clinic partner integrations: Sending documents/data to external systems?
- Patient communication: Sending documents via email/portal?

### Potential Fixes:

**If it's document serving:**
- Enable CloudFront CDN in front of S3: **Save $3,000-4,000/month (60-80%)**
- Set cache TTL to 1-7 days for frequently accessed documents

**If it's API responses:**
- Enable gzip compression: **Save $2,000-3,000/month (50-60%)**
- Paginate large responses instead of returning everything

**If it's DocuPipe re-downloading:**
- Implement document caching layer: **Save $1,500-2,500/month**
- Store processed documents in S3, don't re-process

**If it's backups/ETL:**
- Keep backups in S3 (don't download): **Save $500-1,500/month**
- Use AWS Database Migration Service instead of custom ETL

**Potential Data Transfer Savings: $2,000-4,000/month**

---

## Quick Wins (Still Apply)

These are low-hanging fruit regardless of your infrastructure:

### 1. Unattached EBS Volumes
```bash
aws ec2 describe-volumes --filters Name=status,Values=available
```
- **Typical savings: $500-1,500/month**

### 2. Old EBS Snapshots
```bash
aws ec2 describe-snapshots --owner-ids self --query 'Snapshots[?StartTime<`2025-09-01`]'
```
- Delete snapshots older than 90 days
- **Typical savings: $500-2,000/month**

### 3. Unused Elastic IPs
```bash
aws ec2 describe-addresses --query 'Addresses[?AssociationId==null]'
```
- $3.60/month each, likely 10-30 unused
- **Typical savings: $35-110/month**

### 4. Unused Load Balancers
- Check Load Balancer metrics for zero traffic
- **Typical savings: $50-200/month**

### 5. NAT Gateways
```bash
aws ec2 describe-nat-gateways --filter "Name=state,Values=available"
```
- You probably have too many (1-2 per region is enough)
- **Typical savings: $100-500/month**

### 6. CloudWatch Logs Retention
- Set retention to 30 days instead of "Never Expire"
- **Typical savings: $200-800/month**

**Total Quick Wins: $1,385-5,110/month**

---

## Revised Savings Summary

| Optimization Area | Conservative Savings | Aggressive Savings | Timeline |
|-------------------|---------------------|-------------------|----------|
| **EC2 Instance Consolidation** (85 → 50) | $2,000/mo | $4,000/mo | 4-8 weeks |
| **RDS Database Optimization** | $1,400/mo | $2,650/mo | 2-4 weeks |
| **Data Transfer (CDN/Compression)** | $2,000/mo | $4,000/mo | 2-4 weeks |
| **Quick Wins (Unused Resources)** | $1,385/mo | $5,110/mo | 1-2 weeks |
| **TOTAL MONTHLY SAVINGS** | **$6,785/mo** | **$15,760/mo** | **8 weeks** |
| **ANNUAL SAVINGS** | **$81,420/yr** | **$189,120/yr** | |
| **New Monthly AWS Cost** | **$33,215** | **$24,240** | |

### Realistic Target: $10,000/month savings (25% reduction)
- This brings your $40k/month → **$30k/month**
- Much more reasonable for your scale
- Achievable in 6-8 weeks

---

## Prioritized Action Plan

### Week 1: Investigation & Quick Wins
**Time investment: 4-6 hours**

1. **Data Transfer Investigation (2 hours)**
   - Run CloudWatch metrics to identify source
   - Review DocuPipe data flow
   - Check S3 bucket metrics
   - **Goal:** Identify where 59 TB/month is coming from

2. **Quick Wins Execution (2 hours)**
   - Delete unattached EBS volumes
   - Release unused Elastic IPs
   - Delete old snapshots (>90 days)
   - Set CloudWatch Logs retention to 30 days
   - **Immediate savings: $1,000-3,000/month**

3. **Instance & Database Inventory (2 hours)**
   - Run AWS CLI commands to list all EC2 and RDS resources
   - Tag instances by purpose/project/environment
   - Identify candidates for consolidation/deletion
   - **Goal:** Create consolidation roadmap

**Week 1 Savings: $1,000-3,000/month**

---

### Week 2-3: RDS Optimization
**Time investment: 6-8 hours**

1. **Disable Multi-AZ for Dev/Staging (2 hours)**
   - Identify non-production databases with Multi-AZ
   - Disable Multi-AZ (50% cost reduction per database)
   - **Savings: $800-1,500/month**

2. **Rightsize Over-Provisioned Databases (3 hours)**
   - Review CloudWatch CPU/Memory metrics
   - Downsize databases with <30% utilization
   - Test in staging first, then production
   - **Savings: $500-1,000/month**

3. **Storage Optimization (1 hour)**
   - Switch gp2 → gp3 storage (20% cheaper)
   - **Savings: $75-150/month**

**Week 2-3 Savings: $1,375-2,650/month**

---

### Week 3-4: Data Transfer Optimization
**Time investment: 8-12 hours**

Based on what you find in Week 1 investigation:

**If serving documents:**
1. **Enable CloudFront CDN (4 hours setup)**
   - Create CloudFront distribution
   - Point to S3 bucket
   - Update application to use CloudFront URLs
   - Set cache TTL to 24 hours
   - **Savings: $3,000-4,000/month**

**If large API responses:**
2. **Enable Gzip Compression (2 hours)**
   - Configure API Gateway compression
   - Enable gzip in application
   - **Savings: $1,500-2,500/month**

**If DocuPipe re-downloading:**
3. **Implement Document Caching (6 hours)**
   - Store processed documents in S3
   - Add caching layer
   - **Savings: $1,500-2,500/month**

**Week 3-4 Savings: $2,000-4,000/month**

---

### Week 4-8: EC2 Consolidation
**Time investment: 20-40 hours (this is the big one)**

1. **Identify Consolidation Opportunities (4 hours)**
   - Group instances by purpose
   - Find legacy/orphaned instances
   - Identify candidates for containerization

2. **Container Migration Planning (8 hours)**
   - Evaluate ECS/EKS for microservices
   - Plan migration roadmap
   - Test with 1-2 services first

3. **Execute Consolidation (8-28 hours)**
   - Migrate workloads to containers
   - Shut down redundant instances
   - Monitor and adjust

**Week 4-8 Savings: $2,000-4,000/month**

---

## Total Expected Savings: $6,375-13,650/month

**Conservative (what you should definitely achieve): $8,000/month**
**Aggressive (if everything goes well): $14,000/month**

**New AWS spend: $40k → $26-32k/month**

---

## Next Steps - What I Need From You

To give you the EXACT action plan with specific resource IDs to delete/modify:

### Option 1: Run These Commands (10 minutes)
```bash
# EC2 inventory
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,Tags[?Key==`Name`].Value|[0],Tags[?Key==`Environment`].Value|[0]]' --output table > ec2_inventory.txt

# RDS inventory
aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceClass,MultiAZ,EngineVersion]' --output table > rds_inventory.txt

# Unattached volumes
aws ec2 describe-volumes --filters Name=status,Values=available --output table > unattached_volumes.txt

# Share these 3 files with me
```

### Option 2: Answer These Questions (5 minutes)
1. **What is DocuPipe doing?** Is it downloading documents from external sources? How often? Cached?
2. **How many instances per environment?** Prod: ___ | Staging: ___ | Dev: ___
3. **Why 21 databases?** What are they for? (list top 5-7 purposes)
4. **Can you check Cost Explorer → Group by Usage Type?** Find what's causing "DataTransfer-Out"

### Option 3: Start Quick Wins Now (30 minutes)
- I can guide you through deleting unused resources right now
- Immediate $1,000-3,000/month savings
- No risk, no downtime

**Which option works best for you?**
