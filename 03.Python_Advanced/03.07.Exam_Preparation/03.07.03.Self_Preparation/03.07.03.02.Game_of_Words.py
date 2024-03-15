text = input()
size = int(input())

matrix = []
player_pos = []

for i in range(size):
    matrix.append(list(input()))

    if "P" in matrix[i]:
        player_pos = [i, matrix[i].index("P")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for j in range(int(input())):
    matrix[player_pos[0]][player_pos[1]] = "-"

    command = input()

    r = player_pos[0] + directions[command][0]
    c = player_pos[1] + directions[command][1]

    if 0 <= r < size and 0 <= c < size:
        if matrix[r][c] != "-":
            text += matrix[r][c]

        player_pos = [r, c]
        matrix[r][c] = "P"

    else:
        if len(text) > 0:
            text = text[:-1]

        matrix[player_pos[0]][player_pos[1]] = "P"

print(text)

print(*[''.join(row) for row in matrix], sep="\n")
