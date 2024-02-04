sequence = input().split()
total_sum = 0

for current_string in sequence:
    first_letter = current_string[0]
    number_str = ""
    last_letter = current_string[-1]
    for i in range(len(current_string)):
        if current_string[i].isnumeric():
            number_str += current_string[i]
    number = int(number_str)

    if first_letter.isupper():
        number /= (ord(first_letter) - 90 + 26)
    elif first_letter.islower():
        number *= (ord(first_letter) - 122 + 26)

    if last_letter.isupper():
        number -= (ord(last_letter) - 90 + 26)
    elif last_letter.islower():
        number += (ord(last_letter) - 122 + 26)

    total_sum += number

print(f"{total_sum:.2f}")
