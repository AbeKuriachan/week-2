# Part D — AI-Augmented Task (10%)

## 1. Prompt Given to AI

"Explain Python dunder methods with examples for beginners and include a custom class implementation."

---

## 2. AI Output

### What are Dunder Methods?

Dunder (Double UNDERscore) methods are special methods in Python that start and end with `__`. They allow developers to define how objects behave with built-in operations.

Examples:
- `__init__` → Initializes an object
- `__str__` → Returns a readable string representation
- `__add__` → Defines behavior for `+` operator

---

### Example 1: Basic Class


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

p = Person("Alice")
print(p) 

## Example 2: Custom Class with Operator Overloading

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return f"Number({self.value})"

n1 = Number(10)
n2 = Number(20)

result = n1 + n2
print(result)


## 3. Evaluation
Are the examples correct?

Yes, the examples are correct.

__init__ properly initializes attributes.

__str__ returns a readable string.

__add__ correctly overloads the + operator.

## Minor Improvements
In __add__, type checking could be added: