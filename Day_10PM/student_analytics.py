"""
Student Performance Analytics Module.

Provides utilities to create student records, calculate GPA,
rank students, generate reports, and classify students.

Example:
    Run this module directly to see example usage.
"""

from collections import defaultdict
from typing import Dict, List, Optional


def create_student(name: str, roll: str, **marks: int) -> dict:
    """
    Create a student record.

    Args:
        name: Student name.
        roll: Roll number.
        **marks: Subject marks.

    Returns:
        dict: Student dictionary.

    Example:
        >>> s = create_student("Amit", "R001", math=90, python=85)
        >>> print(s)
    """

    if not name or not roll:
        raise ValueError("Name and roll are required")

    validated_marks = {}

    for subject, mark in marks.items():
        if not isinstance(mark, (int, float)):
            raise ValueError(f"Invalid mark for {subject}")
        if mark < 0 or mark > 100:
            raise ValueError(f"{subject} mark must be between 0 and 100")

        validated_marks[subject] = int(mark)

    return {
        "name": name,
        "roll": roll,
        "marks": validated_marks,
        "attendance": 0.0,
    }


def calculate_gpa(*marks: float, scale: float = 10.0) -> float:
    """
    Calculate GPA from marks.

    Args:
        *marks: Variable number of marks.
        scale: GPA scale.

    Returns:
        float: GPA value.
    """

    if not marks:
        raise ValueError("At least one mark must be provided")

    avg = sum(marks) / len(marks)
    gpa = (avg / 100) * scale

    return round(gpa, 2)


def _average_marks(student: dict) -> float:
    """Helper function to compute average marks."""
    marks = student.get("marks", {})
    if not marks:
        return 0.0
    return sum(marks.values()) / len(marks)


def get_top_performers(
    students: List[dict], n: int = 5, subject: Optional[str] = None
) -> List[dict]:
    """
    Return top performing students.

    Args:
        students: List of students.
        n: Number of top students.
        subject: Optional subject to rank by.

    Returns:
        list[dict]: Top students.
    """

    if not students:
        return []

    def score(student):
        if subject:
            return student["marks"].get(subject, 0)
        return _average_marks(student)

    ranked = sorted(students, key=score, reverse=True)

    return ranked[:n]


def generate_report(student: dict, **options) -> str:
    """
    Generate a formatted student report.

    Args:
        student: Student dictionary.
        **options:
            include_rank=True
            include_grade=True
            verbose=False

    Returns:
        str: Report string.
    """

    include_rank = options.get("include_rank", True)
    include_grade = options.get("include_grade", True)
    verbose = options.get("verbose", False)

    name = student.get("name", "Unknown")
    roll = student.get("roll", "Unknown")
    marks = student.get("marks", {})

    avg = _average_marks(student)

    lines = []
    lines.append(f"Student: {name} ({roll})")
    lines.append(f"Average: {avg:.2f}")

    if verbose:
        for sub, mark in marks.items():
            lines.append(f"{sub}: {mark}")

    if include_grade:
        if avg >= 85:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "D"

        lines.append(f"Grade: {grade}")

    if include_rank:
        lines.append("Rank: N/A")

    return "\n".join(lines)


def classify_students(students: List[dict]) -> Dict[str, List[dict]]:
    """
    Classify students into grades.

    Args:
        students: List of student dictionaries.

    Returns:
        dict: {'A': [...], 'B': [...], 'C': [...], 'D': [...]}
    """

    result: Dict[str, List[dict]] = defaultdict(list)

    for student in students:
        avg = _average_marks(student)

        if avg >= 85:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "D"

        result[grade].append(student)

    for g in ["A", "B", "C", "D"]:
        result[g]

    return dict(result)



# Example Usage


if __name__ == "__main__":

    print("\n=== Student Analytics Example ===\n")

    # Create students
    students = [
        create_student("Amit", "R001", math=85, python=92, ml=78),
        create_student("Priya", "R002", math=95, python=88, ml=91),
        create_student("Rahul", "R003", math=60, python=70, ml=65),
    ]

    students[0]["attendance"] = 0.9
    students[1]["attendance"] = 0.95
    students[2]["attendance"] = 0.85

    print("Students:")
    for s in students:
        print(s)

    # GPA Example
    print("\nGPA Example:")
    gpa = calculate_gpa(85, 92, 78)
    print("GPA:", gpa)

    # Top performers
    print("\nTop Performers:")
    top = get_top_performers(students, 2)
    for s in top:
        print(s["name"], _average_marks(s))

    # Subject ranking
    print("\nTop Math Student:")
    top_math = get_top_performers(students, 1, subject="math")
    print(top_math[0]["name"], top_math[0]["marks"]["math"])

    # Generate report
    print("\nStudent Report:")
    report = generate_report(students[0], verbose=True)
    print(report)

    # Classification
    print("\nStudent Classification:")
    classified = classify_students(students)

    for grade, studs in classified.items():
        print(f"\nGrade {grade}:")
        for s in studs:
            print("-", s["name"])
