# # Basic Example; Print 10 times "Hello SoftUni"
# for i in range(1, 10):
#     print("Hello SoftUni")
#


# # Numbers from 1 to 100
# for i in range(1, 101):
#     print(i)
#


# # Numbers from 1 to N with Step 3
# n = int(input())
#
# for i in range(1, n + 1, 3):
#     print(i)
#


# # Even Powers of 2 VERSION 01
# num = int(input())
#
# for i in range(0, num + 1, 2):
#     print(pow(2, i))
#

# # Even Powers of 2 VERSION 02
# num = int(input())
#
# result = 1
#
# for i in range(0, num + 1):
#     if i % 2 == 0:
#         print(result)
#     result *=2
#

# # Even Powers of 2 VERSION 03 - DOES NOT WORK PROPERLY, MUST BE REVIEWED BY TEACHER
# num = int(input())
#
# result = 1
#
# for i in range(0, num + 1):
#     print(result)
#     result = result * 2 * 2
#


# # Numbers from N to 1 in Backwards Order
# num = int(input())
#
# for i in range(num, 0, -1):
#     print(i)
#


# # String Example
# name = "Karaibrahim Besnia"
#
# string_length = len(name)   # We take the string's length with len() function
#
# print(string_length)
#
# for i in range(0, string_length):
#     print(name[i])
#


# # Character Sequence
# string = input()
#
# for i in range(0, len(string)):
#     print(string[i])
#


# # Vowels Sum
# string = input()
#
# string_length = len(string)
#
# result = 0
#
# for i in range(0, string_length):
#     current_char = string[i]
#
#     if current_char == "04.03.01.01.Food":
#         result += 1
#     elif current_char == "e":
#         result += 2
#     elif current_char == "i":
#         result += 3
#     elif current_char == "o":
#         result += 4
#     elif current_char == "u":
#         result += 5
#
# print(result)
#


# # Sum of Numbers
# input_count = int(input())
#
# result = 0
#
# for i in range(0, input_count):
#     num = int(input())
#     result += num
#
# print(result)


# # NUmber Sequence
# input_count = int(input())
#
# max_num = 0
# min_num = 0
#
# for i in range(0, input_count):
#     num = int(input())
#     if i == 0:
#         max_num = num
#         min_num = num
#     else:
#         if num > max_num:
#             max_num = num
#         if num < min_num:
#             min_num = num
#
# print(f"Max number: {max_num}")
# print(f"Min number: {min_num}")
#


# # Left and Right Sum
# input_count = int(input())
#
# left_sum = 0
# right_sum = 0
#
# for i in range(0, input_count):
#     num = int(input())
#     left_sum += num
#
# for i in range(0, input_count):
#     num = int(input())
#     right_sum += num
#
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     print(f"No, diff = {abs(left_sum - right_sum)}")
#


# Odd Even Sum
input_count = int(input())

even_sum = 0
odd_sum = 0

for i in range(0, input_count):
    num = int(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

if even_sum == odd_sum:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    print(f"No")
    print(f"Diff = {abs(even_sum - odd_sum)}")


