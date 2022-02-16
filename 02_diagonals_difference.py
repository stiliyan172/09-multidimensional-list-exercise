n_rows = int(input())

matrix = []

primary_diagonal = []
secondary_diagonal = []
for el in range(n_rows):
    nums = matrix.append([int(x) for x in input().split()])
    primary_diagonal.append(matrix[el][el])
    secondary_diagonal.append(matrix[el][-el-1])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))