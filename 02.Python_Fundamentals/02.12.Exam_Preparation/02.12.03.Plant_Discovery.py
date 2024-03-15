num_plants = int(input())

exhibition = {}

for _ in range(num_plants):
    plant, rarity = input().split("<->")

    exhibition[plant] = exhibition.get(plant, {'rarity': int(rarity), 'rating': []})

command = input()

while command != "Exhibition":
    action, info = command.split(": ")

    if action == "Rate":
        plant, rating = info.split(" - ")

        if plant in exhibition:
            exhibition[plant]['rating'].append(rating)
        else:
            print("error")

    elif action == "Update":
        plant, new_rarity = info.split(" - ")

        if plant in exhibition:
            exhibition[plant]['rarity'] = int(new_rarity)
        else:
            print("error")

    elif action == "Reset":
        plant = info

        if plant in exhibition:
            exhibition[plant]['rating'] = []
        else:
            print("error")

    command = input()

print("Plants for the exhibition:")
for plant, info in exhibition.items():
    average_rating = 0
    counter = 0
    if info['rating']:
        for item in info['rating']:
            average_rating += float(item)
            counter += 1
        average_rating /= counter
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {average_rating:.2f}")
