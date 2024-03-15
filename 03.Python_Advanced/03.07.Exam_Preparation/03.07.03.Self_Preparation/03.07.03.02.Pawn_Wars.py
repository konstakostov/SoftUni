def starting_positions(player, index, row):
    if player in board[row]:
        positions[index].append(row)
        positions[index].append(board[row].index(player))


SIZE = 8

board = []
positions = [[], []]    # White, Black

for i in range(SIZE):
    board.append(input().split())

    starting_positions("w", 0, i)
    starting_positions("b", 1, i)

if abs(positions[0][1] - positions[1][1]) != 1:
    if positions[0][0] <= SIZE - positions[1][0] - 1:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + positions[0][1])}8.")
    else:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + positions[1][1])}1.")
else:
    square = (positions[0][0] + positions[1][0]) // 2

    if positions[0][0] % 2 != positions[1][0] % 2:
        print(f"Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - square}.")
    else:
        print(f"Game over! Black win, capture on {chr(97 + positions[0][1])}{SIZE - square}.")
