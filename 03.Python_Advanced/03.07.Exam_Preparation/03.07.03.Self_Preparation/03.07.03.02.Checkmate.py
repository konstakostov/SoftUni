def queen_movement(row_, col_):
    king_capture = False

    for direction in directions:
        r = row_ + direction[0]
        c = col_ + direction[1]

        if king_capture:
            break

        while 0 <= r < SIZE and 0 <= c < SIZE:
            if board[r][c] == "Q":
                break

            elif board[r][c] == "K":
                king_capture = True
                break

            r += direction[0]
            c += direction[1]

    return king_capture


SIZE = 8

board = []

for _ in range(SIZE):
    board.append(input().split())

directions = [
    (-1, 0),     # Up
    (1, 0),     # Down
    (0, -1),     # Left
    (0, 1),     # Right
    (-1, -1),     # Up-Left
    (-1, 1),     # Up-Right
    (1, -1),     # Down-Left
    (1, 1),     # Down-Right
]

positions = []

for row in range(SIZE):
    for col in range(SIZE):
        if board[row][col] == "Q":
            # result = []
            result = queen_movement(row, col)

            if result:
                positions.append([row, col])

if positions:
    print(*positions, sep='\n')
else:
    print("The king is safe!")
