# Operational Automation Project — Meeting Facilitation Guide

**Meeting Purpose:** Review findings from stakeholder pre-reads and prioritize automation opportunities
**Attendees:** Leadership, Coaches, Intake/Scheduling Team
**Status:** Draft — Awaiting Intake Team responses

---

## Agenda Overview

1. [Coach Workflow Findings](#1-coach-workflow-findings)
2. [Salesforce Email Issue — Critical Bottleneck](#2-salesforce-email-issue--critical-bottleneck)
3. [Intake Team Findings](#3-intake-team-findings) *(pending)*
4. [Prioritization Discussion](#4-prioritization-discussion)
5. [Next Steps & Action Items](#5-next-steps--action-items)

---

## 1. Coach Workflow Findings

*Reference: [COACH_QUESTIONNAIRE_SUMMARY.md](./COACH_QUESTIONNAIRE_SUMMARY.md)*

### Key Statistics
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

---

## 2. Salesforce Email Issue — Critical Bottleneck

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

### Clarifying Questions for the Meeting

#### Understanding the Scope
1. **How many emails per day/week are affected by this issue?**
   - Per case manager?
   - Organization-wide?

2. **Which roles are most impacted?**
   - Coaches?
   - Intake team?
   - Other case managers?

3. **How long has this issue existed?**
   - Was there a point when replies worked correctly?
   - Did it start after a Salesforce update or configuration change?

#### Technical Verification Needed
4. **Where do replies from non-adjuster stakeholders actually go?**
   - Do they disappear entirely?
   - Do they land in the shared inbox but not attach to the Case?
   - Do they bounce?

5. **Do Salesforce Email Logs show the reply emails as successfully delivered or blocked?**
   - Has anyone checked the email delivery logs in Salesforce?

6. **Are there automation rules, flows, or processes that intercept or reroute replies?**
   - Any Process Builder or Flow automations on Cases?
   - Any email routing rules?

7. **What are the header differences between "new outbound email" vs. "reply"?**
   - Is the token being handled differently?

#### Business Impact Assessment
8. **What is the estimated time cost per case manager per day due to this workaround?**
   - 5 minutes? 30 minutes? More?

9. **Have any emails been lost or missed due to this issue?**
   - Any stakeholder complaints?
   - Any delayed case actions?

10. **Is this issue documented with Salesforce Support?**
    - Has a case been opened?
    - Any response from Salesforce?

#### Decision Points
11. **What is the urgency level for fixing this?**
    - Critical (blocking daily work)?
    - High (significant inefficiency)?
    - Medium (annoying but manageable)?

12. **Who owns the Salesforce configuration and can investigate?**
    - Internal admin?
    - External consultant?
    - Salesforce support?

13. **What is the acceptable timeline for resolution?**
    - Immediate workaround needed?
    - Can wait for proper fix?

---

## 3. Intake Team Findings

**⏳ PENDING — Awaiting intake questionnaire responses**

*This section will be populated with:*
- Referral processing volume and time data
- DocuPipe effectiveness assessment
- Data entry error rates
- Missing field collection workflows
- Automation opportunities identified by intake team

### Placeholder Questions for Intake Discussion
1. What is your current referral volume per day?
2. What percentage of referrals require manual data correction?
3. What fields does DocuPipe struggle with most?
4. Would automated patient texting for missing data be helpful?

---

## 4. Prioritization Discussion

### Framework for Prioritization

| Criteria | Weight | Description |
|----------|--------|-------------|
| Time Saved | High | Hours saved per week across team |
| Error Reduction | High | Fewer mistakes, less rework |
| Clinical Focus | High | Allows clinicians to do clinical work |
| Implementation Effort | Medium | Complexity and resources needed |
| Quick Win | Medium | Can be done in < 2 weeks |

### Candidate Initiatives (Draft)

| Initiative | Time Impact | Effort | Priority |
|------------|-------------|--------|----------|
| Fix Salesforce email reply issue | High | Unknown | **TBD** |
| Automated patient check-ins | High | Medium | **TBD** |
| PT Note summarization tool | High | High | **TBD** |
| Admin issue routing from coaches | Medium | Medium | **TBD** |
| *Intake initiatives TBD* | — | — | — |

### Discussion Questions
1. Which issue causes the most daily frustration?
2. Which fix would have the biggest immediate impact?
3. What resources (people, budget, time) are available?
4. Are there dependencies between initiatives?

---

## 5. Next Steps & Action Items

*To be filled in during/after meeting*

| Action Item | Owner | Due Date | Status |
|-------------|-------|----------|--------|
| | | | |
| | | | |
| | | | |

---

## Appendix: Source Documents

- `COACH_QUESTIONNAIRE_SUMMARY.md` — Coach questionnaire analysis
- `salesforce_email_issue_summary.md` — Salesforce email problem detail
- `questionnaire_coach_1-5.docx` — Raw coach responses
- `Pre_Read_Stakeholder_Questionnaire.docx` — Original questionnaire
- *Intake responses — pending*

---

*Last Updated: December 2024*
