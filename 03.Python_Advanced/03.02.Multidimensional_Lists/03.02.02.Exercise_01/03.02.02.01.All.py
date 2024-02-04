# # 01. Diagonals
# n = int(input())
#
# matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
#
# primary = [matrix[r][r] for r in range(n)]
# secondary = [matrix[r][n - r - 1] for r in range(n)]
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")
#


# # 02. Diagonal Difference
# num = int(input())
#
# matrix = [[int(n) for n in input().split()] for row in range(num)]
#
# primary_sum = 0
# secondary_sum = 0
#
# for i in range(num):
#     primary_sum += matrix[i][i]
#     secondary_sum += matrix[i][num - i - 1]
#
# print(abs(primary_sum - secondary_sum))
#


# # 03. 2x2 Squares in Matrix
# rows, columns = [int(x) for x in input().split()]
#
# matrix = [input().split() for _ in range(rows)]
#
# equal_blocks = 0
#
# for r in range(rows - 1):
#     for c in range(columns - 1):
#         symbol = matrix[r][c]
#
#         if matrix[r + 1][c] == symbol and matrix[r][c + 1] == symbol and matrix[r + 1][c + 1] == symbol:
#             equal_blocks += 1
#
# print(equal_blocks)
#


# 04. Maximal Sum
# rows, columns = [int(x) for x in input().split()]
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# max_sum = float('-inf')
# square_matrix = []
#
# for r in range(rows - 2):
#     for c in range(columns - 2):
#         first_row = matrix[r][c:c+3]
#         second_row = matrix[r+1][c:c+3]
#         third_row = matrix[r+2][c:c+3]
#
#         current_sum = sum(first_row) + sum(second_row) + sum(third_row)
#
#         if current_sum > max_sum:
#             max_sum = current_sum
#             square_matrix = [first_row, second_row, third_row]
#
# print(f"Sum = {max_sum}")
# [print(*row) for row in square_matrix]



# # 05. Matrix of Palindromes
# rows, columns = [int(x) for x in input().split()]
#
# start = ord('04.03.01.01.Food')
#
# for r in range(start, start + rows):
#     for c in range(start, start + columns):
#         print(f"{chr(r)}{chr(r + c - start)}{chr(r)}", end=" ")
#
#     print()
#


# # 06. Matrix Shuffling
# def check_valid_indices(indices):
#     return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_columns)
#
#
# def swap_command(command, indices):
#     if check_valid_indices(indices) and command == "swap" and len(indices) == 4:
#         row1, column1, row2, column2 = indices
#
#         matrix[row1][column1], matrix[row2][column2] = matrix[row2][column2], matrix[row1][column1]
#
#         print(*[' '.join(r) for r in matrix], sep='\n')
#     else:
#         print("Invalid input!")
#
#
# rows, columns = [int(x) for x in input().split()]
#
# matrix = [input().split() for _ in range(rows)]
#
# valid_rows = range(rows)
# valid_columns = range(columns)
#
# while True:
#     command_type, *info = [int(x) if x.isdigit() else x for x in input().split()]
#
#     if command_type == "END":
#         break
#
#     swap_command(command_type, info)
#


# # 07. Snake Moves
# from collections import deque
#
# rows, columns = [int(x) for x in input().split()]
# word = list(input())
#
# word_copy = deque(word)
#
# for r in range(rows):
#     while len(word_copy) < columns:
#         word_copy.extend(word)
#
#     if r % 2 == 0:
#         print(*[word_copy.popleft() for _ in range(columns)], sep="")
#     else:
#         print(*[word_copy.popleft() for _ in range(columns)][::-1], sep="")
#


# 08. *Bombs


# 09. *Miner


# # 10. *Radioactive Mutant Vampire Bunnies
# def find_player_position():
#     for row in range(rows):
#         if "P" in matrix[row]:
#             return row, matrix[row].index("P")
#
#
# def check_valid_index(row, col, player=False):
#     global wins
#
#     if 0 <= row < rows and 0 <= col < columns:
#         return True
#     if player:
#         wins = True
#
#
# def bunnies_pos():
#     positions = []
#
#     for row in range(rows):
#         for column in range(columns):
#             if matrix[row][column] == "B":
#                 positions.append([row, column])
#
#     return positions
#
#
# def bunnies_moves(bunny_pos):
#     for row, column in bunny_pos:
#         for bunny_move in directions.values():
#             new_row, new_column = row + bunny_move[0], column + bunny_move[1]
#
#             if check_valid_index(new_row, new_column):
#                 matrix[new_row][new_column] = "B"
#
#
# def show_results(status="won"):
#     [print(*row, sep='') for row in matrix]
#     print(f"{status}: {player_row} {player_column}")
#
#     raise SystemExit
#
#
# def check_player_alive(row, column):
#     if matrix[row][column] == "B":
#         show_results("dead")
#
#
# rows, columns = [int(x) for x in input().split()]
# matrix = [list(input()) for _ in range(rows)]
#
# commands = input()
#
# wins = False
#
# directions = {
#     "U": (-1, 0),
#     "D": (1, 0),
#     "L": (0, -1),
#     "R": (0, 1),
# }
#
#
# player_row, player_column = find_player_position()
# matrix[player_row][player_column] = '.'
#
# for command in commands:
#     player_movement_row, player_movement_column = \
#         player_row + directions[command][0], player_column + directions[command][1]
#
#     if check_valid_index(player_movement_row, player_movement_column, True):
#         player_row, player_column = player_movement_row, player_movement_column
#
#     bunnies_moves(bunnies_pos())
#
#     if wins:
#         show_results()
#
#     check_player_alive(player_row, player_column)
#
