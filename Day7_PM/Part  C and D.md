## PART C  

### 1. Output  

```
<class 'bool'>
True
2
3
True
False
False
53
8
```

---

### 2. Function  

```python
def analyse_value(input):
    '''This function takes ANY Python value
    and returns a formatted string with:
    - The value itself
    - Its type
    - Its truthiness (True/False)
    - Its length (if applicable, "N/A" otherwise)'''
    
    type_name = type(input).__name__
    truthy = bool(input)
    
    try:
        length = len(input)
    except:
        length = "N/A"
```

---

### 3. Corrected Code  

```python
name = input("Name: ")
age = int(input("Age: "))  # convert to int

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(f"{name} is {age} years old and is a {status}")
print(f"In 5 years: {age + 5}")

score = 85.5
print(f"Score: {score:.0f}")
```

---

## PART D  

**Prompt:**  
> Generate a Python type conversion matrix showing what happens when you convert between int, float, str, bool, list, and tuple — include edge cases and potential errors.

The AI-generated type conversion matrix was a strong starting point, capturing most standard behaviors in Python’s type system. It correctly described:

- Conversions between numeric types (`int ↔ float`)
- Truthiness rules for `bool`
- Conversion between iterable types (`list ↔ tuple`)

The examples were generally accurate and helpful for learners.

### Identified Gaps and Inaccuracies

- Converting a string to a list splits into **individual characters**, not words.
- Converting very large integers to floats can cause **precision loss**.
- `int("3.5")` raises a **ValueError**.
- Converting scalars like `int` directly into `list` or `tuple` raises a **TypeError**.
- Edge cases were not fully explored:
  - Scientific notation strings
  - Nested iterables
  - Empty conversions

### Overall Evaluation

The AI output was approximately **80% accurate**, but required testing and clarification.

### Improvements Needed

- Add explicit notes on **exceptions**
- Document **precision limitations**
- Clarify **string-to-bool behavior**
- Include more comprehensive **edge case coverage**
