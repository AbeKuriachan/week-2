"""
Week 04 · Day 21 PM — Part B: Stretch Problem
Topics: Bias-Variance Tradeoff, Polynomial Fitting, Train vs Test Error
"""

import numpy as np

rng = np.random.default_rng(42)


X       = np.linspace(0, 1, 60)
y_true  = np.sin(2 * np.pi * X)
y_noisy = y_true + rng.normal(0, 0.3, 60)

# Train / test split (first 40 train, last 20 test)
X_train, X_test = X[:40], X[40:]
y_train, y_test = y_noisy[:40], y_noisy[40:]




print(f"{'Degree':>6}  {'Train MSE':>10}  {'Test MSE':>10}  {'Behaviour'}")
print("-" * 55)

for deg in [1, 2, 3, 5, 7, 10]:
    coeffs     = np.polyfit(X_train, y_train, deg)
    train_mse  = np.mean((y_train - np.polyval(coeffs, X_train)) ** 2)
    test_mse   = np.mean((y_test  - np.polyval(coeffs, X_test))  ** 2)

    if deg <= 2:
        label = "underfitting (high bias)"
    elif deg <= 5:
        label = "good fit"
    else:
        label = "overfitting (high variance)"

    print(f"{deg:>6}  {train_mse:>10.4f}  {test_mse:>10.4f}  {label}")

# Key insight: train MSE always falls as degree rises.
# Test MSE falls then rises — the minimum is the optimal complexity.
# Degree 1: both errors high → underfitting
# Degree 5: sweet spot
# Degree 10: train error low, test error high → overfitting

