# Day 17 PM — Part D: AI-Augmented Task (Evaluation)

Code is in `D17_PM_PartD_Code.py`.

## Prompt
"Write a NumPy function that performs IQR-based outlier detection on each column
of a 2D array, replacing outliers with the column median."
Model: Claude (claude-sonnet-4-6)

## Critical Evaluation

**IQR computed per column (axis=0)?**
Yes — it slices `arr[:, col]` and calls `np.percentile` on the 1D column.
Correct result, but achieved via a loop rather than a vectorized axis call.

**In-place vs copy?**
Handled correctly. `arr.copy()` is made upfront; all replacements go into
`result`. Original array is never mutated.

**Truly vectorized?**
No — there is an explicit `for col in range(arr.shape[1])` loop.
`np.percentile` and `np.median` both accept `axis=0`, making the loop
unnecessary. Improved version in the `.py` file removes it entirely.

**Test on known outliers:**
- `data[0, 0] = 100` → replaced with column median ✓
- `data[1, 1] = -100` → replaced with column median ✓
- Constant column (all 5.0, IQR=0) → untouched ✓ — edge case handled naturally
  since no values fall outside `[5.0 - 0, 5.0 + 0]`.
