# # 01. Jenny's Secret Message
# name = input()
#
# if name != "Johnny":
#     print(f"Hello, {name}!")
# else:
#     print(f"Hello, my love!")
#


# # 02. Drink Something
# age = int(input())
#
# if age <= 14:
#     print("drink toddy")
# elif 14 < age <= 18:
#     print("drink coke")
# elif 18 < age <= 21:
#     print("drink beer")
# else:
#     print("drink whisky")
#


# # 03. Chat Codes
# n = int(input())
#
# for _ in range(n):
#     num = int(input())
#
#     if num == 88:
#         print("Hello")
#     elif num == 86:
#         print("How are you?")
#     elif num < 88:
#         print("GREAT!")
#     else:
#         print("Bye.")
#


# # 04. Maximum Multiple
# divisor = int(input())
# boundary = int(input())
#
# num = 0
# max_num = 0
#
# for i in range(1, boundary + 1):
#     if i % divisor == 0:
#         num = i
#     if 0 < num <= boundary:
#         max_num = num
#     if num > max_num:
#         max_num = num
#
# print(max_num)
#


# # 05. Orders
# orders = int(input())   # Number of Orders
#
# total_price = 0         # Total Price of All Orders
#
# for i in range(orders):
#     price_capsule = float(input())  # Price per Capsule
#     days = int(input())             # Days
#     capsules = int(input())         # Capsules per Day
#
#     if price_capsule < 0.01 or price_capsule > 100.00:  # Correct Order Check
#         continue
#
#     if days < 1 or days > 31:   # Correct Order Check
#         continue
#
#     if capsules < 1 or capsules > 2000:     # Correct Order Check
#         continue
#
#     price = (price_capsule * capsules) * days   # Price of Each Order
#     total_price += price
#
#     print(f"The price for the coffee is: ${price:.2f}")
#
# print(f"Total: ${total_price:.2f}")
#


# # 06. String Pureness
# n = int(input())
#
# for _ in range(n):
#     text = input()
#
#     is_pure = True
#     for ch in text:
#         if ch == "," or ch == "." or ch == "_":
#             is_pure = False
#             break
#
#     if is_pure:
#         print(f"{text} is pure.")
#     else:
#         print(f"{text} is not pure!")
#


# # 07. Double Char, Version 01
# while True:
#     line = input()
#     if line == "End":
#         break
#
#     if line == "SoftUni":
#         continue
#
#     # Version 01
#     for ch in line:
#         print(f"{ch}{ch}", end="")
#
#     print()
#
#     # # Version 02
#     # converted_line = ""
#     # for ch in line:
#     #     converted_line += 2 * ch
#     #
#     # print(converted_line)
#


# # 08. How Much Coffee Do You Need
# coffee_counter = 0
#
# while True:
#     line = input()
#
#     if line == "END":
#         break
#
#     if line == "coding" or line == "dog" or line == "cat" or line == "movie":
#         coffee_counter += 1
#     elif line == "CODING" or line == "DOG" or line == "CAT" or line == "MOVIE":
#         coffee_counter += 2
#
# if coffee_counter > 5:
#     print("You need extra sleep")
# else:
#     print(coffee_counter)
#


# # 09. Sorting Hat
# while True:
#     name = input()
#
#     if name == "Voldemort":
#         print("You must not speak of that name!")
#         break
#
#     if name == "Welcome!":
#         print("Welcome to Hogwarts.")
#         break
#
#     if len(name) < 5:
#         print(f"{name} goes to Gryffindor.")
#     elif len(name) == 5:
#         print(f"{name} goes to Slytherin.")
#     elif len(name) == 6:
#         print(f"{name} goes to Ravenclaw.")
#     else:
#         print(f"{name} goes to Hufflepuff.")
#


# # 10. * Mutate Strings
# first = input()
# second = input()
#
# result = first
#
# for idx in range(len(result)):
#     if first[idx] == second[idx]:
#         continue
#
#     result = second[:idx + 1] + first[idx + 1:]
#     print(result)
#


# 11. * Easter Bread
# import math
#
# budget = float(input())             # Total Budget
# flour_1_kg = float(input())         # Price 1kg of flour
#
# eggs_1_pack = flour_1_kg * 0.75     # Price 1 Egg Carton
# milk_1_l = flour_1_kg * 1.25        # Price 1L Milk
#
# current_eggs = 0        # Eggs in possession
#
# price_per_bread = flour_1_kg + eggs_1_pack + (milk_1_l * 0.25)      # Price per 1 bread
#
# bread_count = math.floor(budget / price_per_bread)                  # Breads Produced
#
# money_left = budget - (price_per_bread * bread_count)               # Money Left
#
# for i in range(1, bread_count + 1):     # Counting Eggs
#     if i % 3 != 0:          # +3 Eggs per Loaf
#         current_eggs += 3
#     else:                   # +3 Eggs per Loaf & (Current Loaf - 2) Eggs are Broken
#         current_eggs += 3
#         current_eggs -= (i - 2)
#
# print(f"You made {bread_count} loaves of Easter bread! Now you have {current_eggs} eggs and {money_left:.2f}BGN left.")
#


# 12. * Christmas Spirit








