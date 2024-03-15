def even_num(some_num):
    if some_num % 2 == 0:
        return True


num_list = [int(i) for i in input().split()]
final_list = []

result = filter(even_num, num_list)

for num in result:
    final_list.append(num)

print(final_list)
