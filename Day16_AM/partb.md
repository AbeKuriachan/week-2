## Part B — Multiple Comparison Problem

### Problem

If we run multiple hypothesis tests simultaneously, the chance of observing at least one false positive increases. This is known as the **multiple comparison problem** or **p-hacking**.

Given:
- number of tests = 20  
- significance level = α = 0.05  

We want to compute the probability of **at least one false positive**.

---

### Analytical Calculation

The probability of **no false positives** in a single test is:

P(no false positive) = 1 − α

For **n independent tests**:

P(no false positives in all tests) = (1 − α)^n

Therefore:

P(at least one false positive) = 1 − (1 − α)^n

Substituting values:
P = 1 − (0.95)^20
P ≈ 0.642


Interpretation:

There is about a **64.2% chance of getting at least one false positive** when running 20 tests with α = 0.05.

---

### Simulation 

import numpy as np

alpha = 0.05
n_tests = 20
simulations = 100000

false_positive_count = 0

for _ in range(simulations):
    p_values = np.random.uniform(0,1,n_tests)
    
    if np.any(p_values < alpha):
        false_positive_count += 1

false_positive_rate = false_positive_count / simulations
false_positive_rate

## Bonferroni Correction

To control the overall false positive rate, we apply the Bonferroni correction:

α_corrected = α / n_tests

Substituting values:

α_corrected = 0.05 / 20
α_corrected = 0.0025

Now each individual test must use α = 0.0025 instead of 0.05.