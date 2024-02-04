from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    MEAL_TYPES = ["Starter", "MainDish", "Dessert"]

    def __init__(self) -> None:
        self.menu: list = []
        self.clients: list = []

    def register_client(self, client_phone_number: str):    # ALL VARIANTS HAVE BEEN TESTED
        for client in self.clients:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)

        self.clients.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):  # ALL VARIANTS HAVE BEEN TESTED
        for meal in meals:
            if meal.__class__.__name__ in self.MEAL_TYPES:
                self.menu.append(meal)

    def show_menu(self):    # ALL VARIANTS HAVE BEEN TESTED
        self._validate_menu_length()

        meal_details = []

        for meal in self.menu:
            meal_details.append(meal.details())

        return '\n'.join(meal_details)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self._validate_menu_length()

        if not self._check_if_client_is_registered(client_phone_number):
            self.register_client(client_phone_number)

        client = self._find_client(client_phone_number)
        meals_to_order = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if meal_name not in client.shopping_cart:
                client.shopping_cart[meal_name] = 0

            client.shopping_cart[meal_name] += meal_quantity

            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

        # for meal_name, meal_quantity in meal_names_and_quantities.items():
        #     if meal_name not in client.shopping_cart:
        #         client.shopping_cart[meal_name] = 0
        #     client.shopping_cart[meal_name] += meal_quantity
        #     for meal in self.menu:
        #         if meal.name == meal_name:
        #             meal.quantity -= meal_quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def _check_if_phone_in_clients_list(self, client_phone_number: str):
        for client in self.clients:
            if client.phone_number == client_phone_number:
                return client

    def _validate_menu_length(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def _check_if_client_is_registered(self, phone_number):
        for client in self.clients:
            if client.phone_number == phone_number:
                return True

    def _find_client(self, phone_number: str):
        for client in self.clients:
            if client.phone_number == phone_number:
                return client

    def cancel_order(self, client_phone_number: str):
        pass

    def finish_order(self, client_phone_number: str):
        pass

    def __str__(self):
        pass
