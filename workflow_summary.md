# Work Comp PT Referral Workflow — Problem Summary & Meeting Guide

## 1. Background
Your organization manages **Physical Therapy (PT) referrals** for injured workers (IWs) in a workers’ compensation environment.  
You use **Salesforce HealthCloud** as the central system of record.  

All inbound communication — **emails, texts, and voice calls/voicemails** — automatically generates a **task** for a case manager to review.

### Current Situation
- Case managers receive **hundreds of tasks per day**.
- Each task must be manually reviewed:
  - Emails must be read.
  - Text messages must be read.
  - Voicemails must be listened to in full (CloudCall does not currently transcribe).
- Case managers must determine:
  - What the communication is about.
  - Whether it contains required referral information.
  - Which internal team or workflow should receive the task.
- This results in a **severe processing bottleneck** that slows the PT placement process.

### HIPAA Considerations
- Any solution must be **HIPAA compliant**.
- Preference is leaning toward **Salesforce-native AI** or HIPAA-capable integrated systems.

---

## 2. Key Workflow Problems Identified

### A. Manual Review Load
Every message requires human review before a case manager can take action or route it.

### B. Lack of Automated Understanding
The system does not:
- Summarize messages  
- Extract key data  
- Classify message types  
- Auto-route tasks  

### C. Voicemail Bottleneck
Voicemails are particularly time-consuming:
- No transcription  
- Full audio must be reviewed  
- Often unclear routing until fully heard  

### D. Task Routing Ambiguity
Case managers must decide manually who should receive each task, which consumes time and introduces inconsistency.

---

## 3. Potential Technology Solutions (High-Level)

### Native or Salesforce-Affiliated Options
- **Salesforce Service Cloud Voice + Einstein Conversation Intelligence**  
- **Amazon Connect integrated with Salesforce**

### VoIP/CTI Vendors with AI + HIPAA Plans
- **RingCentral for Salesforce (HIPAA plan)**
- **Five9 Intelligent Cloud Contact Center**
- **NICE InContact**

### Specialized Healthcare AI Transcription Vendors
- DeepScribe  
- Suki  
- Augmedix  

*Primarily clinical documentation tools, not voicemail-first.*

---

## 4. Meeting Purpose
To gather **clear, factual, operational details** from cross-functional stakeholders so that a concrete automation strategy can be developed.  
No assumptions should be made — only verified information will inform the next design iteration.

---

# 5. Meeting Questions (Facilitator Guide)

## Section A — Current Operations
1. What is the **average daily volume** of:
   - Emails?
   - Text messages?
   - Voicemails?
2. What portion of communications result in **actionable work** vs **FYI** vs **noise**?
3. What types of communications consume the **most review time**?

## Section B — Required Information
4. What **specific data elements** must be present before a PT referral can progress?  
5. Of these elements, which are:
   - Usually included?
   - Sometimes included?
   - Rarely included?
6. Which missing data items cause the **most follow-up work**?

## Section C — Routing & Workflow
7. What communication categories exist now?  
8. How is **routing** currently determined?  
9. How often does **misrouting** occur?

## Section D — Pain Points
10. What tasks feel the **most repetitive or redundant**?
11. Which tasks could be **automated** (even partially)?
12. Which tasks must **always** remain manual?

## Section E — Technology, Compliance & Constraints
13. Is storing **call recordings/transcripts** in Salesforce HIPAA-compliant under current policies?
14. Do vendors need to sign a **BAA**?
15. Must we keep CloudCall, or can we replace it?
16. What Salesforce automation tools are currently in use?

## Section F — Metrics & Outcomes
17. What KPIs define success today?
18. What improvements justify automation investment?
19. How should a pilot be evaluated?

## Section G — Future Vision
20. What should the ideal triage process look like?
21. What should be:
    - Fully automated?
    - Human-assisted?
    - Human-only?
22. What long-term improvements would provide the **most value**?

---

## 6. Expected Meeting Output

### A. Validated lists:
- Required referral fields  
- Communication categories  
- Routing rules  
- Compliance requirements  

### B. Clear understanding of:
- Automation candidates  
- Required data extraction  
- Workflow bottlenecks  

### C. Foundation for:
- Workflow design  
- Vendor evaluations  
- Implementation roadmap  
