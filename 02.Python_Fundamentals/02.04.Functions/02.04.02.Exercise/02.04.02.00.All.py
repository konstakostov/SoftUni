# # 01. Smallest of Three Numbers
# def smallest_number(numbers):
#     return min(numbers)
#
#
# num_01 = int(input())
# num_02 = int(input())
# num_03 = int(input())
#
# num_all = [num_01, num_02, num_03]
#
# min_num = smallest_number(num_all)
#
# print(min_num)
#


# # 02. Add and Subtract
# def sum_numbers(first, second):
#     return first + second
#
#
# def subtract(num_sum, third):
#     return num_sum - third
#
#
# def add_and_subtract(first, second, third):
#     sum_first_second = sum_numbers(first, second)
#     result = subtract(sum_first_second, third)
#     return result
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
# print(add_and_subtract(first_number, second_number, third_number))
#


# # 03. Characters in Range
# def collected_characters(first_char, second_char):
#     characters = []
#     for current_character in range(ord(first_char) + 1, ord(second_char)):
#         characters.append(chr(current_character))
#     return characters
#
#
# char_01 = input()
# char_02 = input()
#
# result = collected_characters(char_01, char_02)
#
# print(' '.join(result))
# # print(*result)
#


# # 04. Odd and Even Sum
# def even_odd_num(numbers):
#     sum_of_odd_digits = 0
#     sum_of_even_digits = 0
#
#     for digit in numbers:
#         if int(digit) % 2 == 0:
#             sum_of_even_digits += int(digit)
#         else:
#             sum_of_odd_digits += int(digit)
#
#     return sum_of_odd_digits, sum_of_even_digits
#
#
# num = input()
#
# sum_of_odd_digits, sum_of_even_digits = even_odd_num(num)
#
# print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
#


# 05. Even Numbers


# 06. Sort


# 07. Min Max and Sum


# 08. Palindrome Integers


# # 09. Password Validator, Version 01
# def password_validation(some_password):
#     pass_is_valid = True
#
#     if len(some_password) < 6 or len(some_password) > 10:
#         print("Password must be between 6 and 10 characters")
#         pass_is_valid = False
#
#     if not some_password.isalnum():
#         print("Password must consist only of letters and digits")
#         pass_is_valid = False
#
#     digit_counter = 0
#
#     for character in some_password:
#         if character.isdigit():
#             digit_counter += 1
#
#     if digit_counter < 2:
#         print("Password must have at least 2 digits")
#         pass_is_valid = False
#
#     return pass_is_valid
#
#
# password = input()
#
# password_is_valid = password_validation(password)
# if password_is_valid:
#     print("Password is valid.")
#

# # 09. Password Validator, Version 02
# def password_validation(some_password):
#     validation = []
#
#     if len(some_password) < 6 or len(some_password) > 10:
#         validation.append("Password must be between 6 and 10 characters")
#
#     if not some_password.isalnum():
#         validation.append("Password must consist only of letters and digits")
#
#     digit_counter = 0
#
#     for character in some_password:
#         if character.isdigit():
#             digit_counter += 1
#
#     if digit_counter < 2:
#         validation.append("Password must have at least 2 digits")
#
#     return validation
#
#
# password = input()
#
# password_is_not_valid = password_validation(password)
# if len(password_is_not_valid) == 0:
#     print("Password is valid.")
# else:
#     print('\n'.join(password_is_not_valid))
#


# # 10. Perfect Number
# def is_perfect(some_number):
#     num_sum = 0
#
#     for divisor in range(1, some_number):
#         if some_number % divisor == 0:
#             num_sum += divisor
#
#     if num_sum == some_number:
#         return "We have 04.03.01.01.Food perfect number!"
#
#     return "It's not so perfect."
#
#
# num = int(input())
#
# print(is_perfect(num))
#


# # 11. * Loading Bar
# def loading_bar(num):
#     if num == 100:
#         return "100% Complete!\n[%%%%%%%%%%]"
#
#     return f"{num}% [{'%' * (num // 10)}{'.' * (10 - num // 10)}]\nStill loading."
#
#
# single_num = int(input())
#
# print(loading_bar(single_num))
#


# # 12. * Factorial Division
# def factorial(num):
#     factorial_result = 1
#
#     for current_num in range(1, num + 1):
#         factorial_result *= current_num
#
#     return factorial_result
#
#
# num_01 = int(input())
# num_02 = int(input())
#
# num_01_factorial = factorial(num_01)
# num_02_factorial = factorial(num_02)
#
# final_result = num_01_factorial / num_02_factorial
#
# print(f"{final_result:.2f}")
#
