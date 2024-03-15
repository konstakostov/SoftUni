size = int(input())
commands = [x for x in input().split(", ")]

hazelnuts = 0
problem = False

matrix = []
squirrel = []

for _ in range(size):
    matrix.append(list(input()))

for row in range(size):
    if squirrel:
        break
    for col in range(size):
        if matrix[row][col] == "s":
            squirrel = [row, col]
            break

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(len(commands)):
    command = commands[i]

    row = squirrel[0] + directions[command][0]
    col = squirrel[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        print("The squirrel is out of the field.")
        problem = True
        break

    squirrel = [row, col]

    if matrix[row][col] == "h":
        hazelnuts += 1
        matrix[row][col] = "*"

        if hazelnuts == 3:
            break

    elif matrix[row][col] == "t":
        print("Unfortunately, the squirrel stepped on 04.03.01.01.Food trap...")
        problem = True
        break

if not problem:
    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
    else:
        print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
