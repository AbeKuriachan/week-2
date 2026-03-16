# Artifact 7 --- Part B (BCNF)

## What is BCNF?

Boyce‑Codd Normal Form is a stronger version of 3NF.

A relation is in BCNF if:

For every functional dependency

X → Y

X must be a superkey.

## Example Schema (3NF but not BCNF)

CourseEnrollments:

| Student \| Course \| Instructor \|

Functional dependencies:

Course → Instructor\
(Student, Course) → Instructor

Problem:

Course determines Instructor but Course is not a key.

This violates BCNF.

## BCNF Decomposition

Split into two tables:

Courses(Course, Instructor)\
Enrollments(Student, Course)

Now:

Course → Instructor

Course is a key in Courses table.

Both tables satisfy BCNF.

## When keeping 3NF is acceptable

BCNF decomposition may cause:

-   loss of dependency preservation
-   additional joins

Therefore systems sometimes keep schema in **3NF** when:

-   performance is important
-   dependencies must be preserved
