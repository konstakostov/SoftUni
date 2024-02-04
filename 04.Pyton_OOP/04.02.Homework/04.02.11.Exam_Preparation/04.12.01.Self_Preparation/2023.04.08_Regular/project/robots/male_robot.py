from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    STARTING_WEIGHT = 9
    MALE_EAT = 3
    VALID_SERVICE = 'MainService'

    def __init__(self, name: str, kind: str, price: float) -> None:
        super().__init__(name, kind, price, weight=self.STARTING_WEIGHT)

    def eating(self):
        self.weight += self.MALE_EAT
