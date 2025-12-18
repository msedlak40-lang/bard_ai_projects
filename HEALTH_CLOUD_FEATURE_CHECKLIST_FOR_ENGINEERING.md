# Health Cloud Capabilities — Engineering Review Request

**Our Licensing:** Salesforce Unlimited Edition with Health Cloud, Service Cloud, and Sales Cloud

**Purpose:** Based on our licensing, most core Health Cloud features should be available. Please verify:
1. Which features are currently enabled and in use?
2. Which features are available but not yet enabled?
3. Which features require additional licensing we don't have?

---

## ✅ SHOULD BE INCLUDED — Please Confirm Availability & Usage

These features are typically included with Health Cloud Unlimited + Service Cloud:

### Patient & Care Management

| Feature | Description | Enabled? | In Use? |
|---------|-------------|----------|---------|
| Patient Data Model | Unified patient record (Person Account or Individual) | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Care Plans | Structured treatment journey with phases, milestones, automated tasks | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Care Plan Templates | Reusable templates for standard care pathways | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Care Teams | Role-based assignment (Coach, Intake, Billing) with visibility controls | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Timeline View | Visual patient journey across all touchpoints | ☐ Yes ☐ No | ☐ Yes ☐ No |

### Utilization Management

| Feature | Description | Enabled? | In Use? |
|---------|-------------|----------|---------|
| CareRequest Object | Prior authorization, concurrent review, re-authorization tracking | ☐ Yes ☐ No | ☐ Yes ☐ No |
| CareRequestItem | Line items (authorized visits, services) | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Utilization Alerts | Triggers when approaching visit limits | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Member Plan Integration | Links patient to coverage/benefits | ☐ Yes ☐ No | ☐ Yes ☐ No |

### Referral Management

| Feature | Description | Enabled? | In Use? |
|---------|-------------|----------|---------|
| Referral Tracking | Lifecycle from receipt → placement | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Required Field Validation | Enforce completeness before progression | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Referral Source Analytics | Track which sources send incomplete referrals | ☐ Yes ☐ No | ☐ Yes ☐ No |

### Provider Network Management

| Feature | Description | Enabled? | In Use? |
|---------|-------------|----------|---------|
| Provider Data Model | Manage PT clinic network | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Provider Search/Match | Find providers by location, specialty, network status | ☐ Yes ☐ No | ☐ Yes ☐ No |

### Communication & Routing (Service Cloud)

| Feature | Description | Enabled? | In Use? |
|---------|-------------|----------|---------|
| Omni-Channel Routing | Skills-based, queue-based work distribution | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Email-to-Case | Email integration with cases | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Queues | Department-based work distribution | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Case Management | Standard case tracking and routing | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Knowledge Base | Standard responses, articles | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Macros | One-click actions for routine tasks | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Service Console | Agent workspace | ☐ Yes ☐ No | ☐ Yes ☐ No |

### Automation

| Feature | Description | Enabled? | In Use? |
|---------|-------------|----------|---------|
| Flow Builder | Automated workflows, triggers, escalations | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Platform Events | Real-time event-driven automation | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Scheduled Flows | Time-based automation | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Approval Processes | Multi-step approvals | ☐ Yes ☐ No | ☐ Yes ☐ No |

### Integration

| Feature | Description | Enabled? | In Use? |
|---------|-------------|----------|---------|
| REST/SOAP APIs | External system integration | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Platform Events | Real-time sync triggers | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Outbound Messages | Event-based external notifications | ☐ Yes ☐ No | ☐ Yes ☐ No |

### Analytics

| Feature | Description | Enabled? | In Use? |
|---------|-------------|----------|---------|
| Reports & Dashboards | Standard Salesforce reporting | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Health Cloud Dashboards | Pre-built healthcare analytics | ☐ Yes ☐ No | ☐ Yes ☐ No |

---

## ⚠️ NEEDS VERIFICATION — May Require Additional Licensing

These features are sometimes included with Unlimited but often require separate licensing:

### Einstein AI Features

| Feature | Description | Do We Have? | Notes |
|---------|-------------|-------------|-------|
| Einstein Classification | Auto-categorize messages/cases | ☐ Yes ☐ No ☐ Unknown | |
| Einstein Prediction Builder | Risk scoring, outcome prediction | ☐ Yes ☐ No ☐ Unknown | |
| Einstein GPT | Generative AI, summarization | ☐ Yes ☐ No ☐ Unknown | |
| Einstein for Service | Service-specific AI features | ☐ Yes ☐ No ☐ Unknown | |

### Document Processing

| Feature | Description | Do We Have? | Notes |
|---------|-------------|-------------|-------|
| Intelligent Document Automation (IDA) | OCR + AI extraction from documents | ☐ Yes ☐ No ☐ Unknown | |
| Document Classification | Auto-identify document types | ☐ Yes ☐ No ☐ Unknown | |

### Experience Cloud (Portals)

| Feature | Description | Do We Have? | Notes |
|---------|-------------|-------------|-------|
| Experience Cloud Licenses | Portal capability | ☐ Yes ☐ No ☐ Unknown | |
| Patient Portal | Patient self-service | ☐ Yes ☐ No ☐ Unknown | |
| Provider Portal | Clinic self-service | ☐ Yes ☐ No ☐ Unknown | |
| Payer/Adjuster Portal | Adjuster status visibility | ☐ Yes ☐ No ☐ Unknown | |

### Messaging

| Feature | Description | Do We Have? | Notes |
|---------|-------------|-------------|-------|
| SMS Messaging (Native) | Salesforce native SMS | ☐ Yes ☐ No ☐ Unknown | |
| Messaging Credits | SMS/messaging allowance | ☐ Yes ☐ No ☐ Unknown | |
| Third-Party SMS Integration | Current provider? | ☐ Yes ☐ No ☐ Unknown | Provider: _________ |

### Integration Platforms

| Feature | Description | Do We Have? | Notes |
|---------|-------------|-------------|-------|
| MuleSoft | Integration platform | ☐ Yes ☐ No ☐ Unknown | |
| HL7 FHIR Connector | Healthcare interoperability | ☐ Yes ☐ No ☐ Unknown | |

---

## 📋 Current State Questions

### Objects in Use

1. **Are we using standard Health Cloud objects or custom objects?**

   | Object Type | Using Standard? | Using Custom? | Custom Object Name |
   |-------------|-----------------|---------------|-------------------|
   | Patient/Member | ☐ | ☐ | _______________ |
   | Cases/Referrals | ☐ | ☐ | _______________ |
   | Authorizations | ☐ | ☐ | _______________ |
   | Care Plans | ☐ | ☐ | _______________ |
   | Tasks | ☐ | ☐ | _______________ |
   | Tickets | ☐ | ☐ | _______________ |

2. **What object is the "Ticket" that gets created alongside Tasks?**
   - ☐ Standard Case
   - ☐ Custom Object — Name: _______________
   - ☐ Other: _______________

3. **Do we have the Health Cloud managed package installed?**
   - ☐ Yes
   - ☐ No
   - ☐ Unknown

---

## 🎯 Priority Verification Items

For our automation initiatives, we specifically need to know:

| Priority | Feature | Why We Need It |
|----------|---------|----------------|
| **HIGH** | Care Plans | Automated patient journey for coaches |
| **HIGH** | CareRequest/Utilization Mgmt | Re-auth automation |
| **HIGH** | Omni-Channel/Queues | Fix task routing mess |
| **HIGH** | SMS Capability | Automated patient check-ins |
| **MEDIUM** | Einstein Classification | Route admin vs clinical messages |
| **MEDIUM** | IDA | Replace/enhance DocuPipe |
| **MEDIUM** | Experience Cloud | Adjuster self-service portal |
| **LOW** | Einstein GPT | PT note summarization |

---

## Response Requested

Please complete the tables above and return. Key questions:

1. **Which "should be included" features are NOT currently enabled?**
2. **Which "needs verification" features do we actually have?**
3. **What would we need to purchase to fill gaps?**
4. **Is the Health Cloud managed package installed and up to date?**

---

**Contact:** [Your Name]
**Deadline:** [Date]
**Purpose:** Planning for Operational Automation Project
