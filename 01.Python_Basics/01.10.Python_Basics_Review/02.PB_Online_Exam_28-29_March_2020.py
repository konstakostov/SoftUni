# # 01. Birthday Party; PB Online Exam 28-29 March 2020
# rent = float(input())
# cake = rent * 0.20
# drinks = cake * 0.55
# animator = rent / 3
#
# budget = rent + cake + drinks + animator
# print(f"{budget:.1f}")
#


# # 01. Change Bureau; PB Online Exam 28-29 March 2020
# bitcoins_quantity = int(input())
# yuan_quantity = float(input())
# commission = float(input())
#
# leva = 0
#
# # Bitcoin to BGN
# bitcoins_to_bgn = bitcoins_quantity * 1168
# leva += bitcoins_to_bgn
#
# # Yuan to USD
# yuan_to_usd = yuan_quantity * 0.15
# usd = yuan_to_usd
#
# # USD to BGN
# usd_to_bgn = usd * 1.76
# leva += usd_to_bgn
#
# # BGN to Euro
# bgn_to_euro = leva / 1.95
# after_commission = bgn_to_euro * (commission / 100)
#
# # Final Euro
# euro = bgn_to_euro - after_commission
#
# print(f"{euro:.2f}")
#


# # 02. Cat Walking; PB Online Exam 28-29 March 2020
# walk_minutes = int(input())
# walks_per_day = int(input())
# calories_intake = int(input())
#
# calories_per_minute = 5
#
# calories_burned = walk_minutes * (calories_per_minute * walks_per_day)
#
# if calories_burned >= calories_intake * 0.5:
#     print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
# else:
#     print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
#


# # 02. Mountain Run; PB Online Exam 28-29 March 2020
# import math
#
# record_seconds = float(input())
# distance_meters = float(input())
# seconds_per_meter = float(input())
#
# delay = (math.floor(distance_meters / 50) * 30)
#
# new_time = (distance_meters * seconds_per_meter) + delay
#
# if new_time < record_seconds:
#     print(f" Yes! The new record is {new_time:.2f} seconds.")
# else:
#     print(f"No! He was {(new_time - record_seconds):.2f} seconds slower.")
#


# # 03. Energy Booster; PB Online Exam 28-29 March 2020
# fruit = input()
# set_size = input()
# set_quantity = int(input())
#
# price = 0
# quantity = 0
#
# final_price = 0
#
# if fruit == "Watermelon":
#     if set_size == "small":
#         price = 56
#         quantity = 2
#     elif set_size == "big":
#         price = 28.70
#         quantity = 5
#     final_price = (price * quantity) * set_quantity
#
# elif fruit == "Mango":
#     if set_size == "small":
#         price = 36.66
#         quantity = 2
#     elif set_size == "big":
#         price = 19.60
#         quantity = 5
#     final_price = (price * quantity) * set_quantity
#
# elif fruit == "Pineapple":
#     if set_size == "small":
#         price = 42.10
#         quantity = 2
#     elif set_size == "big":
#         price = 24.80
#         quantity = 5
#     final_price = (price * quantity) * set_quantity
#
# elif fruit == "Raspberry":
#     if set_size == "small":
#         price = 20
#         quantity = 2
#     elif set_size == "big":
#         price = 15.20
#         quantity = 5
#     final_price = (price * quantity) * set_quantity
#
# if final_price > 1000:
#     final_price *= 0.5
# elif 400 <= final_price <= 1000:
#     final_price *= 0.85
#
# print(f"{final_price:.2f} lv.")



# # 03. Fitness Card; PB Online Exam 28-29 March 2020
# available_sum = float(input())
# sex = input()
# age = int(input())
# sport = input()
#
# price = 0
#
# if sex == "m":
#     if sport == "Gym":
#         price = 42
#     elif sport == "Boxing":
#         price = 41
#     elif sport == "Yoga":
#         price = 45
#     elif sport == "Zumba":
#         price = 34
#     elif sport == "Dances":
#         price = 51
#     elif sport == "Pilates":
#         price = 39
#
# elif sex == "f":
#     if sport == "Gym":
#         price = 35
#     elif sport == "Boxing":
#         price = 37
#     elif sport == "Yoga":
#         price = 42
#     elif sport == "Zumba":
#         price = 31
#     elif sport == "Dances":
#         price = 53
#     elif sport == "Pilates":
#         price = 37
#
# if age <= 19:
#     price *= 0.80
#
# if available_sum >= price:
#     print(f"You purchased 04.03.01.01.Food 1 month pass for {sport}.")
# else:
#     print(f"You don't have enough money! You need ${(price - available_sum):.2f} more.")
#


# # 04. Food for Pets; PB Online Exam 28-29 March 2020
# days = int(input())
# food = float(input())
#
# eaten = 0
# dog = 0
# cat = 0
# biscuit = 0
#
# for i in range(1, days + 1):
#     dog_day = int(input())
#     cat_day = int(input())
#
#     if i % 3 != 0:
#         dog += dog_day
#         cat += cat_day
#         eaten += dog_day + cat_day
#     else:
#         biscuit_size = (dog_day + cat_day) * 0.10
#         biscuit += biscuit_size
#         dog += dog_day
#         cat += cat_day
#         eaten += dog_day + cat_day
#
# print(f"Total eaten biscuits: {round(biscuit)}gr.")
# print(f"{((eaten / food) * 100):.2f}% of the food has been eaten.")
# print(f"{((dog / eaten) * 100):.2f}% eaten from the dog.")
# print(f"{((cat / eaten) * 100):.2f}% eaten from the cat.")
#


# # 04. Trekking Mania; PB Online Exam 28-29 March 2020
# groups = int(input())
#
# musala = 0
# monblan = 0
# kilimanjaro = 0
# k2 = 0
# everest = 0
# total = 0
#
# for i in range(1, groups + 1):
#     people = int(input())
#     if people <= 5:
#         musala += people
#         total += people
#
#     elif 6 <= people <= 12:
#         monblan += people
#         total += people
#
#     elif 13 <= people <= 25:
#         kilimanjaro += people
#         total += people
#
#     elif 26 <= people <= 40:
#         k2 += people
#         total += people
#
#     elif people >= 41:
#         everest += people
#         total += people
#
# print(f"{((musala / total) * 100):.2f}%")
# print(f"{((monblan / total) * 100):.2f}%")
# print(f"{((kilimanjaro / total) * 100):.2f}%")
# print(f"{((k2 / total) * 100):.2f}%")
# print(f"{((everest / total) * 100):.2f}%")
#


# # 05. Care of Puppy; PB Online Exam 28-29 March 2020
# food_bought_kg = int(input())
# food_bought_g = food_bought_kg * 1000
#
#
# days = 0
# food_eaten_g = 0
#
# while True:
#     command = input()
#     if command == "Adopted":
#         break
#     else:
#         days += 1
#         food = int(command)
#         food_eaten_g += food
#
# if food_bought_g >= food_eaten_g:
#     print(f"Food is enough! Leftovers: {food_bought_g - food_eaten_g} grams.")
# else:
#     print(f"Food is not enough. You need {food_eaten_g - food_bought_g} grams more.")
#


# # 05. Suitcases Load; PB Online Exam 28-29 March 2020
# capacity = float(input())
#
# filled_volume = 0
# volume_left = capacity
# counter = 0
#
# while True:
#     command = input()
#
#     if command == "End":
#         print("Congratulations! All suitcases are loaded!")
#         print(f"Statistic: {counter} suitcases loaded.")
#         break
#
#     volume = float(command)
#     counter += 1
#
#     if counter % 3 == 0:
#         volume += volume * 0.10
#
#     if volume_left - volume < 0:
#         counter -= 1
#         print("No more space!")
#         print(f"Statistic: {counter} suitcases loaded.")
#         break
#     else:
#         filled_volume += volume
#         volume_left -= volume
#


# # 06. Tournament of Christmas; PB Online Exam 28-29 March 2020
# days = int(input())
#
# win_day = 0
# lose_day = 0
# money_day = 0
#
# win_day_counter = 0
# lose_day_counter = 0
# money_total = 0
#
# for current_day in range(1, days + 1):
#     while True:
#         game = input()
#
#         if game == "Finish":
#             if win_day > lose_day:
#                 money_day += money_day * 0.10
#                 money_total += money_day
#                 win_day_counter += 1
#             else:
#                 money_total += money_day
#                 lose_day_counter += 1
#             win_day = 0
#             lose_day = 0
#             money_day = 0
#             break
#
#         status = input()
#         if status == "win":
#             win_day += 1
#             money_day += 20
#         elif status == "lose":
#             lose_day += 1
#
# if win_day_counter > lose_day_counter:
#     money_total += money_total * 0.20
#     print(f"You won the tournament! Total raised money: {money_total:.2f}")
# else:
#     print(f"You lost the tournament! Total raised money: {money_total:.2f}")
#

