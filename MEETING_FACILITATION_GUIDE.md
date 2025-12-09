# Operational Automation Project — Meeting Facilitation Guide

**Meeting Purpose:** Review findings from stakeholder pre-reads, understand broken workflows, and prioritize automation opportunities
**Attendees:** Leadership, Coaches, Intake/Scheduling Team
**Status:** Ready for Meeting

---

## Meeting Structure

| Session | Time | Focus |
|---------|------|-------|
| **MORNING** | AM | Questionnaire Review — Coaches & Intake findings |
| **AFTERNOON** | PM | Broken Process Deep-Dive — Task Triage Workflow |

---

# MORNING SESSION: Questionnaire Findings

## Agenda — Morning

1. [Coach Workflow Findings](#1-coach-workflow-findings)
2. [Intake Team Findings](#2-intake-team-findings)
3. [Salesforce Email Issue — Critical Bottleneck](#3-salesforce-email-issue--critical-bottleneck)
4. [Morning Wrap-Up & Prioritization](#4-morning-wrap-up--prioritization)

---

## 1. Coach Workflow Findings

*Reference: [COACH_QUESTIONNAIRE_SUMMARY.md](./COACH_QUESTIONNAIRE_SUMMARY.md)*

### Key Statistics (5 Coaches Responded)
| Metric | Finding |
|--------|---------|
| PT Notes Read | **40+ per day** (not per week as assumed) |
| Time per Note | 5-15 minutes |
| Daily Note Review Time | **3-10+ hours** |
| Daily Messaging Time | 30-90+ minutes |

### Unanimous Coach Feedback
> **"Most patient messages do not require clinical expertise."**

Admin issues dominate coach messaging:
- Scheduling
- Payment issues
- Transportation needs
- Authorization/new script questions

### Coach-Suggested Solution
**Automated Check-In System:**
- Initial automated check-in after Initial Eval
- Biweekly automated check-ins for first month (3 total)
- Manual intervention only when warranted by patient response

### Discussion Questions — Coaches
1. How many early-stage cases (pre-midpoint) could be handled with automated check-ins only?
2. What specific triggers should escalate a case from automated to coach intervention?
3. What admin issues should route to a non-clinical team instead of coaches?
4. What would you do with the time saved if messaging was automated?

---

## 2. Intake Team Findings

*Source: questionnaire_intake_1.docx*

### Key Statistics (1 Respondent)

| Metric | Finding |
|--------|---------|
| Referrals per Day | **20+** |
| Time per Referral | **15-30 minutes** |
| Data Correction Rate | 5-15% of cases |
| Document Sources | DocuPipe, Email, Portals, Eligibility feeds, Webforms, MSQ, API |

### DocuPipe Assessment

**What Works Well:**
- Expiration dates
- Surgery dates
- Highlights where information came from

**What Struggles:**
- Therapy type (when multiple mentioned)
- Dates extracted incorrectly (e.g., date sent recorded as script date)
- Multiple body parts/diagnoses
- Picks up service types from email instead of document
- Some processing delays

> **Note:** A spreadsheet documenting DocuPipe issues exists. A "missing critical report with live examples" was mentioned.

### Missing Data Collection Process
Current methods for collecting missing fields:
- Phone calls
- Emails
- Text messages
- Contacts: Stakeholders, MDs, patients, and clinics

### Automated Patient Texting — Intake Perspective
If texting patients to collect missing data, intake would ask:
- Any and all missing referral information
- Availability/time preference for scheduling
- Requested clinic or current PT clinic
- If already treating: how long, in/out of network status
- Next steps toward Initial Eval

### Discussion Questions — Intake
1. **The 20+ referrals/day at 15-30 min each = 5-10+ hours/day.** Is this accurate across the team?
2. What are the top 3 fields that DocuPipe gets wrong most often?
3. Can we see the spreadsheet documenting DocuPipe issues?
4. What does the "missing critical report with live examples" refer to?
5. How much time is spent chasing missing information via calls/emails/texts?
6. What percentage of patients respond to texts vs. requiring phone calls?

---

## 3. Salesforce Email Issue — Critical Bottleneck

*Reference: [salesforce_email_issue_summary.md](./salesforce_email_issue_summary.md)*

### Problem Statement
> **When a case manager replies to a tokenized email inside Salesforce, the reply is logged on the Case but does not reach the external recipient. New emails send successfully, but replies do not. This forces case managers to manually copy/paste content into new emails, creating inefficiency and risk.**

### Current Workaround
Case managers must:
1. Open the inbound email logged on the Case
2. **Copy/paste** the content into a **NEW** email
3. Send the new email from the Case

### Impact
- Manual effort on every reply
- Higher risk of missing details
- Workflow confusion
- Time waste across the organization

### Clarifying Questions

#### Scope & Impact
1. How many emails per day/week are affected?
2. Which roles are most impacted — Coaches? Intake? Both?
3. How long has this issue existed?

#### Technical
4. Where do replies from non-adjuster stakeholders actually go?
5. Do Salesforce Email Logs show replies as delivered or blocked?
6. Are there automation rules intercepting replies?

#### Resolution
7. Is this documented with Salesforce Support?
8. Who owns the Salesforce configuration?
9. What is the urgency level and acceptable timeline?

---

## 4. Morning Wrap-Up & Prioritization

### Cross-Team Patterns Identified

| Theme | Coaches | Intake | Common? |
|-------|---------|--------|---------|
| High volume of manual work | 40+ notes/day | 20+ referrals/day | ✓ |
| Time per task adds up | 5-15 min/note | 15-30 min/referral | ✓ |
| Non-clinical work burden | Admin messaging | Chasing missing data | ✓ |
| Automation desire | Check-ins | Patient texting | ✓ |
| System issues | — | DocuPipe errors | — |
| Salesforce email issue | Affected | Affected | ✓ |

### Prioritization Framework

| Criteria | Weight | Description |
|----------|--------|-------------|
| Time Saved | High | Hours saved per week across team |
| Error Reduction | High | Fewer mistakes, less rework |
| Clinical Focus | High | Allows clinicians to do clinical work |
| Implementation Effort | Medium | Complexity and resources needed |
| Quick Win | Medium | Can be done in < 2 weeks |

### Candidate Initiatives

| Initiative | Time Impact | Effort | Priority |
|------------|-------------|--------|----------|
| Fix Salesforce email reply issue | High | Unknown | **TBD** |
| Automated patient check-ins (Coaches) | High | Medium | **TBD** |
| Automated patient texting (Intake) | High | Medium | **TBD** |
| PT Note summarization tool | High | High | **TBD** |
| DocuPipe accuracy improvements | Medium | Unknown | **TBD** |
| Admin issue routing from coaches | Medium | Medium | **TBD** |

### Morning Discussion Questions
1. Which issue causes the most daily frustration?
2. Which fix would have the biggest immediate impact?
3. What resources (people, budget, time) are available?
4. Are there dependencies between initiatives?

---

# AFTERNOON SESSION: Broken Process Deep-Dive

## The Problem We're Solving

*Reference: [workflow_summary.md](./workflow_summary.md)*

### Current State
- Case managers receive **hundreds of tasks per day**
- Every inbound communication (email, text, voicemail) creates a task
- Each task must be **manually reviewed** before routing or action
- Voicemails must be **listened to in full** (no transcription)
- This creates a **severe processing bottleneck** slowing PT placement

### Why This Matters
**Goal:** Get injured workers into PT faster
**Blocker:** Manual triage of hundreds of messages per day
**Result:** Delays, frustration, potential compliance issues

---

## Afternoon Agenda — Learning-Focused Discovery

The goal of this session is **learning**, not solving. We need to deeply understand the problem before designing solutions.

### Section A: Understanding the Volume

**Purpose:** Quantify the actual workload

1. What is the **average daily volume** of:
   - Emails?
   - Text messages?
   - Voicemails?

2. How does volume vary by day of week? Beginning/end of month?

3. Who receives these tasks?
   - One shared queue?
   - Individual queues?
   - Role-based assignment?

4. What is the **current backlog** of unprocessed tasks?
   - Hours behind? Days behind?

5. How many FTEs are dedicated to task triage today?

---

### Section B: Understanding the Content

**Purpose:** Learn what's actually in these messages

6. What **percentage** of communications are:
   - Actionable work requiring immediate response?
   - FYI/status updates (no action needed)?
   - Noise/spam/irrelevant?

7. Can you **show us examples** of each type?
   - Walk through 3-5 real emails
   - Walk through 3-5 real texts
   - Listen to 2-3 voicemails together

8. What are the **most common message types**?
   - New referral information?
   - Missing data responses?
   - Status inquiries?
   - Scheduling requests?
   - Authorization questions?
   - Other?

9. How do you **currently categorize** messages (if at all)?

---

### Section C: Understanding the Required Data

**Purpose:** Know what we're looking for in messages

10. What **specific data elements** must be present before a PT referral can progress?
    - List every required field

11. Of these elements, which are:
    - Usually included in initial referral?
    - Sometimes included?
    - Rarely included (always requires follow-up)?

12. Which missing data items cause the **most follow-up work**?

13. How do you know when a referral is **"complete enough"** to proceed?

---

### Section D: Understanding the Routing

**Purpose:** Map where things go and why

14. What are all the possible **destinations** for a task?
    - List every team/role/queue

15. How is **routing currently determined**?
    - Written rules?
    - Tribal knowledge?
    - Individual judgment?

16. How often does **misrouting** occur?
    - What happens when something goes to the wrong place?
    - How long until it's corrected?

17. Are there tasks that **bounce between teams**? Why?

18. **Draw the current routing decision tree** together
    - "If X, then route to Y"
    - Capture every branch

---

### Section E: Understanding the Pain

**Purpose:** Feel the problem from the workers' perspective

19. What tasks feel the **most repetitive or redundant**?

20. What makes you think "I can't believe I have to do this manually"?

21. What tasks could be **automated** (even partially)?

22. What tasks must **always** remain manual? Why?

23. What **workarounds** have you created to cope?
    - Personal systems?
    - Unofficial processes?
    - Tools outside Salesforce?

24. What would you do with **2 extra hours per day** if triage was automated?

---

### Section F: Understanding Voicemails Specifically

**Purpose:** Deep-dive on the worst bottleneck

25. What percentage of voicemails contain **new information** vs. duplicating an email/text?

26. How long is the **average voicemail**?

27. What information do callers typically leave?
    - Just "call me back"?
    - Detailed referral info?
    - Questions?

28. How often do you have to **call back** just to understand what they wanted?

29. If voicemails were **transcribed automatically**, would that solve the problem?
    - Or is the issue deeper (still need to read/categorize/route)?

30. Are there callers who **should** be routed differently?
    - Adjusters vs. patients vs. clinics vs. MDs?

---

### Section G: Understanding Constraints

**Purpose:** Know the boundaries before designing solutions

31. What **HIPAA considerations** apply to:
    - Storing call recordings?
    - Storing transcripts?
    - Using AI to process messages?

32. Do vendors need to sign a **BAA** (Business Associate Agreement)?

33. Must we keep **CloudCall**, or can we replace it?

34. What **Salesforce automation tools** are currently in use?
    - Flows?
    - Process Builder?
    - Einstein?

35. What **budget** exists for this problem?
    - Approved?
    - Needs justification?

36. Who has **authority** to approve changes to:
    - Salesforce configuration?
    - Phone system?
    - Workflow processes?

---

### Section H: Defining Success

**Purpose:** Know what "fixed" looks like

37. What **KPIs** define success today?
    - Task completion time?
    - Referral-to-placement time?
    - Other?

38. What **improvements would justify** automation investment?
    - Time saved?
    - Error reduction?
    - Faster placement?

39. How should a **pilot** be structured and evaluated?

40. What does the **ideal triage process** look like?
    - Describe your dream state

41. In the ideal state, what should be:
    - Fully automated (no human touch)?
    - Human-assisted (AI suggests, human confirms)?
    - Human-only (always manual)?

---

## Afternoon Session Output

By the end of this session, we should have:

### A. Validated Lists
- [ ] Required referral fields (complete list)
- [ ] Communication categories/types
- [ ] Routing rules (documented decision tree)
- [ ] Compliance requirements

### B. Quantified Understanding
- [ ] Daily volumes by channel
- [ ] Time spent per task type
- [ ] Error/misrouting rates
- [ ] Actionable vs. noise percentages

### C. Pain Points Ranked
- [ ] Top 5 most painful manual tasks
- [ ] Tasks that can be automated
- [ ] Tasks that must stay manual

### D. Foundation for Design
- [ ] Clear problem statement
- [ ] Success criteria defined
- [ ] Constraints documented
- [ ] Stakeholder buy-in on priorities

---

# Action Items

*To be filled in during/after meeting*

| Action Item | Owner | Due Date | Status |
|-------------|-------|----------|--------|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

---

## Appendix: Source Documents

- `COACH_QUESTIONNAIRE_SUMMARY.md` — Coach questionnaire analysis (5 respondents)
- `questionnaire_intake_1.docx` — Intake team response (1 respondent)
- `salesforce_email_issue_summary.md` — Salesforce email problem detail
- `workflow_summary.md` — Broken process background and initial questions
- `questionnaire_coach_1-5.docx` — Raw coach responses
- `Pre_Read_Stakeholder_Questionnaire.docx` — Original questionnaire

---

*Last Updated: December 2024*
