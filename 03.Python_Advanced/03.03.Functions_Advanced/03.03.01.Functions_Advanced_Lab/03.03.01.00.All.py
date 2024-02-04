# # 01. Multiplication Function
# def multiply(*args):
#     res = 1
#
#     for num in args:
#         res *= num
#
#     return res
#
#
# # print(multiply(1, 4, 5))
# # print(multiply(4, 5, 6, 1, 3))
# # print(multiply(2, 0, 1000, 5000))
#


# # 02. Person Info
# def get_info(name, town, age):
#     return f"This is {name} from {town} and he is {age} years old"
#
#
# # print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
#


# # 03. Cheese Showcase
# def sorting_cheeses(**kwargs):
#     result = ""
#
#     sorted_cheeses = sorted(kwargs.items(),
#                             key=lambda kvp: (-len(kvp[1]), kvp[0]))
#
#     for cheese_name, quantity in sorted_cheeses:
#         result += cheese_name + "\n"
#         reversed_quantities = sorted(quantity, reverse=True)
#         result += "\n".join(str(el) for el in reversed_quantities) + "\n"
#
#     return result
#
#
# # print(sorting_cheeses(Parmesan=[102, 120, 135],
# #                       Camembert=[100, 100, 105, 500, 430],
# #                       Mozzarella=[50, 125],))
#
# # print(sorting_cheeses(Parmigiano=[165, 215],
# #                       Feta=[150, 515],
# #                       Brie=[150, 125]))
#


# # 04. Rectangle
# def rectangle(length, width):
#     if not isinstance(length, int) or not isinstance(width, int):
#         return "Enter valid values!"
#
#     def area():
#         return length * width
#
#     def perimeter():
#         return 2 * (length + width)
#
#     return f"Rectangle area: {area()}\n" \
#            f"Perimeter area: {perimeter()}"
#
#
# # print(rectangle(2, 10))
# # print(rectangle('2', 10))
#


# # 05. Recursive Power
# def recursive_power(number, power):
#     if power == 1:
#         return number
#
#     return number * recursive_power(number, power-1)
#
#
# # print(recursive_power(2, 10))
# # print(recursive_power(10, 100))
#


# # 06. Operate, Version 01
# def operate(operator, *args):
#     def sum_nums():
#         res = 0
#         for num in args:
#             res += num
#         return res
#
#     def subtract_nums():
#         res = 0
#         for num in args:
#             res -= num
#         return res
#
#     def multiply_nums():
#         res = 1
#         for num in args:
#             res *= num
#         return res
#
#     def divide_nums():
#         res = 1
#         for num in args:
#             res /= num
#         return res
#
#     if operator == "+":
#         return sum_nums()
#     elif operator == "-":
#         return subtract_nums()
#     elif operator == "*":
#         return multiply_nums()
#     else:
#         return divide_nums()
#
#
# # print(operate("+", 1, 2, 3))
# # print(operate("*", 3, 4))
#

# # 06. Operate, Version 02
# from functools import reduce
#
#
# def operate(operator, *args):
#     if operator == "+":
#         return reduce(lambda 04.03.01.01.Food, b: 04.03.01.01.Food+b, args)
#
#     elif operator == "-":
#         return reduce(lambda 04.03.01.01.Food, b: 04.03.01.01.Food-b, args)
#
#     elif operator == "*":
#         return reduce(lambda 04.03.01.01.Food, b: 04.03.01.01.Food*b, args)
#
#     elif operator == "/":
#         return reduce(lambda 04.03.01.01.Food, b: 04.03.01.01.Food/b, args)
#
#
# # print(operate("+", 1, 2, 3))
# # print(operate("*", 3, 4))
#

# # 06. Operate, Version 03
# from functools import reduce
#
#
# def operate(operator, *args):
#     return reduce(lambda 04.03.01.01.Food, b: eval(f"{04.03.01.01.Food}{operator}{b}"), args)
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
#
