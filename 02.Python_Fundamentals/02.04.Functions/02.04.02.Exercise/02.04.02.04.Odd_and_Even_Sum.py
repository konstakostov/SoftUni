def sum_odd_even(num):
    sum_odd_digits = 0
    sum_even_digits = 0

    for digit in num:
        if int(digit) % 2 == 0:
            sum_even_digits += int(digit)
        else:
            sum_odd_digits += int(digit)

    return sum_odd_digits, sum_even_digits


num_input = input()

sum_of_odd_digits, sum_of_even_digits = sum_odd_even(num_input)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
