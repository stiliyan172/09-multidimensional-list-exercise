rows, cols = [int(el) for el in input().split()]

matrix = []
for row_index in range(rows):
    matrix.append([])
    for col_index in range(cols):
        element = chr(row_index + 97) + chr(row_index + col_index + 97) + chr(row_index + 97)
        matrix[row_index].append(element)

for row in matrix:
    print(" ".join(row))