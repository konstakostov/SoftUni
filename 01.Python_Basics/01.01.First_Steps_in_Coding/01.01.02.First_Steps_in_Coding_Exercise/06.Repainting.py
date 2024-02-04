nylon = int(input()) + 2
paint = int(input())
thinner = int(input())
hours = int(input())

paint = paint + paint * 0.10

nylon_price = nylon * 1.50
paint_price = paint * 14.50
thinner_price = thinner * 5
bags_price = 0.40

materials_price = nylon_price + paint_price + thinner_price + bags_price

one_hour_pay = materials_price * 0.30

total_hours_pay = one_hour_pay * hours

total_price = materials_price + total_hours_pay

print(total_price)
