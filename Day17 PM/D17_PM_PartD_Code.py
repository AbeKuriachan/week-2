"""
Day 17 PM — Part D: AI-Augmented Task
Prompt: "Write a NumPy function that performs IQR-based outlier detection on
        each column of a 2D array, replacing outliers with the column median."
Model: Claude (claude-sonnet-4-6)
Evaluation in D17_PM_PartD_AIAugmented.md
"""

import numpy as np

# ── AI Output (pasted verbatim) ───────────────────────────────────────────

def iqr_outlier_replace(arr: np.ndarray) -> np.ndarray:
    """Replace IQR-based outliers in each column with the column median.

    Args:
        arr: 2D NumPy array of shape (n_samples, n_features)

    Returns:
        New array with outliers replaced (original unchanged).
    """
    result = arr.copy()
    for col in range(arr.shape[1]):          # loops over columns — not vectorized
        col_data        = arr[:, col]
        q1, q3          = np.percentile(col_data, [25, 75])
        iqr             = q3 - q1
        lower           = q1 - 1.5 * iqr
        upper           = q3 + 1.5 * iqr
        median          = np.median(col_data)
        mask            = (col_data < lower) | (col_data > upper)
        result[mask, col] = median
    return result


# ── Test on data with known outliers ─────────────────────────────────────
rng  = np.random.default_rng(42)
data = rng.standard_normal((100, 3))
data[0, 0]  =  100.0     # extreme high outlier in col 0
data[1, 1]  = -100.0     # extreme low  outlier in col 1
data[:, 2]  =    5.0     # constant column — no outliers (IQR = 0)

result = iqr_outlier_replace(data)

print("Outlier [0,0] replaced?", abs(result[0, 0]) < 10)     # → True
print("Outlier [1,1] replaced?", abs(result[1, 1]) < 10)     # → True
print("Constant col unchanged?", np.all(result[:, 2] == 5.0))# → True
print("result[0,0]:", round(result[0, 0], 4))                 # column median


# ── Improved version — fully vectorized (no column loop) ─────────────────

def iqr_outlier_replace_v2(arr: np.ndarray) -> np.ndarray:
    """IQR outlier replacement — fully vectorized, no column loop."""
    result  = arr.copy()
    q1      = np.percentile(arr, 25, axis=0)   # (n_features,)
    q3      = np.percentile(arr, 75, axis=0)   # (n_features,)
    iqr     = q3 - q1
    lower   = q1 - 1.5 * iqr
    upper   = q3 + 1.5 * iqr
    median  = np.median(arr, axis=0)           # (n_features,)
    mask    = (arr < lower) | (arr > upper)    # (n_samples, n_features)
    result[mask] = np.broadcast_to(median, arr.shape)[mask]
    return result

result_v2 = iqr_outlier_replace_v2(data)
print("\nV2 matches V1:", np.allclose(result, result_v2))
