# # 01. Which Are In?, Version 01
# first_list = input().split(", ")
# second_list = input().split(", ")
#
# substring = []
#
# for first in first_list:
#     for second in second_list:
#         if first in second and first not in substring:
#             substring.append(first)
#             break
#
# print(substring)
#

# # 01. Which Are In?, Version 02
# first_list = input().split(", ")
# second_list = input().split(", ")
#
# substring = [first for first in first_list if any(first in second for second in second_list)]
#
# print(substring)
#


# # 02. Next Version
# version = [int(number) for number in input().split(".")]
#
# version[-1] += 1
#
# for index in range(len(version) - 1, -1, -1):
#     if version[index] > 9:
#         version[index] = 0
#
#         if (index - 1) >= 0:
#             version[index - 1] += 1
#
# print(".".join(str(number) for number in version))
#


# # 03. Word Filter
# words = input().split(" ")
#
# result = [word for word in words if len(word) % 2 == 0]
#
# print("\n".join(result))
#


# # 04. Number Classification
# def positive(some_num):
#     return [pos for pos in some_num if int(pos) >= 0]
#
#
# def negative(some_num):
#     return [neg for neg in some_num if int(neg) < 0]
#
#
# def even(some_num):
#     return [ev for ev in some_num if int(ev) % 2 == 0]
#
#
# def odd(some_num):
#     return [od for od in some_num if int(od) % 2 != 0]
#
#
# num = input().split(", ")
#
#
# print(f"Positive: {', '.join(positive(num))}")
# print(f"Negative: {', '.join(negative(num))}")
# print(f"Even: {', '.join(even(num))}")
# print(f"Odd: {', '.join(odd(num))}")
#


# # 05. Office Chairs, Version 01
# n_rooms = int(input())
#
# not_filled_rooms = 0
# chairs_left = 0
#
# for room in range(1, n_rooms + 1):
#     chairs, visitors = input().split()
#     chairs_count = len(chairs)
#
#     if chairs_count >= int(visitors):
#         chairs_left += (chairs_count - int(visitors))
#         not_filled_rooms += 1
#     else:
#         print(f"{int(visitors) - chairs_count} more chairs needed in room {room}")
#
# if not_filled_rooms == n_rooms:
#     print(f"Game On, {chairs_left} free chairs left")
#
# # 05. Office Chairs, Version 02
# def room_check(room_num):
#     free_chairs = 0
#     needed_chairs = 0
#
#     for room in range(1, room_num + 1):
#         chairs, visitors = input().split()
#         difference = len(chairs) - int(visitors)
#
#         if difference >= 0:
#             free_chairs += difference
#         else:
#             needed_chairs += abs(difference)
#             print(f"{abs(difference)} more chairs needed in room {room}")
#
#     return free_chairs, needed_chairs
#
#
# num_rooms = int(input())
#
# free_chairs_total, needed_chairs_total = room_check(num_rooms)
#
# if free_chairs_total >= needed_chairs_total:
#     print(f"Game On, {free_chairs_total} free chairs left")
#



