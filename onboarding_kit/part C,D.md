### Q1️⃣ Conceptual — Virtual Environments

In 3–4 sentences, explain to a non-technical interviewer what a virtual environment is

A Python virtual environment is an isolated workspace where a project keeps its own libraries and 
dependencies separate from other projects on the same computer. Developers use it to ensure that each 
project runs with the exact package versions it needs, without interfering with others. Without a 
virtual environment, the code would be run using the default system python that has been added to path and
different projects can conflict — for example, one project might require an older 
version of a library while another needs a newer one, causing errors and instability. A good analogy is 
having separate toolboxes for different jobs: instead of mixing all tools together and risking confusion,
each project gets its own organized, self-contained kit.

"""
Simple script to validate Python version compatibility.
Requires Python 3.11 or higher.
"""
### q2
- Multiple imports on one line (import os, sys, json)
- Unused imports (os, json)
- Function name not snake_case (checkVersion)
- Python version logic is incorrect (>= 3 and >= 11 fails for 4.x cases)
- Unused variable (temp = 42)
- Missing module and function docstrings (Pylint warning)

### corrrected code


import sys


def check_version():
    """Return version status based on Python version."""
    version = sys.version_info
    required = (3, 11)

    if (version.major, version.minor) >= required:
        return "Good"

    return "Bad"


def main():
    """Execute version check and print result."""
    result = check_version()
    print("Version status:", result)


if __name__ == "__main__":
    main()

### q3
Cause: Installed in a Different Python Environment
May have:
- Installed globally
- May have installed numpy but may be using global python as interpreter
- Virtual environment may not be activated

#### Diagnostic commands
- python -m pip show numpy
- where python

### q4

prompt : Generate a beginner-friendly .pylintrc configuration file for a Python AI/ML project.

Requirements:
- Should not be overly strict for beginners
- Allow common data science patterns (short variable names like X, y, df)
- Increase max line length to 100
- Disable overly pedantic warnings
- Keep code quality reasonable (target >= 8/10 score)
- Include comments explaining important sections

The AI-generated .pylintrc configuration strikes a practical balance between code quality enforcement 
and beginner accessibility. It appropriately relaxes overly strict warnings such as missing docstrings 
and invalid variable names, which are common in AI/ML workflows where variables like X, y, and df are 
standard. Increasing the maximum line length to 100 also aligns with modern formatting tools like Black 
while improving readability for data-heavy code.
However, disabling warnings like broad-except may hide potentially unsafe error handling practices if
not used carefully

