rows, columns = [int(x) for x in input().split(',')]

matrix = []
mouse_pos = []

cheese_total = 0
cheese_eaten = 0

for rw in range(rows):
    matrix.append(list(input()))

    if "M" in matrix[rw]:
        mouse_pos = [rw, matrix[rw].index("M")]

    if "C" in matrix[rw]:
        cheese_total += matrix[rw].count("C")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    if command == "danger":
        matrix[mouse_pos[0]][mouse_pos[1]] = "M"
        print("Mouse will come back later!")
        break

    r = mouse_pos[0] + directions[command][0]
    c = mouse_pos[1] + directions[command][1]

    matrix[mouse_pos[0]][mouse_pos[1]] = "*"

    if not (0 <= r < rows and 0 <= c < columns):
        matrix[mouse_pos[0]][mouse_pos[1]] = "M"
        print("No more cheese for tonight!")
        break

    if matrix[r][c] == "C":
        cheese_eaten += 1
        matrix[r][c] = "*"

    elif matrix[r][c] == "T":
        mouse_pos = [r, c]
        matrix[r][c] = "M"
        print("Mouse is trapped!")
        break

    elif matrix[r][c] == "@":
        continue

    if cheese_eaten == cheese_total:
        mouse_pos = [r, c]
        matrix[r][c] = "M"
        print("Happy mouse! All the cheese is eaten, good night!")
        break

    mouse_pos = [r, c]
    matrix[r][c] = "M"

print(*[''.join(row) for row in matrix], sep='\n')
