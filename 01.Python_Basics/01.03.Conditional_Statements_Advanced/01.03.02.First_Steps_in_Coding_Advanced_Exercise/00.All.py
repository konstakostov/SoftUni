# # CINEMA
# movie_type = input()
# rows = int(input())
# cols = int(input())
#
# income = 0
# cinema_capacity = rows * cols
#
# if movie_type == 'Premiere':
#     income = cinema_capacity * 12
# elif movie_type == 'Normal ':
#     income = cinema_capacity * 7.50
# else:
#     income = cinema_capacity * 5.00
#
# print(f"{income:.2f} leva")
#


# # SUMMER OUTFIT
# degrees = int(input())
# day_time = input()
#
# outfit = None
# shoes = None
#
# if 10 <= degrees <= 18:
#     if day_time == 'Morning':
#         outfit = 'Sweatshirt'
#         shoes = 'Sneakers'
#     elif day_time == 'Afternoon':
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     else:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#
# elif 18 < degrees <= 24:
#     if day_time == 'Morning':
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif day_time == 'Afternoon':
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
#     else:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#
# else:
#     if day_time == 'Morning':
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
#     elif day_time == 'Afternoon':
#         outfit = 'Swim Suit'
#         shoes = 'Barefoot'
#     else:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
#


# # NEW HOUSE
# flowers = input()
# flowers_count = int(input())
# budget = int(input())
#
# rose_price = 5
# dahlia_price = 3.80
# tulip_price = 2.80
# narcissus_price = 3
# gladiolus_price = 2.50
#
# total_price = 0
#
# if flowers == "Roses":
#     total_price = flowers_count * rose_price
#
#     if flowers_count >= 80:
#         total_price *= 0.90
#
# elif flowers == "Dahlias":
#     total_price = flowers_count * dahlia_price
#
#     if flowers_count >= 90:
#         total_price *= 0.85
#
# elif flowers == "Tulips":
#     total_price = flowers_count * tulip_price
#
#     if flowers_count >= 80:
#         total_price *= 0.85
#
# elif flowers == "Narcissus":
#     total_price = flowers_count * narcissus_price
#
#     if flowers_count <= 120:
#         total_price *= 1.15
#
# elif flowers == 'Gladiolus':
#     total_price = flowers_count * gladiolus_price
#
#     if flowers_count <= 90:
#         total_price *= 1.20
#
# if total_price <= budget:
#     print(f"Hey, you have 04.03.01.01.Food great garden with {flowers_count} {flowers} and {(budget - total_price):.2f} leva left.")
# else:
#     print(f"Not enough money, you need {(total_price - budget):.2f} leva more.")
#


# # FALSE AND TRUE STATEMENT
# emotion = input()   # Happy or Sad
#
# is_happy = False
#
# if emotion == "happy":
#     is_happy = True
#
# if is_happy:
#     print("I am happy for you")
# else:
#     print("What's wrong")
#


# # FISHING BOAT
# budget = int(input())
# season = input()
# fisherman = int(input())
#
# if season == "Spring":
#     rent = 3000
# elif season == "Winter":
#     rent = 2600
# else:
#     rent = 4200
#
# if fisherman <= 6:
#     rent *= 0.90
# elif 7 <= fisherman <=11:
#     rent *= 0.85
# else:
#     rent *= 0.80
#
# if fisherman % 2 == 0 and season != "Autumn":
#     rent *= 0.95
#
# if rent <= budget:
#     print(f"Yes! You have {(budget - rent):.2f} leva left.")
# else:
#     print(f"Not enough money! You need {(rent - budget):.2f} leva.")
#


# # BUDGET
# budget = float(input())
# season = input()
#
# price = 0
# destination = None
# place = None
#
# if budget <= 100:
#     destination = "Bulgaria"
#
#     if season == "summer":
#         place = "Camp"
#         price = budget * 0.30
#     else:
#         place = "Hotel"
#         price = budget * 0.70
#
# elif budget <= 1000:
#     destination = "Balkans"
#
#     if season == "summer":
#         place = "Camp"
#         price = budget * 0.40
#     else:
#         place = "Hotel"
#         price = budget * 0.80
#
# else:
#     destination = "Europe"
#     place = "Hotel"
#     price = budget * 0.90
#
# print(f"Somewhere in {destination}")
# print(f"{place} - {price:.2f}")
#


# # OPERATIONS BETWEEN NUMBERS
# num1 = int(input())
# num2 = int(input())
# operator = input()
#
# result = None
#
# if operator == "+":
#     result = f"{num1} + {num2} = {num1 + num2}" + (" - even" if (num1 + num2) % 2 == 0 else " - odd")
#
# elif operator == "-":
#     result = f"{num1} - {num2} = {num1 - num2}" + (" - even" if (num1 - num2) % 2 == 0 else " - odd")
#
# elif operator == "*":
#     result = f"{num1} * {num2} = {num1 * num2}" + (" - even" if (num1 * num2) % 2 == 0 else " - odd")
#
# elif num2 == 0:
#     result = f"Cannot divide {num1} by zero"
#
# elif operator == "/":
#     result = f"{num1} / {num2} = {(num1 / num2):.2f}"
#
# elif operator == "%":
#     result = f"{num1} % {num2} = {num1 % num2}"
#
# print(result)
#


# # HOTEL ROOM
# month = input()
# nights = int(input())
#
# studio = 0
# apartment = 0
#
# if month == "May" or "October":
#     studio = 50
#     apartment = 65
#
#     if nights > 14:
#         studio *= 0.70
#     elif nights > 7:
#         studio *= 0.95
#
# elif month == "June" or "September":
#     studio = 75.20
#     apartment = 68.70
#
#     if nights > 14:
#         studio *= 0.80
#
# else:
#     studio = 76
#     apartment = 77
#
# if nights > 14:
#     apartment *= 0.90
#
# print(f"Apartment: {(nights * apartment):.2f} lv")
# print(f"Studio: {(nights * studio):.2f} lv.")
#


# # ON TIME FOR EXAM
# exam_hour = int(input())
# exam_minutes = int(input())
#
# arrival_hour = int(input())
# arrival_minutes = int(input())
#
# exam_time_in_minutes = exam_hour * 60 + exam_minutes
# arrival_time_in_minutes = arrival_hour * 60 + arrival_minutes
#
# time_diff = exam_time_in_minutes - arrival_time_in_minutes
#
# if time_diff > 30:
#     print("Early")
# elif time_diff < 0:
#     print("Late")
# else:
#     print("On time")
#
# hours = 0
# minutes = abs(time_diff)
#
# if minutes >= 60:
#     hours = minutes // 60
#     minutes = minutes % 60
#
# result = ""
#
# if hours > 0:
#     result += str(hours) + ":" + ("0" + str(minutes) if minutes < 10 else str(minutes)) + " hours"
# else:
#     result += str(minutes) + " minutes"
#
# if time_diff >= 0:
#     result += " before the start"
# else:
#     result += " after the start"
#
# print(result)
#


# # SKI TRIP
# nights = int(input()) - 1
# suite = input()
# review = input()
#
# price = 0
# if suite == "room for one person":
#     price = 18
#
# elif suite == "apartment":
#     price = 25
#
#     if nights < 10:
#         price *= 0.70
#     elif 10 <= nights <= 15:
#         price *= 0.65
#     else:
#         price *= 0.50
#
# else:
#     price = 35
#
#     if nights < 10:
#         price *= 0.90
#     elif 10 <= nights <= 15:
#         price *= 0.85
#     else:
#         price *= 0.80
#
# if review == "positive":
#     price *= 1.25
# else:
#     price *= 0.90
#
# print(f"{(price * nights):.2f}")
#



