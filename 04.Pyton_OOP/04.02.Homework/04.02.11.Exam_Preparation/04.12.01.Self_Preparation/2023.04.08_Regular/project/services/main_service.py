from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str) -> None:
        super().__init__(name, capacity=30)

    def details(self):
        robots_on_service = len(self.robots)

        if robots_on_service == 0:
            return f"{self.name} Main Service:\n" \
                   f"Robots: none"

        return f"{self.name} Main Service:\n" \
               f"Robots: {' '.join([r for r in self.robots])}"
