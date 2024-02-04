rows, columns = [int(x) for x in input().split()]

playground = []
buff_pos = []

for r in range(rows):
    playground.append(input().split())

    if "B" in playground[r]:
        buff_pos = [r, playground[r].index("B")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

moves_made = 0
touched_opponents = 0

while True:
    command = input()

    if command == "Finish":
        break

    row = buff_pos[0] + directions[command][0]
    col = buff_pos[1] + directions[command][1]

    if not (0 <= row < rows and 0 <= col < columns):
        continue

    if playground[row][col] == "O":
        continue

    elif playground[row][col] == "P":
        touched_opponents += 1
        playground[row][col] = "-"

    buff_pos = [row, col]
    moves_made += 1

    if touched_opponents == 3:
        break


print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
