size = int(input())

matrix = []
bunny_pos = []

best_direction = None
best_path = []
max_eggs = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index("B")]

for direction, position in directions.items():
    row, col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1]
    ]

    path = []
    eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break

        path.append([row, col])
        eggs += int(matrix[row][col])

        row += position[0]
        col += position[1]

    if eggs >= max_eggs:
        best_direction = direction
        best_path = path
        max_eggs = eggs

print(best_direction)
print(*best_path, sep="\n")
print(max_eggs)
