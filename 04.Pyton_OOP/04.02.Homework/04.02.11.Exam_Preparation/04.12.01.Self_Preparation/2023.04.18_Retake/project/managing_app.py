# from typing import List
# from project.route import Route
# from project.user import User
# from project.vehicles.cargo_van import CargoVan
# from project.vehicles.passenger_car import PassengerCar
#
#
# class ManagingApp:
#     VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}
#
#     def __init__(self) -> None:
#         self.users: List[User] = []
#         self.vehicles: list = []
#         self.routes: List[Route] = []
#
#     def register_user(self, first_name: str, last_name: str, driving_license_number: str):
#         if self._user_by_license(driving_license_number) is not None:
#             return f"{driving_license_number} has already been registered to our platform."
#
#         new_user = self._create_user(first_name, last_name, driving_license_number)
#
#         self.users.append(new_user)
#
#         return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"
#
#     def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
#         if vehicle_type not in self.VEHICLE_TYPES:
#             return f"Vehicle type {vehicle_type} is inaccessible."
#
#         if self._vehicle_by_plate(license_plate_number) is not None:
#             return f"{license_plate_number} belongs to another vehicle."
#
#         new_vehicle = self._add_vehicle(vehicle_type, brand, model, license_plate_number)
#
#         self.vehicles.append(new_vehicle)
#
#         return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."
#
#     # Adding Routes All Methods
#     def allow_route(self, start_point: str, end_point: str, length: float):
#         current_route = self._is_route_allowed(start_point, end_point)
#
#         if current_route is not None:
#             if current_route.length == length:
#                 return f"{start_point}/{end_point} - {length} km had already been added to our platform."
#
#             elif current_route.length < length:
#                 return f"{start_point}/{end_point} shorter route had already been added to our platform."
#
#             elif current_route.length > length:
#                 current_route.is_locked = True
#
#         new_route = self._add_route(start_point, end_point, length)
#
#         self.routes.append(new_route)
#
#         return f"{start_point}/{end_point} - {length} km is unlocked and available to use."
#
#     # Making Trip
#     def make_trip(self, driving_license_number: str, license_plate_number: str,
#                   route_id: int, is_accident_happened: bool):
#         user = self._user_by_license(driving_license_number)
#         vehicle = self._vehicle_by_plate(license_plate_number)
#         route = self._route_by_id(route_id)
#
#         if user.is_blocked:
#             return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
#
#         if vehicle.is_damaged:
#             return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
#
#         if route.is_locked:
#             return f"Route {route_id} is locked! This trip is not allowed."
#
#         vehicle.drive(route.length)
#
#         if is_accident_happened:
#             vehicle.change_status()
#             user.decrease_rating()
#         else:
#             user.increase_rating()
#
#         return str(vehicle)
#
#     # Repairing Vehicles
#     def repair_vehicles(self, count: int):
#         damaged = [x for x in self.vehicles if x.is_damaged]
#         sorted_damaged = sorted(damaged, key=lambda x: (x.brand, x.model))[:count]
#
#         vehicle_counter = 0
#
#         for vehicle in sorted_damaged:
#             vehicle.is_damaged = False
#             vehicle.battery_level = 100
#             vehicle_counter += 1
#
#         return f"{vehicle_counter} vehicles were successfully repaired!"
#
#     # Generating User Report
#     def users_report(self):
#         result = ["*** E-Drive-Rent ***"]
#         sorted_users = sorted(self.users, key=lambda user: -user.rating)
#         result.append(('\n'.join(str(user) for user in sorted_users)))
#         return '\n'.join(result)
#
#     def _user_by_license(self, driving_license_number: str) -> User or None:
#         curr_user = [user for user in self.users if user.driving_license_number == driving_license_number]
#
#         if curr_user:
#             return curr_user[0]
#
#         return None
#
#     @staticmethod
#     def _create_user(first_name: str, last_name: str, driving_license_number: str) -> User:
#         return User(first_name, last_name, driving_license_number)
#
#     def _vehicle_by_plate(self, license_plate_number):
#         curr_vehicle = [vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number]
#
#         if curr_vehicle:
#             return curr_vehicle[0]
#
#         return None
#
#     def _add_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
#         return self.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
#
#     def _is_route_allowed(self, start_point, end_point) -> Route or None:
#         curr_route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point]
#
#         if curr_route:
#             return curr_route[0]
#
#         return None
#
#     def _add_route(self, start_point: str, end_point: str, length: float) -> Route:
#         index = len(self.routes) + 1
#
#         return Route(start_point, end_point, length, route_id=index)
#
#     def _route_by_id(self, route_id) -> Route or None:
#         curr_route = [r for r in self.routes if r.route_id == route_id]
#
#         if curr_route:
#             return curr_route[0]
#
#         return None
