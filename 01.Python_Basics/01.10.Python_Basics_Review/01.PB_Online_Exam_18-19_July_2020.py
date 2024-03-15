# # 01. Agency Profit; PB Online Exam 18-19 July 2020
#
# name = input()
# adult_tickets = int(input())
# kid_tickets = int(input())
# adult_price = float(input())
# kid_price = adult_price * 0.30
# service_price = float(input())
#
# adult_total = (adult_tickets * adult_price) + (adult_tickets * service_price)
# kid_total = (kid_tickets * kid_price) + (kid_tickets * service_price)
#
# total_price = adult_total + kid_total
#
# profit_agency = total_price * 0.20
#
# print(f"The profit of your agency from {name} tickets is {profit_agency:.2f} lv.")
#

# # 02. Add Bags; PB Online Exam 18-19 July 2020
#
# price_above_20_kg = float(input())
# bags_kg = float(input())
# days_till_travel = int(input())
# bags_quantity = int(input())
#
# price_bags = 0
#
# # Bags prices per total kg
# if bags_kg < 10:
#     price_bags = price_above_20_kg * 0.20
# elif 10 <= bags_kg <= 20:
#     price_bags = price_above_20_kg * 0.50
# elif bags_kg > 20:
#     price_bags = price_above_20_kg
#
# # Bags prices per days left to travel
# if days_till_travel > 30:
#     price_bags *= 1.10
# elif 7 <= days_till_travel <= 30:
#     price_bags *= 1.15
# elif days_till_travel < 7:
#     price_bags *= 1.40
#
# # Total bags price
# price_bags *= bags_quantity
#
# print(f" The total price of bags is: {price_bags:.2f} lv.")
#


# # 03. Aluminum Joinery; PB Online Exam 18-19 July 2020
# #
# joinery_quantity = int(input())
# joinery_type = input()
# delivery = input()
#
# if joinery_quantity < 10:
#     print("Invalid order")
#     exit()
#
# single_price = 0
# discount = 0
# total_price = 0
#
# if joinery_type == "90X130":
#     single_price = 110
#
#     if joinery_quantity > 60:
#         discount = 0.08
#     elif joinery_quantity > 30:
#         discount = 0.05
#     else:
#         discount = 0
#     total_price = joinery_quantity * single_price
#     total_price = total_price - total_price * discount
#
#     if delivery == "With delivery":
#         total_price += 60
#     elif delivery == "Without delivery":
#         total_price += 0
#
# elif joinery_type == "100X150":
#     single_price = 140
#     if joinery_quantity > 80:
#         discount = 0.10
#     elif joinery_quantity > 40:
#         discount = 0.06
#     else:
#         discount = 0
#     total_price = joinery_quantity * single_price
#     total_price = total_price - total_price * discount
#
#     if delivery == "With delivery":
#         total_price += 60
#     elif delivery == "Without delivery":
#         total_price += 0
#
# elif joinery_type == "130X180":
#     single_price = 190
#     if joinery_quantity > 50:
#         discount = 0.12
#     elif joinery_quantity > 20:
#         discount = 0.07
#     else:
#         discount = 0
#     total_price = joinery_quantity * single_price
#     total_price = total_price - total_price * discount
#
#     if delivery == "With delivery":
#         total_price += 60
#     elif delivery == "Without delivery":
#         total_price += 0
#
# elif joinery_type == "200X300":
#     single_price = 250
#     if joinery_quantity > 50:
#         discount = 0.14
#     elif joinery_quantity > 25:
#         discount = 0.09
#     else:
#         discount = 0
#     total_price = joinery_quantity * single_price
#     total_price = total_price - total_price * discount
#
#     if delivery == "With delivery":
#         total_price += 60
#     elif delivery == "Without delivery":
#         total_price += 0
#
# if joinery_quantity > 99:
#     total_price *= 0.96
# else:
#     total_price *= 1
#
# print(f"{total_price:.2f} BGN")
#


# # 04. Balls; PB Online Exam 18-19 July 2020
# #
# import math
# balls = int(input())
#
# # Balls Count per Color
# red_balls = 0
# orange_balls = 0
# yellow_balls = 0
# white_balls = 0
# black_balls = 0
# other_balls = 0
#
# #Points Total
# points_total = 0
#
# for i in range(balls):
#     color = input()
#
#     if color == "red":
#         red_balls += 1
#         points_total += 5
#
#     elif color == "orange":
#         orange_balls += 1
#         points_total += 10
#
#     elif color == "yellow":
#         yellow_balls += 1
#         points_total += 15
#
#     elif color == "white":
#         white_balls += 1
#         points_total += 20
#
#     elif color == "black":
#         black_balls += 1
#         points_total = math.floor(points_total / 2)
#
#     else:
#         other_balls += 1
#         points_total += 0
#
# print(f"Total points: {points_total}")
# print(f"Red balls: {red_balls}")
# print(f"Orange balls: {orange_balls}")
# print(f"Yellow balls: {yellow_balls}")
# print(f"White balls: {white_balls}")
# print(f"Other colors picked: {other_balls}")
# print(f"Divides from black balls: {black_balls}")
#


# # 05. Best Player; PB Online Exam 18-19 July 2020
# #
# max_goals = 0
# best_player = ""
#
# while True:
#     text = input()
#
#     if text == "END":
#         print(f"{best_player} is the best player!")
#         if max_goals < 3:
#             print(f"He has scored {max_goals} goals.")
#         else:
#             print(f"He has scored {max_goals} goals and made 04.03.01.01.Food hat-trick !!!")
#         break
#
#     else:
#         player = text
#         goals = int(input())
#
#         if goals > max_goals:
#             max_goals = goals
#             best_player = player
#
#         if goals >= 10:
#             print(f"{best_player} is the best player!")
#             if max_goals < 3:
#                 print(f"He has scored {max_goals} goals.")
#             else:
#                 print(f"He has scored {max_goals} goals and made 04.03.01.01.Food hat-trick !!!")
#             break
#


# # 06. Barcode Generator; PB Online Exam 18-19 July 2020
# #
# start = input()
# end = input()
#
# start_0 = int(start[0])
# start_1 = int(start[1])
# start_2 = int(start[2])
# start_3 = int(start[3])
#
# end_0 = int(end[0])
# end_1 = int(end[1])
# end_2 = int(end[2])
# end_3 = int(end[3])
#
# for n0 in range(start_0, end_0 + 1):
#     for n1 in range(start_1, end_1 + 1):
#         for n2 in range(start_2, end_2 + 1):
#             for n3 in range(start_3, end_3 + 1):
#                 if n0 %2 !=0 and n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0:
#                     print(f"{n0}{n1}{n2}{n3}", end=" ")
#

