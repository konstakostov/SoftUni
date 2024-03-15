# # 01.Number Definer
# num = float(input())
#
# if num == 0:
#     print("zero")
#
# if num > 0:
#     if num < 1:
#         print("small positive")
#     elif num > 1000000:
#         print("large positive")
#     else:
#         print("positive")
# else:
#     if abs(num) < 1:
#         print("small negative")
#     elif abs(num) > 1000000:
#         print("large negative")
#     else:
#         print("negative")
#


# # 02. Largest of Three
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# # # 02. Largest of Three, Version 01
# # if num1 > num2 and num1 > num3:
# #     print(num1)
# # elif num2 > num1 and num2 > num3:
# #     print(num2)
# # else:
# #     print(num3)
#
# # # 02. Largest of Three, Version 02
# print(max(num1, num2, num3))
#


# # 03. Word Reverse
# word = input()
#
# # # 03. Word Reverse, Version 01
# # reverse = ""
# # for i in range(len(word) - 1, -1, -1):
# #     reverse += word[i]
# # print(reverse)
#
# # # 03. Word Reverse, Version 02
# # for i in range(len(word) - 1, -1, -1):
# #     print(word[i], end='')
#
# # # 03. Word Reverse, Version 03
# # print(word[::-1])
#


# 04. Even Numbers
# n = int(input())
#
# # # 04. Even Numbers, Version 01
# all_nums_are_even = True
#
# for _ in range(n):
#     num = int(input())
#     if num % 2 != 0:
#         all_nums_are_even = False
#         print(f"{num} is odd!")
#         break
#
# if all_nums_are_even:
#     print("All numbers are even.")
#
#
# # 04. Even Numbers, Version 02
# for _ in range(n):
#     num = int(input())
#     if num % 2 != 0:
#         print(f"{num} is odd!")
#         break
# else:
#     print("All numbers are even.")
#


# # 05. Number Between 1 and 100
# num = float(input())
#
# while num < 1 or num > 100:
#     num = float(input())
# print(f"The number {num} is between 1 and 100")
#


# # 06. Shopping
# budget = int(input())
#
# spent = 0
#
# while spent <= budget:
#     command = input()
#
#     if command == "End":
#         print("You bought everything you needed")
#         exit()
#
#     receipt = int(command)
#     spent += receipt
#
# print("You went in overdraft!")
#


# # 07. Patterns
# num = int(input())
#
# for i in range(1, num + 1):
#     for j in range(0, i):
#         print('*', end='')
#     print()
#
# for i in range(num - 1, 0, -1):
#     for j in range(0, i):
#         print('*', end='')
#     print()
#
