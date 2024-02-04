budget = float(input())
season = input()

lodging = ""
location = ""
costs = 0

if budget <= 1000:
    lodging = "Camp"
    if season == "Summer":
        location = "Alaska"
        costs = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        costs = budget * 0.45

elif 1000 < budget <= 3000:
    lodging = "Hut"
    if season == "Summer":
        location = "Alaska"
        costs = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        costs = budget * 0.60

elif budget > 3000:
    lodging = "Hotel"
    costs = budget * 0.90
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {lodging} - {costs:.2f}")
