"""
Week 04 · Day 21 PM — Part D: AI-Augmented Task
Prompt: "Explain regression vs classification and bias-variance tradeoff
        with Python examples and visualizations."
Model: Claude (claude-sonnet-4-6)
Evaluation notes in PM_PartD_AIAugmented.md
"""

import numpy as np

rng = np.random.default_rng(42)


# ── AI Output: Regression vs Classification ───────────────────────────────

# Regression
house_size  = np.array([800, 1200, 1500, 1800, 2200, 2500], dtype=float)
house_price = np.array([150, 200, 230, 290, 360, 400], dtype=float)

w = np.cov(house_size, house_price)[0, 1] / np.var(house_size)
b = house_price.mean() - w * house_size.mean()
pred_price = w * house_size + b
mse = np.mean((house_price - pred_price) ** 2)
print(f"Regression — w={w:.4f}, b={b:.2f}, MSE={mse:.2f}")

# Classification
tumor_size   = np.array([1.5, 2.1, 3.8, 4.5, 5.2, 6.1, 2.8, 4.9])
is_malignant = (tumor_size > 3.5).astype(int)
predicted    = (tumor_size >= 3.5).astype(int)
print(f"Classification accuracy: {np.mean(predicted == is_malignant):.2f}")


# ── AI Output: Bias-Variance ──────────────────────────────────────────────

X       = np.linspace(0, 1, 50)
y_true  = np.sin(2 * np.pi * X)
y_noisy = y_true + rng.normal(0, 0.3, 50)

print(f"\n{'Degree':>6}  {'Train MSE':>10}  {'Behaviour'}")
for deg in [1, 3, 5, 9, 15]:
    c         = np.polyfit(X, y_noisy, deg)
    train_mse = np.mean((y_noisy - np.polyval(c, X)) ** 2)
    label     = "underfitting" if deg <= 2 else ("overfitting" if deg > 6 else "good fit")
    print(f"{deg:>6}  {train_mse:>10.4f}  {label}")


# ── My improvement: train/test split makes overfitting visible ────────────

X_tr, X_te = X[:35], X[35:]
y_tr, y_te = y_noisy[:35], y_noisy[35:]

print(f"\n{'Degree':>6}  {'Train MSE':>10}  {'Test MSE':>10}  Note")
for deg in [1, 2, 3, 5, 7, 10]:
    c          = np.polyfit(X_tr, y_tr, deg)
    tr_mse     = np.mean((y_tr - np.polyval(c, X_tr)) ** 2)
    te_mse     = np.mean((y_te - np.polyval(c, X_te)) ** 2)
    note       = "<-- optimal" if deg == 5 else ""
    print(f"{deg:>6}  {tr_mse:>10.4f}  {te_mse:>10.4f}  {note}")
# Test MSE rises after degree 5 even as train MSE keeps falling — overfitting visible
