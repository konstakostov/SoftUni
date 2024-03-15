# Testing
#
# num = 0
# while num < 10:
#     print(num)
#     num += 1
#


# # READ TEXT VER 01
# string = ""
#
# while string != "Stop":
#     string = input()
#     if string != "Stop":
#         print(string)
#

# # READ TEXT VER 02
# string = input()
#
# while string != "Stop":
#     print(string)
#     string = input()
#


# # READ TEXT VER 03
# while True:
#     string = input()
#     if string == "Stop":
#         break
#      print(string)
#


# PASSWORD
# username = input()  # Username added by User
# password = input()  # Password added by User
#
# data = input()      # Password entered by User, trying to Login
#
# while data != password:     # Logic
#     data = input()
#
# print(f"Welcome {username}")    # Welcome message when correct Password is entered
#


# SUM NUMBERS
# upper_num = int(input())
#
# num = 0
#
# while num < upper_num:      # If we use <= we will enter the loo again if the num is = to upper_sum
#     user_input = int(input())
#     num += user_input
#
# print(num)
#


# # SEQUENCE 2K+1
# upper_limit = int(input())
#
# num = 1
#
# while num <= upper_limit:
#     print(num)
#     num = (num * 2) + 1
#


# # ACCOUNT BALANCE
# balance = 0
#
# while True:
#     user_input = input()
#     if user_input == "NoMoreMoney":
#         break
#     money = float(user_input)
#     if money < 0:
#         print("Invalid operation!")
#         break
#     print(f"Increase: {money:.2f}")
#     balance += money
#
# print(f"Total: {balance:.2f}")
#


# # MAX NUMBER
# max_number = int(input())
#
# while True:
#     user_input = input()
#     if user_input == "Stop":
#         break
#     else:
#         num = int(user_input)
#     if num > max_number:
#         max_number = num
#
# print(max_number)
#


# # MIN NUMBER
# min_num = int(input())
#
# while True:
#     user_input = input()
#     if user_input == "Stop":
#         break
#     num = int(user_input)
#     if num < min_num:
#         min_num = num
#
# print(min_num)
#


# # GRADUATION
# name = input()
#
# fails = 0
# average = 0
# grade = 1
#
# while True:
#     curr_input = float(input())
#     if curr_input < 4:
#         fails += 1
#         if fails >= 2:
#             break
#         continue
#     average += curr_input
#     grade += 1
#
#     if grade > 12:
#         break
#
# median_grade = average / 12
#
# if fails >= 2:
#     print(f"{name} has been excluded at {grade} grade")
# else:
#     print(f"{name} graduated. Average grade: {median_grade:.2f} ")
#