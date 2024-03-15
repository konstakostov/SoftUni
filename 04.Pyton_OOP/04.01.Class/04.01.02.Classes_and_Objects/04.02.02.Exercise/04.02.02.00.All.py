# # 01. Vet
# from typing import 04.10.01.03.List
#
#
# class Vet:
#     animals: 04.10.01.03.List[str] = []
#     space = 5
#
#     def __init__(self, name: str):
#         self.name = name
#         self.animals: 04.10.01.03.List[str] = []
#
#     def register_animal(self, animal_name) -> str:
#         if len(self.animals) >= Vet.space:
#             return f"Not enough space"
#
#         self.animals.append(animal_name)
#         Vet.animals.append(animal_name)
#
#         return f"{animal_name} registered in the clinic"
#
#     def unregister_animal(self, animal_name) -> str:
#         if animal_name not in self.animals:
#             return f"{animal_name} not in the clinic"
#
#         self.animals.remove(animal_name)
#         Vet.animals.remove(animal_name)
#
#         return f"{animal_name} unregistered successfully"
#
#     def info(self) -> str:
#         return f"{self.name} has {len(self.animals)} animals. " \
#                f"{Vet.space - len(Vet.animals)} space left in clinic"
#
#
# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())
#


# # 02. Time
# class Time:
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours: int, minutes: int, seconds: int):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def set_time(self, hours: int, minutes: int, seconds: int) -> None:
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def get_time(self) -> str:
#         return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
#
#     def update_valid_time(self) -> None:
#         if self.seconds > Time.max_seconds:
#             self.seconds = 0
#             self.minutes += 1
#
#             if self.minutes > Time.max_minutes:
#                 self.minutes = 0
#                 self.hours += 1
#
#                 if self.hours > Time.max_hours:
#                     self.hours = 0
#
#     def next_second(self) -> str:
#         self.seconds += 1
#
#         self.update_valid_time()
#
#         return self.get_time()
#
#
# time = Time(9, 30, 59)
# print(time.next_second())
#
# time = Time(10, 59, 59)
# print(time.next_second())
#
# time = Time(23, 59, 59)
# print(time.next_second())
#


# 03. Account


# 04. Pizza Delivery


# # 05. To-do 04.10.01.03.List
# 05.01. Section


# 05.02. Task



