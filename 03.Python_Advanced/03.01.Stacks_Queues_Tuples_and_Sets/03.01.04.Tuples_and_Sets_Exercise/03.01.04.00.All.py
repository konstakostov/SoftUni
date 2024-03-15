# # 01. Unique Usernames, Version 01
# num_usernames = int(input())
#
# usernames = set()
#
# for _ in range(num_usernames):
#     username = input()
#
#     usernames.add(username)
#
# print(*usernames, sep='\n')
#

# # 01. Unique Usernames, Version 02
# print(*{input() for _ in range(int(input()))}, sep='\n')
#


# # 02. Sets of Elements
# n_length, m_length = [int(num) for num in input().split()]
#
# n_set = {int(input()) for _ in range(n_length)}
# m_set = {int(input()) for _ in range(m_length)}
#
# print(*(n_set.intersection(m_set)), sep='\n')   # First version for print;
# # print(*(n_set & m_set), sep='\n')   # Second version for print;
#


# # 03. Periodic Table
# table = set()
#
# for _ in range(int(input())):
#     for el in input().split():
#         table.add(el)
#
# print(*table, sep='\n')
#


# # 04. Count Symbols
# occurrences = {}
#
# for letter in input():
#     occurrences[letter] = occurrences.get(letter, 0) + 1
#
# for letter, times in sorted(occurrences.items()):
#     print(f"{letter}: {times} time/s")
#


# # 05. Longest Intersection
# longest_intersection = set()
#
# for _ in range(int(input())):
#     first_data, second_data = [el.split(',') for el in input().split('-')]
#
#     first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
#     second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))
#
#     intersection = first_range.intersection(second_range)
#
#     if len(intersection) > len(longest_intersection):
#         longest_intersection = intersection
#
# print(f"Longest intersection is "
#       f"[{', '.join(str(x) for x in longest_intersection)}] "
#       f"with length {len(longest_intersection)}")
#


# # 06. Battle of Names
# odd_set = set()
# even_set = set()
#
# for row in range(1, int(input()) + 1):
#     ascii_sum_name = sum(ord(char) for char in input()) // row
#
#     if ascii_sum_name % 2 == 0:
#         even_set.add(ascii_sum_name)
#     else:
#         odd_set.add(ascii_sum_name)
#
# if sum(odd_set) > sum(even_set):
#     print(*odd_set.difference(even_set), sep=", ")
# else:
#     print(*odd_set.symmetric_difference(even_set), sep=', ')
#
