price_no_taxes = 0
taxes = 0
total_price = 0

special = False

while True:
    command = input()

    if command == "special":
        special = True
        break
    elif command == "regular":
        break

    price = float(command)
    if price < 0:
        print("Invalid price!")
        continue

    price_no_taxes += price
    taxes += price * 0.20

if special:
    total_price = (price_no_taxes + taxes) * 0.90
else:
    total_price = price_no_taxes + taxes

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought 04.03.01.01.Food new computer!")
    print(f"Price without taxes: {price_no_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
