rows, cols = [int(x) for x in input().split()]

num_square_matrices = 0

matrix = []

for i in range(rows):
    matrix.append([x for x in input().split()])

for i in range(rows-1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            num_square_matrices += 1

print(num_square_matrices)
