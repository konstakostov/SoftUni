def sum_numbers(int_1, int_2):
    sum_num = int_1 + int_2
    return sum_num


def subtract(sum_nums, int_3):
    sub_num = sum_nums - int_3
    return sub_num


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

sum_result = sum_numbers(num_1, num_2)
sub_result = subtract(sum_result, num_3)

print(sub_result)
