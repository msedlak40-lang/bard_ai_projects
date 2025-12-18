# Health Cloud Capabilities — Engineering Review Request

**Purpose:** Please review this list of Health Cloud features and indicate:
1. Are we aware of this feature?
2. Are we currently using it?
3. Do we have access with our current license?

---

## Patient & Care Management

- [ ] **Patient Data Model** — Unified patient record (Person Account or Individual)
- [ ] **Care Plans** — Structured treatment journey with phases, milestones, automated tasks
- [ ] **Care Plan Templates** — Reusable templates for standard care pathways (e.g., PT referral)
- [ ] **Care Teams** — Role-based assignment (Coach, Intake, Billing) with visibility controls
- [ ] **Timeline View** — Visual patient journey across all touchpoints

---

## Utilization Management

- [ ] **CareRequest Object** — Prior authorization, concurrent review, re-authorization tracking
- [ ] **CareRequestItem** — Line items (authorized visits, services)
- [ ] **Utilization Alerts** — Triggers when approaching visit limits
- [ ] **Member Plan Integration** — Links patient to coverage/benefits

---

## Referral Management

- [ ] **Referral Tracking** — Lifecycle from receipt → placement
- [ ] **Required Field Validation** — Enforce completeness before progression
- [ ] **Referral Source Analytics** — Track which sources send incomplete referrals

---

## Provider Network Management

- [ ] **Provider Data Model** — Manage PT clinic network
- [ ] **Provider Search/Match** — Find providers by location, specialty, network status
- [ ] **Provider Portal** — Self-service for clinics (Experience Cloud)

---

## Document & Data Processing

- [ ] **Intelligent Document Automation (IDA)** — OCR + AI extraction from documents
- [ ] **Document Classification** — Auto-identify document types
- [ ] **Field Extraction with Confidence Scoring** — Flag low-confidence for human review

---

## Communication & Engagement

- [ ] **Omni-Channel Routing** — Skills-based, queue-based work distribution
- [ ] **Email-to-Case (Enhanced)** — Smarter routing, classification
- [ ] **SMS Messaging** — Native or integrated texting capability
- [ ] **Two-Way Messaging** — Capture patient responses, route appropriately
- [ ] **Automated Outreach Flows** — Scheduled check-ins, reminders

---

## AI & Automation

- [ ] **Einstein Classification** — Auto-categorize messages (admin vs. clinical)
- [ ] **Einstein GPT / AI Summarization** — Summarize clinical notes
- [ ] **Einstein Prediction Builder** — Risk scoring, outcome prediction
- [ ] **Flow Builder** — Automated workflows, triggers, escalations
- [ ] **Platform Events** — Real-time event-driven automation

---

## Integration & Interoperability

- [ ] **Health Cloud APIs** — REST/SOAP for external system integration
- [ ] **HL7 FHIR Support** — Healthcare data standard
- [ ] **MuleSoft Health Cloud Accelerator** — Pre-built healthcare integrations
- [ ] **Platform Events** — Real-time sync triggers

---

## Portals & Self-Service

- [ ] **Experience Cloud (Patient Portal)** — Patient self-service
- [ ] **Experience Cloud (Provider Portal)** — Clinic self-service
- [ ] **Experience Cloud (Payer/Adjuster Portal)** — Adjuster status visibility

---

## Analytics & Dashboards

- [ ] **Health Cloud Dashboards** — Pre-built healthcare analytics
- [ ] **Utilization Reports** — Auth vs. used, re-auth pipeline
- [ ] **Care Gap Analytics** — Identify patients needing intervention
- [ ] **SLA Monitoring** — Response time, turnaround tracking

---

## Questions for Engineering

1. **What Health Cloud edition/license do we have?**
   - Health Cloud Enterprise?
   - Health Cloud Unlimited?
   - Other?

2. **Which features above are:**
   - Already enabled and in use?
   - Enabled but not used?
   - Not enabled but available with our license?
   - Would require additional licensing?

3. **Do we have access to:**
   - Einstein AI features?
   - Intelligent Document Automation?
   - Experience Cloud (for portals)?
   - MuleSoft (for integrations)?

4. **Current object usage:**
   - Are we using standard Health Cloud objects (CareRequest, CarePlan, CareTeam)?
   - Or mostly custom objects?

---

**Please respond with your assessment. This will help us determine how to leverage Health Cloud for our workflow automation initiatives.**
