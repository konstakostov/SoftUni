from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    # NB!!!
    def details(self):
        result = f"{self.name} Main Service:\n"

        if len(self.robots) <= 0:
            result += f"Robots: none"
        else:
            result += "Robots: " + ' '.join([r.name for r in self.robots])

        return result.strip()
