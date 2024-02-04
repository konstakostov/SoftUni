days = int(input())
hours = int(input())

price_total = 0
day_price = 0

for current_day in range(1, days + 1):
    for current_hour in range(1, hours + 1):

        if current_day % 2 == 0:
            if current_hour % 2 == 0:
                day_price += 1
            else:
                day_price += 2.50

        else:
            if current_hour % 2 == 0:
                day_price += 1.25
            else:
                day_price += 1.

    print(f"Day: {current_day} - {day_price:.2f} leva")
    price_total += day_price
    day_price = 0

print(f"Total: {price_total:.2f} leva")
