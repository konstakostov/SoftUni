budget = float(input())
people = int(input())
costume = float(input())

decor = budget * 0.10
costume_price = 0

if people <= 150:
    costume_price = people * costume
else:
    costume_price = (people * costume) * 0.90

total = decor + costume_price

if total <= budget:
    print(f"Action!")
    money = budget - total
    print(f"Wingard starts filming with {money:.2f} leva left.")
else:
    print(f"Not enough money!")
    money = total - budget
    print(f"Wingard needs {money:.2f} leva more.")

