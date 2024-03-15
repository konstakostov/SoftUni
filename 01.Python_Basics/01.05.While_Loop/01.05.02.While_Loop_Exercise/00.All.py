# # OLD BOOKS
# searched_book = input()
# number_of_books = 0
#
# while True:
#     book = input()
#
#     if book == searched_book:
#         print(f"You checked {number_of_books} books and found it.")
#         break
#
#     if book == "No More Books":
#         print(f"The book you search is not here!")
#         print(f"You checked {number_of_books} books.")
#         break
#
#     number_of_books += 1
#


# # EXAM PREPARATION
# bad_grades_max = int(input())
# bad_grades = 0
#
# total_grades = 0
# sum_grades = 0
# last_problem = None
#
# while bad_grades < bad_grades_max:
#     exercise = input()
#
#     if exercise == "Enough":
#         print(f"Average score: {(sum_grades / total_grades):.2f}")
#         print(f"Number of problems: {total_grades}")
#         print(f"Last problem: {last_problem}")
#         break
#
#     grade = int(input())
#
#     if grade <= 4:
#         bad_grades += 1
#
#     sum_grades += grade
#     total_grades += 1
#     last_problem = exercise
#
# else:
#     print(f"You need 04.03.01.01.Food break, {bad_grades} poor grades.")
#


# # VACATION
# vacation_money = float(input())
# balance = float(input())
#
# days_spending = 0
# days = 0
#
# while days_spending < 5:
#     action = input()
#     money = float(input())
#
#     days += 1
#
#     if action == "spend":
#         balance = balance - money if balance - money > 0 else 0
#         days_spending += 1
#     else:
#         balance += money
#         days_spending = 0
#
#     if balance >= vacation_money:
#         print(f"You saved the money for {days} days.")
#         break
#
# else:
#     print(f"You can't save the money.")
#     print(days)
#


# # WALKING - ERROR!!!!!!
# steps_walked = 0
# goal = 10000
#
# while steps_walked < goal:
#     steps = input()
#
#     if steps == "Going home":
#         steps_walked += int(input())
#         break
#
#     steps_walked += int(steps)
#
#
# if steps_walked >= goal:
#     print(f"Goal reached! Good job!")
#     print(f"{steps_walked - goal} steps over the goal!")
# else:
#     print(f"{goal - steps_walked} more steps to reach goal.")
#


# # COINS
# change = round(float(input()) * 100)
# coins = 0
#
# while change > 0:
#     if change >= 200:
#         change -= 200
#     elif change >= 100:
#         change -= 100
#     elif change >= 50:
#         change -= 50
#     elif change >= 20:
#         change -= 20
#     elif change >= 10:
#         change -= 10
#     elif change >= 5:
#         change -= 5
#     elif change >= 2:
#         change -= 2
#     elif change >= 1:
#         change -= 1
#
#     coins += 1
#
# print(coins)


# # CAKE
# total_pieces = int(input()) * int(input())
# pieces_eaten = 0
#
# while total_pieces >= pieces_eaten:
#     pieces = input()
#
#     if pieces == "STOP":
#         print(f"{total_pieces - pieces_eaten} pieces are left.")
#         break
#     else:
#         pieces_eaten += int(pieces)
#
# else:
#     print(f"No more cake left! You need {pieces_eaten - total_pieces} pieces more.")
#


# # MOVING
# total_space = int(input()) * int(input()) * int(input())
# space_filled = 0
#
# while space_filled < total_space:
#     box = input()
#
#     if box == "Done":
#         print(f"{total_space - space_filled} Cubic meters left.")
#         break
#
#     space_filled += int(box)
#
# else:
#     print(f"No more free space! You need {space_filled - total_space} Cubic meters more.")
#


