flowers = input()
quantity = int(input())
budget = int(input())

roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

total_price = 0

if flowers == "Roses":
    total_price = roses_price * quantity
    if quantity > 80:
        total_price *= 0.90


elif flowers == "Dahlias":
    total_price = dahlias_price * quantity
    if quantity > 90:
        total_price *= 0.85

elif flowers == "Tulips":
    total_price = tulips_price * quantity
    if quantity > 80:
        total_price *= 0.80

elif flowers == "Narcissus":
    total_price = narcissus_price * quantity
    if quantity < 120:
        total_price *= 1.15

else:
    total_price = gladiolus_price * quantity
    if quantity < 80:
        total_price *= 1.20

if total_price <= budget:
    print(f"Hey, you have a great garden with {quantity} {flowers} and {(budget - total_price):.2f} leva left.")
else:
    print(f"Not enough money, you need {(total_price - budget):.2f} leva more.")
