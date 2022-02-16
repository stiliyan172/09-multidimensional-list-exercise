n_rows = int(input())

matrix = []

primary_diagonal = []
secondary_diagonal = []
for el in range(n_rows):
    nums = matrix.append([int(x) for x in input().split(", ")])
    primary_diagonal.append(matrix[el][el])
    secondary_diagonal.append(matrix[el][-el-1])

print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')