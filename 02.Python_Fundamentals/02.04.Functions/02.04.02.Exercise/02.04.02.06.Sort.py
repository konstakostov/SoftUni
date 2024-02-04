def sort_num(num_input):
    sorted_nums = sorted(num_input)
    return sorted_nums


num_list = [int(i) for i in input().split()]

print(sort_num(num_list))
