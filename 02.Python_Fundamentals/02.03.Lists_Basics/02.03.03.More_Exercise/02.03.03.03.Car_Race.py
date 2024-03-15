# Version 01
times = list(map(int, input().split()))

finish_line = len(times) // 2
left_car = times[0:finish_line]
right_car = times[finish_line + 1::]
right_car.reverse()

left_time = 0
right_time = 0

for time in left_car:
    if time != 0:
        left_time += int(time)
    else:
        left_time *= 0.80

for time in right_car:
    if time != 0:
        right_time += int(time)
    else:
        right_time *= 0.80

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
elif right_time < left_time:
    print(f"The winner is right with total time: {right_time:.1f}")

# # Version 02
# num_seq = input().split(" ")
#
# num_seq_digit = []
#
# for i in num_seq:
#     num_seq_digit.append(int(i))
#
# cars_time = len(num_seq_digit) // 2
#
# finish_time = num_seq_digit[cars_time]
# left_car = num_seq_digit[0:cars_time]
# right_car = num_seq_digit[cars_time + 1::]
# right_car.reverse()
#
# left_time = 0
# right_time = 0
#
# for current_index in range(len(left_car)):
#     left_time += int(left_car[current_index])
#     if left_car[current_index] == 0:
#         left_time *= 0.80
#
#     right_time += int(right_car[current_index])
#     if right_car[current_index] == 0:
#         right_time *= 0.80
#
# if left_time < right_time:
#     print(f"The winner is left with total time: {left_time:.1f}")
# elif right_time < left_time:
#     print(f"The winner is right with total time: {right_time:.1f}")
#
