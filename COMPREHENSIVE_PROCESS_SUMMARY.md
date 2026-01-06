# Bardavon Operations - Comprehensive Process Summary

**Purpose:** This document consolidates all discovery findings, team feedback, workflow documentation, system architecture, and pain points for use in planning Health Cloud optimization initiatives.

**Date:** January 2026
**Status:** Discovery Complete - Ready for Solution Design

---

## Table of Contents
1. [Company Overview & Systems](#1-company-overview--systems)
2. [Team Feedback Summary](#2-team-feedback-summary)
3. [Current Workflow & SLAs](#3-current-workflow--slas)
4. [Critical Pain Points](#4-critical-pain-points)
5. [DocuPipe Assessment](#5-docupipe-assessment)
6. [Health Cloud Current State](#6-health-cloud-current-state)
7. [Proposed Solutions & Phases](#7-proposed-solutions--phases)
8. [Open Questions](#8-open-questions)

---

## 1. Company Overview & Systems

### Business Context
- **Industry:** Workers' Compensation Physical Therapy Management
- **Business Model:** Coordinates PT services between injured workers, adjusters/payers, and PT clinics
- **Unique Position:** Has own PPO network AND own EMR system

### System Landscape

| System | Purpose | Key Functions |
|--------|---------|---------------|
| **Salesforce Health Cloud** | Case management, referral tracking | Patient records, case workflows, task management |
| **In-House EMR** | Clinical documentation | PT notes, progress tracking |
| **RainTree** | Billing/Revenue Cycle | Claims processing, visit billing, Patient ID generation |
| **DocuPipe** | Document processing (testing) | OCR extraction from referral documents |
| **bNOTES** | Clinical notes platform | Provider note submission |
| **Dremio** | Data analytics | Case prioritization, reporting |
| **BCS (Bardavon Core System)** | Core platform | Coach case list, Quality tab |

### Licensing
- **Salesforce Edition:** Unlimited
- **Clouds Licensed:** Health Cloud + Service Cloud + Sales Cloud

### Key Data Flow
```
Patient ID (Generated in RainTree) → Connects all systems
             ↓
   SF Case ←→ EMR Record ←→ RainTree Billing
```

---

## 2. Team Feedback Summary

### Coach Team (5 Respondents)

| Metric | Finding |
|--------|---------|
| **Note Volume** | 40+ PT notes reviewed per day |
| **Time per Note** | 5-15 minutes each |
| **Note Quality Issues** | Lack of subjective detail, vague objective measures, insufficient work-related info |
| **Messaging Burden** | Most messages are administrative/non-clinical |
| **Admin Tasks** | Re-auths, locating patient info, tracking cases |

**Key Coach Pain Points:**
1. Excessive non-clinical messaging consumes clinical time
2. PT notes lack detail needed for case management
3. Manual tracking of re-authorization timing
4. Difficulty finding patient information across systems
5. No automated prioritization of clinical vs administrative tasks

### Intake Team

| Metric | Finding |
|--------|---------|
| **Referral Volume** | 20+ referrals per day |
| **Time per Referral** | 15-30 minutes processing time |
| **Data Quality** | ~75% of referrals missing required information |
| **Primary Pain** | Dual data entry (Salesforce + RainTree) |

**Key Intake Pain Points:**
1. Missing data requires extensive follow-up
2. DocuPipe extraction inconsistent
3. Duplicate data entry across systems
4. No validation to catch errors before progression
5. Manual status updates throughout process

---

## 3. Current Workflow & SLAs

### Service Level Agreements (From Bardavon Workflow 2025)

| SLA | Target |
|-----|--------|
| Referral Confirmation Receipt | < 4 hours |
| Patient Initial Contact | < 4 hours |
| IE Scheduled Confirmed | 2 business days |
| Referral Date to IE Date | 3 business days |

### Workflow Stages

#### Stage 1: Intake (8 Steps)
1. Receipt of referral (Email, Fax, API, Webform, Phone)
2. Enter patient & case demographics
3. Referral receipt email to stakeholders (< 4 hours)
4. Reach out for missing critical info
5. Send authorization request if needed
6. Send welcome SMS to injured worker
7. Request authorization from adjuster if needed
8. Move to Triage status

#### Stage 2: Triage
1. Contact IW for IE availability (within 3 business days)
2. Enter remaining demographics
3. Log call with availability
4. Move to Scheduling status
- If no contact: SMS reminder, escalate to adjuster

#### Stage 3: Scheduling
1. Call network clinics using Clinic Placement Tool
2. Schedule IE within 3-day SLA
3. Send confirmation to clinic and stakeholders
4. Text IE details to patient
5. 24-hour confirmation text before appointment

#### Stage 4: Visit Management - IE Confirmation
1. Wait for note/bill within 48 hours
2. If no documentation, call clinic to confirm attendance
3. If attended: Move to "Therapy in Progress", reassign to Case Admin
4. If not attended: Move back to Scheduling

#### Stage 5: Therapy in Progress
- VM gets task if no notes/bills within 5 days
- Escalation paths:
  - **Re-Auth:** End of authorization needs
  - **Clinical Coach:** Medical issues/clinical concerns
  - **Rev Cycle:** Direct billing issues
  - **Case Administrator:** Delinquent clinic response, gaps in care

#### Stage 6: Case Administrator
- Primary contact for client stakeholders
- Manage Clinical Solutions inbox (24-48 hour response)
- Task delegation to Coaches, Reauth, Visit Management

#### Stage 7: Clinical Coach
- Invite to Recovery+ program at scheduling
- Intermittent patient engagement
- Daily/progress note review
- Case risk stratification and prioritization
- Provider education and case remediation

#### Stage 8: Re-Authorization (Care Coordinator)
- Trigger: 2 visits prior to end of authorization
- Send notice to clinic for progress note
- Collect additional scripts/signed plans of care
- Consult with Coach on medical necessity
- Send new authorization to clinic (24-48 hours)

---

## 4. Critical Pain Points

### Task/Ticket Explosion Problem
```
Current Flow:
Adjuster Email → Shared Inbox → Task + Ticket Created → Case Owner

Problem: Case owner can't forward tasks in Salesforce
         ↓
Workaround: Copy to Outlook → Email other department
         ↓
Result: Email-to-Case triggers AGAIN → Another Task + Ticket
         ↓
ONE CONVERSATION = 8+ TASKS/TICKETS
```

### Email Reply Bug (Salesforce)
- **Issue:** Replies sent from Salesforce don't reach external recipients
- **Workaround:** Copy content, exit SF, paste in Outlook
- **Impact:** Breaks audit trail, loses case context, time-consuming

### Data Quality Issues
| Issue | Impact |
|-------|--------|
| 75% referrals missing data | Extensive follow-up, delays |
| Token recycling | Emails land in wrong case or with departed employees |
| No cross-department visibility | Duplicate outreach, lost context |
| Dual data entry | SF + RainTree both need same information |
| Direct billing clinics | Visits not tracked in central system |

### Utilization Management Gaps
- No proactive visit tracking (rely on manual checks)
- Re-auth triggered reactively (patient or clinic calls)
- Manual outreach for MD visit dates and progress notes
- No structured authorization records
- Visit counts live in EMR/RainTree, not synced to Salesforce

---

## 5. DocuPipe Assessment

### UAT Testing Results (24+ Issues Logged)

| Issue Category | Count | Examples |
|----------------|-------|----------|
| Data in docs but not extracted | 18+ | Mobile phone, fax numbers, service types, referrer info |
| Extracted data incorrect | 3 | Wrong physician, wrong dates |
| Other/System issues | 3 | Document glitching, docs not transferred |

### Common Extraction Failures
- **Contact Info:** Mobile phone, fax numbers not extracting
- **Service Types:** Handwritten orders fail; multiple service types only capture one
- **Multiple Values:** Two addresses/DOIs only captures first, no flag for discrepancy
- **Referrer Info:** Pulls wrong name when multiple signatures present
- **Authorization Dates:** End date field was missing (now added)

### Positive Notes
- Some fixes applied during testing showing improvement
- Engineering responsive to field additions
- Core extraction working for standard typed documents

### DocuPipe Status
- **Phase:** UAT Testing
- **Recommendation:** Continue testing, address extraction gaps before production rollout

---

## 6. Health Cloud Current State

### Intake User Guide (Current Implementation)

The current Health Cloud implementation includes a 3-step referral intake process:

#### Step 1: Check for Duplicates
- Search existing records before creating new patient
- Match on name, DOB, SSN
- Option to use existing patient or create new

#### Step 2: About This Referral
- Capture referral source information
- Client/payer details
- Basic case information

#### Step 3: Case Details
- Patient demographics
- Injury information
- Authorization details
- Clinic preferences

### Coach Case List (Separate Project - Bardavon Platform)
- Prioritized case view for coaches
- Daily refresh from Dremio
- Filters: All, Coaching, No Coaching, Due Today/Overdue, New Notes
- Salesforce as system of truth for assignments
- Data synced to BCS for case list generation

### Features Potentially Underutilized
Based on licensing (Unlimited + Health + Service + Sales Cloud), these should be available:

| Feature | Expected Status | Actual Usage |
|---------|-----------------|--------------|
| Care Plans | Included | Unknown |
| Care Teams | Included | Unknown |
| CareRequest (Utilization Mgmt) | Included | Unknown |
| Omni-Channel Routing | Included | Unknown |
| Queues | Included | Limited |
| Flow Builder | Included | Unknown |
| Timeline View | Included | Unknown |
| Knowledge Base | Included | Unknown |
| Macros | Included | Unknown |

### Engineering Verification Needed
A checklist has been sent to engineering to verify:
1. Which Health Cloud features are currently enabled
2. Which are available but not enabled
3. Which require additional licensing

---

## 7. Proposed Solutions & Phases

### Phase 1: Referral Intake Optimization (20 weeks)
**Goal:** Reduce intake time from 15-30 min to under 10 min

| Component | Description |
|-----------|-------------|
| DocuPipe Integration | Auto-populate fields from scanned documents |
| Completeness Validation | Block progression until required fields populated |
| Referral Source Scoring | Track which sources send incomplete data |
| Duplicate Prevention | Enhanced matching before case creation |
| RainTree Integration | Eliminate dual data entry |

### Phase 2: Utilization Management (14 weeks)
**Goal:** Proactive re-authorization, eliminate therapy gaps

| Component | Description |
|-----------|-------------|
| CareRequest Objects | Structured authorization tracking |
| Visit Sync Integration | Real-time visit count from EMR/RainTree |
| Automated Alerts | Trigger at 2 visits remaining |
| Patient Outreach | Auto-SMS for MD visit dates |
| Clinic Outreach | Auto-email for progress notes |
| SLA Monitoring | Dashboard for re-auth pipeline |

### Phase 3: Coach Workflows (22 weeks)
**Goal:** Reduce administrative burden, prioritize clinical work

| Component | Description |
|-----------|-------------|
| Care Plans | Automated task generation by case stage |
| Smart Prioritization | Risk-based case sorting |
| Message Classification | Route admin vs clinical separately |
| Note Quality Scoring | Flag notes missing key information |
| Patient Timeline | 360-degree view of all touchpoints |
| Automated Check-ins | SMS-based patient engagement |

### Cross-Phase: Adjuster Communication Fix
**Goal:** Eliminate task explosion, unified case view

| Component | Description |
|-----------|-------------|
| Queue-Based Routing | Route by message type, not person |
| Care Teams | All departments on single case |
| Activity Timeline | All communications in one view |
| Transfer Actions | Handoff within Salesforce (no Outlook) |
| Email Reply Fix | Prerequisite - must resolve SF email bug |

---

## 8. Open Questions

### Systems & Integration
1. What is the authoritative source for visit counts - EMR or RainTree?
2. How do we track visits for direct-billing clinics?
3. Is API access available for EMR and RainTree integration?
4. What object is the "Ticket" that gets created alongside Tasks?

### Health Cloud Configuration
1. Is the Health Cloud managed package installed and current?
2. Are we using standard HC objects or custom objects?
3. Which features are enabled but not configured?
4. What customizations exist on standard objects?

### Process & Routing
1. Is there a documented routing matrix (if adjuster asks X, route to Y)?
2. Who is designated as "Case Owner" at each lifecycle stage?
3. What happens when something is sent to the wrong department?
4. Are there SLAs for responding to adjusters?

### DocuPipe
1. Timeline for production readiness?
2. Plan for handling handwritten orders?
3. Integration method (real-time vs batch)?

### Departments & Roles
1. Which departments communicate with adjusters?
2. Who reviews completed tickets?
3. What is the escalation path for unresolved issues?

---

## Appendix: Document Sources

| Document | Content |
|----------|---------|
| Coach Questionnaires (5) | Direct team feedback on daily work |
| Intake Questionnaire | Intake process pain points |
| Workflow Details Document | System architecture, data flows |
| Salesforce Email Issue Summary | Email reply bug documentation |
| Intake User Guide V4.3 | Current Health Cloud intake screens |
| Bardavon Workflow 2025 | SLAs and process stages |
| DocuPipe UAT Issues Log | 24+ extraction issues identified |
| Coach Case List Functional Overview | Bardavon Platform case list specs |
| Health Cloud Feature Checklist | Engineering verification request |
| Adjuster Communication Analysis | Task explosion problem mapping |
| Health Cloud Scope Documents | Phase 1-3 implementation plans |

---

*This document serves as the foundation for Health Cloud optimization planning. Updates will be made as engineering verification and additional discovery is completed.*
