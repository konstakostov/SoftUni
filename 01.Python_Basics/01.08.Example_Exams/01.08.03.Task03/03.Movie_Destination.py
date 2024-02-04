budget = float(input())
destination = input()
season = input()
days = int(input())

price_per_day = 0
total_price = 0

if destination == "Dubai":
    if season == "Winter":
        price_per_day = 45000
    elif season == "Summer":
        price_per_day =40000
    total_price = price_per_day * days
    total_price *= 0.70

elif destination == "Sofia":
    if season == "Winter":
        price_per_day = 17000
    elif season == "Summer":
        price_per_day = 12500
    total_price = price_per_day * days
    total_price *= 1.25

elif destination == "London":
    if season == "Winter":
        price_per_day = 24000
    elif season == "Summer":
        price_per_day = 20250
    total_price = price_per_day * days

if total_price <= budget:
    print(f"The budget for the movie is enough! We have {(budget - total_price):.2f} leva left!")
else:
    print(f"The director needs {(total_price - budget):.2f} leva more!")
