days = int(input())
room = input()
grade = input()

nights = days - 1
discount = 0
price = 0

if room == "room for one person":
    price = 18
    if days < 10:
        price = nights * price
    elif 10 <= days <= 15:
        price = nights * price
    elif days > 15:
        price = nights * price

elif room == "apartment":
    price = 25
    if days < 10:
        price = nights * price
        price *= 0.70
    elif 10 <= days <= 15:
        price = nights * price
        price *= 0.65
    elif days > 15:
        price = nights * price
        price *= 0.50

elif room == "president apartment":
    price = 35
    if days < 10:
        price = nights * price
        price *= 0.90
    elif 10 <= days <= 15:
        price = nights * price
        price *= 0.85
    elif days > 15:
        price = nights * price
        price *= 0.80

if grade == "positive":
    price *= 1.25
elif grade == "negative":
    price *= 0.90

print(f"{price:.2f}")
