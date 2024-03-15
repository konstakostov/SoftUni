city_number = int(input())

total_money = 0

for current_city in range(1, city_number + 1):
    city_name = input()
    earnings = float(input())
    expenses = float(input())
    event_expenses = 0
    city_profit = 0

    if current_city % 3 == 0:
        event_expenses = expenses * 0.50

    if current_city % 5 == 0:
        earnings *= 0.90

    if current_city % 3 == 0 and current_city % 5 == 0:
        event_expenses = 0

    city_profit += (earnings - (expenses + event_expenses))
    total_money += city_profit

    print(f"In {city_name} Burger Bus earned {city_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_money:.2f} leva.")
