from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPES = ["PassengerCar", "CargoVan"]
    route_id = 0

    def __init__(self):
        self.users: list = []
        self.vehicles: list = []
        self.routes: list = []

    def __find_user_by_license_number(self, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return user

    def __check_if_licence_plate_is_registered_to_vehicle(self, license_plate_number):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return vehicle

    def __route_start_end_equal_length(self, start_point: str, end_point: str, length: float):
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point and r.length == length:
                return r

    def __route_start_end_lesser_length(self, start_point: str, end_point: str, length: float):
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point and r.length < length:
                return r

    def __route_start_end_greater_length(self, start_point: str, end_point: str, length: float):
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point and r.length > length:
                return r

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self.__find_user_by_license_number(driving_license_number)

        if user:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)

        self.users.append(new_user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = self.__check_if_licence_plate_is_registered_to_vehicle(license_plate_number)

        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = None

        if vehicle_type == "PassengerCar":
            new_vehicle = PassengerCar(brand, model, license_plate_number)
        elif vehicle_type == "CargoVan":
            new_vehicle = CargoVan(brand, model, license_plate_number)

        self.vehicles.append(new_vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        equal_route = self.__route_start_end_equal_length(start_point, end_point, length)

        if equal_route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        lesser_route = self.__route_start_end_lesser_length(start_point, end_point, length)

        if lesser_route:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        greater_route = self.__route_start_end_greater_length(start_point, end_point, length)

        if greater_route:
            greater_route.is_locked = True

        # ROUTE ID CAN CREATE PROBLEMS!!!
        new_route = Route(start_point, end_point, length, self.route_id + 1)

        self.routes.append(new_route)
        self.route_id = len(self.routes)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                                    route_id: int,  is_accident_happened: bool):
        user = self.__find_user_by_license_number(driving_license_number)
        vehicle = self.__check_if_licence_plate_is_registered_to_vehicle(license_plate_number)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = None

        for r in self.routes:
            if r.route_id == route_id:
                if r.is_locked:
                    return f"Route {route_id} is locked! This trip is not allowed."
                else:
                    route = r

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return vehicle.__str__()

    # TODO FIX THIS FUNCTION
    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        selected_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))[:count]

        for vehicle in selected_vehicles:
            vehicle.change_status()
            vehicle.recharge()

        return f"{len(selected_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = "*** E-Drive-Rent ***\n"

        sorted_users = sorted(self.users, key=lambda u: -u.rating)

        for user in sorted_users:
            result += f"{user.__str__()}\n"

        return result.strip()
