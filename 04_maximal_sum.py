rows, cols = [int(el) for el in input().split()]
matr = []

for _ in range(rows):
    matr.append([int(el) for el in input().split()])

max_sum = -999
max_matrix = []
number_of_equal_el_matrices = 0
for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matr[row][col] + matr[row][col + 1] + matr[row][col + 2] + \
                      matr[row + 1][col] + matr[row + 1][col + 1] + matr[row + 1][col + 2] + \
                      matr[row + 2][col] + matr[row + 2][col + 1] + matr[row + 2][col + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            best_row = row
            best_col = col

print(f'Sum = {max_sum}')
print(f'{matr[best_row][best_col]} {matr[best_row][best_col + 1]} {matr[best_row][best_col + 2]}')
print(f'{matr[best_row + 1][best_col]} {matr[best_row + 1][best_col + 1]} {matr[best_row + 1][best_col + 2]}')
print(f'{matr[best_row + 2][best_col]} {matr[best_row + 2][best_col + 1]} {matr[best_row + 2][best_col + 2]}')

# rows, cols = [int(el) for el in input().split()]
#
# max_sum = -999
# matrix = []
# for row in range(rows):
#     matrix.append([int(el) for el in input().split()])
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
#                       matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
#                       matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
#         if current_sum > max_sum:
#             max_sum = current_sum
#             max_matrix = [
#                 [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
#                 [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
#                 [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
#                  ]
#
# print(f'Sum = {max_sum}')
# for row in max_matrix:
#     print(" ".join([str(el) for el in row]))
#
