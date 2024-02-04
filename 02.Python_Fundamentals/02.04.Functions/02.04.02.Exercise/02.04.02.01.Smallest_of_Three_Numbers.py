def smallest(int_1, int_2, int_3):
    minimum = min(int_1, int_2, int_3)

    return minimum


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

min_num = smallest(num_1, num_2, num_3)

print(min_num)
