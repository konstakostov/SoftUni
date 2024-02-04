from typing import Dict


class PizzaDelivery:
    ordered = False

    def __init__(self, name: str, price: float, ingredients: Dict[str, int]):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> None or str:
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0

        self.ingredients[ingredient] += quantity
        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> str or None:
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        current_quantity = self.ingredients[ingredient]

        if current_quantity < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self):
        PizzaDelivery.ordered = True

        ingrid = ""

        for key, value in self.ingredients.items():
            ingrid += f"{key}: {value}"

            if key != list(self.ingredients.keys())[-1]:
                ingrid += ", "
            else:
                ingrid += " "

        return f"You've ordered pizza {self.name} prepared with {ingrid}" \
               f"and the price will be {self.price}lv."


# margarita = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('cheese', 1, 2)
# margarita.add_extra('mozzarella', 1, 2.5)
#
#
# print(margarita.price)
# print(margarita.ingredients)

# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))


