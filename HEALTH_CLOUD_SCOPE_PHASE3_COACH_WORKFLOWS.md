# Health Cloud Streamlined Workflow Scope
## Phase 3: Coach Workflows & Patient Engagement

**Version:** 1.0 — Draft for Review
**Date:** December 2024
**Status:** Scoping
**Prerequisite:** Phase 1 (Referral Intake) and Phase 2 (Utilization Management) foundations in place

---

## Executive Summary

Coaches are clinical professionals spending the majority of their time on non-clinical tasks: reading PT notes, sending routine check-in messages, and handling admin issues. Health Cloud's Care Plans, Care Teams, and automation capabilities can shift coaches from reactive task processing to proactive clinical oversight of cases that truly need their expertise.

---

## Current State — Coach Workflows

### The Data (From Questionnaire Analysis)

| Metric | Finding |
|--------|---------|
| PT Notes Read | **40+ per day** (not per week) |
| Time per Note | 5-15 minutes |
| Daily Note Review Time | **3-10+ hours** |
| Daily Messaging Time | 30-90+ minutes |
| Message Type | **Mostly non-clinical** (admin issues) |

### Coach Feedback (Unanimous)

> **"Most patient messages do not require clinical expertise."**
>
> **"Eliminating the texting would be a massive help."**
>
> **"I believe I'm doing more admin work than utilizing my clinical acumen."**

### Process Flow (Today)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ CURRENT STATE: COACH DAILY WORKFLOW                                          │
└──────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  MORNING: CHECK TASK QUEUE                                                   │
│                                                                              │
│  Tasks from:                                                                 │
│  ├── Email-to-Case (every communication = task + ticket)                    │
│  ├── Patient text responses                                                  │
│  ├── Internal team forwards                                                  │
│  ├── System-generated alerts                                                 │
│  └── Follow-up reminders                                                     │
│                                                                              │
│  Problem: Hundreds of tasks, no prioritization                               │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  PT NOTE REVIEW (3-10+ hours/day)                                            │
│                                                                              │
│  For each case on audit list:                                                │
│  1. Open bNOTES or document repository                                       │
│  2. Find latest PT note(s)                                                   │
│  3. Read note (5-15 min each)                                                │
│  4. Extract key information:                                                 │
│     - ROM changes                                                            │
│     - Pain level/trend                                                       │
│     - Exercise progression                                                   │
│     - Compliance                                                             │
│     - Functional improvements (especially work-related)                      │
│     - Red flags                                                              │
│  5. Document findings in Salesforce                                          │
│  6. Determine action needed (if any)                                         │
│                                                                              │
│  Problem: Manual, repetitive, time-consuming                                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  PATIENT MESSAGING (30-90+ min/day)                                          │
│                                                                              │
│  Message Types:                                                              │
│  ├── Check-ins: "How are you feeling about your PT?"                        │
│  ├── Encouragement: "Keep it up!"                                           │
│  ├── Barrier identification: "What's getting in the way?"                   │
│  ├── Admin issues: Scheduling, payment, transportation, auth                │
│  └── Red flag escalation                                                    │
│                                                                              │
│  Problem: Most messages are admin, not clinical                              │
│  Problem: Early-stage cases get same attention as problem cases              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  REACTIVE ISSUE HANDLING                                                     │
│                                                                              │
│  Common issues (NON-CLINICAL):                                               │
│  ├── "I can't get scheduled"                                                │
│  ├── "I haven't received my pay"                                            │
│  ├── "I need transportation"                                                │
│  ├── "Do I have more visits?"                                               │
│  ├── "The clinic says I'm out of visits"                                    │
│  └── "I have a new PT script"                                               │
│                                                                              │
│  Problem: Coaches handling admin issues that don't need clinical judgment    │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  CLINICAL OVERSIGHT (What coaches SHOULD be doing)                           │
│                                                                              │
│  Cases needing clinical attention:                                           │
│  ├── Midpoint cases (are they progressing?)                                 │
│  ├── Outlier cases (why are they going long?)                               │
│  ├── Red flags (pain increase, non-compliance, setbacks)                    │
│  ├── Peer reviews requested by NCM/adjuster                                 │
│  └── Discharge planning                                                      │
│                                                                              │
│  Problem: Not enough time for this after admin work                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Current Pain Points

| Pain Point | Impact | Who Said It |
|------------|--------|-------------|
| Task overload | Can't prioritize what matters | All coaches |
| Non-clinical messaging | Wastes clinical expertise | Coach 1, 3, 4, 5 |
| Early-stage cases get too much attention | Time away from problem cases | Coach 1, 2 |
| Manual PT note reading | Hours per day | All coaches |
| Admin issues routed to coaches | Should go elsewhere | Coach 4 |
| No automated check-ins | Everything is manual | Coach 2 (suggested solution) |

---

## Future State — Health Cloud Coach Workflows

### Design Principles

1. **Automate the routine** — Check-ins, status updates, admin triage
2. **Surface the exceptions** — Only show coaches cases needing clinical judgment
3. **Summarize, don't read** — AI-assisted PT note summarization
4. **Route appropriately** — Admin issues go to admin team, clinical to coaches
5. **Prioritize by risk** — Midpoint/outlier cases get attention first

### Process Flow (Proposed)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ FUTURE STATE: HEALTH CLOUD COACH WORKFLOW                                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  CARE PLAN = AUTOMATED PATIENT JOURNEY                                       │
│                                                                              │
│  CarePlan (per patient)                                                      │
│  ├── Phase 1: Intake (0-2 days)                                             │
│  │   └── Auto: Welcome message                                              │
│  │                                                                           │
│  ├── Phase 2: Initial Evaluation (days 1-7)                                 │
│  │   └── Auto: "Did you attend your IE?" (Day 2)                            │
│  │   └── Auto: Capture response, update status                              │
│  │   └── If no IE → Alert coach                                             │
│  │                                                                           │
│  ├── Phase 3: Active Treatment (ongoing)                                    │
│  │   └── Auto: Biweekly check-in (visits 1-6)                               │
│  │   └── Auto: "How is PT going?" + response capture                        │
│  │   └── If negative response → Route to coach                              │
│  │   └── If admin issue detected → Route to admin team                      │
│  │                                                                           │
│  ├── Phase 4: Midpoint Review (trigger: 50% of visits used)                 │
│  │   └── Alert: Coach review required                                       │
│  │   └── Auto: Request progress note from clinic                            │
│  │   └── Auto: Generate PT note summary for coach                           │
│  │                                                                           │
│  ├── Phase 5: Outlier Management (trigger: case going long)                 │
│  │   └── Alert: High priority coach review                                  │
│  │   └── Auto: Full case summary generated                                  │
│  │   └── Coach: Clinical intervention                                       │
│  │                                                                           │
│  └── Phase 6: Discharge (trigger: DC note received)                         │
│      └── Auto: Discharge survey to patient                                  │
│      └── Auto: Update case status                                           │
│      └── Auto: Notify stakeholders                                          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  AUTOMATED PATIENT CHECK-INS                                                 │
│                                                                              │
│  Schedule (Coach 2's suggestion):                                            │
│  ├── Initial check-in after IE                                              │
│  ├── Biweekly for first month (3 automated)                                 │
│  └── Manual only when warranted                                             │
│                                                                              │
│  Message Examples:                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │ "Hi [Name], this is your Bard Health coach. How is PT going?        │    │
│  │  Reply: 1=Great  2=OK  3=Having issues"                             │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  Response Routing:                                                           │
│  ├── "1" (Great) → Log response, no action needed                           │
│  ├── "2" (OK) → Log response, continue monitoring                           │
│  ├── "3" (Issues) → Route to coach for follow-up                            │
│  └── Free text → AI classify: Admin issue? Clinical issue? Route accordingly│
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  INTELLIGENT MESSAGE ROUTING                                                 │
│                                                                              │
│  All inbound patient messages analyzed:                                      │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  ADMIN ISSUES (Route to Admin Team)                                  │    │
│  │  - Scheduling: "I can't get an appointment"                          │    │
│  │  - Payment: "When will I get paid?"                                  │    │
│  │  - Transportation: "I need a ride"                                   │    │
│  │  - Authorization: "Do I have more visits?"                           │    │
│  │  - General questions: "What's your address?"                         │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  CLINICAL ISSUES (Route to Coach)                                    │    │
│  │  - Pain concerns: "My pain is getting worse"                         │    │
│  │  - Progress concerns: "I'm not getting better"                       │    │
│  │  - Compliance issues: "I can't do my exercises"                      │    │
│  │  - Red flags: "I fell" / "New symptoms"                              │    │
│  │  - Treatment questions: "Should I use ice or heat?"                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  Implementation: Einstein Classification or keyword rules                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  PT NOTE SUMMARIZATION (AI-Assisted)                                         │
│                                                                              │
│  When PT note received:                                                      │
│  1. AI extracts key data points:                                             │
│     ├── ROM: Shoulder flexion 120° → 145° (+25°)                            │
│     ├── Pain: 6/10 → 4/10 (improving)                                       │
│     ├── Compliance: Attending 2x/week as prescribed                         │
│     ├── Function: Now able to reach overhead                                │
│     ├── Red flags: None                                                     │
│     └── Therapist assessment: Progressing well, continue plan              │
│                                                                              │
│  2. Generate summary card for coach:                                         │
│     ┌─────────────────────────────────────────────────────────────────┐     │
│     │  PT NOTE SUMMARY - John Smith - 12/15/2024                       │     │
│     │  ─────────────────────────────────────────────────────────────── │     │
│     │  ✅ ROM: Improving (+25° shoulder flexion)                       │     │
│     │  ✅ Pain: Improving (6→4)                                        │     │
│     │  ✅ Compliance: Good (2x/week)                                   │     │
│     │  ✅ Function: New milestone (overhead reach)                     │     │
│     │  ⚪ Red flags: None                                              │     │
│     │  ─────────────────────────────────────────────────────────────── │     │
│     │  RECOMMENDATION: No coach action needed                          │     │
│     │  [View Full Note]                                                │     │
│     └─────────────────────────────────────────────────────────────────┘     │
│                                                                              │
│  3. Route based on findings:                                                 │
│     ├── All green → Auto-close review task                                  │
│     ├── Yellow flags → Queue for coach review                               │
│     └── Red flags → High priority coach alert                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  COACH DASHBOARD: EXCEPTIONS ONLY                                            │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  MY CASES NEEDING ATTENTION                          December 2024   │    │
│  │  ─────────────────────────────────────────────────────────────────── │    │
│  │                                                                       │    │
│  │  🔴 RED FLAGS (3)                                    [View All]       │    │
│  │     • Smith, John - Pain increased, non-compliant                    │    │
│  │     • Garcia, Maria - New symptoms reported                          │    │
│  │     • Johnson, Robert - Therapist concerned about progress           │    │
│  │                                                                       │    │
│  │  🟡 MIDPOINT REVIEWS (5)                             [View All]       │    │
│  │     • Williams, Sarah - 6 of 12 visits used                          │    │
│  │     • Brown, Michael - 8 of 15 visits used                           │    │
│  │     • ...                                                             │    │
│  │                                                                       │    │
│  │  🟠 OUTLIERS (2)                                     [View All]       │    │
│  │     • Davis, Lisa - 18 visits, no discharge in sight                 │    │
│  │     • Miller, James - 3 re-auths, still treating                     │    │
│  │                                                                       │    │
│  │  🔵 PATIENT ESCALATIONS (4)                          [View All]       │    │
│  │     • Messages flagged as clinical concerns                          │    │
│  │                                                                       │    │
│  │  ─────────────────────────────────────────────────────────────────── │    │
│  │  ✅ AUTOMATED TODAY: 47 check-ins sent, 38 responses logged          │    │
│  │  ✅ ADMIN ROUTED: 12 messages sent to admin team                     │    │
│  │  ✅ NO ACTION NEEDED: 23 cases progressing normally                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Health Cloud Features to Leverage

### 1. Care Plans

**What It Does:** Defines the patient journey with automated milestones and tasks

| Component | Purpose |
|-----------|---------|
| `CarePlan` | Overall treatment plan for patient |
| `CarePlanTemplate` | Reusable template for PT cases |
| `CareplanActivity` | Individual tasks/milestones |
| `CarePlanActivityGoal` | Measurable outcomes |

**Configuration Needed:**
- Build PT Care Plan template with phases
- Define automated activities (check-ins, reviews)
- Configure triggers for phase transitions

---

### 2. Care Teams

**What It Does:** Assigns roles to patient's care, routes work appropriately

| Role | Responsibility |
|------|----------------|
| Coach (Primary) | Clinical oversight, escalations |
| Admin Support | Scheduling, payment, transport issues |
| Intake Specialist | Initial setup, missing data |
| UM Specialist | Re-auth management |

**Configuration Needed:**
- Define Care Team roles
- Auto-assign based on case attributes
- Route messages/tasks by role

---

### 3. Automated Messaging (Flows + SMS)

**What It Does:** Sends scheduled check-ins, captures responses

| Capability | Implementation |
|------------|----------------|
| Scheduled messages | Flow with scheduled paths |
| Response capture | Inbound SMS handling |
| Response routing | Flow decision based on response |
| Escalation | Create task if response = issue |

**Configuration Needed:**
- Enable Salesforce SMS (or integrate with existing)
- Build check-in message templates
- Build response parsing logic
- Configure escalation flows

---

### 4. Einstein Classification (or Rules-Based)

**What It Does:** Analyzes message content, routes to right team

| Approach | Pros | Cons |
|----------|------|------|
| Einstein | Learns from data, handles nuance | Requires training data |
| Keyword rules | Simple, predictable | May miss variations |
| Hybrid | Best of both | More setup |

**Categories to Classify:**
- Admin: Scheduling, payment, transportation, authorization
- Clinical: Pain, progress, compliance, symptoms
- Neutral: General questions, acknowledgments

---

### 5. PT Note Summarization (Einstein or Integration)

**Options:**

| Approach | Description | Effort |
|----------|-------------|--------|
| **Einstein GPT** | Salesforce native AI summarization | Medium (if available) |
| **External AI** | Send note to external LLM, return summary | Medium |
| **Structured extraction** | Parse SOAP note sections into fields | High |
| **Human-in-loop** | AI suggests, coach confirms | Medium |

**Key Extractions:**
- ROM measurements (current vs. previous)
- Pain scores (current vs. previous)
- Compliance indicators
- Functional milestones
- Red flags
- Therapist assessment

---

### 6. Exception-Based Dashboard

**What It Does:** Shows only cases needing coach attention

| Queue | Trigger |
|-------|---------|
| Red Flags | AI detects concern in note or message |
| Midpoint Reviews | 50% of visits used |
| Outliers | Case exceeds expected duration |
| Patient Escalations | Patient response indicates issue |
| Clinic Escalations | Clinic reports concern |

**Configuration Needed:**
- Define thresholds for each queue
- Build list views and dashboard
- Configure alert rules

---

## Implementation Phases

### Phase 3A: Care Plan Foundation (Weeks 1-4)
**Goal:** Automated patient journey structure

| Task | Effort | Dependencies |
|------|--------|--------------|
| Design Care Plan template for PT | Medium | Business input |
| Configure Care Plan phases | Medium | Template approved |
| Build Care Team role structure | Low | Roles defined |
| Auto-assign Care Plans on referral | Low | Phase 1 complete |

---

### Phase 3B: Automated Check-Ins (Weeks 5-8)
**Goal:** Routine messaging without coach involvement

| Task | Effort | Dependencies |
|------|--------|--------------|
| Enable Salesforce SMS | Medium | Licensing/vendor |
| Build check-in message templates | Low | Content approved |
| Build scheduled check-in Flow | Medium | SMS working |
| Build response capture Flow | Medium | SMS working |
| Configure response routing | Medium | Classification logic |

---

### Phase 3C: Message Intelligence (Weeks 9-12)
**Goal:** Route messages to right team automatically

| Task | Effort | Dependencies |
|------|--------|--------------|
| Define admin vs. clinical categories | Low | Business input |
| Build classification model or rules | High | Training data |
| Configure routing Flows | Medium | Classification ready |
| Create admin team queue | Low | Team identified |
| Test and refine accuracy | Medium | Live messages |

---

### Phase 3D: PT Note Summarization (Weeks 13-18)
**Goal:** Coaches review summaries, not full notes

| Task | Effort | Dependencies |
|------|--------|--------------|
| Evaluate AI options (Einstein, external) | Medium | Licensing |
| Build note ingestion pipeline | Medium | Notes flowing to SF |
| Configure extraction/summarization | High | AI setup |
| Build summary display component | Medium | Extraction working |
| Define routing based on findings | Medium | Categories defined |
| Test with real notes | High | End-to-end ready |

---

### Phase 3E: Coach Dashboard (Weeks 19-22)
**Goal:** Single view of cases needing attention

| Task | Effort | Dependencies |
|------|--------|--------------|
| Define exception queues/criteria | Low | Business input |
| Build dashboard layout | Medium | Data available |
| Configure alerts/notifications | Low | Queues defined |
| Train coaches on new workflow | Medium | System ready |
| Monitor and adjust thresholds | Ongoing | Live usage |

---

## Effort Summary

| Phase | Duration | Effort | Impact |
|-------|----------|--------|--------|
| 3A: Care Plan Foundation | 4 weeks | Medium | High |
| 3B: Automated Check-Ins | 4 weeks | Medium | Very High |
| 3C: Message Intelligence | 4 weeks | High | Very High |
| 3D: PT Note Summarization | 6 weeks | High | Transformational |
| 3E: Coach Dashboard | 4 weeks | Medium | High |
| **Total** | **22 weeks** | **High** | **Transformational** |

---

## Success Metrics

| Metric | Current State | Target |
|--------|---------------|--------|
| Time on PT note review | 3-10+ hrs/day | < 1 hr/day |
| Manual check-ins sent | 100% | < 20% |
| Admin issues handled by coaches | High | < 10% |
| Cases reviewed per day | Limited by time | All exceptions covered |
| Coach time on clinical work | ~30%? | > 80% |
| Patient check-in response rate | Unknown | > 70% |

---

## Open Questions

1. **SMS provider:** What SMS capability exists today? Salesforce native? Third-party?
2. **Note format:** Are PT notes structured (SOAP) or free text? OCR quality?
3. **AI licensing:** Do you have Einstein GPT or would we need external AI?
4. **Admin team:** Does an admin team exist to receive routed issues, or would we need to create one?
5. **Coach buy-in:** Have coaches seen this vision? Are they supportive?
6. **Compliance review:** Does automated messaging require compliance/legal approval?

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Coaches resist change | Involve coaches in design, show time savings |
| Automated messages feel impersonal | Allow coach override, personalization options |
| Classification errors | Start with rules, add AI later; human review of uncertain |
| Note summarization inaccuracy | Human-in-loop: AI suggests, coach confirms |
| Patients prefer human contact | Escalation path always available; coach intervenes on request |

---

*This completes the Phase 3 scope. Combined with Phase 1 (Referral Intake) and Phase 2 (Utilization Management), this represents a comprehensive Health Cloud transformation.*
