input_string = input()
dictionary = {}

for char in input_string:
    if char == " ":
        continue

    if char not in dictionary:
        dictionary[char] = 0

    dictionary[char] += 1

for char, occurrences in dictionary.items():
    print(f"{char} -> {occurrences}")
