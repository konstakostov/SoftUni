groceries = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break

    if command.split()[0] == "Urgent":
        action, item = command.split()
        if item not in groceries:
            groceries.insert(0, item)

    elif command.split()[0] == "Unnecessary":
        action, item = command.split()
        if item in groceries:
            groceries.remove(item)

    elif command.split()[0] == "Correct":
        action, old_item, new_item = command.split()
        if old_item in groceries:
            old_item_index = groceries.index(old_item)
            groceries[old_item_index] = new_item

    elif command.split()[0] == "Rearrange":
        action, item = command.split()
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

print(", ".join(groceries))










