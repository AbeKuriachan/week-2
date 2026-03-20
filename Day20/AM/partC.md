# Part C — Interview Ready (20%)

## Q1 — Difference between *args and **kwargs

### *args
- Used to pass a variable number of **positional arguments**
- Stored as a **tuple**
- Example:


def func(*args):
    print(args)

func(1, 2, 3)  
Output: (1, 2, 3)

## **kwargs

- Used to pass a variable number of keyword arguments
- Stored as a dictionary
- Example:

def func(**kwargs):
    print(kwargs)

func(a=1, b=2)  
Output: {'a': 1, 'b': 2}

## Q2 — Coding: Student Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        else:
            return 'C'

    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}, Grade: {self.calculate_grade()}"


### Example usage
s1 = Student("Alice", 92)
s2 = Student("Bob", 78)
s3 = Student("Charlie", 60)

print(s1)
print(s2)
print(s3)


## Q3 — What are dunder methods?
Definition

Dunder (Double UNDERscore) methods are special methods in Python

They start and end with __

Used to define behavior for built-in operations

Why are they important?

Enable operator overloading

Make custom objects behave like built-in types

Improve code readability and integration with Python features

Examples

__init__ → Constructor (object initialization)

__str__ → Human-readable string representation

__add__ → Defines behavior for + operator