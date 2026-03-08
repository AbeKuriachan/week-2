# PAN Card Validator – AI Prompt Evaluation

## 1. Exact Prompt Used

"Write a Python program that validates an Indian PAN card number format using if-else conditions.  
PAN format: 5 uppercase letters, 4 digits, 1 uppercase letter (e.g., ABCDE1234F).  
The 4th character indicates the type of taxpayer."

---

# 2. AI-Generated Code


pan = input("Enter PAN number: ")

if len(pan) != 10:
    print("Invalid PAN format")
else:
    if pan[:5].isalpha() and pan[:5].isupper() and pan[5:9].isdigit() and pan[9].isalpha() and pan[9].isupper():
        print("Valid PAN format")

        taxpayer_type = pan[3]

        if taxpayer_type == 'P':
            print("Individual")
        elif taxpayer_type == 'C':
            print("Company")
        elif taxpayer_type == 'H':
            print("HUF")
        elif taxpayer_type == 'F':
            print("Firm")
        elif taxpayer_type == 'A':
            print("Association of Persons")
        elif taxpayer_type == 'T':
            print("Trust")
        else:
            print("Other taxpayer type")

    else:
        print("Invalid PAN format")

# 3. Issues

Issues:

Nested if statements

Repeated logic

No function used

No input sanitation

Pythonic improvements:

Use a function

Strip whitespace

Normalize case

Use a dictionary for taxpayer type mapping



# 4. Corrected code

def validate_pan(pan):
    pan = pan.strip().upper()

    if len(pan) != 10:
        return "Invalid PAN format"

    # Validate first 5 characters (letters)
    for i in range(5):
        if not ('A' <= pan[i] <= 'Z'):
            return "Invalid PAN format"

    # Validate next 4 characters (digits)
    for i in range(5, 9):
        if not pan[i].isdigit():
            return "Invalid PAN format"

    # Validate last character (letter)
    if not ('A' <= pan[9] <= 'Z'):
        return "Invalid PAN format"

    taxpayer_types = {
        'P': "Individual",
        'C': "Company",
        'H': "HUF",
        'F': "Firm",
        'A': "Association of Persons",
        'T': "Trust"
    }

    taxpayer_type = pan[3]

    if taxpayer_type in taxpayer_types:
        return f"Valid PAN. Taxpayer Type: {taxpayer_types[taxpayer_type]}"
    else:
        return "Valid PAN. Taxpayer Type: Other"

pan_input = input("Enter PAN number: ")
print(validate_pan(pan_input))
