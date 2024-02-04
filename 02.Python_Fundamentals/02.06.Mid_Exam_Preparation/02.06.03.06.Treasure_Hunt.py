loot = input().split("|")

input_data = input()

while input_data != "Yohoho!":
    command, *data = [x for x in input_data.split()]

    if command == "Loot":
        for item in data:
            if item not in loot:
                loot.insert(0, item)

    elif command == "Drop":
        index = int(data[0])

        if 0 <= index < len(loot):
            loot.append(loot.pop(index))

    elif command == "Steal":
        items_to_steal = int(data[0])
        stolen_items = loot[-items_to_steal:]
        loot = loot[:-items_to_steal]
        print(*stolen_items, sep=", ")

    input_data = input()

if loot:
    average_gain = sum(len(x) for x in loot) / len(loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
