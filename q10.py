import numpy as np
print("Using Numpy\n")
A=np.array([[1,2],[7,5]])
B=np.array([[1,6],[4,5]])
print("Matrix A:",A,"\nMatrix B:",B)
print("\nA+B matrix is:",A+B)
print("A-B matrix is:",A-B)
print("AB=",np.matmul(A,B))
print("Transpose of A is :\n",A.transpose())
print("Without using numpy\n")
addition = [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        addition[i][j] = A[i][j] + B[i][j]
subtraction = [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        subtraction[i][j] = A[i][j] - B[i][j]
multiplication = [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            multiplication[i][j] += A[i][k] * B[k][j]
transpose_A = [[A[j][i] for j in range(2)] for i in range(2)]
print("A + B =", addition)
print("A - B =", subtraction)
print("AB =", multiplication)
print("Transpose of A =", transpose_A)

