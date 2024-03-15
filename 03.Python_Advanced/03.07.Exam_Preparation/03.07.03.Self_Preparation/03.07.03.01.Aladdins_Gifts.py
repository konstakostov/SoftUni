from collections import deque

materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

success = False

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()

    present = material + magic

    if present < 100:
        if present % 2 == 0:
            present = (material * 2) + (magic * 3)
        elif present % 2 != 0:
            present = (material * 2) + (magic * 2)
    elif present > 499:
        present = (material / 2) + (magic / 2)

    if 100 <= present <= 199:
        gifts["Gemstone"] += 1

    elif 200 <= present <= 299:
        gifts["Porcelain Sculpture"] += 1

    elif 300 <= present <= 399:
        gifts["Gold"] += 1

    elif 400 <= present <= 499:
        gifts["Diamond Jewellery"] += 1


if gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0:
    success = True
if gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0:
    success = True


if success:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")

if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

gifts = sorted(gifts.items(), key=lambda x: x[0])

for key, value in gifts:
    if value > 0:
        print(f"{key}: {value}")
