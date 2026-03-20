
import numpy as np
import time

# ── Q1: Vectorized rewrite ────────────────────────────────────────────────
# Original slow code:
#   for i in range(len(data)):
#       for j in range(len(data[0])):
#           result.append(data[i][j] ** 2 + 2 * data[i][j] + 1)
#
# x² + 2x + 1 = (x + 1)²  — algebraic simplification + single vectorized op

data = np.random.default_rng(42).standard_normal((1000, 1000))

t0 = time.perf_counter()
result_loop = []
for i in range(len(data)):
    for j in range(len(data[0])):
        result_loop.append(data[i][j] ** 2 + 2 * data[i][j] + 1)
result_loop = np.array(result_loop).reshape(data.shape)
loop_ms = (time.perf_counter() - t0) * 1000

t0 = time.perf_counter()
result_vec = (data + 1) ** 2
np_ms = (time.perf_counter() - t0) * 1000

print(f"Loop:     {loop_ms:.1f} ms")
print(f"NumPy:    {np_ms:.1f} ms")
print(f"Speedup:  ~{loop_ms / np_ms:.0f}x")
print("Results match:", np.allclose(result_loop, result_vec))


# ── Q2: k Nearest Neighbors (NumPy only) ─────────────────────────────────

def k_nearest(data: np.ndarray, point: np.ndarray, k: int) -> np.ndarray:
    """Return indices of k closest points to 'point' in 'data'.

    Args:
        data:  (n, 2) array of 2D points
        point: (2,) query point
        k:     number of neighbours

    Returns:
        (k,) array of indices, sorted nearest-first
    """
    dists = np.sqrt(((data - point) ** 2).sum(axis=1))
    return np.argsort(dists)[:k]

pts = np.array([[1,2],[3,4],[0,0],[5,5],[2,3]], dtype=float)
q   = np.array([2.0, 2.0])
print("\nk_nearest result:", k_nearest(pts, q, 3))   # → [0 4 1]


# ── Q3: Fixed column normalisation ───────────────────────────────────────
# Bug 1: axis=1 computes row-wise mean  → should be axis=0 (column-wise)
# Bug 2: axis=1 computes row-wise std   → should be axis=0
# Bug 3: (data - means) shape mismatch  → (100,) can't broadcast vs (100,5)
#         fixed automatically once axis=0 gives shape (5,)

raw   = np.random.default_rng(0).standard_normal((100, 5))
means = raw.mean(axis=0)                 # (5,) — one mean per column
stds  = raw.std(axis=0)                  # (5,) — one std per column
normalized = (raw - means) / stds        # (100,5) - (5,) / (5,) — correct broadcast

print("\nColumn means after normalisation:", normalized.mean(axis=0).round(3))
print("Column stds  after normalisation:", normalized.std(axis=0).round(3))
