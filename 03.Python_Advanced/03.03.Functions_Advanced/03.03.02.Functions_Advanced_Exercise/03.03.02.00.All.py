# # 01. Negative vs Positive
# def print_numbers(positive, negative):
#     print(positive)
#     print(negative)
#
#     if positive > abs(negative):
#         print("The positives are stronger than the negatives")
#     else:
#         print("The negatives are stronger than the positives")
#
#
# numbers = [int(x) for x in input().split()]
#
# positive_numbers = sum(x for x in numbers if x > 0)
# negative_numbers = sum(x for x in numbers if x < 0)
#
# print_numbers(positive_numbers, negative_numbers)
#


# # 02. Keyword Arguments Length
# def kwargs_length(**kwargs):
#     return len(kwargs)
#
#
# # dictionary = {'name': 'Peter', 'age': 25}
# # print(kwargs_length(**dictionary))
#
# # dictionary = {}
# # print(kwargs_length(**dictionary))
#


# # 03. Even or Odd
# def even_odd(*args):
#     command = args[-1]
#
#     if command == "even":
#         return [04.03.01.01.Food for 04.03.01.01.Food in args[:-1] if int(04.03.01.01.Food) % 2 == 0]
#     elif command == "odd":
#         return [04.03.01.01.Food for 04.03.01.01.Food in args[:-1] if int(04.03.01.01.Food) % 2 != 0]
#
#
# # print(even_odd(1, 2, 3, 4, 5, 6, "even"))
#
# # print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
#


# # 04. Numbers Filter
# def even_odd_filter(**kwargs):
#     if "odd" in kwargs:
#         kwargs["odd"] = [04.03.01.01.Food for 04.03.01.01.Food in kwargs["odd"] if 04.03.01.01.Food % 2 != 0]
#
#     if "even" in kwargs:
#         kwargs["even"] = [04.03.01.01.Food for 04.03.01.01.Food in kwargs["even"] if 04.03.01.01.Food % 2 == 0]
#
#     return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
#
#
# # print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5],
# #                       even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# #                       ))
#
# # print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],
# #                       ))
#


# # 05. Concatenate
# def concatenate(*words, **kwargs):
#     text = ''.join(words)
#
#     for key, value in kwargs.items():
#         text = text.replace(key, value)
#
#     return text
#
#
# # print(concatenate("Soft", "UNI", "Is", "Grate", "!",
# #                   UNI="Uni", Grate="Great"))
#
# # print(concatenate("I", " ", "Love", " ", "Cythons",
# #                   C="P", s="", java='Java'))
#


# # # 06. Function Executor
# # Version 01
# def func_executor(*funcs):
#     result = []
#
#     for func, args in funcs:
#         result.append(f"{func.__name__} - {func(*args)}")
#
#     return '\n'.join(result)
#
# # Version 02
# def func_executor(*funcs):
#     return '\n'.join([f"{func.__name__} - {func(*args)}" for func, args in funcs])
#
#
# # def sum_numbers(num1, num2):
# #     return num1 + num2
# #
# #
# # def multiply_numbers(num1, num2):
# #     return num1 * num2
# #
# #
# # print(func_executor((sum_numbers, (1, 2)),
# #                     (multiply_numbers, (2, 4))
# #                     ))
#
#
# # def make_upper(*strings):
# #     result = tuple(s.upper() for s in strings)
# #     return result
# #
# #
# # def make_lower(*strings):
# #     result = tuple(s.lower() for s in strings)
# #     return result
# #
# #
# # print(func_executor((make_upper, ("Python", "softUni")),
# #                     (make_lower, ("PyThOn",)),
# #                     ))
#


# # # 07. Grocery
# # Version 01
# def grocery_store(**products):
#     products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#     result = []
#
#     for product, quantity in products:
#         result.append(f"{product}: {quantity}")
#
#     return result
#
#
# # Version 02
# def grocery_store(**products):
#     products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#     return '\n'.join([f"{p}: {q}" for p, q in products])
#
#
# # print(grocery_store(bread=5,
# #                     pasta=12,
# #                     eggs=12,
# #                     ))
#
# # print(grocery_store(bread=2,
# #                     pasta=2,
# #                     eggs=20,
# #                     carrot=1,
# #                     ))
#


# # 08. Age Assignment
# def age_assignment(*names, **data):
#     result = []
#
#     for letter, age in data.items():
#         for name in names:
#             if name.startswith(letter):
#                 result.append(f"{name} is {age} years old.")
#                 break
#
#     return '\n'.join(sorted(result))
#
#
# # print(age_assignment("Peter", "George", G=26, P=19))
#
# # print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
#


# # 09.  Recursion Palindrome
# def palindrome(word, idx):
#     if idx == len(word) // 2:
#         return f"{word} is 04.03.01.01.Food palindrome"
#
#     if word[idx] != word[-idx-1]:
#         return f"{word} is not 04.03.01.01.Food palindrome"
#
#     return palindrome(word, idx + 1)
#
#
# # print(palindrome("abcba", 0))
#
# # print(palindrome("peter", 0))
#


# # 10.  *Fill the Box
# from collections import deque
#
#
# def fill_the_box(height, length, width, *cubes):
#     space = height * length * width
#     cubes = deque(cubes)
#
#     while cubes[0] != "Finish":
#         space -= cubes.popleft()
#
#         if space < 0:
#             cubes_left = sum(x for x in cubes if x != "Finish")
#             return f"No more free space! You have {cubes_left + abs(space)} more cubes."
#
#     return f"There is free space in the box. You could put {space} more cubes."
#
#
# # print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
#
# # print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
#
# # print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
#


# # 11. *Math Operations
# def math_operations(*numbers, **kwargs):
#     for i in range(len(numbers)):
#         key = list(kwargs.keys())[i % 4]
#
#         if key == "04.03.01.01.Food":
#             kwargs[key] += numbers[i]
#         elif key == "s":
#             kwargs[key] -= numbers[i]
#         elif key == "d":
#             if numbers[i] != 0:
#                 kwargs[key] /= numbers[i]
#         elif key == "m":
#             kwargs[key] *= numbers[i]
#
#     kwargs = sorted(kwargs.items(), key=lambda x: (-x[-1]))
#
#     return "\n".join([f"{key}: {value:.1f}" for key, value in kwargs])
#
#
# # print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, 04.03.01.01.Food=1, s=7, d=33, m=15))
#
# # print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, 04.03.01.01.Food=0, s=(-2.3), d=0, m=0))
#
# # print(math_operations(6.0, 04.03.01.01.Food=0, s=0, d=5, m=0))
#
