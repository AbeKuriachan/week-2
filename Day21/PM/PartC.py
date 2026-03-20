"""
Week 04 · Day 21 PM — Part C: Interview Ready (Coding)
Q2: calculate_mse implementation
Written answers (Q1, Q3) are in PM_PartC_InterviewReady.md
"""

import numpy as np


# ── Q2: calculate_mse ─────────────────────────────────────────────────────

def calculate_mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Mean Squared Error between true and predicted values.

    Args:
        y_true: Ground truth values, shape (n,)
        y_pred: Model predictions, shape (n,)

    Returns:
        MSE as float. Lower is better; 0 means perfect predictions.
    """
    return float(np.mean((y_true - y_pred) ** 2))


# Tests
y_true = np.array([3.0, 5.0, 2.5, 7.0])
y_pred = np.array([2.8, 5.2, 2.3, 6.5])
print(f"MSE: {calculate_mse(y_true, y_pred):.4f}")   # → 0.0875

# Perfect predictions
print("Perfect MSE:", calculate_mse(y_true, y_true))  # → 0.0

# Larger dataset
rng    = np.random.default_rng(42)
y_t    = rng.uniform(0, 10, 1000)
y_p    = y_t + rng.normal(0, 0.5, 1000)   # predictions with noise
print(f"Noisy MSE: {calculate_mse(y_t, y_p):.4f}")   # → ~0.25
