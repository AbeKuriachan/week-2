# matrix_ops.py

# 1️⃣ Matrix Addition
def matrix_add(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Matrix dimensions must match for addition.")
        return None

    return [
        [A[i][j] + B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]


# 2️⃣ Matrix Transpose
def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]


# 3️⃣ Matrix Multiplication
def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        print("Matrix dimensions incompatible for multiplication.")
        return None

    return [
        [
            sum(a * b for a, b in zip(row_a, col_b))
            for col_b in zip(*B)
        ]
        for row_a in A
    ]


# 🧪 Testing the functions
if __name__ == "__main__":

    # First test matrices
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    print("Matrix A:", a)
    print("Matrix B:", b)

    print("\nMatrix Addition:")
    print(matrix_add(a, b))

    print("\nMatrix Transpose:")
    print(matrix_transpose(a))

    print("\nMatrix Multiplication:")
    print(matrix_multiply(a, b))

    # Second test with different size matrices
    c = [[1, 2, 3], [4, 5, 6]]
    d = [[7, 8], [9, 10], [11, 12]]

    print("\nSecond Test Multiplication:")
    print(matrix_multiply(c, d))