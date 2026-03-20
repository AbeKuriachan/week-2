"""
Week 04 · Day 21 AM — Part C: Interview Ready (Coding)
Q2: normalize(X) implementation
See AM_PartC_InterviewReady.md for Q1 and Q3 written answers.
"""

import numpy as np
import time


# ── Q2: normalize(X) ──────────────────────────────────────────────────────

def normalize(X: np.ndarray) -> np.ndarray:
    """Scale all values in X to [0, 1] using min-max normalization.

    Args:
        X: Input NumPy array of any shape.

    Returns:
        Array of same shape with values scaled to [0, 1].
        Returns all-zeros if X is constant (avoids division by zero).
    """
    x_min = X.min()
    x_max = X.max()
    if x_max == x_min:
        return np.zeros_like(X, dtype=float)
    return (X - x_min) / (x_max - x_min)


# Tests
X1 = np.array([2.0, 5.0, 10.0, 1.0, 8.0])
print("1D normalize:", normalize(X1).round(4))
# → [0.111 0.444 1.    0.    0.778]

X2 = np.array([[1, 2], [3, 4]], dtype=float)
print("2D normalize:\n", normalize(X2).round(4))
# → [[0.    0.333]
#    [0.667 1.   ]]

X3 = np.array([5.0, 5.0, 5.0])
print("Constant array:", normalize(X3))
# → [0. 0. 0.]  — edge case handled


# ── Q3: Vectorisation speedup demo ────────────────────────────────────────

data = np.random.default_rng(0).standard_normal(1_000_000)

t0 = time.perf_counter()
slow = [x ** 2 for x in data]
loop_ms = (time.perf_counter() - t0) * 1000

t0 = time.perf_counter()
fast = data ** 2
np_ms = (time.perf_counter() - t0) * 1000

print(f"\nLoop:  {loop_ms:.1f} ms")
print(f"NumPy: {np_ms:.1f} ms")
print(f"Speedup: ~{loop_ms / np_ms:.0f}x")
