from student_analytics import *

print("\nCreating Students\n")

students = [
    create_student("Amit", "R001", math=85, python=92, ml=78),
    create_student("Priya", "R002", math=95, python=88, ml=91),
    create_student("Rahul", "R003", math=60, python=70, ml=65),
]

for s in students:
    print(s)

# -------------------
# create_student tests
# -------------------

print("\nTesting create_student")

s = create_student("Test", "R100", math=90)
print(s)

assert s["name"] == "Test"
assert "math" in s["marks"]

# -------------------
# calculate_gpa tests
# -------------------

print("\nTesting calculate_gpa")

gpa = calculate_gpa(80, 90, 100)
print("GPA:", gpa)

assert round(gpa, 2) == 9.0

gpa2 = calculate_gpa(70, 80, scale=5)
print("GPA scale 5:", gpa2)

assert gpa2 <= 5

# -------------------
# get_top_performers
# -------------------

print("\nTesting get_top_performers")

top_students = get_top_performers(students, 2)
print("Top Students:", top_students)

assert top_students[0]["name"] == "Priya"

top_math = get_top_performers(students, subject="math")
print("Top Math Student:", top_math[0])

assert top_math[0]["marks"]["math"] == 95

# -------------------
# generate_report
# -------------------

print("\nTesting generate_report")

report = generate_report(students[0], verbose=True)
print(report)

assert "Amit" in report

# -------------------
# classify_students
# -------------------

print("\nTesting classify_students")

classified = classify_students(students)

for grade, studs in classified.items():
    print(f"\nGrade {grade}:")
    for s in studs:
        print(s["name"])

assert "A" in classified
assert isinstance(classified["A"], list)

print("\nAll tests passed successfully!")
