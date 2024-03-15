from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.secondary_service import SecondaryService
from project.services.main_service import MainService


class RobotsManagingApp:
    SERVICES_TYPES = {'MainService': MainService, 'SecondaryService': SecondaryService}
    ROBOT_TYPES = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}

    robots = []
    services = []

    def add_service(self, service_type: str, name: str) -> Exception or str:
        if service_type not in self.SERVICES_TYPES:
            raise Exception("Invalid service type!")

        new_service = self._add_service(service_type, name)
        self.services.append(new_service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> Exception or str:
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        new_robot = self._add_robot(robot_type, name, kind, price)
        self.robots.append(new_robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._object_by_name(robot_name, self.robots)
        service = self._object_by_name(service_name, self.services)

        if robot.VALID_SERVICE != service.__class__.__name__:
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.services.append(robot)
        self.robots.remove(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._object_by_name(service_name, self.services)

        robot = [r for r in service.robots if r.name == robot_name][0]

        if not robot:
            raise Exception("No such robot in this service!")

        self.services.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self._object_by_name(service_name, self.services)
        [r.eating() for r in service.robots]
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self._object_by_name(service_name, self.services)
        price = sum([r.price for r in service.robots])

        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        return '\n'.join([s.details() for s in self.services])

    # ADDITIONAL METHODS
    def _add_service(self, service_type: str, name: str):
        return self.SERVICES_TYPES[service_type](name)

    def _add_robot(self, robot_type: str, name: str, kind: str, price: float):
        return self.ROBOT_TYPES[robot_type](name, kind, price)

    @staticmethod
    def _object_by_name(name, collection):
        return [obj for obj in collection if obj.name == name][0]
