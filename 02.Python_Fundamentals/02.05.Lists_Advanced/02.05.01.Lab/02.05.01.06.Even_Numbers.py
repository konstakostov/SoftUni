input_numbers = list(map(int, input().split(", ")))

even_indices = [index for index in range(len(input_numbers)) if input_numbers[index] % 2 == 0]

print(even_indices)
