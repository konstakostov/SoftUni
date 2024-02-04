# Some Example
# class Bottle:
#     def __init__(self, ml, name, color, material="Plastic"):
#         self.ml = ml
#         self.name = name
#         self.color = color
#         self.material = material
#
#     def open(self):
#         print("Opening bottle")
#
#     def close(self):
#         print("Closing bottle")
#
#
# bottle1 = Bottle(500, "Devin", "Blue", "Glass")
# bottle2 = Bottle(1500, "Devin", "Pink")
# bottle3 = Bottle(600, "Gorna Banya", "Blue")
#
# print(bottle1.ml, bottle1.material)
# print(bottle2.name)
# print(bottle3.color)
#

# # 01.Comment
# class Comment:
#     def __init__(self, username, content, likes=0):
#         self.username = username
#         self.content = content
#         self.likes = likes
#


# # 02. Party
# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
# line = input()
#
# while line != "End":
#     party.people.append(line)
#     line = input()
#
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")
#


# # 03. Email
# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
#
# emails = []
# data = input()
#
# while data != "Stop":
#     sender, receiver, content = data.split()
#     email = Email(sender, receiver, content)
#     emails.append(email)
#
#     data = input()
#
# sent_emails_indexes = [int(idx) for idx in input().split(", ")]
#
# for index, email in enumerate(emails):
#     if index in sent_emails_indexes:
#         emails[index].send()
#     print(f"{email.sender} says to {email.receiver}: "
#           f"{email.content}. Sent: {email.is_sent}")
#


# 04. Zoo
# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "04.10.02.01.Mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ""
#
#         if species == "04.10.02.01.Mammal":
#             result = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == "fish":
#             result = f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
#         elif species == "bird":
#             result = f"Birds in {self.name}: {', '.join(self.birds)}\n"
#
#         result += f"Total animals: {Zoo.__animals}"
#         return result
#
#
# zoo_name = input()
# animals_count = int(input())
#
# zoo = Zoo(zoo_name)
#
# for i in range(animals_count):
#     species, name = input().split()
#     zoo.add_animal(species, name)
#
# info = input()
# print(zoo.get_info(info))
#


# 05. Circle
