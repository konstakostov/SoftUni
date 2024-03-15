first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

for _ in range(int(input())):
    command, sequence, *data = input().split()

    if command == "Add" and sequence == "First":
        [first.add(int(x)) for x in data]
    elif command == "Add" and sequence == "Second":
        [second.add(int(x)) for x in data]
    elif command == "Remove" and sequence == "First":
        [first.discard(int(x)) for x in data]
    elif command == "Remove" and sequence == "Second":
        [second.discard(int(x)) for x in data]
    elif command == "Check":
        if first.issubset(second) or second.issubset(first):
            print(True)
        else:
            print(False)

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
