from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar_sequence = deque(int(x) for x in input().split())
symbols = deque(x for x in input().split())

honey = 0

operations = {
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y
}

while working_bees and nectar_sequence:
    bee = working_bees.popleft()
    nectar = nectar_sequence.pop()

    if nectar > bee:
        honey += abs(operations[symbols.popleft()](bee, nectar))
    elif nectar < bee:
        working_bees.appendleft(bee)

print(f"Total honey made: {honey}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")

if nectar_sequence:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_sequence)}")
