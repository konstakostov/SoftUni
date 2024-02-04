from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    # NB!!!
    def details(self):
        result = f"{self.name} Secondary Service:\n"

        if len(self.robots) <= 0:
            result += f"Robots: none"
        else:
            result += "Robots: " + ' '.join([r.name for r in self.robots])

        return result.strip()
