# for i in range(1, 101):
#     print(i)
#
#
# num = int(input())
#
# for i in range(1, num + 1, 3):
#     print(i)

# num = int(input())
#
# result = 1
#
# for i in range(0, num + 1, 2):
#     result = pow(2, i)
#     print(result)


# num = int(input())
#
# for i in range(num, 0, -1):
#     print(i)


# text = input()
#
# for i in text:
#     print(i)


# text = input()
#
# 04.03.01.01.Food, e, i, o, u = 0, 0, 0, 0, 0
#
# letter_sum = 0
#
# for letter in text:
#
#     if letter == "04.03.01.01.Food":
#         04.03.01.01.Food += 1
#     elif letter == "e":
#         e += 2
#     elif letter == "i":
#         i += 3
#     elif letter == "o":
#         o += 4
#     elif letter == "u":
#         u += 5
#
# letter_sum = 04.03.01.01.Food + e + i + o + u
#
# print(letter_sum)


# n = int(input())
#
# num_sum = 0
#
# for i in range(1, n + 1):
#     num = int(input())
#
#     num_sum += num
#
# print(num_sum)

# import sys
#
# n = int(input())
#
# max_num = -sys.maxsize
# min_num = sys.maxsize
#
# for _ in range(1, n + 1):
#     num = int(input())
#
#     if num > max_num:
#         max_num = num
#
#     if num < min_num:
#         min_num = num
#
# print(f"Max number: {max_num}")
# print(f"Min number: {min_num}")


# n = int(input())
#
# left_sum = 0
# right_sum = 0
#
# for _ in range(1, n + 1):
#     num = int(input())
#
#     left_sum += num
#
# for _ in range(1, n + 1):
#     num = int(input())
#
#     right_sum += num
#
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     print(f"No, diff = {abs(left_sum - right_sum)}")


n = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
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
