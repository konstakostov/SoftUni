def shopping_list(money, **kwargs):
    result = ""

    budget = int(money)
    basket = {}

    if budget < 100:
        return "You do not have enough budget."

    for product, data in kwargs.items():
        if len(basket) == 5:
            break

        data = str(data)

        data = [float(num) for num in data.strip("()").split(",")]
        price, quantity = data[0], data[1]

        if budget >= (price * quantity):
            if product not in basket:
                basket[product] = 0

            basket[product] += price * quantity
            budget -= price * quantity

    for key, value in basket.items():
        result += f"You bought {key} for {value:.2f} leva.\n"

    return result.strip()


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print()

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print()

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
