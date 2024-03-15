# # 01. Christmas Elves
# from collections import deque
#
# elves = deque([int(x) for x in input().split()])
# boxes = deque([int(x) for x in input().split()])
#
# toys = 0
# energy = 0
# index = 0
#
# while elves and boxes:
#     elf = elves.popleft()
#     box = boxes[-1]
#
#     if elf < 5:
#         continue
#
#     index += 1
#     current_toys = 0
#
#     if index % 3 == 0:
#         box *= 2
#         current_toys += 1
#
#     if elf >= box:
#         energy += box
#         elf -= box
#
#         if index % 5 != 0:
#             elf += 1
#             current_toys += 1
#         else:
#             current_toys = 0
#
#         boxes.pop()
#
#     else:
#         elf *= 2
#         current_toys = 0
#
#     toys += current_toys
#
#     elves.append(elf)
#
# print(f"Toys: {toys}")
# print(f"Energy: {energy}")
#
# if elves:
#     print(f"Elves left: {', '.join(str(x) for x in elves)}")
#
# if boxes:
#     print(f"Boxes left: {', '.join(str(x) for x in boxes)}")
#


# # 02. Pawn Wars
# SIZE = 8
#
# board = []
# positions = [[], []]     # 0 - White, 1 - Black
#
#
# def save_positions(search_for, index_to_save, r):
#     if search_for in board[r]:
#         positions[index_to_save].append(r)
#         positions[index_to_save].append(board[r].index(search_for))
#
#
# for row in range(SIZE):
#     board.append(input().split())
#
#     save_positions("w", 0, row)
#     save_positions("b", 1, row)
#
# if abs(positions[0][1] - positions[1][1]) != 1:
#     if SIZE - positions[0][0] - 1 <= positions[1][0]:
#         print(f"Game over! Black pawn is promoted to 04.03.01.01.Food queen at {chr(97 + positions[1][1])}1.")
#     else:
#         print(f"Game over! White pawn is promoted to 04.03.01.01.Food queen at {chr(97 + positions[0][1])}8.")
# else:
#     place = (positions[0][0] + positions[1][0]) // 2
#
#     if positions[0][0] % 2 == positions[1][0] % 2:
#         print(f"Game over! Black win, capture on {chr(97 + positions[0][1])}{SIZE - place}.")
#     else:
#         print(f"Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - place}.")
#


# # 03. Words Sorting
# def words_sorting(*words):
#     dictionary = {word: sum(map(ord, word)) for word in words}
#
#     if sum(dictionary.values()) % 2 != 0:
#         return '\n'.join([f"{w} - {s}" for w, s in sorted((dictionary.items()), key=lambda x: -x[1])])
#     else:
#         return '\n'.join([f"{w} - {s}" for w, s in sorted((dictionary.items()), key=lambda x: x[0])])
#
#
# print(words_sorting('escape',
#                     'charm',
#                     'mythology'
#                     ))
#
# print(words_sorting('escape',
#                     'charm',
#                     'eye'
#                     ))
#
# print(words_sorting('cacophony',
#                     'accolade',
#                     ))
#
