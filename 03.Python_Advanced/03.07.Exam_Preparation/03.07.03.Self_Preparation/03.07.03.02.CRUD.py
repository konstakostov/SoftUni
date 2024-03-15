def movement(action, info):
    r = position[0] + directions[info[0]][0]
    c = position[1] + directions[info[0]][1]

    if action == "Create":
        if matrix[r][c] == ".":
            matrix[r][c] = info[1]

    elif action == "Update":
        if matrix[r][c] != ".":
            matrix[r][c] = info[1]

    elif action == "Delete":
        if matrix[r][c] != ".":
            matrix[r][c] = "."

    elif action == "Read":
        if matrix[r][c] != ".":
            print(matrix[r][c])

    return [r, c]


SIZE = 6

matrix = []

for row in range(SIZE):
    matrix.append(input().split())

position = list(input())
position = [int(position[1]), int(position[4])]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command, *data = input().split(', ')

    if command == "Stop":
        break

    position = movement(command, data)

print(*[' '.join(row) for row in matrix], sep="\n")
