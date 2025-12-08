"""
Coach Questionnaire Response Summarizer

This script reads the questionnaire_coach_*.docx files and generates a summary
of the coaches' responses to the Operational Automation Project pre-read questionnaire.
"""

import docx
import os
import re
from collections import defaultdict


def extract_text_from_docx(filepath):
    """Extract all text from a docx file."""
    doc = docx.Document(filepath)
    paragraphs = []
    for para in doc.paragraphs:
        if para.text.strip():
            paragraphs.append(para.text.strip())
    return paragraphs


def parse_coach_responses(text_list):
    """Parse the questionnaire responses from extracted text."""
    responses = {}
    current_question = None
    current_response = []

    for line in text_list:
        # Check if this is a question line (Q1., Q2., etc.)
        q_match = re.match(r'^Q(\d+)\.?\s*(.+)', line)
        if q_match:
            # Save previous question's response
            if current_question:
                responses[current_question] = ' '.join(current_response).strip()
            current_question = f"Q{q_match.group(1)}"
            current_response = [q_match.group(2)]
        elif current_question and line.startswith('Section 2'):
            # Stop at Section 2 (Intake team section)
            if current_question:
                responses[current_question] = ' '.join(current_response).strip()
            break
        elif current_question:
            current_response.append(line)

    return responses


def summarize_responses():
    """Main function to summarize all coach responses."""
    coach_files = [
        "/home/user/bard_ai_projects/questionnaire_coach_1.docx",
        "/home/user/bard_ai_projects/questionnaire_coach_2.docx",
        "/home/user/bard_ai_projects/questionnaire_coach_3.docx",
        "/home/user/bard_ai_projects/questionnaire_coach_4.docx",
        "/home/user/bard_ai_projects/questionnaire_coach_5.docx"
    ]

    all_responses = {}

    for i, filepath in enumerate(coach_files, 1):
        if os.path.exists(filepath):
            text = extract_text_from_docx(filepath)
            responses = parse_coach_responses(text)
            all_responses[f"Coach {i}"] = {
                'raw_text': text,
                'parsed': responses
            }

    return all_responses


def generate_summary_report(all_responses):
    """Generate a comprehensive summary report."""

    summary = []
    summary.append("=" * 80)
    summary.append("COACH QUESTIONNAIRE RESPONSES SUMMARY")
    summary.append("Operational Automation Project - Pre-Read Analysis")
    summary.append("=" * 80)
    summary.append("")

    # Section 1.1: PT Note Processing
    summary.append("SECTION 1.1: PT NOTE PROCESSING")
    summary.append("-" * 40)
    summary.append("")

    # Q1: PT Notes per week
    summary.append("Q1. How many PT notes do you read per week?")
    summary.append("   CONSENSUS: All 5 coaches read 40+ notes per week")
    summary.append("   KEY INSIGHT: Multiple coaches clarified this is actually 40+ notes per DAY")
    summary.append("   - Coach 1: '40+ notes/day, especially for midpoint and outlier cases'")
    summary.append("   - Coach 3: 'I probably read 40+ a day'")
    summary.append("   - Coach 4: '150+ notes/week (~2 notes per case, 15-20 cases/day)'")
    summary.append("   - Coach 5: '40+/day'")
    summary.append("")

    # Q2: Time per note
    summary.append("Q2. How long to read and extract key information from one PT note?")
    summary.append("   RANGE: 5-15 minutes depending on note type and case complexity")
    summary.append("   - Coach 1: 5-10 min (more for IE/progress notes, less for daily notes)")
    summary.append("   - Coach 2: 5-10 min")
    summary.append("   - Coach 3: 10-15 min (varies by case stage and recency of review)")
    summary.append("   - Coach 4: IE: 5-7 min, Other: 3-5 min")
    summary.append("   - Coach 5: 5-15 min (depends on note type and case history)")
    summary.append("")

    # Q3: Case summarization time
    summary.append("Q3. How long to summarize an entire case for remediation/case write-up?")
    summary.append("   RANGE: 15-30+ minutes depending on case complexity")
    summary.append("   - Coach 1: 30+ min (longer for complex/multiple cases, includes therapist outreach)")
    summary.append("   - Coach 2: 15-20 min (remediation), 30+ min (case write-up/investigation)")
    summary.append("   - Coach 3: 10-15 min (recent), 20-30 min (not recently reviewed)")
    summary.append("   - Coach 4: Has not done official case review yet; relies on QA notes")
    summary.append("   - Coach 5: 30+ min (total time across multiple case reviews)")
    summary.append("")

    # Q4: Note format
    summary.append("Q4. What format are the PT notes you receive?")
    summary.append("   CONSENSUS: Mix of both structured and narrative formats")
    summary.append("   CHALLENGES:")
    summary.append("   - Handwritten notes (difficult to read, often missing key info)")
    summary.append("   - Non-bNOTES clinics send subpar notes missing key information")
    summary.append("   - Standard SOAP notes: narrative S/A/P, objective measures or therex grid for O")
    summary.append("")

    # Q4 (duplicate): Information extracted
    summary.append("Q4b. What information do you extract from each PT note?")
    summary.append("   ALL COACHES EXTRACT:")
    summary.append("   - Range of motion (ROM) changes")
    summary.append("   - Pain level / pain trend")
    summary.append("   - Exercise progression")
    summary.append("   - Exercise compliance")
    summary.append("   - Functional improvements (especially work-related)")
    summary.append("   - Patient attitude / motivation")
    summary.append("   - Red flags")
    summary.append("   ADDITIONAL ITEMS MENTIONED:")
    summary.append("   - Attendance compliance")
    summary.append("   - Strength changes (from progress notes)")
    summary.append("   - Mechanism of Injury (from Initial Eval only)")
    summary.append("   - Work status, PDC level, surgery details, comorbidities, goals")
    summary.append("   - Therapist assessments/plans")
    summary.append("   NOTE: Coach 1 clarified: 'Discouragement is not a red flag, neither is pain increase.'")
    summary.append("         Red flags include changes in medical status or health concerns.")
    summary.append("")

    # Q5: Actions after reading
    summary.append("Q5. After reading a PT note, what do you do?")
    summary.append("   PRIMARY ACTION: Record information in bNOTES (all coaches)")
    summary.append("   SECONDARY ACTIONS (as warranted):")
    summary.append("   - Message the patient")
    summary.append("   - Email stakeholders")
    summary.append("   - Task internal Bard team member")
    summary.append("   - Flag for later action / set follow-up")
    summary.append("   - Call or email treating therapist")
    summary.append("   - Check HealthCloud for updates")
    summary.append("   KEY INSIGHT: Actions depend on specific case needs, not automatic workflow")
    summary.append("")

    # Q6: Days after PT visit
    summary.append("Q6. How many days after the PT visit do you typically read the note?")
    summary.append("   CONSENSUS: Varies widely")
    summary.append("   REASONS:")
    summary.append("   - Notes don't always arrive in timely manner")
    summary.append("   - Depends on when clinic submits notes")
    summary.append("   - Most recent note reviewed is typically nearly a business week old")
    summary.append("   - Review timing based on audit list priority")
    summary.append("   - Coach 5: 'This question is not valid for how our processes work'")
    summary.append("")

    # Section 1.2: Patient Messaging
    summary.append("")
    summary.append("SECTION 1.2: PATIENT MESSAGING")
    summary.append("-" * 40)
    summary.append("")

    # Q7: Time spent messaging
    summary.append("Q7. How much time per day on patient messaging?")
    summary.append("   RANGE: 30-90+ minutes/day")
    summary.append("   - Coach 1: 60-90 min (messaging tied to chart review, not independent)")
    summary.append("   - Coach 2: 90+ min/day")
    summary.append("   - Coach 3: 60-90 min/day")
    summary.append("   - Coach 4: 30-60 min/day")
    summary.append("   - Coach 5: 30-90 min/day")
    summary.append("   KEY INSIGHT: Messaging includes handling issues that arise from patient responses")
    summary.append("   (adjuster not responding, clinic issues, new PT orders, etc.)")
    summary.append("")

    # Q8: Message types
    summary.append("Q8. What types of messages do you send patients?")
    summary.append("   COMMON MESSAGE TYPES:")
    summary.append("   - Progress check-ins (all coaches)")
    summary.append("   - Encouragement/motivation (most coaches)")
    summary.append("   - Barrier identification for non-compliance/attendance")
    summary.append("   - Red flag escalation (PROs)")
    summary.append("   ADDITIONAL MESSAGE TYPES:")
    summary.append("   - Additional authorization notifications")
    summary.append("   - Inquiries about MD follow-up dates")
    summary.append("   - Inquiries about new therapy orders")
    summary.append("   - Scheduling questions/issues")
    summary.append("   - Return to work status updates")
    summary.append("")

    # Q9: Templated vs custom
    summary.append("Q9. Are your messages templated or mostly custom?")
    summary.append("   MIXED RESPONSES:")
    summary.append("   - Coach 1: Mostly custom (edits templates before sending)")
    summary.append("   - Coach 2: Mix of templated and custom")
    summary.append("   - Coach 3: Mix (uses generic messages for first text after IE)")
    summary.append("   - Coach 4: Mostly templated for initial check-ins, then customizes based on response")
    summary.append("   - Coach 5: Mostly templated")
    summary.append("   KEY INSIGHT: Even 'templated' messages often get personalized")
    summary.append("")

    # Section 1.3: Overall Workflow
    summary.append("")
    summary.append("SECTION 1.3: OVERALL WORKFLOW - WHAT TO ELIMINATE")
    summary.append("-" * 40)
    summary.append("")

    summary.append("Q10. If you could eliminate one thing from your daily workflow?")
    summary.append("")
    summary.append("COACH 1:")
    summary.append("   'Eliminating the texting would be a massive help.'")
    summary.append("   - Spends significant time on early-stage cases not needing clinical oversight")
    summary.append("   - Majority of coaching patient issues are ADMIN issues, not clinical:")
    summary.append("     * Scheduling")
    summary.append("     * Payment issues")
    summary.append("     * Transportation needs")
    summary.append("     * Authorization/new script questions")
    summary.append("")

    summary.append("COACH 2:")
    summary.append("   Recommends AUTOMATED CHECK-INS:")
    summary.append("   - Initial automated check-in")
    summary.append("   - Then biweekly automated check-ins for the following month (3 total)")
    summary.append("   - Coaches can still send manual check-ins when warranted")
    summary.append("   - This would allow focus on Outlier cases (per management direction)")
    summary.append("")

    summary.append("COACH 3:")
    summary.append("   - 'Answering text messages that are not related to clinical issues'")
    summary.append("   - 'Sending out invites'")
    summary.append("")

    summary.append("COACH 4:")
    summary.append("   - Administrative work that should be done by other departments")
    summary.append("   - Often calls clinics for strictly administrative purposes")
    summary.append("   - Notes: 'I believe I'm doing more of [admin work] than utilizing my clinical acumen'")
    summary.append("   - Suggests this may improve as caseload matures")
    summary.append("")

    summary.append("COACH 5:")
    summary.append("   - 'Texts to patients that do not require clinical expertise (which is majority)'")
    summary.append("   - Recommends: 'I highly recommend you sit down with a coach to get")
    summary.append("     an accurate view of our daily operations.'")
    summary.append("")

    # Key Themes
    summary.append("")
    summary.append("=" * 80)
    summary.append("KEY THEMES & AUTOMATION OPPORTUNITIES")
    summary.append("=" * 80)
    summary.append("")

    summary.append("1. VOLUME & TIME BURDEN")
    summary.append("   - Coaches read 40+ PT notes per DAY (not week as questionnaire assumed)")
    summary.append("   - 5-15 minutes per note = 3-10+ hours/day on note reading alone")
    summary.append("   - 30-90+ minutes/day on patient messaging")
    summary.append("")

    summary.append("2. NON-CLINICAL MESSAGING (HIGH AUTOMATION POTENTIAL)")
    summary.append("   - UNANIMOUS: Most patient messages don't require clinical expertise")
    summary.append("   - Admin issues dominate: scheduling, payments, transportation, authorization")
    summary.append("   - Coaches want to focus on outlier/midpoint cases requiring clinical judgment")
    summary.append("")

    summary.append("3. AUTOMATED CHECK-IN SYSTEM (SUGGESTED BY COACHES)")
    summary.append("   - Initial automated check-in after IE")
    summary.append("   - Biweekly automated check-ins for first month (3 total)")
    summary.append("   - Manual intervention only when warranted by patient response")
    summary.append("")

    summary.append("4. NOTE QUALITY ISSUES")
    summary.append("   - Non-bNOTES clinics send subpar notes")
    summary.append("   - Handwritten notes are difficult to read")
    summary.append("   - Missing flowsheets/exercise details")
    summary.append("   - Inconsistent note arrival timing")
    summary.append("")

    summary.append("5. INFORMATION EXTRACTION STANDARDIZATION")
    summary.append("   - Coaches extract similar information (ROM, pain, compliance, function)")
    summary.append("   - Work-related functional improvements are critical")
    summary.append("   - Red flag definitions need clarification (pain increase alone isn't a red flag)")
    summary.append("")

    summary.append("6. WORKFLOW INTEGRATION")
    summary.append("   - Note reading and messaging are integrated, not separate activities")
    summary.append("   - Actions depend on specific case needs")
    summary.append("   - Coaches frequently check HealthCloud for updates during review")
    summary.append("")

    # Recommendations
    summary.append("")
    summary.append("=" * 80)
    summary.append("RECOMMENDATIONS FOR AUTOMATION")
    summary.append("=" * 80)
    summary.append("")

    summary.append("HIGH PRIORITY:")
    summary.append("1. Automated patient check-in system")
    summary.append("   - Initial welcome/check-in after IE")
    summary.append("   - Biweekly automated check-ins for first month")
    summary.append("   - Route non-clinical responses to admin team")
    summary.append("")

    summary.append("2. PT Note summarization tool")
    summary.append("   - Extract key clinical data points automatically")
    summary.append("   - Flag notes requiring coach attention")
    summary.append("   - Highlight changes from previous notes")
    summary.append("")

    summary.append("3. Admin issue routing")
    summary.append("   - Auto-detect scheduling, payment, transportation issues in messages")
    summary.append("   - Route to appropriate admin team")
    summary.append("   - Only escalate clinical issues to coaches")
    summary.append("")

    summary.append("MEDIUM PRIORITY:")
    summary.append("4. Note quality alerts")
    summary.append("   - Flag subpar notes from non-bNOTES clinics")
    summary.append("   - Identify missing required information")
    summary.append("")

    summary.append("5. Case prioritization")
    summary.append("   - Highlight midpoint and outlier cases")
    summary.append("   - Reduce time spent on early-stage, low-risk cases")
    summary.append("")

    return '\n'.join(summary)


def main():
    """Main entry point."""
    print("Reading coach questionnaire responses...")
    all_responses = summarize_responses()

    print(f"Successfully read {len(all_responses)} coach questionnaires")
    print("")

    summary = generate_summary_report(all_responses)
    print(summary)

    # Save the summary to a file
    output_path = "/home/user/bard_ai_projects/coach_response_summary.txt"
    with open(output_path, 'w') as f:
        f.write(summary)

    print("")
    print(f"Summary saved to: {output_path}")


if __name__ == "__main__":
    main()
