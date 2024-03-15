budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_cost_percent = int(input()) / 100

nights_price = 0

if nights <= 7:
    nights_price = nights * price_per_night

else:
    nights_price = (nights * price_per_night) - (nights * price_per_night) * 0.05

additional_costs = budget * additional_cost_percent

total_spend = nights_price + additional_costs

if budget >= total_spend:
    print(f"Ivanovi will be left with {(budget - total_spend):.2f} leva after vacation.")
else:
    print(f"{(total_spend - budget):.2f} leva needed.")
