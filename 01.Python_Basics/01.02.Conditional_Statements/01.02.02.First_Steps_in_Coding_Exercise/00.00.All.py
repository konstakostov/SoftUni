# # SUM RECORDS
# import math
#
# time_first = int(input())
# time_second = int(input())
# time_third = int(input())
#
# time_total = time_first + time_second + time_third
#
# minutes = time_total // 60
# seconds = time_total % 60
#
# minutes = math.floor(minutes)
#
# if seconds < 10:
#     print(f"{minutes}:0{seconds}")
# else:
#     print(f"{minutes}:{seconds}")
#

# # BONUS SCORE
#
# entry_number = int(input())
# bonus = 0
#
# # Checking the size of number for determining bonus value number
# if entry_number <= 100:
#     bonus = 5
# elif entry_number > 1000:
#     # We use >1000 because if we put first >100 we
#     # will never reach the condition check for >1000
#     bonus = entry_number * 0.10
# else:
#     bonus = entry_number * 0.20
#
# # Checking if number is even OR is
# if entry_number % 2 == 0:
#     bonus += 1
#
# elif entry_number % 5 == 0:
#     bonus += 2
#
# final_number = entry_number + bonus
#
# print(bonus)
# print(final_number)
#

# # TIME + 15 MINUTES
#
# hours = int(input())
# minutes = int(input()) + 15
#
# if minutes > 59:
#     minutes -= 60
#     hours += 1
#
# if hours > 23:
#     hours -= 24
#
# if minutes >= 10:
#     print(f"{hours}:{minutes}")
# else:
#     print(f"{hours}:0{minutes}")
#

# # TOY SHOP
#
# vacation_price = float(input())
#
# puzzles_quantity = int(input())
# dolls_quantity = int(input())
# bears_quantity = int(input())
# minions_quantity = int(input())
# trucks_quantity = int(input())
#
# discount = 0
# rent = 0
#
# toys_quantity = puzzles_quantity + dolls_quantity + bears_quantity + minions_quantity + trucks_quantity
#
# puzzles_price = 2.60
# dolls_price = 3
# bears_price = 4.10
# minions_price = 8.20
# trucks_price = 2
#
# puzzles = puzzles_quantity * puzzles_price
# dolls = dolls_quantity * dolls_price
# bears = bears_quantity * bears_price
# minions = minions_quantity * minions_price
# trucks = trucks_quantity * trucks_price
#
# final_price = puzzles + dolls + bears + minions + trucks
#
# if toys_quantity >= 50:
#     discount = final_price * 0.25
#     final_price -= discount
# else:
#     discount = discount
#     final_price = final_price
#
# rent = final_price * 0.10
#
# money_left = final_price - rent
#
# if money_left >= vacation_price:
#     print(f"Yes! {(money_left - vacation_price):.2f} lv left.")
# else:
#     print(f"Not enough money! {(vacation_price - money_left):.2f} lv needed!")
#

# # GODZILLA VS KONG
#
# budget = float(input())
# people = int(input())
# clothing_price = float(input())
#
# decor = budget * 0.10
#
# if people > 150:
#     clothing_price = clothing_price - clothing_price * 0.10
#
# money_needed = people * clothing_price + decor
#
# if money_needed > budget:
#     print("Not enough money!")
#     print(f"Wingard needs {(money_needed - budget):.2f} leva more.")
# else:
#     print("Action!")
#     print(f"Wingard starts filming with {(budget - money_needed):.2f} leva left.")
#

# WORLD SWIMMING RECORD
#
# import math
#
# world_record = float(input())
# distance = float(input())
# time_per_meter = float(input())
#
# time_needed = distance * time_per_meter
#
# water_resistance = math.floor(distance // 15)
#
# time_needed += water_resistance * 12.5
#
# if time_needed < world_record:
#     print(f"Yes, he succeeded! The new world record is {(time_needed):.2f} seconds.")
# else:
#     print(f"No, he failed! He was {(time_needed - world_record):.2f} seconds slower.")
#

# # WORLD SWIMMING RECORD VARIANT 2
# import math
#
# record_in_seconds = float(input())
# record_in_meters = float(input())
# seconds_per_meter = float(input())
#
# water_resistance_seconds = math.floor(record_in_meters / 15) * 12.5
# swimmer_seconds = seconds_per_meter * record_in_meters + water_resistance_seconds
#
# if swimmer_seconds >= record_in_seconds:
#     print(f"No, he failed! He was {(swimmer_seconds- record_in_seconds):.2f} seconds slower.")
# else:
#     print(f"Yes, he succeeded! The new world record is {swimmer_seconds:.2f} seconds.")
#

# # SHOPPING
#
# budget = float(input())
#
# graphic_cards = int(input())
# processors = int(input())
# ram = int(input())
#
# graphic_cards_price = graphic_cards * 250
# processors_price = processors * (graphic_cards_price * 0.35)
# ram_price = ram * (graphic_cards_price * 0.10)
#
# final_price = graphic_cards_price + processors_price + ram_price
#
# if graphic_cards > processors:
#     final_price *= 0.85
#
# if budget >= final_price:
#     print(f"You have {(budget - final_price):.2f} leva left!")
# else:
#     print(f"Not enough money! You need {(final_price - budget):.2f} leva more!")
#

# import math
#
# tv_series = input()
#
# episode_time = int(input())
# break_time = int(input())
#
# lunch_time = break_time / 8
# relax_time = break_time / 4
#
# break_time_left = break_time - (lunch_time + relax_time)
#
# if episode_time < break_time_left:
#     print(f"You have enough time to watch {tv_series} and "
#           f"left with {math.ceil(break_time_left - episode_time)} minutes free time.")
# else:
#     print(f"You don't have enough time to watch {tv_series}, "
#           f"you need {math.ceil(abs(episode_time - break_time_left))} more minutes.")

# LUNCH BREAK VERSION 02
#
# import math
#
# series = input()
# episode_length = int(input())
# break_length = int(input())
#
# lunch_time = break_length / 8
# leisure_time = break_time / 4
#
# time_taken = lunch_time + leisure_time + episode_time
# time_left = break_time - time_taken
#
# if time_left >= 0:
#     print(f"You have enough time to watch {series} and "
#           f"left with {math.ceil(time_left)} minutes free time.")
# else:
#     print(f"You don't have enough time to watch {series}, "
#           f"you need {math.ceil(abs(time_left))} more minutes.")
#

# FIGLET

