groups_count = int(input())

g1, g2, g3, g4, g5 = 0, 0, 0, 0, 0

people_count = 0

for _ in range(1, groups_count + 1):
    people_group = int(input())

    people_count += people_group

    if people_group <= 5:
        g1 += people_group
    elif people_group <= 12:
        g2 += people_group
    elif people_group <= 25:
        g3 += people_group
    elif people_group <= 40:
        g4 += people_group
    else:
        g5 += people_group

print(f"{((g1 / people_count) * 100):.2f}%")
print(f"{((g2 / people_count) * 100):.2f}%")
print(f"{((g3 / people_count) * 100):.2f}%")
print(f"{((g4 / people_count) * 100):.2f}%")
print(f"{((g5 / people_count) * 100):.2f}%")
