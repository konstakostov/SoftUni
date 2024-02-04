list_01 = input().split(", ")
list_02 = input().split(", ")

substring = []

for elem_01 in list_01:
    for elem_02 in list_02:
        if elem_01 in elem_02 and elem_01 not in substring:
            substring.append(elem_01)

print(substring)
