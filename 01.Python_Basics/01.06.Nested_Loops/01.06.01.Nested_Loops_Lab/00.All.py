# # CLOCK
# for h in range(0, 24):
#     for m in range(0, 60):
#         print(f"{h}:{m}")
#
#
# # CLOCK, VARIANT FOR SELF
# for h in range(24):
#     for m in range(60):
#
#         if h < 10:
#             hours = '0' + str(h)
#         else:
#             hours = h
#
#         if m < 10:
#             minutes = '0' + str(m)
#         else:
#             minutes = m
#
#         print(f"{hours}:{minutes}")
#
#
# # MULTIPLICATION TABLE
# for n1 in range(1, 11):
#     for n2 in range(1, 11):
#         product = n1 * n2
#         print(f"{n1} * {n2} = {product}")
#
#
# # COMBINATIONS
# n = int(input())
#
# combinations_count = 0
#
# for x1 in range(0, n + 1):
#     for x2 in range(0, n + 1):
#         for x3 in range(0, n + 1):
#             if x1 + x2 + x3 == n:
#                 combinations_count += 1
#
# print(combinations_count)
#
#
# # SUM OF TWO NUMBERS
# start = int(input())
# end = int(input())
# magic = int(input())
#
# counter = 0
#
# num_found = False
#
# for x1 in range(start, end + 1):
#     if num_found:
#         break
#     for x2 in range(start, end + 1):
#         counter += 1
#         if x1 + x2 == magic:
#             print(f"Combination N:{counter} ({x1} + {x2} = {magic})")
#             num_found = True
#             break
#
# if not num_found:
#     print(f"{counter} combinations - neither equals {magic}")
#
#
# # TRAVELING
# money = 0
#
# while True:
#     destination = input()
#     if destination == "End":
#         break
#     trip_cost = float(input())
#     while True:
#         deposit = float(input())
#         money += deposit
#         if money >= trip_cost:
#             print(f"Going to {destination}!")
#             money = 0
#             break
#
#
# # BUILDING
# floor = int(input())
# rooms = int(input())
#
# for i in range(floor, 0, -1):
#     for j in range(0, rooms):
#         if i == floor:
#             print(f"L{i}{j} ", end="")
#             continue
#         if i % 2 == 0:
#             print(f"O{i}{j} ", end="")
#             continue
#         else:
#             print(f"A{i}{j} ", end="")
#     print("")
#
#
# # BONUS TASKS #01
# cards = "AKQJT98765432"
#
# colors = "CSHD"
#
# for i in range(0, len(colors)):
#     for j in range(0, len(cards)):
#         print(f"{cards[j]}{colors[i]}")
#
# # BONUS TASK 02
# for digit_1 in range(10):
#     for digit_2 in range(10):
#         if digit_1 == digit_2:
#             continue
#         for digit_3 in range(10):
#             if digit_2 == digit_3 or digit_1 == digit_3:
#                 continue
#             for digit_4 in range(10):
#                 if digit_1 == digit_4 or digit_2 == digit_4 or digit_3 == digit_4:
#                     continue
#                 for digit_5 in range(10):
#                     if digit_1 == digit_5 or digit_2 == digit_5 or digit_3 == digit_5 or \
#                             digit_4 == digit_5:
#                         continue
#                     print(f"{digit_1}{digit_2}{digit_3}{digit_4}{digit_5}")
#
