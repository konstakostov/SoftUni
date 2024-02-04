# # Numbers Ending in 7 VER.01
# for number in range(1, 1001):
#     if number % 10 == 7:
#         print(number)
#
# # Numbers Ending in 7 VER.02
# for number in range(7, 1001, 10):
#     print(number)
#
import math

# # Half Sum Element
# import sys
#
# n = int(input())
#
# max_number = -sys.maxsize
# sum_numbers = 0
#
# for _ in range(n):
#     number = int(input())
#
#     if number > max_number:
#         max_number = number
#
#     sum_numbers += number
#
# if max_number == sum_numbers - max_number:
#     print(f"Yes\nSum = {max_number}")
# else:
#     print(f"No\nDiff = {abs(max_number - (sum_numbers - max_number))}")
#


# # Histogram
# n = int(input())
#
# p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0
#
# for _ in range(n):
#     number = int(input())
#
#     if number < 200:
#         p1 += 1
#     elif number < 400:
#         p2 += 1
#     elif number < 600:
#         p3 += 1
#     elif number < 800:
#         p4 += 1
#     else:
#         p5 += 1
#
# print(f"{((p1 / n) * 100):.2f}%")
# print(f"{((p2 / n) * 100):.2f}%")
# print(f"{((p3 / n) * 100):.2f}%")
# print(f"{((p4 / n) * 100):.2f}%")
# print(f"{((p5 / n) * 100):.2f}%")
#


# # Clever Lily
# years = int(input())
# washer_price = float(input())
# toy_price = int(input())
#
# money_given = 10
# money_gifts = 0
#
# toys_count = 0
#
#
# for age in range(1, years + 1):
#     if age % 2 == 0:
#         money_gifts += money_given - 1
#         money_given += 10
#     else:
#         toys_count += 1
#
# money_gifts += toys_count * toy_price
#
# if money_gifts >= washer_price:
#     print(f"Yes! {money_gifts - washer_price:.2f}")
# else:
#     print(f"No! {washer_price - money_gifts:.2f}")
#


# # Salary
# n = int(input())
# salary = int(input())
#
# for _ in range(n):
#     tab = input()
#
#     if tab == "Facebook":
#         salary -= 150
#     elif tab == "Instagram":
#         salary -= 100
#     elif tab == "Reddit":
#         salary -= 50
#
#     if salary <= 0:
#         print(f"You have lost your salary.")
#         break
# else:
# print(salary)
#


# # Oscars
# actor = input()
# points = float(input())
# judges = int(input())
#
# MAX_POINTS = 1250.52
#
# for _ in range(judges):
#     judge_name = input()
#     judge_points = float(input())
#
#     points += len(judge_name) * judge_points / 2
#
#     if points > MAX_POINTS:
#         print(f"Congratulations, {actor} got 04.03.01.01.Food nominee for leading role with {points:.1f}!")
#         break
# else:
#     print(f"Sorry, {actor} you need {(MAX_POINTS - points):.1f} more!")


# # Trekking Mania
# groups = int(input())
#
# musala = 0
# monblan = 0
# kilimanjaro = 0
# k2 = 0
# everest = 0
#
# for _ in range(groups):
#     group = int(input())
#
#     if group < 6:
#         musala += group
#     elif group < 13:
#         monblan += group
#     elif group < 26:
#         kilimanjaro += group
#     elif group < 41:
#         k2 += group
#     else:
#         everest += group
#
# total_people = musala + monblan + kilimanjaro + k2 + everest
#
# print(f"{musala / total_people * 100:.2f}%")
# print(f"{monblan / total_people * 100:.2f}%")
# print(f"{kilimanjaro / total_people * 100:.2f}%")
# print(f"{k2 / total_people * 100:.2f}%")
# print(f"{everest / total_people * 100:.2f}%")
#


# Tennis Ranklist
tournaments = int(input())
starting_points = int(input())

win_tournaments = 0
gained_points = 0

for _ in range(tournaments):
    tournament = input()

    if tournament == "W":
        win_tournaments += 1
        gained_points += 2000
    elif tournament == "F":
        gained_points += 1200
    elif tournament == "SF":
        gained_points += 720

print(f"Final points: {starting_points + gained_points}")
print(f"Average points: {math.floor(gained_points / tournaments)}")
print(f"Final points: {win_tournaments / tournaments * 100:.2f}%")
