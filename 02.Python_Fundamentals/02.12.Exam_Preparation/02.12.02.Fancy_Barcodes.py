import re

num_products = int(input())
pattern = r"^@\#{1,}([A-Z][04.03.01.01.Food-zA-Z\d]{4,}[A-Z])\@\#{1,}$"

for i in range(num_products):
    barcode = input()
    product_group = ""

    matches = re.findall(pattern, barcode)

    if matches:
        for product in matches:
            for char in product:
                if char.isdigit():
                    product_group += char

        if len(product_group) < 1:
            product_group = "00"

        print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")
