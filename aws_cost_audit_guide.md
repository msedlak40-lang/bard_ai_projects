# AWS Cost Audit Guide - Finding the Waste in $40k/Month

## Executive Summary

You're spending ~$40k/month on AWS. For a healthcare operations company with ~15 coaches and ~20+ referrals/day, this suggests potential waste. This guide will help you identify where the money is going and where to cut costs.

**Expected outcome:** Identify $8-16k/month (20-40%) in savings within 2-4 weeks.

---

## Step 1: Run AWS Cost Explorer Analysis (Do This First)

### Access AWS Cost Explorer
1. Log into AWS Console → https://console.aws.amazon.com/
2. Navigate to **Billing Dashboard** → **Cost Explorer**
3. If Cost Explorer isn't enabled, enable it (takes 24 hours for data to populate)

### Key Reports to Run

#### Report 1: Top 10 Services by Cost (Last 3 Months)
**Purpose:** Identify which AWS services are eating your budget

**Steps:**
1. Cost Explorer → **Monthly costs**
2. Group by: **Service**
3. Time range: **Last 3 months**
4. Download CSV

**What to look for:**
- Which services are in your top 5? (EC2, RDS, S3, Data Transfer, CloudFront, etc.)
- Are there services you don't recognize or didn't expect?
- Are costs increasing month-over-month?

**Example output:**
| Service | Nov Cost | Dec Cost | Jan Cost | Trend |
|---------|----------|----------|----------|-------|
| EC2 | $15,000 | $16,200 | $17,500 | ⬆️ +16% |
| RDS | $8,000 | $8,100 | $8,200 | ➡️ Stable |
| Data Transfer | $6,500 | $7,200 | $8,000 | ⬆️ +23% |
| S3 | $3,200 | $3,400 | $3,300 | ➡️ Stable |
| CloudWatch | $1,800 | $1,900 | $2,000 | ⬆️ +11% |

#### Report 2: EC2 Instance Costs (If EC2 is in Top 5)
**Purpose:** Find over-provisioned or idle instances

**Steps:**
1. Cost Explorer → Group by: **Instance Type**
2. Filter: Service = **EC2**
3. Time range: **Last month**
4. Download CSV

**What to look for:**
- Large instance types (m5.2xlarge, c5.4xlarge, etc.) that might be oversized
- Multiple instances of the same type (why 10x m5.large instead of autoscaling?)
- Unusual instance types (GPU instances p3.*, memory-optimized r5.* when you don't need them)

#### Report 3: Reserved Instance Coverage
**Purpose:** See if you're paying On-Demand prices for steady-state workloads

**Steps:**
1. Cost Explorer → **Reservation Utilization**
2. Service: **EC2**
3. Time range: **Last 3 months**

**What to look for:**
- **Reservation coverage** < 50% = you're likely overpaying
- Steady workloads (24/7 services) should use Reserved Instances (30-70% cheaper)
- Alternatively, check Savings Plans coverage

#### Report 4: Data Transfer Costs
**Purpose:** Identify expensive data egress (data leaving AWS)

**Steps:**
1. Cost Explorer → Filter: Service = **EC2-Other** or **Data Transfer**
2. Group by: **Region**
3. Time range: **Last month**

**What to look for:**
- High "Data Transfer Out" costs (>$5k/month)
- Inter-region transfers (moving data between us-east-1 and us-west-2)
- Transfers to internet (CloudFront can reduce this)

#### Report 5: RDS Database Costs
**Purpose:** Find oversized databases or unnecessary multi-AZ deployments

**Steps:**
1. Cost Explorer → Filter: Service = **RDS**
2. Group by: **Database Engine**
3. Time range: **Last month**

**What to look for:**
- Large database instances (db.r5.2xlarge, db.m5.4xlarge)
- Multi-AZ enabled for dev/staging (expensive redundancy you might not need)
- Multiple databases doing the same thing

---

## Step 2: Use AWS CLI for Detailed Analysis

If you have AWS CLI access, run these commands for deeper insights:

### Get EC2 Instance Details
```bash
# List all running EC2 instances with size and cost estimates
aws ec2 describe-instances \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,Tags[?Key==`Name`].Value|[0]]' \
  --output table \
  --region us-east-1

# Get instance utilization (requires CloudWatch)
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --start-time 2025-12-01T00:00:00Z \
  --end-time 2025-12-19T23:59:59Z \
  --period 86400 \
  --statistics Average \
  --region us-east-1
```

### Get RDS Instance Details
```bash
# List all RDS instances
aws rds describe-db-instances \
  --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceClass,Engine,MultiAZ,AllocatedStorage]' \
  --output table \
  --region us-east-1
```

### Get S3 Storage Breakdown
```bash
# List S3 buckets and estimated size
aws s3 ls
aws s3api list-buckets --query 'Buckets[*].Name' --output text | \
while read bucket; do
  echo "Bucket: $bucket"
  aws s3 ls s3://$bucket --recursive --summarize | grep "Total Size"
done
```

### Get Unattached EBS Volumes (Common Waste)
```bash
# Find unattached EBS volumes (you're paying for storage but not using them)
aws ec2 describe-volumes \
  --filters Name=status,Values=available \
  --query 'Volumes[*].[VolumeId,Size,VolumeType,CreateTime]' \
  --output table \
  --region us-east-1
```

---

## Step 3: Common AWS Waste Patterns (Check These)

### 1. **Idle or Over-Provisioned EC2 Instances**

**Symptoms:**
- Instance running 24/7 with <10% CPU utilization
- Large instance types (m5.2xlarge) for simple workloads
- Dev/staging environments running when no one's using them

**How to check:**
- AWS Cost Explorer → EC2 by Instance Type
- CloudWatch → EC2 → CPU Utilization (last 30 days)
- AWS Trusted Advisor → "Low Utilization Amazon EC2 Instances"

**Potential savings:**
- Downsize instances: 50% cost reduction (m5.2xlarge → m5.large)
- Stop dev/staging after hours: 60-70% cost reduction (run 40 hrs/week instead of 168)
- Switch to smaller instance types: 30-50% savings

**Example:**
| Current | Waste | Fix | Savings |
|---------|-------|-----|---------|
| 5x m5.2xlarge (8 vCPU, 32GB) @ $0.384/hr = $1,382/month | CPU avg 15% | 5x m5.large (2 vCPU, 8GB) @ $0.096/hr = $345/month | **$1,037/month** |
| Dev environment running 24/7 @ $500/month | Unused nights/weekends | Auto-stop 6pm-8am + weekends = $150/month | **$350/month** |

### 2. **No Reserved Instances or Savings Plans**

**Symptoms:**
- You run the same instances 24/7
- All costs are On-Demand pricing
- Reservation coverage <30%

**How to check:**
- AWS Cost Explorer → Reservation Coverage report
- Check if you have any Reserved Instances or Savings Plans

**Potential savings:**
- Reserved Instances (1-year): 30-40% discount
- Reserved Instances (3-year): 50-60% discount
- Compute Savings Plans: 30-50% discount with flexibility

**Example:**
| Current | Fix | Savings |
|---------|-----|---------|
| 10x m5.large On-Demand @ $0.096/hr = $691/month | 10x m5.large Reserved (1yr) @ $0.061/hr = $439/month | **$252/month** (36% savings) |
| Production RDS db.r5.large @ $0.24/hr = $175/month | db.r5.large Reserved (1yr) @ $0.149/hr = $108/month | **$67/month** (38% savings) |

### 3. **Unattached EBS Volumes and Old Snapshots**

**Symptoms:**
- EBS volumes with status "available" (not attached to any instance)
- Hundreds of old EBS snapshots from deleted instances
- Provisioned IOPS (io1/io2) volumes when gp3 would work

**How to check:**
```bash
# Find unattached volumes
aws ec2 describe-volumes --filters Name=status,Values=available

# Count old snapshots
aws ec2 describe-snapshots --owner-ids self --query 'Snapshots[*].[SnapshotId,StartTime,VolumeSize]' --output table
```

**Potential savings:**
- Delete unattached volumes: $0.10/GB-month (100GB = $10/month per volume)
- Delete old snapshots (>90 days): $0.05/GB-month
- Switch from io2 to gp3: 20-40% cost reduction

**Example:**
| Current | Waste | Fix | Savings |
|---------|-------|-----|---------|
| 50x unattached 100GB volumes @ $0.10/GB = $500/month | Volumes from deleted instances | Delete all unattached volumes | **$500/month** |
| 500 snapshots (avg 50GB) = 25TB @ $0.05/GB = $1,250/month | Snapshots >1 year old | Keep only last 30 days = 5TB @ $250/month | **$1,000/month** |

### 4. **Excessive Data Transfer Costs**

**Symptoms:**
- Data Transfer Out costs >$5k/month
- Frequent inter-region transfers
- Large file downloads from S3 directly (not using CloudFront)

**How to check:**
- AWS Cost Explorer → Filter: Service = "EC2-Other" (data transfer)
- Look for "Data Transfer Out - Internet" and "Data Transfer - Inter-Region"

**Potential savings:**
- Use CloudFront CDN: 60-80% reduction in data transfer costs
- Keep data in same region: Eliminate inter-region transfer fees
- Compress data before transfer: 50-70% reduction in bandwidth

**Example:**
| Current | Waste | Fix | Savings |
|---------|-------|-----|---------|
| 10TB/month direct S3 downloads @ $0.09/GB = $900/month | No CDN caching | CloudFront with 80% cache hit = $200/month | **$700/month** |
| Inter-region transfer (us-east-1 → us-west-2) @ $0.02/GB = $400/month | Databases in different regions | Migrate to single region | **$400/month** |

### 5. **Over-Provisioned RDS Databases**

**Symptoms:**
- Large RDS instances (db.r5.2xlarge) with low CPU/memory usage
- Multi-AZ enabled for dev/staging databases
- General Purpose SSD (gp2) instead of cheaper gp3

**How to check:**
- AWS Cost Explorer → RDS costs by instance type
- RDS Console → Database → Monitoring → CPU/Memory utilization
- Check if Multi-AZ is enabled for non-production databases

**Potential savings:**
- Downsize instances: 50% cost reduction
- Disable Multi-AZ for dev/staging: 50% cost reduction
- Switch gp2 → gp3 storage: 20% cost reduction

**Example:**
| Current | Waste | Fix | Savings |
|---------|-------|-----|---------|
| Production: db.r5.2xlarge Multi-AZ @ $1.92/hr = $1,382/month | CPU avg 25% | db.r5.large Multi-AZ @ $0.48/hr = $346/month | **$1,036/month** |
| Dev: db.r5.large Multi-AZ @ $0.48/hr = $346/month | Multi-AZ not needed | db.r5.large Single-AZ @ $0.24/hr = $173/month | **$173/month** |
| 1TB gp2 storage @ $0.115/GB = $115/month | Using old storage type | 1TB gp3 @ $0.08/GB = $80/month | **$35/month** |

### 6. **Unused Load Balancers, NAT Gateways, Elastic IPs**

**Symptoms:**
- Load Balancers (ALB/NLB) with no active traffic
- NAT Gateways in every availability zone (you usually need 1-2)
- Elastic IPs not attached to running instances

**How to check:**
- EC2 Console → Load Balancers → Check "Active Connection Count" metric
- VPC Console → NAT Gateways → Count how many you have
- EC2 Console → Elastic IPs → Filter: not associated

**Potential savings:**
- Delete unused Load Balancers: $16-25/month each
- Reduce NAT Gateways: $32/month per gateway + data processing fees
- Release unassociated Elastic IPs: $3.60/month each

**Example:**
| Current | Waste | Fix | Savings |
|---------|-------|-----|---------|
| 5 ALBs (3 with zero traffic) @ $16/month = $80/month | Load balancers for old projects | Delete 3 unused ALBs = $32/month | **$48/month** |
| 6 NAT Gateways (1 per AZ across 2 regions) @ $32/month = $192/month | Over-redundancy | Use 2 NAT Gateways (1 per region) = $64/month | **$128/month** |
| 20 unassociated Elastic IPs @ $3.60/month = $72/month | IPs from deleted instances | Release all unused IPs | **$72/month** |

### 7. **CloudWatch Logs Retention Too Long**

**Symptoms:**
- CloudWatch Logs costs >$1,000/month
- Logs retained forever (default: never expire)
- Excessive log verbosity (DEBUG level in production)

**How to check:**
- CloudWatch Console → Logs → Log Groups
- Check "Stored Bytes" and "Retention" settings
- Look for log groups with "Never Expire" retention

**Potential savings:**
- Set retention to 7-30 days instead of "Never Expire": 70-90% reduction
- Reduce log verbosity: 50% reduction in ingestion costs
- Export old logs to S3 (90% cheaper): $0.023/GB-month vs $0.50/GB-month

**Example:**
| Current | Waste | Fix | Savings |
|---------|-------|-----|---------|
| 1TB logs with "Never Expire" @ $0.50/GB = $500/month | Logs from 2+ years ago | Set 30-day retention = 50GB @ $25/month | **$475/month** |
| DEBUG-level logging in production: 500GB/month ingestion @ $0.50/GB = $250/month | Too verbose | Change to INFO level = 100GB/month @ $50/month | **$200/month** |

### 8. **Running Dev/Staging Environments 24/7**

**Symptoms:**
- Development, staging, QA environments running nights and weekends
- No auto-stop/start schedules
- Same instance sizes as production

**How to check:**
- Tag instances with "Environment" tag (dev/staging/prod)
- AWS Cost Explorer → Filter by tag → Compare dev vs prod costs
- If dev costs >30% of prod costs, you're overspending

**Potential savings:**
- Auto-stop dev/staging: 8pm-8am + weekends = 60% cost reduction
- Use smaller instances for non-prod: 50% cost reduction
- Use Spot Instances for dev/staging: 70% cost reduction

**Example:**
| Current | Waste | Fix | Savings |
|---------|-------|-----|---------|
| Dev environment running 24/7 @ $2,000/month | Unused 128 hours/week | Auto-stop 6pm-8am + weekends = $800/month | **$1,200/month** |
| Staging: 3x m5.2xlarge @ $1,382/month | Same size as prod | Use 3x m5.large @ $345/month | **$1,037/month** |

---

## Step 4: Use AWS Cost Optimization Tools

### 1. **AWS Trusted Advisor** (Automatic Recommendations)
- Navigate to: AWS Console → **Trusted Advisor**
- Check "Cost Optimization" section
- Review recommendations:
  - Low Utilization EC2 Instances
  - Unassociated Elastic IP Addresses
  - Underutilized EBS Volumes
  - Idle Load Balancers
  - Unoptimized RDS Instances

**Limitations:** Only available with Business/Enterprise Support plans (costs money)

### 2. **AWS Compute Optimizer** (Rightsizing Recommendations)
- Navigate to: AWS Console → **Compute Optimizer**
- Enable Compute Optimizer (free)
- Wait 24 hours for analysis
- Review recommendations for:
  - EC2 instance rightsizing
  - Auto Scaling group optimization
  - EBS volume type recommendations

### 3. **AWS Cost Anomaly Detection** (Find Unexpected Spikes)
- Navigate to: AWS Console → **Cost Anomaly Detection**
- Create monitor for "AWS Services"
- Set alert threshold: >$500 increase from baseline
- Get alerts when costs spike unexpectedly

### 4. **Third-Party Tools** (More Advanced)
If you want deeper analysis, consider:
- **CloudHealth** (by VMware): Multi-cloud cost optimization
- **Spot.io**: Automated EC2 Spot Instance management (70% savings)
- **Apptio Cloudability**: Cost allocation and showback
- **AWS Well-Architected Tool**: Free tool to review architecture best practices

---

## Step 5: AWS Cost Audit Checklist

Use this checklist to systematically find waste:

### EC2 Compute
- [ ] Run Cost Explorer report: EC2 by Instance Type (last 3 months)
- [ ] Check CloudWatch: CPU/Memory utilization for all instances
- [ ] Identify instances with <20% CPU utilization → Downsize or terminate
- [ ] Check Reserved Instance coverage → If <50%, buy RIs for steady workloads
- [ ] Review dev/staging environments → Implement auto-stop schedules
- [ ] Check for Spot Instance opportunities → Dev/staging, batch jobs
- [ ] Review instance types → Are you using latest generation? (m5 vs m4, c6i vs c5)

### Storage (EBS, S3, Snapshots)
- [ ] Find unattached EBS volumes → Delete if unused
- [ ] Count EBS snapshots → Delete snapshots >90 days old
- [ ] Review EBS volume types → Switch io1/io2 → gp3 where possible
- [ ] Check S3 storage classes → Move infrequent access data to S3 Glacier
- [ ] Review S3 lifecycle policies → Auto-delete old objects
- [ ] Check for incomplete multipart uploads in S3 → Delete to save storage

### Databases (RDS)
- [ ] Run Cost Explorer report: RDS by Instance Type
- [ ] Check RDS CPU/Memory utilization → Downsize if <30%
- [ ] Review Multi-AZ settings → Disable for dev/staging
- [ ] Check RDS Reserved Instance coverage → Buy RIs for production databases
- [ ] Review storage type → Switch gp2 → gp3 (20% savings)
- [ ] Check for idle RDS instances → Stop or delete

### Networking
- [ ] Review Data Transfer Out costs → Use CloudFront CDN if >$2k/month
- [ ] Check NAT Gateway count → Reduce to 1-2 per region
- [ ] Find unassociated Elastic IPs → Release unused IPs
- [ ] Review Load Balancers → Delete unused ALBs/NLBs
- [ ] Check inter-region data transfer → Keep workloads in same region

### Monitoring & Logging
- [ ] Review CloudWatch Logs retention → Set to 7-30 days, not "Never Expire"
- [ ] Check log verbosity → Change DEBUG → INFO in production
- [ ] Review CloudWatch metrics → Delete unused custom metrics
- [ ] Check Lambda function memory → Right-size to actual usage

### Other Services
- [ ] Review unused resources in Cost Explorer → Look for services you don't recognize
- [ ] Check for old Lambda functions → Delete unused functions
- [ ] Review API Gateway usage → Delete unused APIs
- [ ] Check for orphaned resources → Search for "available", "detached", "unused" in console

---

## Step 6: Calculate Your Potential Savings

Use this worksheet to estimate total savings:

| Waste Category | Current Monthly Cost | Potential Savings | Action Required |
|----------------|---------------------|-------------------|-----------------|
| **EC2 Rightsizing** | $_______ | $_______ (30-50%) | Downsize instances |
| **Reserved Instances** | $_______ | $_______ (30-60%) | Buy RIs/Savings Plans |
| **Dev/Staging Auto-Stop** | $_______ | $_______ (60-70%) | Implement schedules |
| **Unattached EBS Volumes** | $_______ | $_______ (100%) | Delete volumes |
| **Old Snapshots** | $_______ | $_______ (70-90%) | Delete old snapshots |
| **Data Transfer (CloudFront)** | $_______ | $_______ (60-80%) | Enable CDN |
| **RDS Rightsizing** | $_______ | $_______ (30-50%) | Downsize databases |
| **RDS Multi-AZ (Dev)** | $_______ | $_______ (50%) | Disable Multi-AZ |
| **Unused Load Balancers** | $_______ | $_______ (100%) | Delete unused LBs |
| **NAT Gateways** | $_______ | $_______ (50-70%) | Reduce count |
| **CloudWatch Logs Retention** | $_______ | $_______ (70-90%) | Set 30-day retention |
| **Elastic IPs** | $_______ | $_______ (100%) | Release unused IPs |
| **Other** | $_______ | $_______ | _____________ |
| **TOTAL** | **$40,000** | **$_______** | |

**Target:** $8,000-$16,000/month savings (20-40% of $40k)

---

## Step 7: Action Plan (Prioritized by Savings)

### Quick Wins (Do This Week) - Low Risk, High Impact
1. **Delete unattached EBS volumes** → Savings: $200-1,000/month, Risk: Low
2. **Release unassociated Elastic IPs** → Savings: $50-200/month, Risk: Low
3. **Delete old EBS snapshots (>90 days)** → Savings: $500-2,000/month, Risk: Low
4. **Set CloudWatch Logs retention to 30 days** → Savings: $200-500/month, Risk: Low
5. **Delete unused Load Balancers** → Savings: $50-200/month, Risk: Low

**Total Quick Wins:** $1,000-3,900/month

### Medium-Term (Next 2-4 Weeks) - Requires Testing
1. **Downsize over-provisioned EC2 instances** → Savings: $2,000-5,000/month, Risk: Medium
2. **Implement dev/staging auto-stop schedules** → Savings: $1,000-3,000/month, Risk: Low
3. **Switch EBS gp2 → gp3** → Savings: $200-800/month, Risk: Low
4. **Downsize over-provisioned RDS instances** → Savings: $1,000-3,000/month, Risk: Medium
5. **Disable Multi-AZ for dev/staging RDS** → Savings: $500-1,500/month, Risk: Low
6. **Enable CloudFront CDN** → Savings: $500-2,000/month, Risk: Low

**Total Medium-Term:** $5,200-15,300/month

### Long-Term (Next 1-3 Months) - Requires Planning
1. **Buy Reserved Instances for steady workloads** → Savings: $3,000-8,000/month, Risk: Low (commitment)
2. **Migrate to Spot Instances for dev/batch jobs** → Savings: $1,000-3,000/month, Risk: Medium
3. **Consolidate services to single region** → Savings: $500-2,000/month, Risk: High
4. **Implement S3 lifecycle policies** → Savings: $200-1,000/month, Risk: Low
5. **Reduce log verbosity (DEBUG → INFO)** → Savings: $200-500/month, Risk: Low

**Total Long-Term:** $4,900-14,500/month

---

## Step 8: Monthly Review Process

**Prevent cost creep** by reviewing AWS costs monthly:

### Monthly AWS Cost Review Checklist (30 minutes)
- [ ] Run Cost Explorer: Monthly costs by Service (compare to last month)
- [ ] Check for anomalies: any service cost increased >20%?
- [ ] Review new resources: any unexpected services or instances?
- [ ] Check Trusted Advisor: any new cost optimization recommendations?
- [ ] Review Reserved Instance utilization: are you using 90%+ of RIs?
- [ ] Spot check 3-5 EC2 instances: still right-sized?
- [ ] Clean up: delete any new unattached volumes, snapshots, IPs

**Assign owner:** Someone on your team should own this monthly review.

---

## Next Steps: Start Your AWS Cost Audit

### Week 1: Data Collection
1. Enable AWS Cost Explorer (if not already enabled)
2. Run all Cost Explorer reports (see Step 1)
3. Enable AWS Compute Optimizer
4. Export data to spreadsheet for analysis

### Week 2: Identify Quick Wins
1. Run unattached EBS volume check
2. Run old snapshot check
3. Run unused Elastic IP check
4. Run unused Load Balancer check
5. Execute deletions (save $1,000-3,900/month)

### Week 3: Analyze Compute & Database
1. Review EC2 instance utilization
2. Review RDS instance utilization
3. Identify rightsizing opportunities
4. Create dev/staging auto-stop schedules
5. Plan instance downsizing (test in staging first)

### Week 4: Execute Optimizations
1. Downsize 2-3 non-critical instances (test)
2. Implement dev/staging auto-stop
3. Switch EBS gp2 → gp3
4. Set CloudWatch Logs retention to 30 days
5. Measure savings

**Expected Result After 4 Weeks:** $5,000-10,000/month savings (12-25% reduction)

---

## Questions to Answer

To prioritize where to look first, answer these:

1. **What's your production vs. dev/staging cost split?**
   - If dev costs >30% of prod, focus on auto-stop schedules

2. **Do you have Reserved Instances or Savings Plans?**
   - If no, this is likely your biggest opportunity (30-60% savings)

3. **What are your top 3 services by cost?**
   - Focus optimization efforts on these services first

4. **Do you run 24/7 workloads or batch jobs?**
   - 24/7 → Reserved Instances
   - Batch → Spot Instances

5. **How old is your infrastructure?**
   - If >2 years, you're likely using outdated instance types and storage

6. **Do you have HIPAA compliance requirements?**
   - If yes, this limits some optimizations (e.g., Spot Instances for patient data)

---

## Summary: Your AWS Cost Audit Roadmap

**Goal:** Find $8,000-$16,000/month in waste (20-40% of $40k budget)

**Timeline:**
- **Week 1:** Data collection (Cost Explorer, Trusted Advisor)
- **Week 2:** Quick wins ($1,000-3,900/month savings)
- **Week 3-4:** Medium-term optimizations ($5,200-15,300/month savings)
- **Month 2-3:** Long-term planning (Reserved Instances, Spot, consolidation)

**Expected Outcome:**
- **Conservative:** $8,000/month savings → $96k/year
- **Aggressive:** $16,000/month savings → $192k/year

**Next Action:** Run Cost Explorer reports and post the top 10 services by cost. I'll help you identify specific waste in your environment.
