field_size = int(input())
coal_quantity = 0

commands = [el for el in input().split()]

matrix = []
for row_index in range(field_size):
    matrix.append([el for el in input().split()])
    for col_index in range(field_size):
        if matrix[row_index][col_index] == "e":
            end_row, end_col = row_index, col_index
        elif matrix[row_index][col_index] == "s":
            start_row, start_col = row_index, col_index
        elif matrix[row_index][col_index] == "c":
            coal_quantity += 1

game_is_on = True
for command in commands:
    if command == "up":
        if start_row > 0:
            next_row, next_col = (start_row - 1), start_col
        else:
            continue
    elif command == "down":
        if start_row < field_size - 1:
            next_row, next_col = (start_row + 1), start_col
        else:
            continue
    elif command == "right":
        if start_col < field_size - 1:
            next_row, next_col = start_row, (start_col + 1)
        else:
            continue
    elif command == "left":
        if start_col > 0:
            next_row, next_col = start_row, (start_col - 1)
        else:
            continue

    if next_row and next_col:
        if matrix[next_row][next_col] == "*":
            matrix[start_row][start_col] = "*"
            start_row, start_col = next_row, next_col

        elif matrix[next_row][next_col] == "c":
            coal_quantity -= 1
            matrix[next_row][next_col] = "*"
            start_row, start_col = next_row, next_col

        elif next_row == end_row and next_col == end_col:
            print(f"Game over! ({next_row}, {next_col})")
            game_is_on = False
            break

if game_is_on and coal_quantity > 0:
    print(f"{coal_quantity} pieces of coal left. ({next_row}, {next_col})")
if game_is_on and coal_quantity == 0:
    print(f"You collected all coal! ({next_row}, {next_col})")