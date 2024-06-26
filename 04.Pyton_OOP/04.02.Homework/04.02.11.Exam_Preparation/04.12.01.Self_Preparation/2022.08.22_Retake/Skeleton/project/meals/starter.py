from project.meals.meal import Meal


class Starter(Meal):
    def __init__(self, name: str, price: float, quantity: int = 60) -> None:
        super().__init__(name, price, quantity)

    def details(self) -> str:
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
