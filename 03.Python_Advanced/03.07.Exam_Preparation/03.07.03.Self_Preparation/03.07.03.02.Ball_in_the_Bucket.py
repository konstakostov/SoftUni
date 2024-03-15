SIZE = 6

board = []
buckets = []

for i in range(SIZE):
    board.append(input().split())

points = 0

for throw in range(3):
    position = [int(x) for x in input()[1:-1].split(', ')]
    r, c = position[0], position[1]

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        continue

    if board[r][c] == "B" and [r, c] not in buckets:
        for i in range(SIZE):
            if board[i][c] != "B":
                points += int(board[i][c])

        buckets.append([r, c])


if 0 <= points <= 99:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")

