def cookie(presents_left, nice_kids):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if neighbourhood[r][c].isalpha():
            if neighbourhood[r][c] == "V":
                nice_kids += 1

            neighbourhood[r][c] = '-'
            presents_left -= 1

            if not presents_left:
                break

    return presents_left, nice_kids


presents = int(input())
size = int(input())

neighbourhood = []
santa_pos = []

nice_kids_total = 0
nice_kids_visited = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    line = input().split()
    neighbourhood.append(line)

    if 'S' in neighbourhood[row]:
        santa_pos = [row, line.index("S")]
        neighbourhood[row][santa_pos[1]] = '-'

    nice_kids_total += line.count("V")

command = input()
while command != "Christmas morning":
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
    ]

    house = neighbourhood[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_visited += 1
        presents -= 1
    elif house == "C":
        presents, nice_kids_visited = cookie(presents, nice_kids_visited)

    neighbourhood[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or nice_kids_visited == nice_kids_total:
        break

    command = input()

neighbourhood[santa_pos[0]][santa_pos[1]] = "S"

if not presents and nice_kids_visited < nice_kids_total:
    print("Santa ran out of presents!")

print(*[' '.join(line) for line in neighbourhood], sep='\n')

if nice_kids_total == nice_kids_visited:
    print(f"Good job, Santa! {nice_kids_visited} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_total - nice_kids_visited} nice kid/s.")
