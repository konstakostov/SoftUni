rows, columns = [int(x) for x in input().split(', ')]

matrix = []
coordinates = []

collectibles = 0
number_of_decoration = 0
number_of_gifts = 0
number_of_cookies = 0

for i in range(rows):
    matrix.append(input().split())

    if "Y" in matrix[i]:
        coordinates = [i, matrix[i].index("Y")]

    collectibles += matrix[i].count("D")
    collectibles += matrix[i].count("G")
    collectibles += matrix[i].count("C")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix[coordinates[0]][coordinates[1]] = "x"

while collectibles > 0:
    commands = input()
    if commands == "End":
        matrix[coordinates[0]][coordinates[1]] = "Y"
        break

    command = commands.split('-')[0]
    steps = commands.split('-')[1]

    for _ in range(int(steps)):
        row = coordinates[0] + directions[command][0]
        col = coordinates[1] + directions[command][1]

        if row < 0:
            row += rows
        elif row >= rows:
            row -= rows

        if col < 0:
            col += columns
        elif col >= columns:
            col -= columns

        if matrix[row][col] == "D":
            number_of_decoration += 1
            collectibles -= 1

        elif matrix[row][col] == "G":
            number_of_gifts += 1
            collectibles -= 1

        elif matrix[row][col] == "C":
            number_of_cookies += 1
            collectibles -= 1

        matrix[row][col] = "x"
        coordinates = [row, col]

        if collectibles <= 0:
            matrix[coordinates[0]][coordinates[1]] = "Y"
            break

if collectibles == 0:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {number_of_decoration} Christmas decorations")
print(f"- {number_of_gifts} Gifts")
print(f"- {number_of_cookies} Cookies")

matrix_final = []

for j in range(rows):
    matrix_final.append(' '.join(str(x) for x in matrix[j]))

print(*matrix_final, sep='\n')
