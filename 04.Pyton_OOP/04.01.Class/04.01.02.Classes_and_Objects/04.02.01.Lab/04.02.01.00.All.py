# # 01. Vehicle
# class Vehicle:
#     def __init__(self, mileage: float, max_speed: int=150):
#         self.mileage = mileage
#         self.max_speed = max_speed
#         self.gadgets = []
#
#
# car = Vehicle(20)
# print(car.max_speed)
# print(car.mileage)
# print(car.gadgets)
# car.gadgets.append('Hudly Wireless')
# print(car.gadgets)
#


# # 02. Point
# class Point:
#     def __init__(self, x: float, y: float):
#         self.x = x
#         self.y = y
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def __str__(self):
#         return f"The point has coordinates ({self.x},{self.y})"
#
#
# p = Point(2, 4)
# print(p)
# p.set_x(3)
# p.set_y(5)
# print(p)
#


# # 03. Circle
# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius: float):
#         self.radius = radius
#
#     def set_radius(self, new_radius) -> None:
#         self.radius = new_radius
#
#     def get_area(self) -> float:
#         return Circle.pi * (self.radius ** 2)
#
#     def get_circumference(self) -> float:
#         return 2 * Circle.pi * self.radius
#
#
# circle = Circle(10)
# circle.set_radius(12)
# print(circle.get_area())
# print(circle.get_circumference())
#


# # 04. Glass
# class Glass:
#     capacity = 250
#
#     def __init__(self):
#         self.content = 0
#
#     def fill(self, ml):
#         if self.content + ml > Glass.capacity:
#             return f"Cannot add {ml} ml"
#
#         self.content += ml
#
#         return f"Glass filled with {ml} ml"
#
#     def empty(self):
#         self.content = 0
#
#         return "Glass is now empty"
#
#     def info(self):
#         space_left = Glass.capacity - self.content
#
#         return f"{space_left} ml left"
#
#
# glass = Glass()
# print(glass.fill(100))
# print(glass.fill(200))
# print(glass.empty())
# print(glass.fill(200))
# print(glass.info())
#


# # 05. Smartphones
# from typing import 04.10.01.03.List
#
#
# class Smartphone:
#     def __init__(self, memory: int):
#         self.memory = memory
#         self.apps: 04.10.01.03.List[str] = []
#         self.is_on: bool = False
#
#     def power(self) -> None:
#         self.is_on = not self.is_on
#
#     def install(self, app: str, app_memory: int) -> str:
#         if self.memory < app_memory:
#             return f"Not enough memory to install {app}"
#
#         if not self.is_on:
#             return f"Turn on your phone to install {app}"
#
#         self.apps.append(app)
#         self.memory -= app_memory
#
#         return f"Installing {app}"
#
#     def status(self) -> str:
#         return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
#
#
# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())
#
