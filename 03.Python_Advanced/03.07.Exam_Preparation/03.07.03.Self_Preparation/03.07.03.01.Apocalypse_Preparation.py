from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

patch = 0
bandage = 0
med_kit = 0

healing_prices = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}

healing_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    item = textile + medicament

    if item in healing_prices:
        healing_items[healing_prices[item]] += 1

    elif item > 100:
        healing_items["MedKit"] += 1
        medicaments[-1] += item - 100

    else:
        medicaments.append(medicament + 10)

healing_items = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))
# On the next n lines print only the created items (if any) ordered by the amount created descending,
# then by name alphabetically:


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for item, quantity in healing_items:
    if quantity > 0:
        print(f"{item} - {quantity}")

if medicaments:
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments][::-1])}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
