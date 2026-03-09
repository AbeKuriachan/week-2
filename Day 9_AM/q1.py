import os

records = [
    ["Aman", "Math", 88],
    ["Priya", "Physics", 91],
    ["Rahul", "Math", 76],
    ["Neha", "Chemistry", 84],
    ["Karan", "Physics", 73],
    ["Sneha", "Math", 95],
    ["Rohit", "Chemistry", 67],
    ["Anjali", "Physics", 89],
    ["Vikas", "Math", 82],
    ["Meera", "Chemistry", 90]
]


def add_student(name, subject, marks):
    for r in records:
        if r[0] == name and r[1] == subject:
            print("Duplicate entry not allowed.")
            return

    records.append([name, subject, marks])
    print("Student added successfully.")


def get_toppers(subject):
    subject_students = [r for r in records if r[1].lower() == subject.lower()]

    if not subject_students:
        print("No students found for this subject.")
        return

    toppers = sorted(subject_students, key=lambda x: x[2], reverse=True)[:3]

    print("\nTop Students:")
    for t in toppers:
        print(t)


def class_average(subject):
    marks = [r[2] for r in records if r[1].lower() == subject.lower()]

    if not marks:
        print("No records for this subject.")
        return

    avg = sum(marks) / len(marks)
    print(f"Average marks in {subject}: {avg:.2f}")


def above_average_students():
    if not records:
        print("No records available.")
        return

    overall_avg = sum(r[2] for r in records) / len(records)

    above_avg = [r for r in records if r[2] > overall_avg]

    print(f"\nOverall class average: {overall_avg:.2f}")
    print("Students scoring above average:")

    for s in above_avg:
        print(s)


def remove_student(name):
    global records

    new_records = [r for r in records if r[0].lower() != name.lower()]

    removed = len(records) - len(new_records)

    if removed == 0:
        print("Student not found.")
    else:
        records = new_records
        print(f"{removed} record(s) removed.")


def save_records():
    with open("students.txt", "w") as f:
        for r in records:
            f.write(f"{r[0]},{r[1]},{r[2]}\n")


def load_records():
    global records

    if not os.path.exists("students.txt"):
        return

    with open("students.txt", "r") as f:
        lines = f.readlines()

    if not lines:
        return

    records.clear()

    for line in lines:
        name, subject, marks = line.strip().split(",")
        records.append([name, subject, int(marks)])


load_records()

while True:

    print("\n--- Student Management System ---")
    print("1 Add student")
    print("2 Show toppers")
    print("3 Show class average")
    print("4 Show above-average students")
    print("5 Remove student")
    print("6 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        subject = input("Enter subject: ")
        marks = int(input("Enter marks: "))
        add_student(name, subject, marks)

    elif choice == "2":
        subject = input("Enter subject: ")
        get_toppers(subject)

    elif choice == "3":
        subject = input("Enter subject: ")
        class_average(subject)

    elif choice == "4":
        above_average_students()

    elif choice == "5":
        name = input("Enter student name to remove: ")
        remove_student(name)

    elif choice == "6":
        save_records()
        print("Records saved to students.txt")
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")