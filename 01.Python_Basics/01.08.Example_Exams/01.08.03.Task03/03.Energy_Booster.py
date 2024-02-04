fruit = input()
set_size = input()
set_quantity = int(input())

price_per_unit = 0
discount = 0
quantity = 0

if fruit == "Watermelon":
    if set_size == "small":
        price_per_unit = 56
        quantity = 2
    elif set_size == "big":
        price_per_unit = 28.70
        quantity = 5

elif fruit == "Mango":
    if set_size == "small":
        price_per_unit = 36.66
        quantity = 2
    elif set_size == "big":
        price_per_unit = 19.60
        quantity = 5

elif fruit == "Pineapple":
    if set_size == "small":
        price_per_unit = 42.10
        quantity = 2
    elif set_size == "big":
        price_per_unit = 24.80
        quantity = 5

elif fruit == "Raspberry":
    if set_size == "small":
        price_per_unit = 20
        quantity = 2
    elif set_size == "big":
        price_per_unit = 15.20
        quantity = 5

price = (price_per_unit * quantity) * set_quantity

if 400 <= price <= 1000:
    discount = price * 0.15
    price -= discount
elif price > 1000:
    discount = price * 0.50
    price -= discount
else:
    price = price

print(f"{price:.2f} lv.")
