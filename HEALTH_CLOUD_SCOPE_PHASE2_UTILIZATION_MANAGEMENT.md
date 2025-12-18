# Health Cloud Streamlined Workflow Scope
## Phase 2: Utilization Management & Re-Authorization

**Version:** 1.0 — Draft for Review
**Date:** December 2024
**Status:** Scoping
**Prerequisite:** Phase 1 (Referral Intake) foundation in place

---

## Executive Summary

Utilization Management (UM) is a core Health Cloud capability designed for exactly what you need: tracking authorized services, monitoring utilization, and managing re-authorization workflows. This phase transforms the manual, reactive re-auth process into an automated, proactive system that prevents therapy delays.

---

## Current State — Utilization Management

### Process Flow (Today)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ CURRENT STATE: RE-AUTHORIZATION PROCESS                                      │
└──────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  INITIAL AUTHORIZATION                                                       │
│  - Referral includes "12 visits authorized"                                  │
│  - Stored as text/number field in Salesforce (?)                            │
│  - No structured tracking object                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  VISIT TRACKING                                                              │
│  - Visit count lives in EMR and/or RainTree                                  │
│  - NOT automatically synced to Salesforce                                    │
│  - Team must manually check or wait for notes                                │
│  - Some clinics direct bill (visits not tracked)                            │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  RE-AUTH TRIGGER (Manual)                                                    │
│  - Someone notices patient is near visit limit                               │
│  - OR patient/clinic calls saying "out of visits"                           │
│  - Often reactive, not proactive                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  MANUAL OUTREACH REQUIRED                                                    │
│  ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐       │
│  │  Patient         │    │  Clinic          │    │  Adjuster        │       │
│  │  "When is your   │    │  "Please send    │    │  "We need more   │       │
│  │   next MD visit?"│    │   progress note" │    │   visits auth'd" │       │
│  └──────────────────┘    └──────────────────┘    └──────────────────┘       │
│                                                                              │
│  All manual, all reactive, all time-consuming                               │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  THERAPY DELAY                                                               │
│  - If re-auth delayed, patient can't continue PT                            │
│  - Adjuster frustrated                                                       │
│  - Patient outcome impacted                                                  │
│  - Clinic may discharge patient                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Current Pain Points

| Pain Point | Impact | Root Cause |
|------------|--------|------------|
| No proactive visit tracking | Reactive re-auth, therapy gaps | Visit count not in SF |
| Manual "within 2 visits" monitoring | Missed triggers, delays | No automation |
| Chasing patients for MD visit date | Time-consuming | No automated outreach |
| Chasing clinics for progress notes | Time-consuming | No automated requests |
| No visibility into re-auth status | Adjusters ask for updates | No structured workflow |
| Direct billing clinics | Visits not tracked | No integration/contract enforcement |

---

## Future State — Health Cloud Utilization Management

### Process Flow (Proposed)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ FUTURE STATE: HEALTH CLOUD UTILIZATION MANAGEMENT                            │
└──────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  STRUCTURED AUTHORIZATION RECORD                                             │
│                                                                              │
│  CareRequest (Type: Authorization)                                           │
│  ├── Authorization Number: AUTH-2024-12345                                   │
│  ├── Service Type: Physical Therapy                                          │
│  ├── Authorized Units: 12 visits                                             │
│  ├── Used Units: 0 (auto-updated)                                            │
│  ├── Remaining Units: 12 (calculated)                                        │
│  ├── Start Date: 12/01/2024                                                  │
│  ├── End Date: 03/01/2025                                                    │
│  ├── Status: Active                                                          │
│  └── Re-Auth Threshold: 2 visits remaining                                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  REAL-TIME VISIT TRACKING (via Integration)                                  │
│                                                                              │
│  EMR/RainTree ──────► Health Cloud                                           │
│                                                                              │
│  When visit documented:                                                      │
│  1. EMR/RT sends visit event to HC                                           │
│  2. Authorization.UsedUnits increments                                       │
│  3. Authorization.RemainingUnits recalculates                                │
│  4. If RemainingUnits ≤ Threshold → Trigger Re-Auth Flow                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  AUTOMATED RE-AUTH WORKFLOW                                                  │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  TRIGGER: Remaining Visits ≤ 2                                       │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                          │                                                   │
│          ┌───────────────┼───────────────┐                                  │
│          ▼               ▼               ▼                                  │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                        │
│  │   PATIENT    │ │    CLINIC    │ │  INTERNAL    │                        │
│  │   OUTREACH   │ │   OUTREACH   │ │    TASK      │                        │
│  │              │ │              │ │              │                        │
│  │ Auto-SMS:    │ │ Auto-Email:  │ │ Create:      │                        │
│  │ "When is     │ │ "Progress    │ │ Re-Auth Case │                        │
│  │  your next   │ │  note needed │ │ Assign to    │                        │
│  │  MD visit?"  │ │  for [Name]" │ │ UM Team      │                        │
│  └──────┬───────┘ └──────┬───────┘ └──────┬───────┘                        │
│         │                │                │                                  │
│         ▼                ▼                ▼                                  │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                        │
│  │ Capture      │ │ Track        │ │ Dashboard    │                        │
│  │ Response     │ │ Note Receipt │ │ Visibility   │                        │
│  │ Update SF    │ │ Flag if Late │ │ for UM Team  │                        │
│  └──────────────┘ └──────────────┘ └──────────────┘                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  RE-AUTH SUBMISSION & TRACKING                                               │
│                                                                              │
│  CareRequest (Type: Re-Authorization)                                        │
│  ├── Parent Authorization: AUTH-2024-12345                                   │
│  ├── Requested Units: 12 additional visits                                   │
│  ├── Clinical Justification: [from progress note]                           │
│  ├── Status: Submitted → Under Review → Approved/Denied                     │
│  ├── Submitted To: [Adjuster/Payer]                                         │
│  ├── Submitted Date: 12/15/2024                                              │
│  ├── Decision Date: [pending]                                                │
│  └── SLA: 5 business days                                                    │
│                                                                              │
│  Automation:                                                                 │
│  - Alert if approaching SLA with no decision                                │
│  - Auto-update original auth when approved                                  │
│  - Notify Care Team of decision                                              │
│  - Update patient if needed                                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  CONTINUOUS MONITORING                                                       │
│                                                                              │
│  Dashboard: Utilization Management Overview                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  Authorizations Approaching Threshold    │  12                       │    │
│  │  Re-Auths Pending Submission             │   4                       │    │
│  │  Re-Auths Awaiting Decision              │   8                       │    │
│  │  Re-Auths Approaching SLA                │   2  ⚠️                   │    │
│  │  Clinics with Outstanding Note Requests  │   6                       │    │
│  │  Patients Pending MD Visit Response      │   9                       │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Health Cloud Features to Leverage

### 1. Authorization Records (CareRequest)

**Native Object:** `CareRequest` with Type = Prior Authorization / Concurrent Review

| Field | Purpose |
|-------|---------|
| `AuthorizedUnits` | Total visits approved |
| `UsedUnits` | Visits consumed (auto-updated) |
| `RemainingUnits` | Formula: Authorized - Used |
| `ServiceType` | PT, OT, etc. |
| `StartDate` / `EndDate` | Authorization validity window |
| `Status` | Active, Exhausted, Expired |
| `ReAuthThreshold` | When to trigger (e.g., 2 remaining) |

**Configuration Needed:**
- Enable CareRequest object
- Create Authorization record type
- Build formula field for RemainingUnits
- Configure status picklist

---

### 2. Visit Tracking Integration

**Approach:** Real-time or near-real-time sync from EMR/RainTree

| Method | Pros | Cons |
|--------|------|------|
| Real-time API | Immediate updates | More complex |
| Batch sync (hourly) | Simpler | Slight delay |
| Event-driven | Best of both | Requires event architecture |

**Integration Logic:**
```
When EMR/RT records a visit:
1. Find matching Patient + Authorization in HC
2. Increment UsedUnits
3. If RemainingUnits ≤ Threshold:
   - Fire Platform Event
   - Trigger Re-Auth Flow
```

**Configuration Needed:**
- API integration with EMR/RT
- Patient ID matching logic
- Platform Event for threshold trigger
- Error handling for unmatched visits

---

### 3. Automated Re-Auth Workflow (Flow)

**Trigger:** Platform Event when RemainingUnits ≤ ReAuthThreshold

**Flow Actions:**

| Step | Action | Details |
|------|--------|---------|
| 1 | Create Re-Auth CareRequest | Link to parent authorization |
| 2 | Patient Outreach | SMS: "When is your next MD visit?" |
| 3 | Clinic Outreach | Email: "Progress note needed for [Patient]" |
| 4 | Create Task | Assign to UM Team for monitoring |
| 5 | Update Timeline | Log all actions on patient record |

**Branching Logic:**
- If patient responds with MD date → Update field, schedule follow-up
- If clinic sends note → Attach to case, update checklist
- If no response in X days → Escalate (call instead of text/email)

---

### 4. Progress Note Request Tracking

**Object:** Custom object or Task with specific record type

| Field | Purpose |
|-------|---------|
| `Clinic` | Which clinic |
| `Patient` | Which patient |
| `RequestDate` | When requested |
| `DueDate` | When needed by |
| `Status` | Requested, Received, Overdue |
| `NoteDocument` | Attached file when received |

**Automation:**
- Auto-create when re-auth triggered
- Auto-close when note attached to case
- Escalate if overdue

---

### 5. MD Visit Date Tracking

**Field on Patient/Case:** `NextMDVisitDate`

**Capture Methods:**
- Patient responds to SMS → Parse and update
- Coach enters manually during check-in
- Clinic provides in progress note

**Automation:**
- Reminder to patient 2 days before MD visit
- Follow-up after MD visit: "Did you get a new PT script?"
- If new script → Alert intake for potential new referral

---

### 6. Re-Auth SLA Monitoring

**Dashboard Component:** Re-Auths Approaching SLA

**Fields:**
- `SubmittedDate`
- `ExpectedDecisionDate` (Submitted + SLA days)
- `ActualDecisionDate`
- `DaysUntilSLA` (formula)

**Automation:**
- Alert at 80% of SLA
- Escalate at 100% of SLA
- Auto-log follow-up attempts

---

### 7. Adjuster/Payer Portal (Optional)

**Capability:** Give adjusters visibility into re-auth requests

| Feature | Benefit |
|---------|---------|
| Status visibility | Reduces "where's my re-auth?" calls |
| Document access | Adjuster can see progress note |
| Decision capture | Adjuster enters approval in portal |
| Notification | Auto-notify when decision entered |

**Implementation:** Experience Cloud community for adjusters

---

## Implementation Phases

### Phase 2A: Authorization Foundation (Weeks 1-3)
**Goal:** Structured authorization tracking

| Task | Effort | Dependencies |
|------|--------|--------------|
| Configure CareRequest for authorizations | Medium | Phase 1 complete |
| Build authorization entry screen | Low | Record type ready |
| Create RemainingUnits formula | Low | Fields defined |
| Migrate existing auth data | Medium | Data mapping |
| Build authorization list views | Low | None |

---

### Phase 2B: Visit Tracking Integration (Weeks 4-7)
**Goal:** Real-time utilization visibility

| Task | Effort | Dependencies |
|------|--------|--------------|
| Map visit data from EMR | Medium | EMR API access |
| Build visit sync integration | High | API development |
| Create Platform Event for threshold | Low | Integration working |
| Handle unmatched visits | Medium | Error queue |
| Test with live data | Medium | Integration complete |

---

### Phase 2C: Automated Re-Auth Workflow (Weeks 8-11)
**Goal:** Proactive re-auth initiation

| Task | Effort | Dependencies |
|------|--------|--------------|
| Build re-auth trigger Flow | Medium | Platform Event ready |
| Create patient outreach (SMS) | Low | Messaging enabled |
| Create clinic outreach (email) | Low | Templates |
| Build response capture | Medium | Two-way messaging |
| Create UM team task/queue | Low | Queue setup |
| Build escalation logic | Medium | Flows working |

---

### Phase 2D: Monitoring & Reporting (Weeks 12-14)
**Goal:** Visibility and continuous improvement

| Task | Effort | Dependencies |
|------|--------|--------------|
| Build UM Dashboard | Medium | Data flowing |
| Create SLA monitoring alerts | Low | Fields in place |
| Build progress note tracker | Medium | Process defined |
| Create adjuster status report | Low | Dashboard ready |
| Train UM team | Medium | System ready |

---

## Effort Summary

| Phase | Duration | Effort | Impact |
|-------|----------|--------|--------|
| 2A: Authorization Foundation | 3 weeks | Medium | High |
| 2B: Visit Tracking Integration | 4 weeks | High | Very High |
| 2C: Automated Re-Auth Workflow | 4 weeks | Medium | Very High |
| 2D: Monitoring & Reporting | 3 weeks | Medium | High |
| **Total** | **14 weeks** | **High** | **Transformational** |

---

## Success Metrics

| Metric | Current State | Target |
|--------|---------------|--------|
| Re-auths triggered proactively | ~25%? | > 90% |
| Therapy gaps due to late re-auth | Unknown | < 5% |
| Manual visit count checks | Daily | Zero |
| Time to initiate re-auth | Days | Hours |
| Progress note request tracking | Manual | Automated |
| Adjuster "where's my re-auth" calls | Frequent | Rare |

---

## Open Questions

1. **Visit data source:** Does visit count come from EMR, RainTree, or both? Which is authoritative?
2. **Direct billing clinics:** How do we track visits for clinics that bypass billing?
3. **Re-auth submission:** How are re-auths submitted to adjusters today? Email? Portal? Fax?
4. **SLA standards:** What is the expected turnaround for re-auth decisions?
5. **Progress note format:** Do clinics send notes via email, fax, portal, or bNOTES?

---

*Continues to Phase 3: Coach Workflows*
