input_string = input()

digits, letters, other = "", "", ""

for char in input_string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        other += char

print(f"{digits}\n{letters}\n{other}")
