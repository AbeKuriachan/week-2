# Day 17 PM — Part B: Linear Algebra (Written)

Code is in `D17_PM_PartB_LinearAlgebra.py`.

---

## What is `np.linalg.svd()` and where is it used in ML?

SVD (Singular Value Decomposition) decomposes any matrix `A` into three matrices:
`A = U @ diag(s) @ Vt`, where `U` and `Vt` are orthogonal and `s` contains the
singular values ranked by magnitude.

In ML, SVD is the backbone of **PCA** (Principal Component Analysis) — by keeping
only the top-k singular values you approximate the original data in a lower-dimensional
space while retaining most variance. It is also central to **collaborative filtering**
in recommendation systems (Netflix, Spotify), where the user-item rating matrix is
decomposed to reveal latent factors connecting users to items.

SVD is preferred over eigendecomposition because it works on any rectangular matrix,
not just square ones, making it universally applicable to real-world datasets where
samples ≠ features.
