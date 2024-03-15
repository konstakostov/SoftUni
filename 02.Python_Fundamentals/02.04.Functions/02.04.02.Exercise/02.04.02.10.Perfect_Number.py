def perfect_num(num):
    num_sum = 0

    for current_num in range(1, num):
        if num % current_num == 0:
            num_sum += current_num

    return num_sum


num_input = int(input())

num_input_sum = perfect_num(num_input)

if num_input == num_input_sum:
    print("We have 04.03.01.01.Food perfect number!")
else:
    print("It's not so perfect." )
