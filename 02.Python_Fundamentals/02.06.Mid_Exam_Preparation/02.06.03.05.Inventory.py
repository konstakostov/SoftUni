journal = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break

    action, item = command.split(" - ")

    if action == "Collect":
        if item not in journal:
            journal.append(item)

    elif action == "Drop":
        if item in journal:
            journal.remove(item)

    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in journal:
            journal.insert(journal.index(old_item) + 1, new_item)

    elif action == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)

print(", ".join(journal))
