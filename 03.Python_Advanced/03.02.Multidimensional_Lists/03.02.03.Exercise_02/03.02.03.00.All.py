# # 01. Flatten Lists, Version 01
# line = input().split("|")
#
# sub_lists = []
#
# for sub_string in line[::-1]:
#     sub_lists.extend(sub_string.split())
#
# print(*sub_lists)

# # # 01. Flatten Lists, Version 02
# line = [sub_string.split() for sub_string in input().split("|")]
# print(*[''.join(sub_list) for sub_list in line[::-1]])
#


# # 02. Matrix Modification
# size = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(size)]
#
# while True:
#     command = input().split()
#
#     if command[0] == "END":
#         break
#
#     action = command[0]
#     row = int(command[1])
#     col = int(command[2])
#     value = int(command[3])
#
#     if not (0 <= row < size and 0 <= col < size):
#         print("Invalid coordinates")
#     elif command[0] == "Add":
#         matrix[row][col] += value
#     elif command[0] == "Subtract":
#         matrix[row][col] -= value
#
# [print(*row) for row in matrix]
#


# # 03. Knight Game
# size = int(input())
# matrix = [list(input()) for _ in range(size)]
#
# positions = (
#     (-2, -1),   # Up 2, Left 1
#     (-2, 1),    # Up 2, Right 1
#     (-1, -2),   # Up 1, Left 2
#     (-1, 2),    # Up 1, Right 2
#     (2, 1),     # Down 2, Right 1
#     (2, -1),    # Down 2, Left 1
#     (1, 2),     # Down 2, Right 1
#     (1, -2),    # Down 2, Left 1
# )
# removed_knights = 0
#
# while True:
#     max_attacks = 0
#     knight_max_attacks_pos = []
#
#     for row in range(size):
#         for col in range(size):
#             if matrix[row][col] == "K":
#                 attacks = 0
#
#                 for pos in positions:
#                     pos_row = row + pos[0]
#                     pos_col = col + pos[1]
#
#                     if 0 <= pos_row < size and 0 <= pos_col < size:
#                         if matrix[pos_row][pos_col] == "K":
#                             attacks += 1
#
#                 if attacks > max_attacks:
#                     knight_max_attacks_pos = [row, col]
#                     max_attacks = attacks
#
#     if knight_max_attacks_pos:
#         matrix[knight_max_attacks_pos[0]][knight_max_attacks_pos[1]] = "0"
#         removed_knights += 1
#     else:
#         break
#
# print(removed_knights)
#


# 04. Easter Bunny


# 05. Alice in Wonderland


# # 06. Range Day
# def move(direction, steps):
#     r = my_position[0] + (directions[direction][0] * steps)
#     c = my_position[1] + (directions[direction][1] * steps)
#
#     if not (0 <= r < SIZE and 0 <= c < SIZE):
#         return my_position
#
#     if field[r][c] == 'x':
#         return my_position
#
#     return r, c
#
#
# def shoot(direction):
#     r = my_position[0] + directions[direction][0]
#     c = my_position[0] + directions[direction][1]
#
#     while 0 <= r < SIZE and 0 <= c < SIZE:
#         if field[r][c] == 'x':
#             field[r][c] = '.'
#             return [r, c]
#
#         r += directions[direction][0]
#         c += directions[direction][1]
#
#
# SIZE = 5
# field = []
#
# targets = 0
# targets_hit = 0
# targets_hit_positions = []
#
# my_position = []
#
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1)
# }
#
#
# for row in range(SIZE):
#     field.append(input().split())
#
#     if 'A' in field[row]:
#         my_position = [row, field[row].index('A')]
#
#     targets += field[row].count('x')
#
# for _ in range(int(input())):
#     command_info = input().split()
#
#     if command_info[0] == "move":
#         my_position = move(command_info[1], int(command_info[2]))
#
#     if command_info[0] == "shoot":
#         targets_down_positions = shoot(command_info[1])
#
#         if targets_down_positions:
#             targets_hit_positions.append(targets_down_positions)
#             targets_hit += 1
#
#         if targets_hit == targets:
#             print(f"Training completed! All {targets} targets hit.")
#             break
# else:
#     print(f"Training not completed! {targets - targets_hit} targets left.")
#
# print(*targets_hit_positions, sep='\n')
#


# # 07. Present Delivery
# def eat_cookie(presents_left, nice_kids):
#     for coordinates in directions.values():
#         r = santa_position[0] + coordinates[0]
#         c = santa_position[1] + coordinates[1]
#
#         if neighbourhood[r][c].isalpha():
#             if neighbourhood[r][c] == "V":
#                 nice_kids += 1
#
#             neighbourhood[r][c] = '-'
#             presents_left -= 1
#
#         if not presents_left:
#             break
#
#     return presents_left, nice_kids
#
#
# presents = int(input())
# size = int(input())
#
# neighbourhood = []
# santa_position = []
#
# total_nice_kids = 0
# nice_kids_visited = 0
#
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1)
# }
#
# for row in range(size):
#     line = input().split()
#
#     neighbourhood.append(line)
#
#     if "S" in line:
#         santa_position = [row, line.index("S")]
#         neighbourhood[row][santa_position[1]] = '-'
#
#     total_nice_kids += line.count("V")
#
# command = input()
#
# while command != "Christmas morning":
#     santa_position = [
#         santa_position[0] + directions[command][0],
#         santa_position[1] + directions[command][1]
#     ]
#
#     house = neighbourhood[santa_position[0]][santa_position[1]]
#
#     if house == "V":
#         nice_kids_visited += 1
#         presents -= 1
#     elif house == "C":
#         presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)
#
#     neighbourhood[santa_position[0]][santa_position[1]] = '-'
#
#     if not presents or nice_kids_visited == total_nice_kids:
#         break
#
#     command = input()
#
# neighbourhood[santa_position[0]][santa_position[1]] = 'S'
#
# if not presents and nice_kids_visited < total_nice_kids:
#     print("Santa ran out of presents!")
#
# print(*[' '.join(line) for line in neighbourhood], sep='\n')
#
# if total_nice_kids == nice_kids_visited:
#     print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')
# else:
#     print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')


