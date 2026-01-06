#!/usr/bin/env python3
"""
Script to read binary document files and extract text content.
"""
import subprocess
import sys

# Install required packages
packages = ['openpyxl', 'python-pptx', 'python-docx']
for pkg in packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', pkg])

from openpyxl import load_workbook
from pptx import Presentation
from docx import Document

def read_xlsx(filepath):
    """Read Excel file and return content."""
    print(f"\n{'='*80}")
    print(f"READING: {filepath}")
    print('='*80)

    wb = load_workbook(filepath)
    for sheet_name in wb.sheetnames:
        print(f"\n--- Sheet: {sheet_name} ---")
        ws = wb[sheet_name]
        for row in ws.iter_rows(values_only=True):
            # Filter out empty rows
            if any(cell is not None for cell in row):
                row_text = ' | '.join(str(cell) if cell is not None else '' for cell in row)
                print(row_text)

def read_pptx(filepath):
    """Read PowerPoint file and return content."""
    print(f"\n{'='*80}")
    print(f"READING: {filepath}")
    print('='*80)

    prs = Presentation(filepath)
    for i, slide in enumerate(prs.slides, 1):
        print(f"\n--- Slide {i} ---")
        for shape in slide.shapes:
            if hasattr(shape, 'text') and shape.text.strip():
                print(shape.text)

def read_docx(filepath):
    """Read Word document and return content."""
    print(f"\n{'='*80}")
    print(f"READING: {filepath}")
    print('='*80)

    doc = Document(filepath)
    for para in doc.paragraphs:
        if para.text.strip():
            print(para.text)

    # Also read tables
    for i, table in enumerate(doc.tables, 1):
        print(f"\n--- Table {i} ---")
        for row in table.rows:
            row_text = ' | '.join(cell.text.strip() for cell in row.cells)
            if row_text.replace('|', '').strip():
                print(row_text)

if __name__ == '__main__':
    # Read DocuPipe UAT issues log
    read_xlsx('/home/user/bard_ai_projects/DocuPipe UAT issues log.xlsx')

    # Read Bardavon Workflow 2025
    read_pptx('/home/user/bard_ai_projects/Bardavon Worklow 2025.pptx')

    # Read Coach Case List document
    read_docx('/home/user/bard_ai_projects/Coach Case List – Functional Overview, Data Logic, and FAQs.docx')
