def shop_from_grocery_list(budget, g_list, *args):
    budget_left = budget
    grocery = g_list
    bought = []

    for product, value in args:
        if budget_left < value:
            break
        if product in grocery:
            bought.append(product)
            grocery.remove(product)
            budget_left -= value

    if len(grocery) == 0:
        return f"Shopping is successful. Remaining budget: {budget_left:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45)
))

# Shopping is successful. Remaining budget: 84.20.

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))
#
# print()
#
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))
#
# print()
#
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))
