def shopping_cart(*args):
    cart = {"Soup": [], "Pizza": [], "Dessert": []}

    for arg in args:
        if arg == "Stop":
            break

        meal, ingredient = arg[0], arg[1]

        if meal == "Soup" and len(cart["Soup"]) == 3:
            continue

        if meal == "Pizza" and len(cart["Pizza"]) == 4:
            continue

        if meal == "Dessert" and len(cart["Dessert"]) == 2:
            continue

        if ingredient not in cart[meal]:
            cart[meal].append(ingredient)

    for value in cart.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    cart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for item in cart:
        result += f"{item[0]}:\n"
        sorted_product = sorted(item[1])

        for product in sorted_product:
            result += f" - {product}\n"

    return result.strip()


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print()

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print()

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
