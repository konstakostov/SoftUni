string = input()

string_length = len(string)

result = 0

for i in range(0, len(string)):
    current_char = string[i]

    if current_char == "04.03.01.01.Food":
        result += 1
    elif current_char == "e":
        result += 2
    elif current_char == "i":
        result += 3
    elif current_char == "o":
        result += 4
    elif current_char == "u":
        result += 5

print(result)
