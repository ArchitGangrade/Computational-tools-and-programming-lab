import numpy as np
A = [
    [4, 1],
    [2, 3]
]
print("\tUSING NUMPY\t")
A_numpy = np.array(A, dtype=float)
eigenvalues, eigenvectors = np.linalg.eig(A_numpy)
print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)

print("\n\tWITHOUT NUMPY\t")
def matrix_vector_multiply(A, v):
    result = []

    for i in range(len(A)):
        total = 0

        for j in range(len(A[0])):
            total += A[i][j] * v[j]

        result.append(total)

    return result
def normalize(v):
    largest = max(abs(x) for x in v)

    if largest == 0:
        return v

    return [x / largest for x in v]
def power_method(A, iterations=100):
    n = len(A)

    v = [1.0] * n

    for _ in range(iterations):
        w = matrix_vector_multiply(A, v)
        v = normalize(w)

    Av = matrix_vector_multiply(A, v)

    for i in range(n):
        if abs(v[i]) > 1e-10:
            eigenvalue = Av[i] / v[i]
            break
    return eigenvalue, v
eigenvalue, eigenvector = power_method(A)

print("Dominant Eigenvalue:")
print(eigenvalue)

print("\nCorresponding Eigenvector:")
print(eigenvector)
