
import numpy as np

# ── Task 1: Matrix operations ─────────────────────────────────────────────
A = np.array([[2, 1, 3],
              [1, 4, 2],
              [3, 2, 5]], dtype=float)

det = np.linalg.det(A)
print(f"Determinant: {det:.4f}")               # → 3.0

A_inv = np.linalg.inv(A)
print("A_inv:\n", A_inv.round(4))
print("A @ A_inv == I:", np.allclose(A @ A_inv, np.eye(3)))   # → True

eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues:", eigvals.round(4))        # → [8.0732  0.133  2.7937]


# ── Task 2: Solve 2x + 3y = 8,  4x + y = 10 ─────────────────────────────
Aeq = np.array([[2, 3],
                [4, 1]], dtype=float)
b   = np.array([8, 10], dtype=float)

sol = np.linalg.solve(Aeq, b)
print(f"\nSolution: x={sol[0]:.4f}, y={sol[1]:.4f}")   # → x=2.20, y=1.20
print("Verify Aeq @ sol == b:", np.allclose(Aeq @ sol, b))



# ── Task 3: SVD explanation → see D17_PM_PartB_LinearAlgebra.md ──────────
U, s, Vt = np.linalg.svd(A)
print(f"\nSVD singular values: {s.round(4)}")
print("Reconstructed A matches:", np.allclose(U @ np.diag(s) @ Vt, A))
