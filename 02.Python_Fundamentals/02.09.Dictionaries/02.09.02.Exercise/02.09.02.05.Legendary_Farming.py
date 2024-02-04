key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}

status = True
legendary_item = ""

while True:
    materials = input().split()

    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1]

        if material.lower() == "shards":
            key_materials["shards"] += quantity
            if key_materials["shards"] >= 250:
                legendary_item = "Shadowmourne"
                status = False
                key_materials["shards"] -= 250
                break

        elif material.lower() == "fragments":
            key_materials["fragments"] += quantity
            if key_materials["fragments"] >= 250:
                legendary_item = "Valanyr"
                status = False
                key_materials["fragments"] -= 250
                break

        elif material.lower() == "motes":
            key_materials["motes"] += quantity
            if key_materials["motes"] >= 250:
                legendary_item = "Dragonwrath"
                status = False
                key_materials["motes"] -= 250
                break

        else:
            if material.lower() not in junk_materials:
                junk_materials[material.lower()] = 0
            junk_materials[material.lower()] += quantity

    if not status:
        break

print(f"{legendary_item} obtained!")

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")

for material, quantity in junk_materials.items():
    print(f"{material}: {quantity}")
