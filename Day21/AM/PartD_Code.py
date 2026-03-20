"""
Week 04 · Day 21 AM — Part D: AI-Augmented Task
Prompt: "Explain NumPy broadcasting and vectorisation with practical Python examples."
Model: Claude (claude-sonnet-4-6)
Evaluation notes in AM_PartD_AIAugmented.md
"""

import numpy as np
import time

# ── AI Output (pasted and verified) ───────────────────────────────────────

# Example 1: Add bias vector to every row of a matrix
weights = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]], dtype=float)
bias = np.array([10, 20, 30])       # shape (3,) broadcasts to (3,3)
print("After adding bias:\n", weights + bias)

# Example 2: Scale each column differently
scale = np.array([[2], [3], [4]])   # shape (3,1) broadcasts to (3,3)
print("\nColumn-wise scaling:\n", weights * scale)

# Example 3: Outer product without loops
a = np.array([1, 2, 3])
b = np.array([10, 20, 30, 40])
outer = a[:, np.newaxis] * b        # (3,1) * (4,) → (3,4)
print("\nOuter product:\n", outer)

# Example 4: Loop vs vectorised timing
data = np.random.default_rng(0).standard_normal(1_000_000)

t0 = time.perf_counter()
slow = [x**2 + 2*x + 1 for x in data]
loop_ms = (time.perf_counter() - t0) * 1000

t0 = time.perf_counter()
fast = (data + 1) ** 2              # algebraic simplification: (x+1)^2
np_ms = (time.perf_counter() - t0) * 1000

print(f"\nLoop time : {loop_ms:.1f} ms")
print(f"NumPy time: {np_ms:.1f} ms")
print(f"Speedup   : {loop_ms / np_ms:.0f}x")

# Example 5: Boolean masking (vectorised filtering)
scores = np.array([45, 72, 58, 90, 33, 81])
passed = scores[scores >= 60]
print("\nPassing scores:", passed)  # → [72 90 81]

# ── My addition: demonstrate broadcasting failure ──────────────────────────
a = np.ones((3, 4))
b = np.ones((3,))
try:
    _ = a + b
except ValueError as e:
    print("\nBroadcasting failed (expected):", e)
# Shape (3,4) vs (3,): (3,) aligns to last dim 4, but 3 ≠ 4 and neither is 1
