Q1

Loops are explicit and flexible but verbose.
List comprehension is concise and readable for simple transformations.
Higher-order functions (map, filter, reduce) are functional and useful when applying operations across collections.

Use:
- loops for complex logic
- list comprehension for simple transformations
- higher-order functions for functional style pipelines


Q2

def flatten_and_remove_even(lst):
    return [x for sub in lst for x in sub if x % 2 != 0]


Q3

Hypothesis testing is a statistical method to decide whether a claim is supported by data.

Null hypothesis (H0): no effect or no difference  
p-value: probability of observing data assuming H0 is true  
significance level: threshold (e.g., 0.05)

Example:
Testing if a new teaching method improves scores.
If p-value < 0.05 → reject H0