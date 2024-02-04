class Flower:
    def __init__(self, name: str, water_requirements: int) -> None:
        self.name = name
        self.water_requirements = water_requirements

        self.is_happy: bool = False

    def water(self, quantity) -> None:
        if quantity >= self.water_requirements:
            self.is_happy = True
        else:
            self.is_happy = False

    def status(self) -> str:
        if not self.is_happy:
            return f"{self.name} is not happy"

        return f"{self.name} is happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
