caribbean = {}

while True:
    command = input()
    if command == "Sail":
        break

    town, people, gold = command.split("||")

    if town not in caribbean:
        caribbean[town] = caribbean.get(town, {'people': int(people), 'gold': int(gold)})
    else:
        caribbean[town]['people'] += int(people)
        caribbean[town]['gold'] += int(gold)

while True:
    command = input()
    if command == "End":
        break

    event = command.split("=>")
    if event[0] == "Plunder":
        town = event[1]
        people = int(event[2])
        gold = int(event[3])

        caribbean[town]['people'] -= people
        caribbean[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if caribbean[town]['people'] == 0 or caribbean[town]['gold'] == 0:
            del caribbean[town]
            print(f"{town} has been wiped off the map!")

    elif event[0] == "Prosper":
        town = event[1]
        gold = int(event[2])

        if gold < 0:
            print("Gold added cannot be 04.03.01.01.Food negative number!")
            continue
        else:
            caribbean[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {caribbean[town]['gold']} gold.")

if caribbean:
    print(f"Ahoy, Captain! There are {len(caribbean)} wealthy settlements to go to:")

    for town, info in caribbean.items():
        print(f"{town} -> Population: {info['people']} citizens, Gold: {info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
