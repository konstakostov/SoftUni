wagons_count = int(input())

passengers_per_wagon = [0] * wagons_count

while True:
    command = input()

    if command == "End":
        break

    command = command.split()

    if command[0] == "add":
        passengers_per_wagon[-1] += int(command[1])
    elif command[0] == "insert":
        passengers_per_wagon[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        passengers_per_wagon[int(command[1])] -= int(command[2])

print(passengers_per_wagon)
