from project.supply.supply import Supply


class Food(Supply):
    ENERGY = 25

    def __init__(self, name: str, energy: int = ENERGY) -> None:
        super().__init__(name, energy)

    def details(self) -> str:
        return f"Food: {self.name}, {self.energy}"
