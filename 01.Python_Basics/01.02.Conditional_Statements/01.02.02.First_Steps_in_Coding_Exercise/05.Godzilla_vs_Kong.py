budget = float(input())
crew = int(input())
clothing_price = float(input())

decor = budget * 0.1

clothing_total = crew * clothing_price

if crew >= 150:
    clothing_total = clothing_total - clothing_total * 0.1
else:
    clothing_total = clothing_total

money_needed = decor + clothing_total

if budget < money_needed:
    print("Not enough money!")
    print(f"Wingard needs {money_needed - budget:.2f} leva more.")
elif budget >= money_needed:
    print("Action!")
    print(f"Wingard starts filming with {budget - money_needed:.2f} leva left.")
