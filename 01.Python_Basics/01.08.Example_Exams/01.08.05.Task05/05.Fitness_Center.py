visitors = int(input())

back = 0
chest = 0
legs = 0
abs_ = 0
shake = 0
bar = 0

workout = 0
protein = 0

for i in range(1, visitors + 1):
    action = input()

    if action == "Back":
        back += 1
        workout += 1
    elif action == "Chest":
        chest += 1
        workout += 1
    elif action == "Legs":
        legs += 1
        workout += 1
    elif action == "Abs":
        abs_ += 1
        workout += 1
    elif action == "Protein shake":
        shake += 1
        protein += 1
    elif action == "Protein bar":
        bar += 1
        protein += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_} - abs")
print(f"{shake} - protein shake")
print(f"{bar} - protein bar")
print(f"{((workout / visitors) * 100):.2f}% - work out")
print(f"{((protein / visitors) * 100):.2f}% - protein")
