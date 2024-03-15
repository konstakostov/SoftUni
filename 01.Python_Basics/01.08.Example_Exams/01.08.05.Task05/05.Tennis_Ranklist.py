import math

tournaments = int(input())
points = int(input())

points_won = 0

win = 0
final = 0
semi = 0

for i in range(1, tournaments + 1):
    stage = input()

    if stage == "W":
        points += 2000
        points_won += 2000
        win += 1
    elif stage == "F":
        points += 1200
        points_won += 1200
        final += 1
    elif stage == "SF":
        points += 720
        points_won += 720
        semi += 1

print(f"Final points: {points}")
print(f"Average points: {math.floor(points_won / tournaments)}")
print(f"{((win / tournaments) * 100):.2f}%")
