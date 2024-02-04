groups = int(input())

g1, g2, g3, g4, g5 = 0, 0, 0, 0, 0

people_count = 0

for _ in range(1, groups + 1):
    people = int(input())

    people_count += people

    if people <= 5:
        g1 += people
    elif people <= 12:
        g2 += people
    elif people <= 25:
        g3 += people
    elif people <= 40:
        g4 += people
    else:
        g5 += people

musala_persent = (g1 / people_count) * 100
monblan_percent = (g2 / people_count) * 100
kili_percent = (g3 / people_count) * 100
k2_percent = (g4 / people_count) * 100
everest_percent = (g5 / people_count) * 100

print(f"{musala_persent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kili_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
