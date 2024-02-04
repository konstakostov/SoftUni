from collections import deque

water = int(input())

people = deque()

while True:
    name = input()

    if name == "Start":
        break

    people.append(name)

while True:
    command = input()

    if command == "End":
        break

    if command.isdigit():
        current_person = people.popleft()

        if water - int(command) < 0:
            print(f"{current_person} must wait")
        else:
            water -= int(command)
            print(f"{current_person} got water")
    else:
        water += int(command.split()[1])

print(f"{water} liters left")
