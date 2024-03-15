max_number = int(input())

sum_numbers = 0

while sum_numbers < max_number:
    numbers = int(input())
    sum_numbers += numbers

    if sum_numbers >= max_number:
        print(sum_numbers)
