# # 01. Shop
# from typing import 04.10.01.03.List
#
#
# class Shop:
#     def __init__(self, name: str, items: 04.10.01.03.List[str]):
#         self.name = name
#         self.items = items
#
#     def get_items_count(self):
#         return len(self.items)
#
#
# shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
# print(shop.get_items_count())
#


# # 02. Hero
# class Hero:
#     def __init__(self, name: str, health: float or int):
#         self.name = name
#         self.health = health
#
#     def defend(self, damage: float or int) -> None or str:
#         self.health -= damage
#
#         if self.health <= 0:
#             return f"{self.name} was defeated"
#
#     def heal(self, amount: float or int) -> None:
#         self.health += amount
#
#
# 04.10.02.03.Hero = Hero("Peter", 100)
# print(04.10.02.03.Hero.defend(50))
# 04.10.02.03.Hero.heal(50)
# print(04.10.02.03.Hero.defend(99))
# print(04.10.02.03.Hero.defend(1))
#


# # 03. Employee
# class Employee:
#     MONTHS = 12
#
#     def __init__(self, id: int or float, first_name: str, last_name: str, salary: float or int):
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#
#     def get_full_name(self) -> str:
#         return f"{self.first_name} {self.last_name}"
#
#     def get_annual_salary(self) -> int or float:
#         return self.salary * Employee.MONTHS
#
#     def raise_salary(self, amount: int or float) -> int or float:
#         self.salary += amount
#         return self.salary
#
#
# employee = Employee(744423129, "John", "Smith", 1000)
# print(employee.get_full_name())
# print(employee.raise_salary(500))
# print(employee.get_annual_salary())
#


# # 04. Cup
# class Cup:
#     def __init__(self, size: int, quantity: int):
#         self.size = size
#         self.quantity = quantity
#
#     def fill(self, quantity: int) -> None:
#         if self.quantity + quantity <= self.size:
#             self.quantity += quantity
#
#     def status(self) -> int:
#         return self.size - self.quantity
#
#
# cup = Cup(100, 50)
# print(cup.status())
# cup.fill(40)
# cup.fill(20)
# print(cup.status())
#


# # 05. Flower
# class Flower:
#     def __init__(self, name: str, water_requirement: float or int):
#         self.name = name
#         self.water_requirement = water_requirement
#         self.is_happy = False
#
#     def water(self, quantity: float or str):
#         if quantity >= self.water_requirement:
#             self.is_happy = True
#
#     def status(self):
#         return f"{self.name} is {'' if self.is_happy else 'not '}happy"
#
#
# flower = Flower("Lilly", 100)
# flower.water(50)
# print(flower.status())
# flower.water(60)
# print(flower.status())
# flower.water(100)
# print(flower.status())
#


# # 06. Steam User
# from typing import 04.10.01.03.List
#
#
# class SteamUser:
#     def __init__(self, username: str, games: 04.10.01.03.List[str]):
#         self.username = username
#         self.games = games
#         self.played_hours = 0
#
#     def play(self, game, hours) -> str:
#         if game not in self.games:
#             return f"{game} is not in library"
#
#         self.played_hours += hours
#
#         return f"{self.username} is playing {game}"
#
#     def buy_game(self, game) -> str:
#         if game in self.games:
#             return f"{game} is already in your library"
#
#         self.games.append(game)
#
#         return f"{self.username} bought {game}"
#
#     def status(self) -> str:
#         return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
#
#
# user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
# print(user.play("Fortnite", 3))
# print(user.play("Oxygen Not Included", 5))
# print(user.buy_game("CS:GO"))
# print(user.buy_game("Oxygen Not Included"))
# print(user.play("Oxygen Not Included", 6))
# print(user.status())
#


# # 07. Programmer
# class Programmer:
#     def __init__(self, name: str, language: str, skills: int):
#         self.name = name
#         self.language = language
#         self.skills = skills
#
#     def watch_course(self, course_name, language, skills_earned) -> str:
#         if language != self.language:
#             return f"{self.name} does not know {language}"
#
#         self.skills += skills_earned
#
#         return f"{self.name} watched {course_name}"
#
#     def change_language(self, new_language, skills_needed) -> str:
#         if skills_needed <= self.skills:
#             if self.language != new_language:
#                 previous_language = self.language
#                 self.language = new_language
#
#                 return f"{self.name} switched from {previous_language} to {new_language}"
#
#             return f"{self.name} already knows {self.language}"
#
#         return f"{self.name} needs {skills_needed - self.skills} more skills"
#
#
# programmer = Programmer("John", "Java", 50)
# print(programmer.watch_course("Python Masterclass", "Python", 84))
# print(programmer.change_language("Java", 30))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Java: zero to 04.10.02.03.Hero", "Java", 50))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Python Masterclass", "Python", 84))
#
