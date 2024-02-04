numbers_string = input().split()

inverted_string = []

for index in numbers_string:
    num = int(index)

    inverted_string.append(-num)

print(inverted_string)
