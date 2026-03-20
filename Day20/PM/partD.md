# Part D — AI-Augmented Task (10%)

## 1. Prompt Given to AI

"Explain normal distribution, Z-score, and hypothesis testing with a simple Python example."

---

## 2. AI Output

### Normal Distribution
A normal distribution is a symmetric, bell-shaped distribution where most values cluster around the mean.  
It is defined by:
- Mean (μ)
- Standard deviation (σ)

---

### Z-score
Z-score standardizes a value using the formula:

Z = (X - μ) / σ

It tells how many standard deviations a value is from the mean.

---

### Hypothesis Testing
Hypothesis testing is used to make decisions about data.

- Null Hypothesis (H₀): Assumes no effect  
- Alternative Hypothesis (H₁): Assumes there is an effect  

We compute a test statistic (like Z) and compare it to a critical value.

---

### Python Example

import random
import math

# Generate data
data = []
for _ in range(100):
    data.append(random.gauss(50, 10))

# Compute mean
total = 0
for x in data:
    total += x
mean = total / len(data)

# Compute std dev
var_sum = 0
for x in data:
    var_sum += (x - mean) ** 2
variance = var_sum / len(data)
std = math.sqrt(variance)

# Z-score for a value
x = data[0]
z = (x - mean) / std

print("Mean:", mean)
print("Std Dev:", std)
print("Z-score of first value:", z)

# Hypothesis Test (H0: mean = 50)
mu_0 = 50
z_stat = (mean - mu_0) / (std / math.sqrt(len(data)))

z_critical = 1.96

if abs(z_stat) > z_critical:
    print("Reject H0")
else:
    print("Fail to reject H0")


### 3. Evaluation
Is the explanation correct?

Yes, the explanation is correct and beginner-friendly.

Normal distribution is correctly described as bell-shaped.

Z-score formula is accurate.

Hypothesis testing concepts (H₀, H₁, decision rule) are correctly explained.

### Is the code logically correct and runnable?

Yes, the code is logically correct and runnable.

Steps are properly followed:

Data generation

Mean and standard deviation calculation

Z-score computation

Hypothesis testing