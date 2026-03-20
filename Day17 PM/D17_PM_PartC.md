# Day 17 PM — Part C: Interview Ready (Written)

Code is in `D17_PM_PartC_Code.py`.

---

## Q1 — Why is the nested loop slow?

The double Python `for` loop iterates element-by-element — 1,000,000 iterations
for a 1000×1000 matrix. Each iteration carries Python interpreter overhead:
object creation, type checking, and bytecode dispatch per element.

NumPy's vectorised `(data + 1) ** 2` runs in compiled C using SIMD instructions,
operating on contiguous memory blocks — no per-element Python overhead. Typical
speedup: **~100–500× faster** on a 1000×1000 matrix.

The algebraic simplification `x² + 2x + 1 = (x+1)²` also halves the number of
operations compared to a naive translation.

---

## Q3 — Three Bugs Explained

**Bug 1 — `data.mean(axis=1)` (Line A)**
`axis=1` averages *across columns* for each row → shape `(100,)`.
We want the mean *across rows* for each column → `axis=0` → shape `(5,)`.

**Bug 2 — `data.std(axis=1)` (Line B)**
Same problem: `axis=1` gives per-row std → shape `(100,)`.
Should be `axis=0` → per-column std → shape `(5,)`.

**Bug 3 — Broadcasting failure (Line C)**
With the wrong axis, `means` has shape `(100,)`. NumPy aligns from the right:
`(100,)` vs `(100, 5)` → tries to match `100` against `5` → **ValueError**.
Fixing to `axis=0` gives shape `(5,)` which broadcasts correctly against `(100, 5)`.
