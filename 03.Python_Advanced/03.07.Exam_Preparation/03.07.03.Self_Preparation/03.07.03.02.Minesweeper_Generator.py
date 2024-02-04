def cell_number(row_, col_):
    cell_num = 0

    r = row_
    c = col_

    for direction in directions:
        r = row_ + direction[0]
        c = col_ + direction[1]

        if 0 <= r < size and 0 <= c < size:
            if matrix[r][c] == "*":
                cell_num += 1

    return cell_num


size = int(input())
bombs = int(input())

matrix = []

for i in range(size):
    matrix.append([0] * size)

for _ in range(bombs):
    position = [int(x) for x in input()[1:-1].split(', ')]
    matrix[position[0]][position[1]] = "*"

directions = [
    (-1, 0),     # Up
    (1, 0),     # Down
    (0, -1),     # Left
    (0, 1),     # Right
    (-1, -1),     # Up-Left
    (-1, 1),     # Up-Right
    (1, -1),     # Down-Left
    (1, 1),     # Down-Right
]

for row in range(size):
    for col in range(size):
        if matrix[row][col] != "*":
            matrix[row][col] = cell_number(row, col)

# print(*[' '.join(str(row) for row in matrix)], sep='\n')

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
