# # 01. Count Chars in 04.03.01.01.Food String
# current_input = input().split()
# symbols = "".join(current_input)
# characters = {}
#
# for symbol in symbols:
#     if symbol not in characters.keys():
#         characters[symbol] = 0
#     characters[symbol] += 1
#
# for char, quantity in characters.items():
#     print(f"{char} -> {quantity}")
#


# # 02. Miner Task
# resources = {}
#
# while True:
#     resource = input()
#     if resource == "stop":
#         break
#     quantity = int(input())
#
#     if resource not in resources:
#         resources[resource] = 0
#
#     resources[resource] += quantity
#
# for resource, quantity in resources.items():
#     print(f"{resource} -> {quantity}")
#


# # 03. Capitals
# countries = input().split(", ")
# capitals = input().split(", ")
# result = list(zip(countries, capitals))
# print(result)
#


# # 04. Phonebook
# phonebook = {}
#
# while True:
#     entry = input()
#
#     if "-" not in entry:
#         break
#
#     name, phone = entry.split("-")
#     phonebook[name] = phone
#
# for check in range(int(entry)):
#     searched_name = input()
#
#     if searched_name in phonebook.keys():
#         print(f"{searched_name} -> {phonebook[searched_name]}")
#     else:
#         print(f"Contact {searched_name} does not exist.")
#


# # 05. Legendary Farming
# items = {"shards": 0, "fragments": 0, "motes": 0}
#
# current_items = input().split()
# obtained = False
#
# while not obtained:
#     for index in range(0, len(current_items), 2):
#         value = int(current_items[index])
#         key = current_items[index + 1].lower()
#
#         if key not in items.keys():
#             items[key] = 0
#         items[key] += value
#
#         if items["shards"] >= 250:
#             print("Shadowmourne obtained!")
#             items["shards"] -= 250
#             obtained = True
#
#         elif items["fragments"] >= 250:
#             print("Valanyr obtained!")
#             items["fragments"] -= 250
#             obtained = True
#
#         elif items["motes"] >= 250:
#             print("Dragonwrath obtained!")
#             items["motes"] -= 250
#             obtained = True
#
#         if obtained:
#             break
#     if obtained:
#         break
#
#     current_items = input().split()
#
# for material, quantity in items.items():
#     print(f"{material}: {quantity}")
#


# # 07. SoftUni Parking
# parking = {}
# number_of_cars = int(input())
#
# for car in range(number_of_cars):
#     current_driver = input().split()
#     action = current_driver[0]
#
#     if action == "register":
#         username = current_driver[1]
#         license_plate_number = current_driver[2]
#
#         if username in parking.keys():
#             print(f"ERROR: already registered with plate number {license_plate_number}")
#         else:
#             parking[username] = license_plate_number
#             print(f"{username} registered {license_plate_number} successfully")
#
#     elif action == "unregister":
#         username = current_driver[1]
#
#         if username not in parking.keys():
#             print(f"ERROR: user {username} not found")
#         else:
#             print(f"{username} unregistered successfully")
#             del parking[username]
# for username, license_plate_number in parking.items():
#     print(f"{username} => {license_plate_number}")
#


