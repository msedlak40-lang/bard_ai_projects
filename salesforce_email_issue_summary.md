
# Salesforce Case Email Handling Issue — Summary

## Context
- Organization uses **Salesforce Cases** with **Email-to-Case** via a **shared inbox**.
- Outbound emails sent **from a Case** include a **token** used to associate replies with the correct Case.

## What Works Correctly
- When a case manager emails an **adjuster** from the Case:
  - A token is added.
  - The adjuster’s reply routes correctly back into the Case via Email-to-Case.
  - This behavior is desired and efficient.

## Core Problem
### **Replying to tokenized emails inside Salesforce does NOT deliver to external recipients.**
- When a case manager clicks **Reply** on an email already attached to a Case:
  - Salesforce **shows** the email as sent.
  - A record of the email appears on the Case.
  - **But the intended recipient does NOT receive the message.**
  - The email effectively “stays inside the Case.”

### What *does* work:
- Case managers **can create a NEW outbound email** from the Case.
  - These *do* send to the intended recipient successfully.
- The problem is **specific to replying** to token-bearing emails.

## Impact on Workflow
- Case managers cannot simply **reply** to external stakeholders from the Case.
- They must:
  1. Open the inbound email logged on the Case.
  2. **Copy/paste** the content into a **NEW** email.
  3. Send the new email from the Case.
- This adds:
  - Manual effort  
  - Higher risk of missing details  
  - Inefficiency and confusion  

## Additional Clarifications Established
- These are **standard Salesforce Case records** (not custom objects).
- The inbound emails come through **Email-to-Case**, triggered by a shared inbox.
- The issue is **not** that outgoing emails fail entirely:
  - Only **replies** fail to reach external recipients.
- It remains unknown:
  - Where replies from stakeholders *other than the adjuster* land.
  - Whether outbound messages to non-adjusters also contain tokens.

## Items Still Needing Verification
These facts affect root cause analysis:
1. **Where do replies from non-adjuster stakeholders actually go?**
2. **Do emails to other stakeholders also contain the token?**
3. **Do Salesforce Email Logs show the reply emails as successfully delivered or blocked?**
4. **Are there automation rules, flows, or processes that intercept or reroute replies?**
5. **Differences between “new outbound email” headers vs. “reply” headers.**

## Summary Problem Statement (for leadership review)
> **When a case manager replies to a tokenized email inside Salesforce, the reply is logged on the Case but does not reach the external recipient.  
New emails send successfully, but replies do not.  
This forces case managers to manually copy/paste content into new emails, creating inefficiency and risk.**  

This behavior is **not standard** for Salesforce and indicates a configuration, routing, or automation interaction that needs investigation.

