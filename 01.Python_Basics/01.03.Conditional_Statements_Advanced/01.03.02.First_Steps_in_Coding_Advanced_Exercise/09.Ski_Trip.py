days = int(input()) - 1
room = input()
review = input()

room_for_one = 18
apartment = 25
president_apartment = 35

costs = 0

if room == "room for one person":
    costs = days * room_for_one

elif room == "apartment":
    costs = days * apartment
    if days < 10:
        costs *= 0.70
    elif days <= 14:
        costs *= 0.65
    elif days > 15:
        costs *= 0.50

elif room == "president apartment":
    costs = days * president_apartment
    if days < 10:
        costs *= 0.90
    elif days <= 14:
        costs *= 0.85
    elif days > 15:
        costs *= 0.80

if review == "positive":
    costs *= 1.25
elif review == "negative":
    costs *= 0.90

print(f"{costs:.2f}")
