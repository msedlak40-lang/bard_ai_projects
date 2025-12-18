# Project Documentation: Operational Automation Initiative

**Last Updated:** December 2024
**Status:** In Progress — Awaiting team responses to clarifying questions

---

## Executive Summary

This project aims to identify and implement automation opportunities across the organization's PT referral and case management workflows. Work began with stakeholder questionnaires and culminated in an in-person meeting. We are now in the discovery phase to deeply understand current workflows before designing solutions.

---

## Work Completed

### Phase 1: Stakeholder Pre-Read Analysis

#### Coach Questionnaire Analysis (5 Respondents)

**Key Findings:**
- Coaches read **40+ PT notes per day** (not per week as originally assumed)
- Time per note: 5-15 minutes = **3-10+ hours/day** on note review
- Additional 30-90+ minutes/day on patient messaging
- **Unanimous feedback:** Most patient messages don't require clinical expertise

**Top Pain Points Identified:**
- Admin issues dominating coach time (scheduling, payments, transportation, authorization)
- Early-stage cases consuming time that should go to midpoint/outlier cases
- Non-clinical text messages

**Coach-Suggested Solution:**
- Automated check-in system: Initial + biweekly for first month (3 total)
- Manual intervention only when warranted

**Files Created:**
- `summarize_coach_responses.py` — Python script to read .docx files and generate summary
- `coach_response_summary.txt` — Plain text summary
- `COACH_QUESTIONNAIRE_SUMMARY.md` — Formatted markdown summary with tables

---

#### Intake Questionnaire Analysis (1 Respondent)

**Key Findings:**
- Processing **20+ referrals per day**
- Time per referral: **15-30 minutes**
- Data correction rate: 5-15% of cases
- Document sources: DocuPipe, Email, Portals, Eligibility feeds, Webforms, MSQ, API

**DocuPipe Assessment:**
| Works Well | Struggles With |
|------------|----------------|
| Expiration dates | Therapy type (multiple) |
| Surgery dates | Date extraction errors |
| Source highlighting | Multiple body parts/dx |
| | Service types from email vs. doc |

**Missing Data Collection:**
- Currently using phone, email, text to stakeholders, MDs, patients, clinics
- Open to automated patient texting for missing info + scheduling

---

### Phase 2: Critical Issues Identified

#### Salesforce Email Reply Issue

**Problem:** When a case manager replies to a tokenized email inside Salesforce, the reply is logged on the Case but does NOT reach the external recipient. New emails work; replies don't.

**Current Workaround:** Copy/paste content into new email (manual, error-prone)

**Status:** Pending discussion with Shiner for technical context

**File Created:**
- `salesforce_email_issue_summary.md` — Problem detail and clarifying questions

---

#### Task Triage Workflow Bottleneck

**Problem:** Case managers receive hundreds of tasks per day from emails, texts, and voicemails. Each must be manually reviewed before routing or action. Voicemails have no transcription.

**Impact:** Severe processing bottleneck slowing PT placement for injured workers

**File Created:**
- `workflow_summary.md` — Background and 22 meeting questions across 7 sections

---

### Phase 3: Meeting Preparation

#### Facilitation Guide Created

Comprehensive meeting guide with two sessions:

**Morning Session — Questionnaire Review:**
1. Coach Workflow Findings
2. Intake Team Findings
3. Salesforce Email Issue
4. Prioritization Discussion

**Afternoon Session — Broken Process Deep-Dive:**
- 41 learning-focused questions across 8 sections:
  - A: Understanding the Volume
  - B: Understanding the Content
  - C: Understanding the Required Data
  - D: Understanding the Routing
  - E: Understanding the Pain
  - F: Understanding Voicemails Specifically
  - G: Understanding Constraints
  - H: Defining Success

**Files Created:**
- `MEETING_FACILITATION_GUIDE.md` — Full markdown version
- `MEETING_FACILITATION_GUIDE.docx` — Print-ready Word document

---

#### Participant Communication

**File Created:**
- `PARTICIPANT_EMAIL_PREREAD.md` — Email template for meeting participants

---

### Phase 4: Post-Meeting Discovery (Current)

#### Workflow Details Received

After the in-person meeting, detailed workflow documentation was provided covering:

**Company Context:**
- Built own PPO of PT providers
- Built own EMR for work comp patient management
- PTs only access EMR when referred a case

**Systems Landscape:**
| System | Purpose | Connection |
|--------|---------|------------|
| Salesforce | Case management, communication | Patient ID (pushed from RT) |
| EMR (in-house) | Clinical documentation | Patient ID |
| RainTree (RT) | Billing (dual ledger) | Patient ID (source) |
| DocuPipe | Document extraction | Testing phase |

**Key Problems Identified:**

1. **Data Entry Duplication**
   - Intake enters data in Salesforce AND RainTree
   - ~75% of referrals lack enough info to proceed

2. **System Disconnection**
   - Patient ID connects EMR ↔ RT (generated in RT)
   - Must push Patient ID to SF manually
   - Claim ID discussed but each claim can have multiple cases

3. **Task/Ticket Explosion**
   - Email-to-case creates task for every communication
   - Every task also creates a ticket (trust-based tracking)
   - Can't forward tasks between departments in SF
   - Must use Outlook workaround (creates more tasks)

4. **Email Token Issues**
   - Clients recycle old emails with tokens
   - Ends up in wrong case or with departed employees
   - No detection mechanism

5. **Patient Check-In / Re-Auth Process**
   - Need to verify IE attendance
   - Need to track next doctor visit
   - Need to trigger outreach at visit threshold (2 remaining)
   - Critical for re-authorization timing
   - Told SF can't email non-individual addresses (needs verification)

6. **Missing Notes**
   - Team calls clinics for notes needed for billing
   - Some clinics direct bill, cutting Bard out of process

**File Received:**
- `Workflow Details.docx` — Comprehensive workflow description

---

#### Clarifying Questions Drafted

14 questions sent to team across 5 categories:

**Systems & Data (Q1-3):**
- EMR required fields vs. clinic required fields
- Patient ID flow sequence
- Claim ID vs. Case relationship

**Referral Intake (Q4-6):**
- Inbox triage volume and staffing
- Web form vs. email percentage
- DocuPipe current state

**Task/Ticket Problem (Q7-9):**
- Task creation triggers (inbound/outbound)
- Ticket object type and review process
- Recycled email token frequency

**Patient Check-In / Re-Auth (Q10-12):**
- IE check-in team size and volume
- Visit count data source
- SF email limitation verification

**Clinics & Notes (Q13-14):**
- Direct billing percentage
- Note lag time and escalation process

**Status:** Awaiting team responses

---

## Files in Repository

| File | Type | Description |
|------|------|-------------|
| `COACH_QUESTIONNAIRE_SUMMARY.md` | Markdown | Detailed coach response analysis |
| `coach_response_summary.txt` | Text | Plain text coach summary |
| `summarize_coach_responses.py` | Python | Script to process .docx questionnaires |
| `salesforce_email_issue_summary.md` | Markdown | SF email reply problem detail |
| `workflow_summary.md` | Markdown | Task triage workflow background |
| `MEETING_FACILITATION_GUIDE.md` | Markdown | Full meeting guide (morning + afternoon) |
| `MEETING_FACILITATION_GUIDE.docx` | Word | Print-ready facilitation guide |
| `PARTICIPANT_EMAIL_PREREAD.md` | Markdown | Email template for participants |
| `Workflow Details.docx` | Word | Post-meeting workflow description |
| `questionnaire_coach_1-5.docx` | Word | Raw coach questionnaire responses |
| `questionnaire_intake_1.docx` | Word | Raw intake questionnaire response |
| `Pre_Read_Stakeholder_Questionnaire.docx` | Word | Original questionnaire template |
| `Pre_Read_Response_Synthesis_Template.docx` | Word | Response synthesis template |
| `Strategic_Plan_Phase1.docx` | Word | Strategic planning document |
| `SIMPLIFIED_Facilitation_Guide.docx` | Word | Simplified facilitation guide |

---

## Next Steps

1. **Receive team responses** to 14 clarifying questions
2. **Document detailed process maps** based on responses
3. **Identify automation candidates** with effort/impact assessment
4. **Verify SF limitations** (email to non-individual addresses, task forwarding)
5. **Connect with Shiner** on Salesforce email reply issue
6. **Evaluate DocuPipe** gaps and potential improvements
7. **Design pilot** for highest-priority automation (likely patient check-ins)

---

## Open Questions Pending Response

### Systems & Data
1. What are EMR required fields vs. clinic required fields?
2. What is the Patient ID creation/flow sequence?
3. How do Claims relate to Cases? (examples needed)

### Referral Intake
4. What is the inbox triage daily volume and staffing?
5. What % of referrals come via web form vs. email?
6. What is DocuPipe's current accuracy?

### Task/Ticket Problem
7. Are tasks created for inbound AND outbound emails?
8. What is the ticket object and who reviews them?
9. How often do recycled email tokens cause issues?

### Patient Check-In / Re-Auth
10. How large is the IE check-in team and what's their volume?
11. Where does visit count data live (SF, EMR, or RT)?
12. Who said SF can't email non-individual addresses?

### Clinics & Notes
13. What % of clinics direct bill?
14. What is the typical note lag time?

---

*This document will be updated as team responses are received.*
