budget = float(input())
n_series = int(input())

money_left = budget

for i in range(1, n_series + 1):
    title = input()
    price = float(input())

    if title == "Thrones":
        price *= 0.50
    elif title == "Lucifer":
        price *= 0.60
    elif title == "Protector":
        price *= 0.70
    elif title == "TotalDrama":
        price *= 0.80
    elif title == "Area":
        price *= 0.90

    money_left -= price

if money_left < 0:
    print(f"You need {abs(money_left):.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {money_left:.2f} lv.")
