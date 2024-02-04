# # 01. Absolute Values
# num = input().split(" ")
#
# num_dig = []
#
# for n in num:
#     num_dig.append(abs(float(n)))
#
# print(num_dig)
#
# print([abs(float(el)) for el in input().split(" ")])  # str to Float 04.10.01.03.List in 1 line
#


# # 02. Grades
# def solve(grade):
#     if 2.00 <= grade <= 2.99:
#         return "Fail"
#     elif 3.00 <= grade <= 3.49:
#         return "Poor"
#     elif 3.50 <= grade <= 4.49:
#         return "Good"
#     elif 4.50 <= grade <= 5.49:
#         return "Very Good"
#     elif 5.50 <= grade <= 6.00:
#         return "Excellent"
#
#
# gr = float(input())
#
# print(solve(gr))
#


# # 03. Calculations
# def solve(number_1, number_2, operator):
#     result = 0
#
#     if operator == "multiply":
#         result = number_1 * number_2
#     elif operator == "divide":
#         result = number_1 // number_2
#     elif operator == "add":
#         result = number_1 + number_2
#     elif operator == "subtract":
#         result = number_1 - number_2
#
#     return result
#
#
# # # Variant 01
# # print(int(solve(int(input()), int(input()), input())))
#
# # # Variant 02
# input_operator = input()
#
# num_1 = int(input())
# num_2 = int(input())
#
# print(int(solve(num_1, num_2, input_operator)))
#


# 04. Repeat Strings
# # # Variant, 01
# def repeat(words, times):
#     return words * times
#
# # # Variant 02
# repeat = lambda 04.03.01.01.Food, b: 04.03.01.01.Food * b
#
#
# text = input()
# n = int(input())
#
# result = repeat(text, n)
# print(result)
#


# # 05. Orders
# def menu(item, amount):
#     final_sum = 0
#
#     if item == "coffee":
#         final_sum = 1.50 * amount
#     elif item == "water":
#         final_sum = 1.0 * amount
#     elif item == "coke":
#         final_sum = 1.40 * amount
#     elif item == "snacks":
#         final_sum = 2.00 * amount
#
#     return final_sum
#
#
# item_input = input()
# amount_input = int(input())
#
# result = menu(item_input, amount_input)
#
# print(f"{result:.2f}")
#


# # 06. Calculate Rectangle Area
# def rectangle_area(width, height):
#     area = width * height
#     return area
#
#
# width_input = int(input())
# height_input = int(input())
#
# area_total = rectangle_area(width_input, height_input)
#
# print(area_total)
#


# 07. Rounding
# num_list = input().split()
#
# num_digits = []
#
# for i in num_list:
#     num_digits.append(round(float(i)))
#
# print(num_digits)
#
