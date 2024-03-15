budget = int(input())
season = input()
fisherman = int(input())

costs = 0

# Determining the Season
if season == "Spring":
    costs = 3000
elif season == "Winter":
    costs = 2600
else:
    costs = 4200

# Determining the Discount
if fisherman <= 6:
    costs *= 0.90
elif 7 <= fisherman <= 11:
    costs *= 0.85
else:
    costs *= 0.75

if fisherman % 2 == 0 and season != "Autumn":
    costs *= 0.95

if budget >= costs:
    print(f"Yes! You have {(budget - costs):.2f} leva left.")
else:
    print(f"Not enough money! You need {(costs - budget):.2f} leva.")
