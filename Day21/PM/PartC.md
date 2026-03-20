# Week 04 · Day 21 PM — Part C: Interview Ready (Written Answers)

Code for Q2 is in `PM_PartC_Code.py`.

---

## Q1 — Regression vs Classification: Real-World Examples

**Regression** predicts a continuous quantity.

| Problem | Input | Output |
|---------|-------|--------|
| House price | area, location | ₹73,50,000 |
| Weather forecast | pressure, humidity | 34.2°C |
| Stock price | historical data | ₹2,341.80 |

**Classification** assigns a discrete label from a fixed set.

| Problem | Input | Output |
|---------|-------|--------|
| Email spam | email text | spam / not-spam |
| Medical diagnosis | symptoms | disease / healthy |
| Image recognition | pixel values | cat / dog / car |

Key distinction: if the target can take any value between two numbers → regression.
If it belongs to one of a fixed set of classes → classification.

---

## Q3 — Bias-Variance Tradeoff

**Total error = Bias² + Variance + Irreducible noise**

**Underfitting (high bias):** model is too simple, makes systematic errors.
Train error high, test error high. Fix: more complex model or more features.

**Overfitting (high variance):** model memorises training noise, fails on new data.
Train error low, test error high. Fix: regularisation, more data, early stopping.

**Optimal model:** minimises test error — found by plotting train vs validation
error across model complexities and picking the valley in the test error curve.
