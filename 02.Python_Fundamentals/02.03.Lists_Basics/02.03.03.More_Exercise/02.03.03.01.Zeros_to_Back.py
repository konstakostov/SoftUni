num_string = list(map(int, input().split(", ")))

for el in num_string:
    element = 0

    if el == 0:
        element = el
        num_string.remove(el)
        num_string.append(element)

print(num_string)
