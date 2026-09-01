A = [[1, 2],[3, 4]]
a = A[0][0]
b = A[0][1]
c = A[1][0]
d = A[1][1]
print("Matrix:")
for row in A:
    print(row)
det = a * d - b * c
print("\nDeterminant =", det)
if det != 0:
    rank = 2
elif a == 0 and b == 0 and c == 0 and d == 0:
    rank = 0
else:
    rank = 1
print("Rank =", rank)
if det != 0:
    inverse = [
        [d / det, -b / det],
        [-c / det, a / det]
    ]
    print("\nInverse:")
    for row in inverse:
        print(row)
else:
    print("\nInverse does not exist.")
