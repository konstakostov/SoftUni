from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    STARTING_WEIGHT = 7
    FEMALE_EAT = 1
    VALID_SERVICE = 'SecondaryService'

    def __init__(self, name: str, kind: str, price: float) -> None:
        super().__init__(name, kind, price, weight=self.STARTING_WEIGHT)

    def eating(self):
        self.weight += self.FEMALE_EAT
