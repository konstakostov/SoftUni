from math import floor

size = int(input())

field = []
player_pos = []

for i in range(size):
    field.append(input().split())

    if "P" in field[i]:
        player_pos = [i, field[i].index("P")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

player_path = [[player_pos[0], player_pos[1]]]
coins = 0

win = False

while True:
    command = input()

    if command not in directions:
        continue

    r = player_pos[0] + directions[command][0]
    c = player_pos[1] + directions[command][1]

    if r < 0:
        r = size - 1
    elif r >= size:
        r = 0

    if c < 0:
        c = size - 1
    elif c >= size:
        c = 0

    if field[r][c] == "X":
        coins = floor(coins / 2)
        player_path.append([r, c])
        break

    elif field[r][c] != "P" and [r, c] not in player_path:
        coins += int(field[r][c])

    if coins >= 100:
        win = True
        player_path.append([r, c])
        break

    player_path.append([r, c])
    player_pos = [r, c]

if win:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
print('\n'.join(str(pos) for pos in player_path))
