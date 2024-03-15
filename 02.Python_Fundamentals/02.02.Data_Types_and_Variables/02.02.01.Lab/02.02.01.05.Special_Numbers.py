# # Version 01
# n = int(input())
#
# for num in range(1, n + 1):
#     str_num = str(num)
#
#     sum_of_digits = 0
#     digits = 0
#
#     for char in str_num:
#         digits = int(char)
#         sum_of_digits += digits
#
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")
#


# # Version 02
# n = int(input())
#
# for num in range(1, n + 1):
#     sum_of_digits = 0
#     digits = num
#
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits / 10)
#
#     if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")
#
