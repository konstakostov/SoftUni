budget = float(input())
season = input()

location = None
lodging = None
cost = 0

if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        lodging = "Camp"
        cost = budget * 0.30
    else:
        lodging = "Hotel"
        cost = budget * 0.70

elif budget <= 1000:
    location = "Balkans"
    if season == "summer":
        lodging = "Camp"
        cost = budget * 0.40
    else:
        lodging = "Hotel"
        cost = budget * 0.80

else:
    location = "Europe"
    lodging = "Hotel"
    cost = budget * 0.90

print(f"Somewhere in {location}")
print(f"{lodging} - {cost:.2f}")
