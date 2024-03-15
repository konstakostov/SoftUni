budget = float(input())
fuel = float(input())
day = input()

fuel_price = 2.10
guide = 100
discount = 0

if day == "Saturday":
    discount = 0.10
elif day == "Sunday":
    discount = 0.20

total = (fuel * fuel_price + guide) - (fuel * fuel_price + guide) * discount

if total >= budget:
    print(f"Not enough money! Money needed: {(total - budget):.2f} lv.")
else:
    print(f"Safari time! Money left: {(budget - total):.2f} lv.")
