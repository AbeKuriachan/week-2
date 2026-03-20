# Q1 — Difference between Normal Distribution and Standard Normal Distribution

| Feature | Normal Distribution | Standard Normal Distribution |
|--------|------------------|-----------------------------|
| Mean (μ) | Any value (e.g., 50) | Always 0 |
| Std Dev (σ) | Any positive value (e.g., 10) | Always 1 |
| Shape | Bell-shaped | Same bell shape |
| Scale | Original data scale | Standardized scale |
| Purpose | Represents real-world data | Used for comparison and analysis |

### Key Insight
- A **standard normal distribution** is just a **normalized version** of a normal distribution.
- It is obtained using the Z-score transformation.

---


# Q3 — Hypothesis Testing

## What is Hypothesis Testing?

Hypothesis testing is a statistical method used to make decisions about a population based on sample data.  
It helps determine whether there is enough evidence to support a claim.

---

## Key Concepts

### 1. Null Hypothesis (H₀)
- The default assumption  
- Assumes **no effect** or **no difference**  
- Example:  
  - H₀: The average score = 50  

---

### 2. Alternative Hypothesis (H₁ or Hₐ)
- Opposes the null hypothesis  
- Represents what we want to prove  
- Example:  
  - H₁: The average score ≠ 50  

---

### 3. p-value
- Probability of observing the result (or more extreme) **if H₀ is true**  
- Helps decide whether to reject H₀  

#### Interpretation:
- Small p-value (≤ α) → Reject H₀  
- Large p-value (> α) → Fail to reject H₀  

---

### 4. Significance Level (α)
- Threshold to decide rejection of H₀  
- Common values:
  - 0.05 (most common)
  - 0.01 (more strict)

#### Meaning:
- α = 0.05 → 5% risk of rejecting a true H₀ (Type I error)

---

## Final Decision Rule

- If p-value ≤ α → Reject H₀  
- If p-value > α → Fail to reject H₀  

---

## Final Insight

- Hypothesis testing helps make **data-driven decisions**  
- It balances evidence against uncertainty  
- Widely used in statistics, experiments, and machine learning