numbers_list = input().split()
numbers_list_as_digits = []

for num in numbers_list:
    numbers_list_as_digits.append(int(num))

num_to_remove = int(input())

for i in range(num_to_remove):
    numbers_list_as_digits.remove(min(numbers_list_as_digits))

print(*numbers_list_as_digits, sep=", ")
