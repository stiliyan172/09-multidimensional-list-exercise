rows, cols = [int(el) for el in input().split()]


def is_valid_row(row_to_check, rows):
    if row_to_check.isnumeric():
        if 0 <= int(row_to_check) < rows:
            return True
    return False


def is_valid_col(col_to_check, cols):
    if col_to_check.isnumeric():
        if 0 <= int(col_to_check) < cols:
            return True
    return False


matrix = []

for row_index in range(rows):
    matrix.append([el for el in input().split(" ")])

while True:
    command = input()
    if command == "END":
        break
    data = command.split()
    if data[0] == "swap" and is_valid_row(data[1], rows) and is_valid_col(data[2], cols) and \
            is_valid_row(data[3], rows) and is_valid_col(data[4], cols):
        first_position_to_swap = matrix[int(data[1])][int(data[2])]
        second_position_to_swap = matrix[int(data[3])][int(data[4])]
        matrix[int(data[1])][int(data[2])] = second_position_to_swap
        matrix[int(data[3])][int(data[4])] = first_position_to_swap
        for row in matrix:
            print(" ".join(row))
    else:
        print("Invalid input!")
