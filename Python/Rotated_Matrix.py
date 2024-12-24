## This takes a matrix and rotates it.
## line 12 rotates it 90 degress.
## line 13 rotates it 180 degress.
## and lastly line 14 rotates it 270 degrees.

def rotated_matrix(matrix):
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_matrix [j] [3 - i - 1] = matrix[i][j]

    return rotated_matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated = rotated_matrix(matrix)
for row in rotated:
    print(row)