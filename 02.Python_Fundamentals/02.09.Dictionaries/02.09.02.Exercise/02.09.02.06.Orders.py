products = {}

while True:
    command = input()

    if command == "buy":
        break

    name = command.split()[0]
    price = float(command.split()[1])
    quantity = int(command.split()[2])

    products[name] = products.get(name, {"product_price": 0, "product_quantity": 0})

    products[name]["product_price"] = price
    products[name]["product_quantity"] += quantity

for product_name, value in products.items():
    total_price = value["product_price"] * value["product_quantity"]
    print(f"{product_name} -> {total_price:.2f}")
