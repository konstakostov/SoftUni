def movement(direction):
    r = rover[0] + directions[direction][0]
    c = rover[1] + directions[direction][1]

    if r < 0:
        r += SIZE
    elif r >= SIZE:
        r -= SIZE

    if c < 0:
        c += SIZE
    elif c >= SIZE:
        c -= SIZE

    return [r, c]


SIZE = 6

water = 0
metal = 0
concrete = 0

matrix = []
rover = []

for i in range(SIZE):
    matrix.append(input().split())

    if "E" in matrix[i]:
        rover = [i, matrix[i].index("E")]

commands = input().split(", ")
index = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while index < len(commands):
    command = commands[index]
    rover = movement(command)

    row, col = rover[0], rover[1]

    if matrix[row][col] == "W":
        water += 1
        print(f"Water deposit found at ({row}, {col})")

    elif matrix[row][col] == "M":
        metal += 1
        print(f"Metal deposit found at ({row}, {col})")

    elif matrix[row][col] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({row}, {col})")

    elif matrix[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

    index += 1

if water >= 1 and metal >= 1 and concrete >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")





SIZE = 6

matrix = []
rover_pos = []

for row in range(SIZE):
    matrix.append(input().split())

    if "E" in matrix[row]:
        rover_pos = [row, matrix[row].index("E")]

commands = input().split(', ')

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

for command in commands:
    r = rover_pos[0] + directions[command][0]
    c = rover_pos[1] + directions[command][1]

    if r < 0:
        r += SIZE
    elif r >= SIZE:
        r -= SIZE

    if c < 0:
        c += SIZE
    elif c >= SIZE:
        c -= SIZE

    if matrix[r][c] == "W":
        print(f"Water deposit found at ({r}, {c})")
        water_deposit += 1

    elif matrix[r][c] == "M":
        print(f"Metal deposit found at ({r}, {c})")
        metal_deposit += 1

    elif matrix[r][c] == "C":
        print(f"Concrete deposit found at ({r}, {c})")
        concrete_deposit += 1

    elif matrix[r][c] == "R":
        print(f"Rover got broken at ({r}, {c})")
        break

    rover_pos = [r, c]


if water_deposit >= 1 and metal_deposit >= 1 and concrete_deposit >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
