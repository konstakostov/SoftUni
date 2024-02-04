price_above_20kg = float(input())
luggage_kg = float(input())
days_left = int(input())
luggage_quantity = int(input())

luggage_price = 0

if luggage_kg < 10:
    luggage_price = price_above_20kg * 0.20
elif 10 <= luggage_kg <= 20:
    luggage_price = price_above_20kg * 0.50
elif luggage_kg > 20:
    luggage_price = price_above_20kg

if days_left < 7:
    luggage_price *= 1.40
elif 7 <= days_left <= 30:
    luggage_price *= 1.15
elif days_left > 30:
    luggage_price *= 1.10

total = luggage_price * luggage_quantity

print(f"The total price of bags is: {total:.2f} lv. ")
