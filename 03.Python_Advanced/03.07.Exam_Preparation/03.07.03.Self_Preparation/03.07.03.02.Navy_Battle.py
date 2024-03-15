size = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

sub_hits = 0
cruisers = 0

battlefield = []
sub_pos = []

for r in range(size):
    battlefield.append(list(input()))

    if "S" in battlefield[r]:
        sub_pos = [r, battlefield[r].index("S")]

battlefield[sub_pos[0]][sub_pos[1]] = "-"

while True:
    command = input()

    row = sub_pos[0] + directions[command][0]
    col = sub_pos[1] + directions[command][1]

    sub_pos = [row, col]

    if battlefield[row][col] == "*":
        sub_hits += 1
        battlefield[row][col] = "-"

    elif battlefield[row][col] == "C":
        cruisers += 1
        battlefield[row][col] = "-"

    if sub_hits == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
        battlefield[row][col] = "S"
        break

    if cruisers == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        battlefield[row][col] = "S"
        break

battlefield_final = []

for row in range(size):
    battlefield_final.append(''.join(str(x) for x in battlefield[row]))

print(*battlefield_final, sep='\n')
