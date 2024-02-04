from collections import deque

SIZE = 6
maze = []

turns = deque(input().split(', '))

for row in range(SIZE):
    maze.append(input().split())

tom_break = 0
jerry_break = 0

while True:
    player = turns[0]

    input_pos = input()

    r = int(input_pos[1])
    c = int(input_pos[4])

    if player == "Tom" and tom_break == 1:
        tom_break = 0
        turns.rotate()
        continue
    if player == "Jerry" and jerry_break == 1:
        jerry_break = 0
        turns.rotate()
        continue

    if maze[r][c] == "E":
        print(f"{player} found the Exit and wins the game!")
        raise SystemExit

    elif maze[r][c] == "T":
        print(f"{player} is out of the game! The winner is {turns[-1]}.")
        raise SystemExit

    elif maze[r][c] == "W":
        print(f"{player} hits a wall and needs to rest.")
        if player == "Tom":
            tom_break += 1
        elif player == "Jerry":
            jerry_break += 1

    turns.rotate()

