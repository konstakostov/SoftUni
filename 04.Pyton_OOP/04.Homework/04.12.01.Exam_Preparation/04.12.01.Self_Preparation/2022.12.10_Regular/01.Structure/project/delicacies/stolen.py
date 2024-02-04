from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    PORTION_SIZE = 250

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, Stolen.PORTION_SIZE, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv"
