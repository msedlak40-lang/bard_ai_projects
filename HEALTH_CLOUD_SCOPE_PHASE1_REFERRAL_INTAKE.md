# Health Cloud Streamlined Workflow Scope
## Phase 1: Referral Intake & Document Processing

**Version:** 1.0 — Draft for Review
**Date:** December 2024
**Status:** Scoping

---

## Executive Summary

This document outlines how Salesforce Health Cloud can streamline the referral intake process, leveraging native healthcare features to replace manual workflows, reduce duplicate data entry, and automate document processing.

---

## Current State — Referral Intake

### Process Flow (Today)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ CURRENT STATE: REFERRAL INTAKE                                               │
└──────────────────────────────────────────────────────────────────────────────┘

    ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
    │   EMAIL     │     │  WEB FORM   │     │   OTHER     │
    │  (majority) │     │  (minority) │     │  (portals)  │
    └──────┬──────┘     └──────┬──────┘     └──────┬──────┘
           │                   │                   │
           └───────────────────┴───────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   SHARED INBOX      │
                    │   (1 person triage) │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   DOCUPIPE          │
                    │   - Merges docs     │
                    │   - Extracts data   │
                    │   - Mixed accuracy  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   MANUAL REVIEW     │
                    │   - 75% incomplete  │
                    │   - Chase missing   │◄───── Phone/Email/Text
                    │     data            │       to Patient/Adjuster
                    └──────────┬──────────┘
                               │
           ┌───────────────────┴───────────────────┐
           │                                       │
           ▼                                       ▼
┌─────────────────────┐               ┌─────────────────────┐
│   SALESFORCE        │               │   RAINTREE          │
│   - Manual entry    │               │   - Manual entry    │
│   - Case created    │               │   - Case created    │
│                     │               │   - Docs uploaded   │
└─────────────────────┘               └─────────────────────┘
           │                                       │
           └───────────────────┬───────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   EMR               │
                    │   - Different       │
                    │     required fields │
                    │   - Case created    │
                    └─────────────────────┘
```

### Current Pain Points

| Pain Point | Impact | Frequency |
|------------|--------|-----------|
| 75% of referrals missing data | Delays placement, adjuster frustration | Daily |
| Manual data entry in 2 systems (SF + RT) | Duplicate work, errors | Every referral |
| Single person inbox triage | Bottleneck, single point of failure | Daily |
| DocuPipe mixed accuracy | Still requires manual review | Every referral |
| Web form allows bad data | Garbage in, garbage out | Ongoing |
| No visibility into referral status | Adjusters ask "where's my referral?" | Daily |
| Task/ticket explosion | Overwhelms case owners | Every communication |
| Email tokens to wrong case | Lost referrals | Unknown frequency |

---

## Future State — Health Cloud Streamlined

### Process Flow (Proposed)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ FUTURE STATE: HEALTH CLOUD REFERRAL INTAKE                                   │
└──────────────────────────────────────────────────────────────────────────────┘

    ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
    │   EMAIL     │     │  WEB FORM   │     │   API/EDI   │
    │             │     │ (validated) │     │   (837/270) │
    └──────┬──────┘     └──────┬──────┘     └──────┬──────┘
           │                   │                   │
           └───────────────────┴───────────────────┘
                               │
                               ▼
              ┌────────────────────────────────────┐
              │  HEALTH CLOUD REFERRAL MANAGEMENT  │
              │                                    │
              │  ┌────────────────────────────┐    │
              │  │ Intelligent Document       │    │
              │  │ Automation (IDA)           │    │
              │  │ - OCR extraction           │    │
              │  │ - AI field mapping         │    │
              │  │ - Confidence scoring       │    │
              │  └─────────────┬──────────────┘    │
              │                │                   │
              │                ▼                   │
              │  ┌────────────────────────────┐    │
              │  │ Auto-Create Records        │    │
              │  │ - CareRequest (referral)   │    │
              │  │ - Patient/Account          │    │
              │  │ - Authorization            │    │
              │  └─────────────┬──────────────┘    │
              │                │                   │
              │                ▼                   │
              │  ┌────────────────────────────┐    │
              │  │ Completeness Check         │    │
              │  │ - Required fields valid?   │    │
              │  │ - Route by status:         │    │
              │  │   ✓ Complete → Placement   │    │
              │  │   ✗ Incomplete → Queue     │    │
              │  └─────────────┬──────────────┘    │
              │                │                   │
              └────────────────┼──────────────────┘
                               │
           ┌───────────────────┴───────────────────┐
           │                                       │
           ▼                                       ▼
┌─────────────────────────┐           ┌─────────────────────────┐
│  COMPLETE REFERRALS     │           │  INCOMPLETE REFERRALS   │
│                         │           │                         │
│  Auto-assign to:        │           │  Auto-trigger:          │
│  - Placement queue      │           │  - Patient outreach     │
│  - Care Team            │           │  - Adjuster outreach    │
│                         │           │  - Track what's missing │
└───────────┬─────────────┘           └───────────┬─────────────┘
            │                                     │
            │         ┌───────────────────────────┘
            │         │ (when complete)
            ▼         ▼
┌─────────────────────────────────────────────────────────────┐
│  HEALTH CLOUD = SINGLE SOURCE OF TRUTH                      │
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │ Salesforce  │◄──►│    EMR      │◄──►│  RainTree   │     │
│  │ Health Cloud│    │ (API sync)  │    │ (API sync)  │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│                                                             │
│  Patient ID + Claim ID flow automatically across systems    │
└─────────────────────────────────────────────────────────────┘
```

---

## Health Cloud Features to Leverage

### 1. Referral Management

**Native Object:** `CareRequest` (Type = Referral)

| Capability | How It Helps |
|------------|--------------|
| Referral lifecycle tracking | See status from receipt → placement |
| Required field enforcement | Can't progress until complete |
| Referral source tracking | Know which adjusters send incomplete referrals |
| SLA tracking | Alert if referral aging |

**Configuration Needed:**
- Define referral record type on CareRequest
- Map required fields for your workflow
- Build referral status picklist (Received → In Review → Pending Info → Ready for Placement → Placed)

---

### 2. Intelligent Document Automation (IDA)

**What It Does:** Extracts data from uploaded documents using OCR + AI

| Capability | How It Helps |
|------------|--------------|
| Document classification | Knows if it's a script, auth letter, medical record |
| Field extraction | Pulls patient name, DOB, diagnosis, authorized visits, etc. |
| Confidence scoring | Flags low-confidence extractions for human review |
| Auto-population | Extracted data pre-fills record fields |

**vs. DocuPipe:**
| Feature | DocuPipe (Current) | Health Cloud IDA |
|---------|-------------------|------------------|
| Native to Salesforce | No (external) | Yes |
| Auto-creates records | No | Yes |
| Trains on your documents | Unknown | Yes |
| Confidence scoring | Unknown | Yes |
| Reduces context switching | No | Yes |

**Configuration Needed:**
- Enable IDA (may require additional licensing)
- Train extraction model on your document types
- Map extracted fields to CareRequest/Patient fields
- Define confidence threshold for auto-accept vs. human review

---

### 3. Omni-Channel Intake

**What It Does:** Routes incoming work to the right person/queue automatically

| Capability | How It Helps |
|------------|--------------|
| Email-to-Case improvements | Smarter routing than current setup |
| Skills-based routing | Route complex referrals to experienced staff |
| Queue management | No single-person bottleneck |
| Presence-based assignment | Only route to available staff |
| Priority handling | Urgent referrals get handled first |

**Configuration Needed:**
- Define intake queues (by client? by complexity? by region?)
- Set routing rules
- Configure agent presence/capacity

---

### 4. Web Form Validation (Experience Cloud or External)

**What It Does:** Enforces data quality at entry point

| Capability | How It Helps |
|------------|--------------|
| Field validation | Date formats, required fields, picklists |
| Conditional logic | Show/hide fields based on answers |
| Document upload | Attach referral docs at submission |
| Auto-create referral | Submitting form creates CareRequest |
| Confirmation + tracking | Adjuster gets confirmation # and status link |

**Configuration Needed:**
- Rebuild web form with proper validation
- Map form fields to Salesforce objects
- Create confirmation email template
- Build status portal (optional)

---

### 5. Automated Outreach for Missing Data

**What It Does:** Automatically contacts patient/adjuster for missing info

| Capability | How It Helps |
|------------|--------------|
| Flow-triggered outreach | When referral incomplete, send request |
| SMS/Email templates | "We need your employment status: A) Employed B) Self-employed..." |
| Response capture | Patient replies, data flows back to record |
| Escalation | If no response in X days, escalate or try another channel |
| Track attempts | Know who was contacted, when, response status |

**Configuration Needed:**
- Define "complete" vs. "incomplete" criteria
- Build outreach Flows for each missing data scenario
- Create SMS/email templates
- Configure response handling
- Set escalation timers

---

### 6. Integration Hub (MuleSoft or Native APIs)

**What It Does:** Connects Health Cloud to EMR and RainTree

| Capability | How It Helps |
|------------|--------------|
| Single data entry | Enter once in HC, sync to EMR + RT |
| Patient ID sync | Auto-push RT Patient ID back to HC |
| Real-time updates | Visit count, notes received flow back to HC |
| Event-driven | When referral placed, trigger EMR case creation |

**Integration Points Needed:**
| System | Direction | Data |
|--------|-----------|------|
| EMR | HC → EMR | Patient demographics, referral details, auth info |
| EMR | EMR → HC | Visit count, clinical status, notes received flag |
| RainTree | HC → RT | Patient, case, authorization, documents |
| RainTree | RT → HC | Patient ID, billing status, claim updates |

**Configuration Needed:**
- API mapping between systems
- Error handling and retry logic
- Sync scheduling (real-time vs. batch)
- Conflict resolution rules

---

## Implementation Phases

### Phase 1A: Foundation (Weeks 1-4)
**Goal:** Establish Health Cloud as referral intake system

| Task | Effort | Dependencies |
|------|--------|--------------|
| Configure CareRequest for referrals | Medium | None |
| Define required fields + validation | Low | Business rules |
| Build referral status workflow | Medium | None |
| Rebuild web form with validation | Medium | None |
| Configure Omni-Channel routing | Medium | Queue definitions |
| Migrate from single-person inbox | Low | Training |

**Quick Wins:**
- Web form stops accepting bad data
- Referrals route to queues, not one person
- Status visibility for adjusters

---

### Phase 1B: Document Intelligence (Weeks 5-8)
**Goal:** Automate document processing

| Task | Effort | Dependencies |
|------|--------|--------------|
| Enable IDA (or evaluate alternatives) | Medium | Licensing |
| Train extraction model on your docs | High | Sample documents |
| Map extracted fields to records | Medium | Field mapping |
| Build human review queue for low-confidence | Medium | IDA working |
| Sunset or integrate DocuPipe | Low | IDA working |

**Quick Wins:**
- Documents auto-populate referral fields
- Staff only review exceptions
- Consistent extraction accuracy

---

### Phase 1C: Automated Outreach (Weeks 9-12)
**Goal:** Auto-collect missing data

| Task | Effort | Dependencies |
|------|--------|--------------|
| Define completeness rules | Low | Business rules |
| Build patient outreach Flow (SMS/email) | Medium | Templates |
| Build adjuster outreach Flow | Medium | Templates |
| Configure response capture | Medium | Messaging setup |
| Build escalation logic | Low | Flows working |

**Quick Wins:**
- Incomplete referrals auto-trigger outreach
- Patients can respond via text
- Less manual chasing

---

### Phase 1D: Integration (Weeks 13-20)
**Goal:** Single entry, multi-system sync

| Task | Effort | Dependencies |
|------|--------|--------------|
| Map EMR API fields | Medium | EMR documentation |
| Build HC → EMR sync | High | API access |
| Map RainTree API fields | Medium | RT documentation |
| Build HC → RT sync | High | API access |
| Build RT → HC Patient ID sync | Medium | RT API |
| Build visit count sync (EMR → HC) | Medium | EMR API |
| End-to-end testing | High | All integrations |

**Quick Wins:**
- Enter data once
- Patient ID flows automatically
- No more duplicate entry

---

## Effort Summary

| Phase | Duration | Effort | Impact |
|-------|----------|--------|--------|
| 1A: Foundation | 4 weeks | Medium | High |
| 1B: Document Intelligence | 4 weeks | High | High |
| 1C: Automated Outreach | 4 weeks | Medium | High |
| 1D: Integration | 8 weeks | High | Very High |
| **Total** | **20 weeks** | **High** | **Transformational** |

---

## Success Metrics

| Metric | Current State | Target |
|--------|---------------|--------|
| Referrals missing data | 75% | < 25% |
| Time to data entry (per referral) | 15-30 min | < 5 min |
| Systems requiring manual entry | 3 (SF, RT, EMR) | 1 (HC only) |
| Inbox triage staffing | 1 person (bottleneck) | Queue-based |
| Adjuster "where's my referral" calls | Daily | Rare (self-service) |
| Task/ticket noise | High | Managed |

---

## Open Questions

1. **Licensing:** What Health Cloud edition do we have? Is IDA included or additional?
2. **EMR APIs:** What APIs does the in-house EMR expose? REST? SOAP? HL7 FHIR?
3. **RainTree APIs:** What integration options exist with RT?
4. **DocuPipe contract:** Are we locked in? Can we sunset it?
5. **Web form platform:** Is current form Salesforce-native or external?
6. **SMS capability:** Do we have Salesforce SMS enabled? What provider?

---

## Next Steps

1. [ ] Review this scope with stakeholders
2. [ ] Answer open questions (licensing, APIs)
3. [ ] Prioritize phases (can we start 1A while investigating 1D?)
4. [ ] Identify pilot group (specific client? referral type?)
5. [ ] Estimate budget (licensing, implementation, integration)

---

*This document will be expanded to cover subsequent phases: Provider Placement, Utilization Management/Re-Auth, Billing Integration, and Coach Workflows.*
