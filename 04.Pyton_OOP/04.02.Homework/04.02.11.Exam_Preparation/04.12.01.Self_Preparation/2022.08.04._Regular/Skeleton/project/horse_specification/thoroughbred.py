from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    SPEED_INCREASE = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
