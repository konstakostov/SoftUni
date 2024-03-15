# # 01. OSCARS
# rent = int(input())
#
# statues = rent * 0.70
# catering = statues * 0.85
# audio = catering * 0.5
#
# total = rent + statues + catering + audio
# print(f"{total:.2f}")
#


# # 02. MOVIE DAY
# time = int(input())
# scenes = int(input())
# scene_time = int(input())
#
# preparation = time * 0.15
# time_scenes = scenes * scene_time
# time_total = time_scenes + preparation
#
# if time_total <= time:
#     print(f"You managed to finish the movie on time! You have {round(time - time_total)} minutes left!")
# else:
#     print(f"Time is up! To complete the movie you need {round(time_total - time)} minutes.")
#


# # 03. EASTER TRIP
# destination = input()
# dates = input()
# nights = int(input())
#
# price = 0
#
# if destination == "France":
#     if dates == "21-23":
#         price = nights * 30
#     elif dates == "24-27":
#         price = nights * 35
#     elif dates == "28-31":
#         price = nights * 40
#
# elif destination == "Italy":
#     if dates == "21-23":
#         price = nights * 28
#     elif dates == "24-27":
#         price = nights * 32
#     elif dates == "28-31":
#         price = nights * 39
#
# elif destination == "Germany":
#     if dates == "21-23":
#         price = nights * 32
#     elif dates == "24-27":
#         price = nights * 37
#     elif dates == "28-31":
#         price = nights * 43
#
# print(f"Easter trip to {destination} : {price:.2f} leva.")
#


# # 04. EASTER EGGS
# eggs_num = int(input())
#
# red = 0
# orange = 0
# blue = 0
# green = 0
#
# max_num = 0
# max_color = ""
#
# for i in range(eggs_num):
#     color = input()
#
#     if color == "red":
#         red += 1
#         if red > max_num:
#             max_num = red
#             max_color = "red"
#
#     elif color == "orange":
#         orange += 1
#         if orange > max_num:
#             max_num = orange
#             max_color = "orange"
#
#     elif color == "blue":
#         blue += 1
#         if blue > max_num:
#             max_num = blue
#             max_color = "blue"
#
#     elif color == "green":
#         green += 1
#         if green > max_num:
#             max_num = green
#             max_color = "green"
#
# print(f"Red eggs: {red}")
# print(f"Orange eggs: {orange}")
# print(f"Blue eggs: {blue}")
# print(f"Green eggs: {green}")
# print(f"Max eggs: {max_num} -> {max_color}")
#


# # 05. DARTS
# player = input()
#
# game = 301
# good_shots = 0
# bad_shots = 0
#
# while True:
#     sector = input()
#
#     if sector == "Retire":
#         print(f"{player} retired after {bad_shots} unsuccessful shots.")
#         break
#
#     points = int(input())
#
#     if sector == "Single":
#         points *= 1
#     elif sector == "Double":
#         points *= 2
#     elif sector == "Triple":
#         points *= 3
#
#     if points <= game and game - points >= 0:
#         game -= points
#         good_shots += 1
#     else:
#         game = game
#         bad_shots += 1
#
#     if game == 0:
#         print(f"{player} won the leg with {good_shots} shots.")
#         break
#


# # 06. EASTER DECORATION
# clients = int(input())
#
# basket_price = 1.50
# wreath_price = 3.80
# bunny_price = 7
#
# product_counter = 0
# client_price = 0
#
# total_price = 0
#
# for i in range(1, clients + 1):
#     while True:
#         product = input()
#
#         if product == "Finish":
#             if product_counter % 2 == 0:
#                 client_price *= 0.80
#             total_price += client_price
#             print(f"You purchased {product_counter} items for {client_price:.2f} leva.")
#             product_counter = 0
#             client_price = 0
#             break
#
#         if product == "basket":
#             client_price += basket_price
#         elif product == "wreath":
#             client_price += wreath_price
#         elif product == "chocolate bunny":
#             client_price += bunny_price
#
#         product_counter += 1
#
# print(f"Average bill per client is: {(total_price / clients):.2f} leva.")
#

