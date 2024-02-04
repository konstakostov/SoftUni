day = input()

price = 0

if day == "Monday" or "Tuesday" or "Friday":
    price = 12
elif day == "Wednesday" or "Thursday":
    price = 14
elif day == "Saturday" or "Sunday":
    price = 16

print(price)
