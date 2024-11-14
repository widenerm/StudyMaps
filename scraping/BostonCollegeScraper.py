import pdfplumber
import re
import pandas as pd

# Define regex patterns for each field
patterns = {
    "Course Code": r"^(CSCI\d+)",  # Matches course codes like "CSCI110217"
    "Course Title": r"^\w+\d+\n(.*)",  # Matches the line after course code
    "Instructor": r"Levear, .*",  # Matches instructor name (assuming "Levear, First Last" format)
    "Semester": r"(Fall|Spring|Summer) \d{4}",  # Matches semester and year like "Fall 2024"
    "Credits": r"Credits: (\d+)",  # Matches credits info
    "Room and Schedule": r"Room and Schedule: (.+)",  # Matches room and schedule
    "Core Requirement": r"Satisies Core Requirement: (.+)",  # Matches core requirements
    "Prerequisites": r"Prerequisites: (.+)",  # Matches prerequisites
    "Corequisites": r"Corequisites: (.+)",  # Matches corequisites
    "Cross-listed": r"Cross-listed with: (.+)",  # Matches cross-listed info
    "Frequency": r"Frequency: (.+)",  # Matches frequency
    "Student Level": r"Student Level: (.+)",  # Matches student level
    "Comments": r"Comments: (.+)",  # Matches comments
    "Status": r"Status: (.+)"  # Matches status
}

def extract_info_from_pdf(pdf_path):
    data = []
    
    # Open the PDF and extract text
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            
            # Extract each field using regex patterns
            entry = {}
            for field, pattern in patterns.items():
                match = re.search(pattern, text, re.MULTILINE)
                entry[field] = match.group(1) if match else "N/A"
                
            data.append(entry)
    
    return data

def save_to_csv(data, csv_path):
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
    print(f"Data saved to {csv_path}")

# Use the functions
pdf_path = "courses.pdf"  # Your PDF file path here
csv_path = "course_data.csv"

data = extract_info_from_pdf(pdf_path)
save_to_csv(data, csv_path)
