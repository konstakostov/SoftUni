command = input()
products = {}

while command != "statistics":
    data = command.split(":")
    product = data[0]
    quantity = int(data[1])

    if product not in products:
        products[product] = 0
    products[product] += quantity

    command = input()

print("Products in stock:")
for product in products:
    print(f"- {product}: {products[product]}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
