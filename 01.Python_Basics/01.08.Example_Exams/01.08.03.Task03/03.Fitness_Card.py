budget = float(input())
gender = input()
age = int(input())
sport = input()

price_sport = 0

if sport == "Gym":
    if gender == "m":
        price_sport = 42
    elif gender == "f":
        price_sport = 35

elif sport == "Boxing":
    if gender == "m":
        price_sport = 41
    elif gender == "f":
        price_sport = 37

elif sport == "Yoga":
    if gender == "m":
        price_sport = 45
    elif gender == "f":
        price_sport = 42

elif sport == "Zumba":
    if gender == "m":
        price_sport = 34
    elif gender == "f":
        price_sport = 31

elif sport == "Dances":
    if gender == "m":
        price_sport = 51
    elif gender == "f":
        price_sport = 53

elif sport == "Pilates":
    if gender == "m":
        price_sport = 39
    elif gender == "f":
        price_sport = 37

if age <= 19:
    price_sport *= 0.80
else:
    price_sport = price_sport

if budget >= price_sport:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${(price_sport - budget):.2f} more.")
