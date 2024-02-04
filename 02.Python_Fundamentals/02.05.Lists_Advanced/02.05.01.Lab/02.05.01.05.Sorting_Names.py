names_list = input().split(", ")

names_sorted = sorted(names_list, key=lambda x: (-len(x), x))

print(names_sorted)
