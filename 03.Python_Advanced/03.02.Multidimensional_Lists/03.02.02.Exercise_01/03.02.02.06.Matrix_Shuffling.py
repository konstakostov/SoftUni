def valid_indices(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and \
        {indices[1], indices[3]}.issubset(valid_columns)


def swap_indices(command, indices):
    if valid_indices(indices) and command == "swap" and len(indices) == 4:
        row1, col1, row2, col2 = indices

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(r) for r in matrix], sep='\n')
    else:
        print("Invalid input!")


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_columns = range(columns)

while True:
    command_type, *data = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == "END":
        break

    swap_indices(command_type, data)
