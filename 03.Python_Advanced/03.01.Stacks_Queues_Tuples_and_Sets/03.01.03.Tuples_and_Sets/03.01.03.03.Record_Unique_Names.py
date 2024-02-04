unique_names = set()

for _ in range(int(input())):
    name = input()

    if name not in unique_names:
        unique_names.add(name)

print(*unique_names, sep='\n')
