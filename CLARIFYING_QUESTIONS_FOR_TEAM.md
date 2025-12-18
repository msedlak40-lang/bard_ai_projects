# Clarifying Questions — Workflow Documentation

Please help us answer these questions so we can properly document our current processes and identify automation opportunities.

---

## Systems & Data

**Q1. EMR Required Fields vs. Clinic Required Fields**
You mentioned these are different. Can you list what the EMR requires to create a case vs. what the clinic needs to accept a placement?

**Q2. Patient ID Flow**
Is Patient ID created in RainTree first, then pushed to EMR, then to Salesforce? Or is there a different sequence?

**Q3. Claim ID vs. Cases**
You said each claim can have multiple cases. Can you give an example? (e.g., same injury with multiple PT episodes? Different body parts? Something else?)

---

## Referral Intake

**Q4. Inbox Triage Staffing & Volume**
The one person manning the referral inbox — are they triaging all referrals for the whole company? What's their daily volume?

**Q5. Web Form vs. Email**
What percentage of referrals come via web form vs. email? You mentioned the web form allows wrong data formats — which fields are problematic?

**Q6. DocuPipe Current State**
What's DocuPipe doing well? What's it missing? (Want to confirm current state post-meeting)

---

## Task/Ticket Problem

**Q7. Task Creation Triggers**
"Tasks created every time a communication happens" — Is this every inbound AND outbound email? Or just inbound?

**Q8. Ticket Object**
The ticket created alongside every task — Is this a Salesforce Case, a custom object, or something else? Who reviews these tickets?

**Q9. Recycled Email Token Issue**
How often does the recycled email with old token problem happen? Is there a way to detect it today, or does it just get lost until someone complains?

---

## Patient Check-In / Re-Auth Process

**Q10. IE Check-In Team**
How many people are on the IE check-in team? How many patients do they check on per day?

**Q11. Visit Count Data**
"Within 2 visits of authorized number" — How do you know how many visits have been used? Is this data in Salesforce, EMR, or RainTree?

**Q12. SF Email Limitation**
Who said Salesforce can't email non-individual addresses (like a clinic's general email)? Is this a Salesforce platform limitation or a configuration/policy choice?

---

## Clinics & Notes

**Q13. Direct Billing Clinics**
What percentage of your network direct bills (cutting you out of the process)? Is there a contract term that should prevent this?

**Q14. Missing Notes Timeline**
How many days/weeks do PT notes typically lag? What's the current escalation process when a clinic doesn't respond to requests for notes?

---

*Please respond to whichever questions you can answer. Partial answers are helpful!*
