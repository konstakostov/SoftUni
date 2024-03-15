# # 02.12.01. Activation Keys
# key = input()
# command = input()
# while command != "Generate":
#     instructions = command.split(">>>")
#
#     if instructions[0] == "Contains":
#         substring = instructions[1]
#
#         if substring in key:
#             print(f"{key} contains {substring}")
#         else:
#             print("Substring not found!")
#
#     elif instructions[0] == "Flip":
#         casing = instructions[1]
#         start_index = int(instructions[2])
#         end_index = int(instructions[3])
#
#         if casing == "Upper":
#             key = key[:start_index] + key[start_index:end_index].upper() + key[end_index::]
#         elif casing == "Lower":
#             key = key[:start_index] + key[start_index:end_index].lower() + key[end_index::]
#         print(key)
#
#     elif instructions[0] == "Slice":
#         start_index = int(instructions[1])
#         end_index = int(instructions[2])
#
#         key = key[:start_index] + key[end_index::]
#         print(key)
#
#     command = input()
#
# print(f"Your activation key is: {key}")
#


# # 02.12.01. Password Reset
# password = input()
# command = input()
# while command != "Done":
#     action = command.split()
#
#     if action[0] == "TakeOdd":
#         odd_text = ""
#         index = 0
#
#         for i in range(1, len(password), 2):
#             odd_text += password[i]
#
#         password = odd_text
#         print(password)
#
#     elif action[0] == "Cut":
#         index = int(action[1])
#         length = int(action[2])
#
#         password = password[:index] + password[(index + length)::]
#         print(password)
#
#     elif action[0] == "Substitute":
#         substring = action[1]
#         substitute = action[2]
#
#         if substring in password:
#             password = password.replace(substring, substitute)
#             print(password)
#         else:
#             print("Nothing to replace!")
#
#     command = input()
#
# print(f"Your password is: {password}")
#


# # 02.12.01. Secret Chat
# message = input()
# command = input()
# while command != "Reveal":
#     instructions = command.split(":|:")
#
#     if instructions[0] == "InsertSpace":
#         index = int(instructions[1])
#         message = message[:index] + " " + message[index::]
#         print(message)
#
#     elif instructions[0] == "Reverse":
#         substring = instructions[1]
#
#         if substring in message:
#             message = message.replace(substring, "", 1)
#             message += substring[::-1]
#             print(message)
#         else:
#             print("error")
#
#     elif instructions[0] == "ChangeAll":
#         substring = instructions[1]
#         replacement = instructions[2]
#         message = message.replace(substring, replacement)
#         print(message)
#
#     command = input()
#
# print(f"You have 04.03.01.01.Food new text message: {message}")
#


# # 02.12.01. The Imitation Game
# message = input()
#
# while True:
#     command = input()
#     if command == "Decode":
#         print(f"The decrypted message is: {message}")
#         break
#
#     instructions = command.split("|")
#
#     if instructions[0] == "Move":
#         num_letters = int(instructions[1])
#         letters = message[:num_letters]
#         message = message[num_letters::] + letters
#
#     elif instructions[0] == "Insert":
#         index = int(instructions[1])
#         value = instructions[2]
#         message = message[:index] + value + message[index::]
#
#     elif instructions[0] == "ChangeAll":
#         substring = instructions[1]
#         replacement = instructions[2]
#         message = message.replace(substring, replacement)
#


# # 02.12.01. World Tour
# text = input()
#
# while True:
#     command = input()
#     if command == "Travel":
#         print(f"Ready for world tour! Planned stops: {text}")
#         break
#
#     instructions = command.split(":")
#
#     if instructions[0] == "Add Stop":
#         index = int(instructions[1])
#         stop = instructions[2]
#
#         if 0 <= index < len(text):
#             text = text[:index] + stop + text[index::]
#
#     elif instructions[0] == "Remove Stop":
#         start_index = int(instructions[1])
#         end_index = int(instructions[2])
#
#         if 0 <= start_index < len(text) and 0 <= end_index < len(text):
#             text = text[:start_index] + text[end_index + 1::]
#
#     elif instructions[0] == "Switch":
#         substring = instructions[1]
#         replacement = instructions[2]
#
#         if substring in text:
#             text = text.replace(substring, replacement)
#
#     print(text)
#


# # 02.12.02. Ad Astra
# import re
#
# text = input()
# pattern = r"(\#|\|)([04.03.01.01.Food-zA-Z\ ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
#
# matches = re.findall(pattern, text)
#
# total_calories = 0
# for match in matches:
#     total_calories += int(match[3])
#
# print(f"You have food to last you for: {total_calories // 2000} days!")
#
# for info in matches:
#     print(f"Item: {info[1]}, Best before: {info[2]}, Nutrition: {info[3]}")
#


# # 02.12.02. Destination Mapper
# import re
#
# text = input()
# pattern = r"(\=|\/)([A-Z][04.03.01.01.Food-zA-Z\ ]{2,})\1"
#
# matches = re.findall(pattern, text)
#
# destinations = []
# travel_points = 0
#
# for match in matches:
#     destinations.append(match[1])
#     travel_points += len(match[1])
#
# if destinations:
#     print(f"Destinations: {', '.join(destinations)}")
#     print(f"Travel Points: {travel_points}")
# else:
#     print(f"Destinations:")
#     print(f"Travel Points: 0")
#


# # 02.12.02. Emoji Detector
# import re
#
# text = input()
# pattern = r"\:{2}[A-Z][04.03.01.01.Food-z]{2,}\:{2}|\*{2}[A-Z][04.03.01.01.Food-z]{2,}\*{2}"
# cool_pattern = r"\d"
#
# cool_threshold = 1
# emojis = []
# cool_emojis = []
#
# coolness = re.findall(cool_pattern, text)
# for cool in coolness:
#     cool_threshold *= int(cool)
#
# matches = re.findall(pattern, text)
# for match in matches:
#     emojis.append(match)
#
# for emoji in emojis:
#     cool_score = 0
#     for char in emoji:
#         if char != ":" and char != "*":
#             cool_score += ord(char)
#
#     if cool_score > cool_threshold:
#         cool_emojis.append(emoji)
#
# print(f"Cool threshold: {cool_threshold}")
# print(f"{len(emojis)} emojis found in the text. The cool ones are:")
# print('\n'.join(cool_emojis))
#


# # 02.12.02. Fancy Barcodes
# import re
# num_input = int(input())
#
# for i in range(num_input):
#     text = input()
#     pattern = r"\@\#+[A-Z][04.03.01.01.Food-zA-Z0-9]{4,}[A-Z]\@\#+"
#     group = ""
#
#     match = re.findall(pattern, text)
#
#     if match:
#         for product in match:
#             for char in product:
#                 if char.isdigit():
#                     group += char
#
#         if len(group) > 0:
#             print(f"Product group: {group}")
#         else:
#             group = "00"
#             print(f"Product group: {group}")
#
#     else:
#         print("Invalid barcode")
#


# # 02.12.02. Mirror Words
# import re
#
# text = input()
# pattern = r"(\@|\#)([04.03.01.01.Food-zA-Z]{3,})\1\1([04.03.01.01.Food-zA-Z]{3,})\1"
#
# matches = re.finditer(pattern, text)
#
# word_pairs = 0
# mirror_words = []
#
# for match in matches:
#     if match[2] == match[3][::-1]:
#         mirror_word = match[2] + " <=> " + match[3]
#         mirror_words.append(mirror_word)
#     word_pairs += 1
#
# if word_pairs == 0:
#     print("No word pairs found!")
# else:
#     print(f"{word_pairs} word pairs found!")
#
# if mirror_words:
#     print("The mirror words are:")
#     print(', '.join(mirror_words))
# else:
#     print("No mirror words!")
#


# # 02.12.03. Heroes of Code and Logic VII
# num_heroes = int(input())
# heroes = {}
#
# for i in range(num_heroes):
#     name, health, mana = input().split()
#     heroes[name] = heroes.get(name, {'health': int(health), 'mana': int(mana)})
#
# command = input()
# while command != "End":
#     info = command.split(" - ")
#
#     if info[0] == "CastSpell":
#         name = info[1]
#         mana_needed = int(info[2])
#         spell = info[3]
#
#         if heroes[name]['mana'] >= mana_needed:
#             heroes[name]['mana'] -= mana_needed
#             print(f"{name} has successfully cast {spell} and now has {heroes[name]['mana']} MP!")
#         else:
#             print(f"{name} does not have enough MP to cast {spell}!")
#
#     elif info[0] == "TakeDamage":
#         name = info[1]
#         damage = int(info[2])
#         attacker = info[3]
#
#         heroes[name]['health'] -= damage
#         if heroes[name]['health'] > 0:
#             print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['health']} HP left!")
#         else:
#             del heroes[name]
#             print(f"{name} has been killed by {attacker}!")
#
#     elif info[0] == "Recharge":
#         name = info[1]
#         recharge = int(info[2])
#
#         heroes[name]['mana'] += recharge
#         if heroes[name]['mana'] <= 200:
#             print(f"{name} recharged for {recharge} MP!")
#         else:
#             recharged = abs(heroes[name]['mana'] - 200 - recharge)
#             heroes[name]['mana'] = 200
#             print(f"{name} recharged for {recharged} MP!")
#
#     elif info[0] == "Heal":
#         name = info[1]
#         heal = int(info[2])
#
#         heroes[name]['health'] += heal
#         if heroes[name]['health'] <= 100:
#             print(f"{name} healed for {heal} HP!")
#         else:
#             healed = abs(heroes[name]['health'] - 100 - heal)
#             heroes[name]['health'] = 100
#             print(f"{name} healed for {healed} HP!")
#
#     command = input()
#
# for name, value in heroes.items():
#     print(name)
#     print(f"  HP: {value['health']}")
#     print(f"  MP: {value['mana']}")
#


# # 02.12.03. Need for Speed III
# num_cars = int(input())
# garage = {}
#
# for _ in range(num_cars):
#     car, mileage, fuel = input().split("|")
#     garage[car] = garage.get(car, {'mileage': int(mileage), 'fuel': int(fuel)})
#
# command = input()
# while command != "Stop":
#     info = command.split(" : ")
#
#     if info[0] == "Drive":
#         car = info[1]
#         distance = int(info[2])
#         fuel_needed = int(info[3])
#
#         if garage[car]['fuel'] >= fuel_needed:
#             garage[car]['fuel'] -= fuel_needed
#             garage[car]['mileage'] += distance
#             print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
#         else:
#             print("Not enough fuel to make that ride")
#
#         if garage[car]['mileage'] >= 100000:
#             del garage[car]
#             print(f"Time to sell the {car}!")
#
#     elif info[0] == "Refuel":
#         car = info[1]
#         refill = int(info[2])
#
#         garage[car]['fuel'] += refill
#         if garage[car]['fuel'] <= 75:
#             print(f"{car} refueled with {refill} liters")
#         else:
#             refilled = abs(garage[car]['fuel'] - 75 - refill)
#             garage[car]['fuel'] = 75
#             print(f"{car} refueled with {refilled} liters")
#
#     elif info[0] == "Revert":
#         car = info[1]
#         kilometers = int(info[2])
#
#         garage[car]['mileage'] -= kilometers
#         if garage[car]['mileage'] <= 10000:
#             garage[car]['mileage'] = 10000
#         else:
#             print(f"{car} mileage decreased by {kilometers} kilometers")
#
#     command = input()
#
# for car, value in garage.items():
#     print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
#


# # 02.12.03. Pirates
# settlements = {}
#
# while True:
#     command = input()
#     if command == "Sail":
#         break
#
#     town, people, gold = command.split("||")
#
#     if town not in settlements:
#         settlements[town] = settlements.get(town, {'people': 0, 'gold': 0})
#
#     settlements[town]['people'] += int(people)
#     settlements[town]['gold'] += int(gold)
#
# while True:
#     events = input()
#     if events == "End":
#         break
#
#     info = events.split("=>")
#
#     if info[0] == "Plunder":
#         town = info[1]
#         people = int(info[2])
#         gold = int(info[3])
#
#         settlements[town]['people'] -= people
#         settlements[town]['gold'] -= gold
#         print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
#
#         if settlements[town]['people'] <= 0 or settlements[town]['gold'] <= 0:
#             del settlements[town]
#             print(f"{town} has been wiped off the map!")
#
#     elif info[0] == "Prosper":
#         town = info[1]
#         gold = int(info[2])
#
#         if gold < 0:
#             print("Gold added cannot be 04.03.01.01.Food negative number!")
#             continue
#         else:
#             settlements[town]['gold'] += gold
#             print(f"{gold} gold added to the city treasury. {town} now has {settlements[town]['gold']} gold.")
#
# if settlements:
#     print(f"Ahoy, Captain! There are {len(settlements)} wealthy settlements to go to:")
#     for town, value in settlements.items():
#         print(f"{town} -> Population: {value['people']} citizens, Gold: {value['gold']} kg")
# else:
#     print("Ahoy, Captain! All targets have been plundered and destroyed!")
#


# # 02.12.03. Plant Discovery
# num_plants = int(input())
# garden = {}
#
# for _ in range(num_plants):
#     plant, rarity = input().split("<->")
#
#     if plant not in garden:
#         garden[plant] = garden.get(plant, {'rarity': 0, 'rating': []})
#
#     garden[plant]['rarity'] = int(rarity)
#
# command = input()
# while command != "Exhibition":
#     action, info = command.split(": ")
#
#     if action == "Rate":
#         plant, rating = info.split(" - ")
#
#         if plant in garden:
#             garden[plant]['rating'].append(rating)
#         else:
#             print("error")
#
#     elif action == "Update":
#         plant, rarity = info.split(" - ")
#
#         if plant in garden:
#             garden[plant]['rarity'] = rarity
#         else:
#             print("error")
#
#     elif action == "Reset":
#         plant = info
#
#         if plant in garden:
#             garden[plant]['rating'] = []
#         else:
#             print("error")
#
#     command = input()
#
# if garden:
#     print("Plants for the exhibition:")
#     for plant, value in garden.items():
#         average_rating = 0
#
#         if len(value['rating']) > 0:
#             for rate in value['rating']:
#                 average_rating += float(rate)
#             average_rating /= len(value['rating'])
#         else:
#             average_rating = 0
#
#         print(f"- {plant}; Rarity: {value['rarity']}; Rating: {average_rating:.2f}")
#


# # 02.12.03. The Pianist
# num_pieces = int(input())
# piano_pieces = {}
#
# for _ in range(num_pieces):
#     piece, composer, key = input().split("|")
#
#     if piece not in piano_pieces:
#         piano_pieces[piece] = piano_pieces.get(piece, {'composer': composer, 'key': key})
#
# command = input()
# while command != "Stop":
#     info = command.split("|")
#
#     if info[0] == "Add":
#         piece = info[1]
#         composer = info[2]
#         key = info[3]
#
#         if piece in piano_pieces:
#             print(f"{piece} is already in the collection!")
#         else:
#             piano_pieces[piece] = piano_pieces.get(piece, {'composer': composer, 'key': key})
#             print(f"{piece} by {composer} in {key} added to the collection!")
#
#     elif info[0] == "Remove":
#         piece = info[1]
#
#         if piece in piano_pieces:
#             del piano_pieces[piece]
#             print(f"Successfully removed {piece}!")
#         else:
#             print(f"Invalid operation! {piece} does not exist in the collection.")
#
#     elif info[0] == "ChangeKey":
#         piece = info[1]
#         new_key = info[2]
#
#         if piece in piano_pieces:
#             piano_pieces[piece]['key'] = new_key
#             print(f"Changed the key of {piece} to {new_key}!")
#         else:
#             print(f"Invalid operation! {piece} does not exist in the collection.")
#
#     command = input()
#
# for piece, value in piano_pieces.items():
#     print(f"{piece} -> Composer: {value['composer']}, Key: {value['key']}")
#
