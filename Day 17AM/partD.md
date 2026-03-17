# Day 17 | AM Session — Part D: AI-Augmented Task

---

## 1. Exact Prompt

> "Write a NumPy function that performs min-max normalization on a 2D array,
> scaling each column to [0, 1] range."

**Model used:** Claude (claude-sonnet-4-6)

---

## 2. AI Output

```python
import numpy as np

def minmax_normalize(arr: np.ndarray) -> np.ndarray:
    """
    Perform min-max normalization on a 2D array, scaling each column to [0, 1].

    Args:
        arr: 2D NumPy array of shape (n_samples, n_features)

    Returns:
        Normalized array with each column scaled to [0, 1] range
    """
    col_min = arr.min(axis=0)
    col_max = arr.max(axis=0)
    return (arr - col_min) / (col_max - col_min)
```

---

## 3. Critical Evaluation

**Edge case — constant column (all same values):**
`col_max - col_min` becomes `0`, producing `nan` via float division or raising
`ZeroDivisionError` on integer arrays. The AI output does not handle this at all —
it's the most obvious edge case and it's completely missing.

**Vectorization:**
Fully vectorized. `min` and `max` along `axis=0` return shape `(n_features,)`,
and the arithmetic broadcasts correctly against `arr` shape `(n_samples, n_features)`.
No hidden loops.

**Broadcasting:**
Used correctly. `col_min` and `col_max` are both `(n_features,)`, which broadcast
against `(n_samples, n_features)` along axis 0 without any reshape needed.

**What I'd improve:**
Handle the zero-range column using `np.where` — same one-liner pattern as `row_normalize`.
A constant column has no spread to normalize, so returning all zeros is the sensible default.

---

## 4. Improved Version

```python
import numpy as np

def minmax_normalize(arr: np.ndarray) -> np.ndarray:
    """Min-max scale each column to [0, 1]. Constant columns return all zeros."""
    col_min = arr.min(axis=0)
    col_range = arr.max(axis=0) - col_min
    safe_range = np.where(col_range == 0, 1, col_range)
    return np.where(col_range == 0, 0, (arr - col_min) / safe_range)
```

**Verification:**
```python
data = np.array([[1.0, 5.0, 3.0],
                 [2.0, 5.0, 6.0],
                 [3.0, 5.0, 9.0]])

print(minmax_normalize(data))
# [[0.  0.  0. ]
#  [0.5 0.  0.5]   <- constant column (all 5s) returns 0, not nan
#  [1.  0.  1. ]]
```

The only change from the AI version is two extra lines using `np.where` —
the function stays fully vectorized with correct broadcasting throughout.