# start = input()
# end = input()
#
# start_01 = int(start[0])
# start_02 = int(start[1])
# start_03 = int(start[2])
# start_04 = int(start[3])
#
# end_01 = int(end[0])
# end_02 = int(end[1])
# end_03 = int(end[2])
# end_04 = int(end[3])
#
# for n1 in range(start_01, end_01 + 1):
#     for n2 in range(start_02, end_02 + 1):
#         for n3 in range(start_03, end_03 + 1):
#             for n4 in range(start_04, end_04 + 1):
#                 if n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0:
#                     print(f"{n1}{n2}{n3}{n4}", end=" ")

num_1 = int(input())
num_2 = int(input())

num1_digit_4 = num_1 % 10
num_1 = num_1 // 10
num1_digit_3 = num_1 % 10
num_1 = num_1 // 10
num1_digit_2 = num_1 % 10
num_1 = num_1 // 10
num1_digit_1 = num_1 % 10
num_1 = num_1 // 10

num2_digit_4 = num_2 % 10
num_2 = num_2 // 10
num2_digit_3 = num_2 % 10
num_2 = num_2 // 10
num2_digit_2 = num_2 % 10
num2_digit_1 = num_2 % 10

for digit_1 in range(num1_digit_1, num2_digit_1 + 1):
    if digit_1 % 2 == 0:
        continue
    for digit_2 in range(num1_digit_2, num2_digit_2 + 1):
        if digit_2 % 2 == 0:
            continue
        for digit_3 in range(num1_digit_3, num2_digit_3 + 1):
            if digit_1 % 2 == 0:
                continue
            for digit_4 in range(num1_digit_4, num2_digit_4 + 1):
                if digit_1 % 2 == 0:
                    continue

                print(f"{digit_1}{digit_2}{digit_3}{digit_4}", end=" ")
