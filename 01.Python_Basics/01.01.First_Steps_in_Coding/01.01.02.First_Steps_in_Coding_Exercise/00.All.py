# #USD to BGN
# usd = float(input())
#
# bgn = usd * 1.79549
#
# print(bgn)
#
#
#
# #RAD to Degrees
#
# #from math import pi, floor, ceil <-- Importing multiple elements from 04.03.01.01.Food library.
#
# ##Ver 01
# import math         #We import the whole library
#
# rad = float(input())
# deg = rad * 180 / math.pi           #We use pi from the library
#
# ##Ver 02
# from math import pi             #We import ONLU pi from the math library
#
# rad = float(input())
# deg = rad * 180 / pi            #We must write pi like so the program can read it
#
# print(deg)
#
#
# #Deposit Calculator
#
# deposit_sum = float(input())
# deposit_deadline = int(input())
# yearly_percentage = float(input()) / 100     # / 100 <-- so we can get from percentage to numberq e.g. 20.0% = 0.20
#
# sum_deposit = deposit_sum + deposit_deadline * ((deposit_sum * yearly_percentage) / 12)
#
# print(sum_deposit)
#
#
#
# #Summer Reading
#
# num_pages = int(input())
# pages_per_hour = int(input())
# days_total = int(input())
#
# total_time_needed = num_pages / pages_per_hour
# pages_per_day = total_time_needed / days_total
#
# print(int(pages_per_day))       #We use int so we round up the number
#
#
# #School Materials
#
# #Ver01
# pens = int(input()) * 5.80
# markers = int(input()) * 7.20
# cleaning = int(input()) * 1.20
# discount = int(input()) / 100
#
# non_discount_price = (pens + markers + cleaning)
# discount_price = (non_discount_price * discount)
# final_price = non_discount_price - discount_price
#
# print(final_price)
#
# #Ver02
# pens = int(input())
# markers = int(input())
# cleaning = int(input())
# discount = int(input()) / 100
#
# pens_price = 5.80
# markers_price = 7.20
# cleaning_price = 1.20
#
# non_discount_price = (pens * pens_price) + (markers * markers_price) + (cleaning * cleaning_price)
# discount_price = non_discount_price - (non_discount_price * discount)
#
# print(discount_price)
#
#
# #Repaint
#
# nylon = int(print())
# paint = int(print())
# thinner = int(input())
# work_hours = int(input())
#
#
# nylon_price = nylon * 1.50
# paint_price = paint * 14.50
# thinner_price = thinner * 5
# bags_price = 0.40
#
# nylon += 2      #We add +2 to final ammount of nylon
# paint += paint * 0.10       #We add 10% to final ammount of paint
#
# materials_price = (nylon * nylon_price) + (paint * paint_price) + (thinner * thinner_price) + (bags_price * 1)
# price_per_one_hour = materials_price * 0.30
# total_price = materials_price + (price_per_one_hour * work_hours)
#
# print(total_price)
#
#
#
# #Food Delivery
#
# chicken_menu_price = int(input()) * 10.35
# fish_menu_price = int(input()) * 12.40
# vegetarian_menu_price = int(input()) * 8.15
#
# menu_price = (chicken_menu_price + fish_menu_price + vegetarian_menu_price)
# dessert_price = menu_price * 0.20
# delivery = 2.50
#
# total_price = menu_price + dessert_price + delivery
#
# print(total_price)
#
#
#
# #Basketball Equipment
#
# yearly_price = int(input())
#
# sneakers = yearly_price - yearly_price * 0.40
# clothing = sneakers - sneakers * 0.20
# ball = clothing * 0.25
# accessories = ball * 0.20
#
# total_price = yearly_price + sneakers + clothing + ball + accessories
#
# print(total_price)
#
#
#
# #Aquarium
#
# lenght =int(input())
# width = int(input())
# height = int(input())
# percentage = float(input()) / 100
# #percentage = 1 - float(input()) / 100      <-- Another way to find needed percantage
#
# volume = (lenght * width * height) / 1000
#
# volume = volume * (1 - percentage)
# #volume -= volume*percentage    <-- Equivalent to the line above
#
# print(volume)
#
#
#
# # += & -= & *= & /=
#
# first_number = 5
# first_number += 3
# print(first_number)
#
# second_number = 5
# second_number = second_number +3
# print(second_number)
#
# third_number = 5
# third_number *= 3
# print(third_number)
#
# fourth_number = 6
# fourth_number /= 3
# print(fourth_number)
#
#
# text = "Hi, "
# text += "my name is "
# print(text)
#
# text_2 = "Hi, "
# text_2 *= 2
# print(text_2)
#
# import random
#
# number = random.randint(1, 10)
# print(number)
#
