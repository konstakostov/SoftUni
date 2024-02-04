import math

tournaments = int(input())
starting_points = int(input())

tournaments_points = 0
won_tournaments = 0

for _ in range(1, tournaments + 1):
    tour_stage = input()

    if tour_stage == "W":
        tournaments_points += 2000
        won_tournaments += 1
    elif tour_stage == "F":
        tournaments_points += 1200
    elif tour_stage == "SF":
        tournaments_points += 720

final_points = starting_points + tournaments_points
average_points = tournaments_points / tournaments
won_percentage = (won_tournaments / tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{won_percentage:.2f}%")
