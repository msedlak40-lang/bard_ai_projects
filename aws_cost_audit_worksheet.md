# AWS Cost Audit Worksheet

**Current Monthly AWS Spend:** $40,000
**Target Savings:** $8,000-$16,000/month (20-40%)
**Audit Date:** ___________
**Completed By:** ___________

---

## Phase 1: Data Collection (Week 1)

### Cost Explorer Reports
- [ ] Enable AWS Cost Explorer (if not already enabled)
- [ ] Run "Monthly costs by Service" (last 3 months) - export CSV
- [ ] Run "EC2 costs by Instance Type" (last month) - export CSV
- [ ] Run "Reservation Utilization" report
- [ ] Run "Data Transfer" costs breakdown
- [ ] Run "RDS costs by Instance Type"

### Quick Checks
- [ ] AWS Trusted Advisor → Cost Optimization section
- [ ] Enable AWS Compute Optimizer
- [ ] Check if you have any Reserved Instances
- [ ] Check if you have any Savings Plans

---

## Phase 2: Top 10 Services Analysis

Fill in your top 10 AWS services by monthly cost:

| Rank | Service | Last Month Cost | Notes/Concerns |
|------|---------|----------------|----------------|
| 1 | _____________ | $_______ | _________________ |
| 2 | _____________ | $_______ | _________________ |
| 3 | _____________ | $_______ | _________________ |
| 4 | _____________ | $_______ | _________________ |
| 5 | _____________ | $_______ | _________________ |
| 6 | _____________ | $_______ | _________________ |
| 7 | _____________ | $_______ | _________________ |
| 8 | _____________ | $_______ | _________________ |
| 9 | _____________ | $_______ | _________________ |
| 10 | _____________ | $_______ | _________________ |

**Focus on services ranked 1-5 for optimization.**

---

## Phase 3: Quick Wins Checklist (Week 2)

### Unattached EBS Volumes
**Command:**
```bash
aws ec2 describe-volumes --filters Name=status,Values=available --query 'Volumes[*].[VolumeId,Size,VolumeType]' --output table
```

| Volume ID | Size (GB) | Type | Monthly Cost | Action |
|-----------|-----------|------|--------------|--------|
| vol-_____ | _____ | _____ | $_____ | [ ] Delete |
| vol-_____ | _____ | _____ | $_____ | [ ] Delete |
| vol-_____ | _____ | _____ | $_____ | [ ] Delete |

**Total Savings from Unattached Volumes:** $______/month

---

### Unassociated Elastic IPs
**Command:**
```bash
aws ec2 describe-addresses --query 'Addresses[?AssociationId==null].[PublicIp,AllocationId]' --output table
```

| Elastic IP | Allocation ID | Action |
|------------|---------------|--------|
| __________ | eipalloc-_____ | [ ] Release |
| __________ | eipalloc-_____ | [ ] Release |

**Count:** _____ IPs × $3.60 = **$_____/month savings**

---

### Old EBS Snapshots
**Command:**
```bash
aws ec2 describe-snapshots --owner-ids self --query 'Snapshots[?StartTime<`2025-09-01`].[SnapshotId,StartTime,VolumeSize]' --output table
```

**Snapshots older than 90 days:**
- Total count: _____
- Total size: _____ GB
- Cost: _____ GB × $0.05 = **$_____/month**
- [ ] Delete snapshots older than 90 days

**Total Savings from Old Snapshots:** $______/month

---

### Unused Load Balancers
Check Load Balancer metrics in AWS Console:
- Navigate to: EC2 → Load Balancers → Select LB → Monitoring → Active Connection Count

| Load Balancer Name | Type | Active Connections (7-day avg) | Monthly Cost | Action |
|--------------------|------|-------------------------------|--------------|--------|
| _________________ | ALB | _____ | $16 | [ ] Delete if zero |
| _________________ | NLB | _____ | $20 | [ ] Delete if zero |
| _________________ | ALB | _____ | $16 | [ ] Delete if zero |

**Total Savings from Unused LBs:** $______/month

---

### CloudWatch Logs Retention
Check log groups with "Never Expire" retention:
- Navigate to: CloudWatch → Logs → Log Groups

| Log Group | Current Retention | Size (GB) | Monthly Cost | Action |
|-----------|-------------------|-----------|--------------|--------|
| __________ | Never Expire | _____ | $_____ | [ ] Set to 30 days |
| __________ | Never Expire | _____ | $_____ | [ ] Set to 30 days |
| __________ | Never Expire | _____ | $_____ | [ ] Set to 30 days |

**Total Savings from Log Retention:** $______/month

---

### ✅ Quick Wins Total Savings

| Category | Savings |
|----------|---------|
| Unattached EBS Volumes | $______/month |
| Unassociated Elastic IPs | $______/month |
| Old EBS Snapshots | $______/month |
| Unused Load Balancers | $______/month |
| CloudWatch Logs Retention | $______/month |
| **QUICK WINS TOTAL** | **$______/month** |

**Target: $1,000-3,900/month**

---

## Phase 4: EC2 Optimization (Weeks 2-3)

### EC2 Instance Inventory

**Command:**
```bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,Tags[?Key==`Name`].Value|[0]]' --output table
```

List all running instances and their utilization:

| Instance ID | Type | Environment | CPU Avg (30d) | Monthly Cost | Optimization | Savings |
|-------------|------|-------------|---------------|--------------|--------------|---------|
| i-________ | m5.2xlarge | Production | ____% | $_____ | Downsize to m5.large | $_____ |
| i-________ | m5.large | Dev | ____% | $_____ | Auto-stop after hours | $_____ |
| i-________ | c5.xlarge | Staging | ____% | $_____ | Auto-stop after hours | $_____ |
| i-________ | _______ | ______ | ____% | $_____ | _______________ | $_____ |
| i-________ | _______ | ______ | ____% | $_____ | _______________ | $_____ |

**Optimization Rules:**
- CPU <20% for >30 days → Downsize instance type (50% savings)
- Dev/Staging environments → Auto-stop 6pm-8am + weekends (60% savings)
- Steady 24/7 workloads → Buy Reserved Instances (30-60% savings)

**Total EC2 Optimization Savings:** $______/month

---

### Reserved Instance Analysis

**Current Reserved Instance Coverage:** _____%

**Eligible for Reserved Instances:**
(Instances running 24/7 for >6 months)

| Instance Type | Count | On-Demand Cost | RI Cost (1yr) | Savings |
|---------------|-------|----------------|---------------|---------|
| m5.large | _____ | $_____ | $_____ | $_____ |
| c5.xlarge | _____ | $_____ | $_____ | $_____ |
| r5.large | _____ | $_____ | $_____ | $_____ |

**Action:**
- [ ] Purchase Reserved Instances for production workloads
- [ ] Or purchase Compute Savings Plan (more flexible)

**Total RI Savings:** $______/month

---

## Phase 5: RDS Optimization (Week 3)

### RDS Instance Inventory

**Command:**
```bash
aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceClass,Engine,MultiAZ,AllocatedStorage]' --output table
```

| DB Identifier | Instance Type | Multi-AZ | Environment | CPU Avg | Monthly Cost | Optimization | Savings |
|---------------|---------------|----------|-------------|---------|--------------|--------------|---------|
| ____________ | db.r5.2xlarge | Yes | Production | ___% | $_____ | Downsize to r5.large | $_____ |
| ____________ | db.r5.large | Yes | Dev | ___% | $_____ | Disable Multi-AZ | $_____ |
| ____________ | ____________ | ____ | ______ | ___% | $_____ | ______________ | $_____ |

**Optimization Rules:**
- CPU <30% for >30 days → Downsize instance (50% savings)
- Dev/Staging databases → Disable Multi-AZ (50% savings)
- Production databases → Buy RDS Reserved Instances (30-60% savings)

**Total RDS Optimization Savings:** $______/month

---

### RDS Storage Optimization

| DB Identifier | Storage Type | Size (GB) | Cost/GB | Monthly Cost | Optimization | Savings |
|---------------|--------------|-----------|---------|--------------|--------------|---------|
| ____________ | gp2 | _____ | $0.115 | $_____ | Switch to gp3 ($0.08) | $_____ |
| ____________ | io1 | _____ | $0.125 | $_____ | Switch to gp3 ($0.08) | $_____ |

**Total RDS Storage Savings:** $______/month

---

## Phase 6: Data Transfer & Networking (Week 3)

### Data Transfer Costs
From Cost Explorer → Filter: Service = "EC2-Other"

| Transfer Type | Monthly Cost | Notes |
|---------------|--------------|-------|
| Data Transfer Out - Internet | $_____ | Consider CloudFront CDN |
| Data Transfer - Inter-Region | $_____ | Consolidate to single region? |
| NAT Gateway Data Processing | $_____ | Review NAT Gateway count |

**Optimization:**
- [ ] If Data Transfer Out >$2k/month → Enable CloudFront CDN (60-80% savings)
- [ ] If Inter-Region >$500/month → Consolidate to single region (100% savings)

**Total Data Transfer Savings:** $______/month

---

### NAT Gateway Inventory

**How many NAT Gateways do you have?** _____

| NAT Gateway | Region | AZ | Monthly Cost | Action |
|-------------|--------|----|--------------|--------|
| nat-_______ | _____ | _____ | $32 + data | [ ] Keep / [ ] Delete |
| nat-_______ | _____ | _____ | $32 + data | [ ] Keep / [ ] Delete |

**Recommendation:** 1-2 NAT Gateways per region is usually sufficient.

**Total NAT Gateway Savings:** $______/month

---

## Phase 7: Dev/Staging Auto-Stop Schedules

### Environments to Auto-Stop

| Environment | Instances | Weekly Hours Running | Weekly Hours Needed | Savings |
|-------------|-----------|---------------------|-------------------|---------|
| Dev | _____ | 168 hrs (24/7) | 40 hrs (8am-5pm M-F) | 76% = $_____ |
| Staging | _____ | 168 hrs (24/7) | 80 hrs (8am-8pm M-F + testing) | 52% = $_____ |
| QA | _____ | 168 hrs (24/7) | 40 hrs (8am-5pm M-F) | 76% = $_____ |

**Implementation:**
- [ ] Use AWS Instance Scheduler (free)
- [ ] Or use Lambda + EventBridge rules
- [ ] Set schedule: Stop 6pm, Start 8am weekdays only

**Total Auto-Stop Savings:** $______/month

---

## Final Savings Summary

| Phase | Optimization | Savings/Month | Status |
|-------|--------------|---------------|--------|
| **Quick Wins** | | | |
| → Unattached EBS volumes | $______ | [ ] Done |
| → Elastic IPs | $______ | [ ] Done |
| → Old snapshots | $______ | [ ] Done |
| → Unused load balancers | $______ | [ ] Done |
| → CloudWatch logs retention | $______ | [ ] Done |
| **EC2 Optimization** | | | |
| → Rightsizing instances | $______ | [ ] Done |
| → Reserved Instances | $______ | [ ] Done |
| → Auto-stop dev/staging | $______ | [ ] Done |
| **RDS Optimization** | | | |
| → Rightsizing databases | $______ | [ ] Done |
| → Disable Multi-AZ (dev) | $______ | [ ] Done |
| → RDS Reserved Instances | $______ | [ ] Done |
| → Storage gp2 → gp3 | $______ | [ ] Done |
| **Networking** | | | |
| → CloudFront CDN | $______ | [ ] Done |
| → Reduce NAT Gateways | $______ | [ ] Done |
| → Consolidate regions | $______ | [ ] Done |
| **TOTAL SAVINGS** | **$______/month** | |

---

## Progress Tracking

**Week 1:** Data collection complete [ ]
**Week 2:** Quick wins executed [ ] → Saved $______/month
**Week 3:** EC2 optimization complete [ ] → Saved $______/month
**Week 4:** RDS & networking complete [ ] → Saved $______/month

**New Monthly AWS Cost:** $40,000 - $______ = **$______/month**
**Annual Savings:** $______ × 12 = **$______/year**
**Savings Percentage:** ______%

---

## Next Actions

**Immediate (This Week):**
1. ________________________________________________
2. ________________________________________________
3. ________________________________________________

**This Month:**
1. ________________________________________________
2. ________________________________________________
3. ________________________________________________

**Ongoing:**
- [ ] Set up monthly cost review meeting (30 min/month)
- [ ] Assign cost optimization owner: _________________
- [ ] Enable AWS Cost Anomaly Detection alerts
- [ ] Review Trusted Advisor recommendations quarterly

---

## Notes / Questions

_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
