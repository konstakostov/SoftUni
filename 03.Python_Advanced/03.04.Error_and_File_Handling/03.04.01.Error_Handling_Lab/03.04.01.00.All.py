# # 01. So Many Exceptions
# numbers_list = [int(x) for x in input().split(", ")]
#
# result = 1
#
# for i in range(len(numbers_list)):
#     number = numbers_list[i]
#     if number <= 5:
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
#
# print(result)
#


# # 02. Repeat Text
# text = input()
#
# try:
#     times = int(input())
#     print(text * times)
# except ValueError:
#     print("Variable times must be an integer")
#


# # 03. Value Cannot Be Negative
# class ValueCannotBeNegative(Exception):
#     """Number is below zero"""
#     pass
#
#
# for _ in range(5):
#     number = int(input())
#     if number < 0:
#         raise ValueCannotBeNegative()
#
