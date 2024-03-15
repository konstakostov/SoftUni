# # 01. Connect Four
# from collections import deque
# from colorama import Fore
# import operator
#
#
# def print_board():
#     [print(f"{', '.join(row)} ") for row in board]
#
#
# def get_circles_count(row, col, dx, dy, operator_func):
#     current_count = 0
#
#     for i in range(1, 4):
#         new_row = operator_func(row, dx * i)
#         new_col = operator_func(col, dy * i)
#
#         if not (0 <= new_row < ROWS and 0 <= new_col < COLUMNS):
#             break
#
#         if board[new_row][new_col] != player_symbol:
#             break
#
#         current_count += 1
#
#     return current_count
#
#
# def place_circle():
#     row = 0
#
#     while row != ROWS and board[row][player_col] == "0":
#         row += 1
#
#     board[row - 1][player_col] = player_symbol
#
#     return row - 1
#
#
# def check_for_win(row, col):
#     for x, y in directions:
#         count = get_circles_count(row, col, x, y, operator.add) + get_circles_count(row, col, x, y, operator.sub) + 1
#
#         if count >= 4:
#             return True
#
#     if counter_for_draw == ROWS * COLUMNS:
#         print_board()
#         print("DRAW!")
#         raise SystemExit
#
#     return False
#
#
# ROWS, COLUMNS = 6, 7
#
# counter_for_draw = 0
#
# board = [["0"] * COLUMNS for row in range(ROWS)]
#
# player_one_symbol = Fore.GREEN + "1" + Fore.RESET
# player_two_symbol = Fore.BLUE + "2" + Fore.RESET
#
# turns = deque([[1, player_one_symbol], [2, player_two_symbol]])
#
# win = False
#
# directions = (
#     (-1, 0),     # Up
#     (0, -1),     # Left
#     (-1, -1),    # Top-Left
#     (-1, 1),     # Top-Right
# )
#
# while not win:
#     print_board()
#
#     player_number, player_symbol = turns[0]
#
#     try:
#         player_col = int(input(f"Player {player_number}, please choose 04.03.01.01.Food column: ")) - 1
#     except ValueError:
#         print(Fore.RED + f"Select 04.03.01.01.Food valid number in the range (1-{COLUMNS})" + Fore.RESET)
#         continue
#
#     if not 0 <= player_col < COLUMNS:
#         print(Fore.RED + f"Select 04.03.01.01.Food valid number in the range (1-{COLUMNS})" + Fore.RESET)
#         continue
#
#     if board[0][player_col] != "0":
#         print(Fore.RED + "No empty spaces on that column!" + Fore.RESET)
#         continue
#
#     row = place_circle()
#     counter_for_draw += 1
#     win = check_for_win(row, player_col)
#
#     turns.rotate()
#
# print_board()
# print(f"Player {turns[1][0]} wins!")


# 02. Console Tic-Tac-Toe
from collections import deque


def check_for_win():
    player_name, player_symbol = players[0]

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])
    second_diagonal_win = all([board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])

    row_win = any([all(player_symbol == pos  for pos in row) for row in board])
    cow_win = any([all(board[r][c] == player_symbol for r in range(SIZE)) for c in range(SIZE)])

    if any([first_diagonal_win, second_diagonal_win, row_win, cow_win]):
        print_board()
        print(f"{player_name} won!")

        raise SystemExit


def place_symbol(row, col):
    board[row][col] = players[0][1]

    check_for_win()
    print_board()

    if turns == SIZE * SIZE:
        print("Draw!")
        raise SystemExit

    players.rotate()


def choose_position():
    while True:
        try:
            position = int(input(f"{players[0][0]}  choose a free position in the range [1-{SIZE * SIZE}]"))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
        except ValueError:
            print(f"{players[0][0]}, please select a valid position in the range [1-9]")
            continue

        if 1 <= position <= SIZE * SIZE and board[row][col] == ' ':
            place_symbol(row, col)
        else:
            print(f"{players[0][0]}, please select a valid position in the range [1-9]")


def print_board(begin=False):
    if begin:
        print("This is the numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]

        for row in range(SIZE):
            for col in range(SIZE):
                board[row][col] = " "

    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
    player_one_name = input("Player one, please enter your name: ")
    player_two_name = input("Player two, please enter your name: ")

    while True:
        player_one_symbol = input(f"{player_one_name} would you like to play 'X' or 'O'").upper()

        if player_one_symbol not in ["X", "O"]:
            print(f"{player_one_name} please select a valid option!")
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    print_board(begin=True)
    choose_position()


SIZE = 3
turns = 0

board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, SIZE * SIZE + 1, SIZE)]
players = deque()


start()







