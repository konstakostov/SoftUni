from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = ["MainService", "SecondaryService"]
    VALID_ROBOTS = ["MaleRobot", "FemaleRobot"]

    def __init__(self):
        self.robots: list = []
        self.services: list = []

    def __find_robot_by_name(self, robot_name: str):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot

    def __find_service_by_name(self, service_name: str):
        for service in self.services:
            if service.name == service_name:
                return service

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        new_service = None

        if service_type == "MainService":
            new_service = MainService(name)
        elif service_type == "SecondaryService":
            new_service = SecondaryService(name)

        self.services.append(new_service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        new_robot = None

        if robot_type == "FemaleRobot":
            new_robot = FemaleRobot(name, kind, price)
        elif robot_type == "MaleRobot":
            new_robot = MaleRobot(name, kind, price)

        self.robots.append(new_robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.__find_robot_by_name(robot_name)
        robot_type = robot.__class__.__name__

        service = self.__find_service_by_name(service_name)
        service_type = service.__class__.__name__

        if ((service_type == "SecondaryService" and robot_type != "FemaleRobot") or
                (service_type == "MainService" and robot_type != "MaleRobot")):
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__find_service_by_name(service_name)
        robot = [r for r in service.robots if r.name == robot_name]

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot[0])
        self.robots.append(robot[0])

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_service_by_name(service_name)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__find_service_by_name(service_name)

        total_price = 0
        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = ""

        for service in self.services:
            result += f"{service.details()}\n"

        return result.strip()
