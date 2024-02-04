from project.supply.supply import Supply


class Drink(Supply):
    ENERGY = 15

    def __init__(self, name: str, energy: int = ENERGY) -> None:
        super().__init__(name, energy)

    def details(self) -> str:
        return f"Drink: {self.name}, {self.energy}"
