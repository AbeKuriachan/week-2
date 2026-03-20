"""
Week 04 · Day 21 AM — Part A: Concept Application
Topics: Array Creation, Indexing, Broadcasting, Vectorisation
"""

import numpy as np

# ── 1. Array Creation, Indexing & Slicing ─────────────────────────────────

a1 = np.array([10, 20, 30, 40, 50])
a2 = np.arange(1, 13).reshape(3, 4)
a3 = np.arange(24).reshape(2, 3, 4)

print("=== 1D Array ===")
print("Full:", a1)
print("Slice [1:4]:", a1[1:4])
print("Last element:", a1[-1])

print("\n=== 2D Array ===")
print(a2)
print("Row 1:", a2[1])
print("Col 2:", a2[:, 2])
print("Subarray [0:2, 1:3]:\n", a2[0:2, 1:3])

print("\n=== 3D Array ===")
print("Shape:", a3.shape)
print("Block 0, Row 1, all cols:", a3[0, 1, :])
print("First col of every block:\n", a3[:, :, 0])


# ── 2. Basic Operations (No Loops) ────────────────────────────────────────

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], dtype=float)

print("\n=== Basic Operations ===")
print("A + 10:\n", A + 10)
print("A * 2:\n", A * 2)
print("A - A.T:\n", A - A.T)
print(f"Mean: {A.mean():.4f}  Variance: {A.var():.4f}  Std: {A.std():.4f}")


# ── 3. Broadcasting ────────────────────────────────────────────────────────

print("\n=== Broadcasting ===")

# (3,4) + (4,) — row vector added to every row
row = np.array([1, 2, 3, 4])
print("a2 + row (shape 4,):\n", a2 + row)

# scalar multiply
print("a2 * 3:\n", a2 * 3)

# (3,1) * (3,4) — column vector scales each row
col = np.array([[10], [20], [30]])
print("a2 * col (shape 3,1):\n", a2 * col)

# How it works: NumPy aligns shapes from the right.
# Missing dims get prepended as 1, then size-1 dims are virtually stretched.


# ── 4. Vectorised Operations ──────────────────────────────────────────────

arr = np.array([-3, -1, 0, 2, 5], dtype=float)

print("\n=== Vectorised Ops ===")
print("Square:", arr ** 2)
print("Cube:", arr ** 3)
print("Replace negatives with 0:", np.where(arr < 0, 0, arr))

normalized = (arr - arr.min()) / (arr.max() - arr.min())
print("Min-max normalized:", normalized.round(4))


# ── 5. Dataset Analysis ───────────────────────────────────────────────────

rng  = np.random.default_rng(42)
data = rng.integers(1, 100, (5, 6)).astype(float)

print("\n=== Dataset Analysis ===")
print("Data:\n", data)

flat = data.flatten()
top5 = flat[np.argsort(flat)[-5:][::-1]]
print("Top 5 values:", top5)

print("Row sums:", data.sum(axis=1))
print("Col sums:", data.sum(axis=0))

threshold = 60
idx = np.argwhere(data > threshold)
print(f"Indices where value > {threshold}:\n", idx)
