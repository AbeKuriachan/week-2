"""
Week 04 · Day 21 PM — Part A: Concept Application
Topics: Regression, Classification, MSE, Accuracy
"""

import numpy as np

rng = np.random.default_rng(42)


X_reg = rng.uniform(0, 10, 100)
y_reg = 3.5 * X_reg + 7 + rng.normal(0, 2, 100)   # true: w=3.5, b=7


w = np.cov(X_reg, y_reg)[0, 1] / np.var(X_reg)
b = y_reg.mean() - w * X_reg.mean()
y_pred_reg = w * X_reg + b

print("=== Regression ===")
print(f"Learned: w={w:.3f}, b={b:.3f}")
print(f"MSE: {np.mean((y_reg - y_pred_reg)**2):.3f}")

# --- Classification ---
X_cls  = rng.normal(0, 1, 200)
y_true = (X_cls > 0).astype(int)
scores = X_cls + rng.normal(0, 0.3, 200)
y_hat  = (scores > 0).astype(int)

print("\n=== Classification ===")
print(f"Accuracy: {np.mean(y_hat == y_true):.3f}")


# ── 3. Identify Problem Type ──────────────────────────────────────────────
# Regression:      target is continuous (house price, temperature)
# Classification:  target is discrete label (spam/not-spam, disease/healthy)
# Rule: if target can take infinitely many values → regression
#       if target belongs to a fixed set of classes → classification



def predict_linear(X: np.ndarray, w: float, b: float) -> np.ndarray:
    return w * X + b

def calculate_mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_true - y_pred) ** 2))

X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2.1, 4.0, 5.9, 8.1, 10.0])

y_hat = predict_linear(X, w=2.0, b=0.0)
print("\n=== Manual Linear Regression ===")
print("Predictions:", y_hat)
print("MSE:", round(calculate_mse(y, y_hat), 4))


scores_cls = np.array([0.2, 0.8, 0.55, 0.1, 0.9, 0.45])
y_true_cls = np.array([0, 1, 1, 0, 1, 0])

threshold  = 0.5
y_hat_cls  = (scores_cls >= threshold).astype(int)
accuracy   = np.mean(y_hat_cls == y_true_cls)

print("\n=== Manual Classification ===")
print("Predicted:", y_hat_cls)
print(f"Accuracy : {accuracy:.2f}")


# ── 6. Regression vs Classification Comparison ────────────────────────────

print("\n=== Comparison ===")
comparison = {
    "Output type"     : ("Continuous value",       "Discrete class label"),
    "Example"         : ("Predict house price",     "Detect spam email"),
    "Primary metric"  : ("MSE / RMSE / R²",         "Accuracy / F1 / AUC"),
    "Loss function"   : ("Mean Squared Error",       "Cross-Entropy"),
}
print(f"{'Aspect':<20} {'Regression':<30} {'Classification'}")
print("-" * 75)
for k, (r, c) in comparison.items():
    print(f"{k:<20} {r:<30} {c}")
