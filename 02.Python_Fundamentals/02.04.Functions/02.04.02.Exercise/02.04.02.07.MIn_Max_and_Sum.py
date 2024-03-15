def min_max_sum(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    sum_num = sum(numbers)

    return max_num, min_num, sum_num


num_list = [int(i) for i in input().split()]

max_number, min_number, total_sum = min_max_sum(num_list)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {total_sum}")
