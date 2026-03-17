# Day 17 | AM Session — Part C: Interview Ready

---

## Q1 — Broadcasting Rules

**Real-world analogy:**
Imagine a café price board (a single column of prices) and a table of customers
each ordering different quantities. To get every customer's bill, you *stretch*
the price list across all customers — you don't rewrite the board for each person.
NumPy does exactly this: smaller arrays are "stretched" to match larger ones
without copying data.

**The 3 Formal Rules:**

1. If arrays have different numbers of dimensions, prepend `1`s to the shape of
   the smaller array until both have the same number of dimensions.
2. Dimensions of size `1` are stretched to match the corresponding dimension of
   the other array.
3. If two dimensions are not equal and neither is `1`, broadcasting fails.

**Works:**
```python
a = np.ones((3, 4))  # shape (3, 4)
b = np.ones((4,))    # shape (4,) → treated as (1, 4) → stretched to (3, 4)
(a + b).shape        # (3, 4) ✓
```

**Fails:**
```python
a = np.ones((3, 4))
b = np.ones((3,))    # shape (3,) → treated as (1, 3) → can't match dim 4
a + b                # ValueError ✗
```

---

## Q2 — Row Normalization

```python
import numpy as np

def row_normalize(arr: np.ndarray) -> np.ndarray:
    """Normalize each row to sum to 1. Zero-sum rows stay as zeros."""
    row_sums = arr.sum(axis=1, keepdims=True)
    safe_sums = np.where(row_sums == 0, 1, row_sums)
    return np.where(row_sums == 0, 0, arr / safe_sums)
```

`keepdims=True` keeps shape `(n, 1)` so division broadcasts across all columns
without any explicit reshape.

**Verification:**
```python
a = np.array([[1, 2, 3],
              [0, 0, 0],
              [4, 4, 2]], dtype=float)

print(row_normalize(a))
# [[0.167 0.333 0.5  ]
#  [0.    0.    0.   ]   <- zero row stays zero
#  [0.4   0.4   0.2  ]]
```

---

## Q3 — Debug & Fix

**Buggy code:**
```python
data = np.array([1, 2, 3, 4, 5])
mask = data > 2 and data < 5   # Line A
filtered = data[mask]
result = filtered.reshape(2, 1)
```

**Bug 1 — `and` instead of `&` (Line A)**

`and` is Python's scalar boolean operator. Applied to an array, it tries to
evaluate the whole array as a single True/False, which raises:
```
ValueError: The truth value of an array is ambiguous.
```
Fix: use element-wise `&` and wrap each condition in parentheses.

**Bug 2 — hardcoded `reshape(2, 1)`**

`(data > 2) & (data < 5)` matches `[3, 4]` — 2 elements — so `reshape(2, 1)`
happens to work here. But hardcoding `2` will silently break if the data or
mask changes. Use `-1` to let NumPy infer the size.

**Fixed:**
```python
data = np.array([1, 2, 3, 4, 5])
mask = (data > 2) & (data < 5)   # element-wise AND
filtered = data[mask]             # -> [3 4]
result = filtered.reshape(-1, 1)  # -> shape (2, 1), robust to any input
```