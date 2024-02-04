quantity = int(input())
product_type = input()
delivery = input()

single_price = 0
quantity_discount = 0
final_price = 0

if quantity < 10:
    print("Invalid order")
    raise SystemExit

if product_type == "90X130":
    single_price = 110
    final_price = (quantity * single_price)
    if quantity > 60:
        quantity_discount = 0.08
        final_price *= 1 - quantity_discount
    elif quantity > 30:
        quantity_discount = 0.05
        final_price *= 1 - quantity_discount

elif product_type == "100X150":
    single_price = 140
    final_price = (quantity * single_price)
    if quantity > 80:
        quantity_discount = 0.10
        final_price *= 1 - quantity_discount
    elif quantity > 40:
        quantity_discount = 0.06
        final_price *= 1 - quantity_discount

elif product_type == "130X180":
    single_price = 190
    final_price = (quantity * single_price)
    if quantity > 50:
        quantity_discount = 0.12
        final_price *= 1 - quantity_discount
    elif quantity > 20:
        quantity_discount = 0.07
        final_price *= 1 - quantity_discount

elif product_type == "200X300":
    single_price = 250
    final_price = (quantity * single_price)
    if quantity > 50:
        quantity_discount = 0.14
        final_price *= 1 - quantity_discount
    elif quantity > 25:
        quantity_discount = 0.09
        final_price *= 1 - quantity_discount

if delivery == "With delivery":
    final_price += 60
elif delivery == "Without delivery":
    final_price += 0

if quantity <= 99:
    print(f"{final_price:.2f} BGN")
else:
    final_price *= 1 - 0.04
    print(f"{final_price:.2f} BGN")
