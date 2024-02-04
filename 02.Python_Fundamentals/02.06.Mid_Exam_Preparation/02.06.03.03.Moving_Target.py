targets = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "End":
        print(*targets, sep="|")
        exit(0)

    command = command.split()
    action = command[0]
    index = int(command[1])

    if action == "Shoot":
        power = int(command[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] < 1:
                targets.pop(index)

    elif action == "Add":
        value = int(command[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(command[2])
        start_index = index - radius
        end_index = index + radius + 1

        if 0 <= start_index < len(targets) and 0 <= end_index < len(targets):
            targets = targets[:start_index] + targets[end_index:]
        else:
            print("Strike missed!")
