'''
def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbours(row, col, matrix):
    size = len(matrix)
    neighbours = []

    # row - 1, col
    if is_inside(row - 1, col, size) and matrix[row - 1][col] > 0:
        neighbours.append([row - 1, col])
    # row + 1, col
    if is_inside(row + 1, col, size) and matrix[row + 1][col] > 0:
        neighbours.append([row + 1, col])
    # row, col - 1
    if is_inside(row, col - 1, size) and matrix[row][col - 1] > 0:
        neighbours.append([row, col - 1])
    # row, col + 1
    if is_inside(row, col + 1, size) and matrix[row][col + 1] > 0:
        neighbours.append([row, col + 1])
    # row - 1, col - 1
    if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
        neighbours.append([row - 1, col - 1])
    # row - 1, col + 1
    if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
        neighbours.append([row - 1, col + 1])
    # row + 1, col - 1
    if is_inside(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
        neighbours.append([row + 1, col - 1])
    # row + 1, col + 1
    if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
        neighbours.append([row + 1, col + 1])
    return neighbours


n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

for bomb_coords in bombs:
    bomb_row, bomb_col = [int(x) for x in bomb_coords.split(',')]

    if matrix[bomb_row][bomb_col] <= 0:
        continue

    bomb_power = matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0

    for row, col in get_neighbours(bomb_row, bomb_col, matrix):
        matrix[row][col] -= bomb_power

alive_cells = 0
alive_cells_sum = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            alive_cells_sum += el

print(f'Alive cells: {alive_cells}')
print(f'Sum: {alive_cells_sum}')

for row in matrix:
    print(*row, sep=' ')
'''

# my way
matrix_size = int(input())

matrix = []
for row_index in range(matrix_size):
    nums = matrix.append([int(el) for el in input().split()])

bomb_coordinates = []
data = input().split()
for el in data:
    bomb_coordinates.append([int(x) for x in el.split(",")])

for coordinates in bomb_coordinates:
    row = coordinates[0]
    col = coordinates[1]
    detonated_bomb = matrix[row][col]
    # right cell
    if col < matrix_size - 1:
        if matrix[row][col + 1] > 0:
            matrix[row][col + 1] -= detonated_bomb
    # down right diagonal
    if col < matrix_size - 1 and row < matrix_size - 1:
        if matrix[row + 1][col + 1] > 0:
            matrix[row + 1][col + 1] -= detonated_bomb
    # down cell
    if row < matrix_size - 1:
        if matrix[row + 1][col] > 0:
            matrix[row + 1][col] -= detonated_bomb
    # down left diagonal
    if col != 0 and row < matrix_size - 1:
        if matrix[row + 1][col - 1] > 0:
            matrix[row + 1][col - 1] -= detonated_bomb
    # left
    if col != 0:
        if matrix[row][col - 1] > 0:
            matrix[row][col - 1] -= detonated_bomb
    # up left diagonal
    if col != 0 and row != 0:
        if matrix[row - 1][col - 1] > 0:
            matrix[row - 1][col - 1] -= detonated_bomb
    # up
    if row != 0:
        if matrix[row - 1][col] > 0:
            matrix[row - 1][col] -= detonated_bomb
    # up right
    if row != 0 and col < matrix_size - 1:
        if matrix[row - 1][col + 1] > 0:
            matrix[row - 1][col + 1] -= detonated_bomb
    matrix[row][col] = 0

alive_cells = []

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells.append(el)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in matrix:
    print(" ".join([str(el) for el in row]))