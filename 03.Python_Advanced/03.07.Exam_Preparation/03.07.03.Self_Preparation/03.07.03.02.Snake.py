size = int(input())

matrix = []
snake_pos = []
burrows_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(size):
    matrix.append(list(input()))

    if "S" in matrix[i]:
        snake_pos = [i, matrix[i].index("S")]

    if "B" in matrix[i]:
        burrows_pos.append([i, matrix[i].index("B")])

if burrows_pos:
    burrow_one = [burrows_pos[0][0], burrows_pos[0][1]]
    burrow_two = [burrows_pos[1][0], burrows_pos[1][1]]

out_of_border = False
food = 0

while True:
    if food >= 10:
        break

    command = input()

    r = snake_pos[0] + directions[command][0]
    c = snake_pos[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        out_of_border = True
        matrix[snake_pos[0]][snake_pos[1]] = "."
        break

    matrix[snake_pos[0]][snake_pos[1]] = "."

    if matrix[r][c] == "*":
        food += 1

    elif matrix[r][c] == "B":
        if burrow_one == [r, c]:
            r = burrow_two[0]
            c = burrow_two[1]

            matrix[burrow_one[0]][burrow_one[1]] = "."

        elif burrow_two == [r, c]:
            r = burrow_one[0]
            c = burrow_one[1]

            matrix[burrow_two[0]][burrow_two[1]] = "."

    snake_pos = [r, c]
    matrix[r][c] = "S"


if out_of_border or food < 10:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {food}")

print(*[''.join(row) for row in matrix], sep="\n")
