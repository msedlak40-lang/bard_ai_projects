# Adjuster Communication & Cross-Department Case Management
## Current State Analysis & Health Cloud Recommendations

**Version:** 1.0 — Draft for Discussion
**Date:** December 2024
**Status:** Discovery — Needs Clarification

---

## Executive Summary

Adjuster communication is currently fragmented across departments, creating a task explosion that overwhelms case owners and makes it difficult to track communication history. This document maps the current state, identifies pain points, and proposes a Health Cloud-based solution.

---

## Current State — What I Understand

### The Task Explosion Problem

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ CURRENT STATE: ADJUSTER COMMUNICATION CHAOS                                  │
└──────────────────────────────────────────────────────────────────────────────┘

                         ┌─────────────────┐
                         │    ADJUSTER     │
                         │  sends email    │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  SHARED INBOX   │
                         │  (Email-to-Case)│
                         └────────┬────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
           ┌───────────────┐           ┌───────────────┐
           │  TASK CREATED │           │ TICKET CREATED│
           │  (for action) │           │ (for tracking)│
           └───────┬───────┘           └───────────────┘
                   │
                   ▼
           ┌───────────────┐
           │  CASE OWNER   │
           │  receives     │
           │  BOTH         │
           └───────┬───────┘
                   │
                   │ Case owner realizes this needs
                   │ to go to another department...
                   │
                   ▼
    ┌──────────────────────────────────────────────┐
    │  CANNOT FORWARD TASK IN SALESFORCE           │
    │                                              │
    │  Workaround:                                 │
    │  1. Copy email content                       │
    │  2. Exit Salesforce                          │
    │  3. Open Outlook                             │
    │  4. Paste and send to other department       │
    │  5. Other department receives...             │
    └──────────────────────────────────────────────┘
                   │
                   ▼
    ┌──────────────────────────────────────────────┐
    │  NEW EMAIL ARRIVES AT OTHER DEPARTMENT       │
    │                                              │
    │  Email-to-Case triggers AGAIN:               │
    │  - Another TASK created                      │
    │  - Another TICKET created                    │
    │  - Now there are 4 records for 1 email       │
    └──────────────────────────────────────────────┘
                   │
                   ▼
    ┌──────────────────────────────────────────────┐
    │  RESULT: TASK EXPLOSION                      │
    │                                              │
    │  Original adjuster email = 2 records         │
    │  Internal forward = 2 more records           │
    │  Reply to adjuster = 2 more records          │
    │  Adjuster replies back = 2 more records      │
    │                                              │
    │  ONE CONVERSATION = 8+ TASKS/TICKETS         │
    └──────────────────────────────────────────────┘
```

### Additional Problems Identified

| Problem | Impact |
|---------|--------|
| **Token recycling** | Adjuster replies to old email, lands in wrong case or with departed employee |
| **No visibility across departments** | Dept A doesn't know Dept B already responded |
| **Duplicate outreach** | Multiple people contact adjuster about same issue |
| **Lost context** | Outlook forwards lose case context |
| **Audit trail gaps** | Communication in Outlook not logged to case |
| **Case owner overload** | Receives tasks for things they can't action |

---

## Questions I Need Answered

Before I can design the solution, I need to understand:

### 1. Departments & Roles

**Q1.** Which departments communicate with adjusters? (Check all that apply)
- [ ] Intake/Scheduling
- [ ] Coaches
- [ ] Utilization Management / Re-Auth
- [ ] Billing
- [ ] Client Services
- [ ] Other: _______________

**Q2.** Is there a "primary" department that owns the adjuster relationship, or is it shared?

**Q3.** Who is the "Case Owner" in Salesforce today?
- [ ] Intake person who created the case
- [ ] Assigned coach
- [ ] Rotates based on lifecycle stage
- [ ] Other: _______________

---

### 2. Communication Types

**Q4.** What types of communications come FROM adjusters? (Check all that apply)
- [ ] New referrals
- [ ] Additional referral information
- [ ] Authorization approvals/denials
- [ ] Re-auth decisions
- [ ] Status inquiries ("where's my case?")
- [ ] Billing questions
- [ ] Complaints/escalations
- [ ] General questions
- [ ] Other: _______________

**Q5.** What types of communications go TO adjusters? (Check all that apply)
- [ ] Referral acknowledgment
- [ ] Missing information requests
- [ ] Status updates
- [ ] Re-auth requests
- [ ] Progress reports
- [ ] Billing/claims information
- [ ] Discharge notifications
- [ ] Other: _______________

---

### 3. Current Routing Logic

**Q6.** When an adjuster email comes in, how is it currently routed to the right person?
- [ ] All go to one inbox, manually triaged
- [ ] Email subject line determines routing
- [ ] Case owner gets everything
- [ ] Other: _______________

**Q7.** What happens when something is sent to the wrong person/department?

**Q8.** Is there a documented routing matrix (if adjuster asks X, route to Y)?

---

### 4. The Task/Ticket System

**Q9.** Why was the dual Task + Ticket system created?
> You mentioned "lack of trust people were doing their jobs" — can you elaborate?

**Q10.** Who reviews the tickets? Is this data used for anything?

**Q11.** Are Tasks and Tickets the same object with different record types, or separate custom objects?

**Q12.** What happens to a Task when it's "completed"? Does anyone verify the work?

---

### 5. Adjuster Experience

**Q13.** Do adjusters have a portal or self-service option, or is everything via email?

**Q14.** Do adjusters complain about:
- [ ] Slow response times
- [ ] Having to repeat information
- [ ] Not knowing case status
- [ ] Getting contacted by multiple people
- [ ] Other: _______________

**Q15.** Are there SLAs for responding to adjusters? If so, are they being met?

---

### 6. The Salesforce Email Reply Issue

**Q16.** The email reply issue (replies don't reach external recipients) — does this affect adjuster communication specifically?

**Q17.** How often do case managers need to reply to adjusters vs. send new emails?

---

## Proposed Future State (Preliminary)

Based on what I understand, here's a directional view of how Health Cloud could fix this:

### Core Concept: Single Case Record, Role-Based Visibility

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ FUTURE STATE: UNIFIED ADJUSTER COMMUNICATION                                 │
└──────────────────────────────────────────────────────────────────────────────┘

                         ┌─────────────────┐
                         │    ADJUSTER     │
                         │  sends email    │
                         └────────┬────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │  INTELLIGENT EMAIL ROUTING   │
                    │                             │
                    │  1. Identify case (token)   │
                    │  2. Classify message type   │
                    │  3. Route to right QUEUE    │
                    │     (not person)            │
                    └─────────────┬───────────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
        ▼                         ▼                         ▼
┌───────────────┐       ┌───────────────┐       ┌───────────────┐
│ INTAKE QUEUE  │       │  COACH QUEUE  │       │ BILLING QUEUE │
│               │       │               │       │               │
│ • New referral│       │ • Clinical Q  │       │ • Claims Q    │
│ • Missing info│       │ • Progress Q  │       │ • Payment Q   │
│ • Auth docs   │       │ • Re-auth dec │       │               │
└───────┬───────┘       └───────┬───────┘       └───────┬───────┘
        │                       │                       │
        └───────────────────────┴───────────────────────┘
                                │
                                ▼
                ┌───────────────────────────────┐
                │  SINGLE CASE RECORD           │
                │                               │
                │  All communication logged     │
                │  All departments can see      │
                │  Full history preserved       │
                │  No duplicate tasks           │
                │                               │
                │  Care Team:                   │
                │  ├── Intake: Jane             │
                │  ├── Coach: Mike              │
                │  ├── Billing: Sarah           │
                │  └── Adjuster: John (Acme)    │
                └───────────────────────────────┘
```

### Key Changes

| Today | Future |
|-------|--------|
| Task per communication | Activity/Email on single case |
| Task + Ticket duplication | Single record, activity history |
| Can't forward in SF | Transfer queue ownership in SF |
| Outlook workaround | Everything stays in Salesforce |
| Case owner gets all | Queue-based, role-based routing |
| Token goes to person | Token goes to case, routed by type |
| No cross-dept visibility | Full case timeline visible to Care Team |

### Health Cloud Features to Leverage

| Feature | Purpose |
|---------|---------|
| **Case (or CareRequest)** | Single record per patient/referral |
| **Queues** | Department-based work distribution |
| **Omni-Channel** | Skills-based routing within queues |
| **Care Teams** | Role-based access and assignment |
| **Email-to-Case (Enhanced)** | Smarter routing, no duplicate tasks |
| **Activity Timeline** | All emails, calls, tasks in one view |
| **Quick Actions** | Transfer to another queue without Outlook |
| **Knowledge Base** | Standard responses for common questions |
| **Macros** | One-click actions for routine responses |

---

## What I Need From You

To design the detailed solution, please answer:

1. **Questions Q1-Q17 above** (or as many as you can)
2. **Example scenarios:**
   - Walk me through a typical adjuster email and what happens today
   - Walk me through an internal handoff that required Outlook
   - Show me an example of a "token went to wrong case" situation
3. **Volume data:**
   - How many adjuster emails per day/week?
   - How many require cross-department coordination?
4. **Current Salesforce objects:**
   - What object is the "Case" today? Standard Case? Custom object?
   - What are Task and Ticket objects?

---

## Next Steps

1. [ ] Answer clarifying questions
2. [ ] Review proposed future state concept
3. [ ] Map detailed routing rules (if X, route to Y)
4. [ ] Design queue structure
5. [ ] Document Care Team roles
6. [ ] Define transfer/handoff process
7. [ ] Address Salesforce email reply issue as prerequisite

---

*This document will be expanded into a full solution design once questions are answered.*
