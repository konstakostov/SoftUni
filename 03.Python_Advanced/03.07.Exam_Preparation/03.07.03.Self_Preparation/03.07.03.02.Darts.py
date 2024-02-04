from collections import deque

SIZE = 7

board = []

players = deque([x for x in input().split(', ')])

player_one = players[0]
points_one = 501
turns_one = 0

player_two = players[-1]
points_two = 501
turns_two = 0

for _ in range(SIZE):
    board.append(input().split())

while True:
    player = players[0]

    coordinates = [int(x) for x in input()[1:-1].split(', ')]

    r = coordinates[0]
    c = coordinates[1]

    if 0 <= r < SIZE and 0 <= c < SIZE:
        if board[r][c] == "D":
            if player == player_one:
                points_one -= (int(board[0][c]) + int(board[-1][c]) + int(board[r][0]) + int(board[r][-1])) * 2
            elif player == player_two:
                points_two -= (int(board[0][c]) + int(board[-1][c]) + int(board[r][0]) + int(board[r][-1])) * 2

        elif board[r][c] == "T":
            if player == player_one:
                points_one -= (int(board[0][c]) + int(board[-1][c]) + int(board[r][0]) + int(board[r][-1])) * 3
            elif player == player_two:
                points_two -= (int(board[0][c]) + int(board[-1][c]) + int(board[r][0]) + int(board[r][-1])) * 3

        elif board[r][c] == "B":
            if player == player_one:
                turns_one += 1
                print(f"{player} won the game with {turns_one} throws!")
            elif player == player_two:
                turns_two += 1
                print(f"{player} won the game with {turns_two} throws!")

            raise SystemExit

        else:
            if player == player_one:
                points_one -= int(board[r][c])
            elif player == player_two:
                points_two -= int(board[r][c])

    if player == player_one:
        turns_one += 1
    elif player == player_two:
        turns_two += 1

    if player == player_one and points_one <= 0:
        print(f"{player} won the game with {turns_one} throws!")
        raise SystemExit

    elif player == player_two and points_two <= 0:
        print(f"{player} won the game with {turns_two} throws!")
        raise SystemExit

    players.rotate(1)
