# for i in range(1, 1001):
#     if i % 10 == 7:
#         print(i)


# import sys
#
# n = int(input())
#
# max_num = -sys.maxsize
# num_sum = 0
#
# for _ in range(1, n + 1):
#     num = int(input())
#
#     if num > max_num:
#         max_num = num
#
#     num_sum += num
#
# if max_num == num_sum - max_num:
#     print(f"Yes")
#     print(f"Sum = {max_num}")
# else:
#     print(f"No")
#     print(f"Diff = {abs(max_num - (num_sum - max_num))}")


# n = int(input())
#
# p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0
#
# for _ in range(1, n + 1):
#     num = int(input())
#
#     if num < 200:
#         p1 += 1
#     elif num < 400:
#         p2 += 1
#     elif num < 600:
#         p3 += 1
#     elif num < 800:
#         p4 += 1
#     elif num >= 800:
#         p5 += 1
#
# print(f"{(p1 / n) * 100:.2f}%")
# print(f"{(p2 / n) * 100:.2f}%")
# print(f"{(p3 / n) * 100:.2f}%")
# print(f"{(p4 / n) * 100:.2f}%")
# print(f"{(p5 / n) * 100:.2f}%")


# age = int(input())
# washer_price = float(input())
# toys_single_price = int(input())
#
# money_gift_total = 0
# money_gift = 10
#
# toys_money_total = 0
# toys_gift = 0
#
# for years in range(1, age + 1):
#     if years % 2 == 0:
#         money_gift_total += money_gift - 1
#         money_gift += 10
#
#     else:
#         toys_gift += 1
#
# toys_money_total = toys_single_price * toys_gift
#
# money_total = toys_money_total + money_gift_total
#
# if money_total >= washer_price:
#     print(f"Yes! {(money_total - washer_price):.2f}")
# else:
#     print(f"No! {(washer_price - money_total):.2f}")
#


# tabs = int(input())
# salary = int(input())
#
# for _ in range(1, tabs + 1):
#     site = input()
#
#     if site == "Facebook":
#         salary -= 150
#     elif site == "Instagram":
#         salary -= 100
#     elif site == "Reddit":
#         salary -= 50
#     else:
#         salary += 0
#
#     if salary <= 0:
#         print(f"You have lost your salary.")
#         break
#
# else:
#     print(salary)


# actor = input()
# points = float(input())
# judges = int(input())
#
# for _ in range(1, judges + 1):
#     judge_name = input()
#     judge_points = float(input())
#
#     points += (len(judge_name) * judge_points) / 2
#
#     if points > 1250.5:
#         print(f"Congratulations, {actor} got 04.03.01.01.Food nominee for leading role with {points:.1f}!")
#         break
# else:
#     print(f"Sorry, {actor} you need {(1250.5 - points):.1f} more!")
#


# groups_count = int(input())
#
# g1, g2, g3, g4, g5 = 0, 0, 0, 0, 0
#
# people_count = 0
#
# for _ in range(1, groups_count + 1):
#     people_group = int(input())
#
#     people_count += people_group
#
#     if people_group <= 5:
#         g1 += people_group
#     elif people_group <= 12:
#         g2 += people_group
#     elif people_group <= 25:
#         g3 += people_group
#     elif people_group <= 40:
#         g4 += people_group
#     else:
#         g5 += people_group
#
# print(f"{((g1 / people_count) * 100):.2f}%")
# print(f"{((g2 / people_count) * 100):.2f}%")
# print(f"{((g3 / people_count) * 100):.2f}%")
# print(f"{((g4 / people_count) * 100):.2f}%")
# print(f"{((g5 / people_count) * 100):.2f}%")

import math

tournaments = int(input())
starting_points = int(input())

tournaments_points = 0
won_tournaments = 0

for _ in range(1, tournaments + 1):
    tour_stage = input()

    if tour_stage == "W":
        tournaments_points += 2000
        won_tournaments += 1
    elif tour_stage == "F":
        tournaments_points += 1200
    elif tour_stage == "SF":
        tournaments_points += 720

final_points = starting_points + tournaments_points
average_points = tournaments_points / tournaments
won_percentage = (won_tournaments / tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{won_percentage:.2f}%")
