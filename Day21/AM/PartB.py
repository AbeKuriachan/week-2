"""
Week 04 · Day 21 AM — Part B: Stretch Problem
Topics: Matrix Operations, Linear Equations, Performance Benchmarking
"""

import numpy as np
import time

# ── 1. Matrix Operations ──────────────────────────────────────────────────

A = np.array([[2, 1, 3],
              [1, 4, 2],
              [3, 2, 5]], dtype=float)

B = np.array([[1, 0],
              [2, 1],
              [0, 3]], dtype=float)

print("=== Matrix Operations ===")
print("A @ B:\n", A @ B)
print("A Transpose:\n", A.T)
print("det(A):", round(np.linalg.det(A), 4))

A_inv = np.linalg.inv(A)
print("A_inv:\n", A_inv.round(4))
print("A @ A_inv == I:", np.allclose(A @ A_inv, np.eye(3)))


# ── 2. Solve System of Linear Equations ──────────────────────────────────
# 2x + 3y = 8
# 4x +  y = 10

print("\n=== Linear System: 2x+3y=8, 4x+y=10 ===")
Aeq = np.array([[2, 3],
                [4, 1]], dtype=float)
b   = np.array([8, 10], dtype=float)

sol = np.linalg.solve(Aeq, b)
print(f"Solution: x={sol[0]:.4f}, y={sol[1]:.4f}")
print("Verify Aeq @ sol == b:", np.allclose(Aeq @ sol, b))


# ── 3. Performance: Python Loop vs NumPy ──────────────────────────────────

N   = 10_000_000
arr = np.ones(N)

print(f"\n=== Performance Benchmark (N={N:,}) ===")

t0 = time.perf_counter()
_ = sum(arr)                    # Python built-in — iterates in Python
loop_ms = (time.perf_counter() - t0) * 1000

t0 = time.perf_counter()
_ = arr.sum()                   # NumPy — compiled C with SIMD
np_ms = (time.perf_counter() - t0) * 1000

print(f"Python sum : {loop_ms:.1f} ms")
print(f"NumPy sum  : {np_ms:.1f} ms")
print(f"Speedup    : {loop_ms / np_ms:.1f}x")

# Why: Python loops carry per-element interpreter overhead (type checks,
# object allocation). NumPy calls pre-compiled C with SIMD vectorisation,
# operating on contiguous memory — no per-element Python overhead.
