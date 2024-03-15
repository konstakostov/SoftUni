# number = 0
# boolean_variable = bool(number)
#
# print(boolean_variable)

# number = 12344221
# # WHen we % 100 we print inky the last 2 numbers-
# # If it is %1000 then it will print the last 3 numbers, and etc.
# result = number % 100
# print(result)


# # DAY OF WEEK
# # Input
# day = input()
#
# # Determining day of the wek
# if day == '1':
#     print('Monday')
# elif day == '2':
#     print('Tuesday')
# elif day == '3':
#     print('Wednesday')
# elif day == '4':
#     print('Thursday')
# elif day == '5':
#     print('Friday')
# elif day == '6':
#     print('Saturday')
# elif day == '7':
#     print('Sunday')
# else:
#     print('Error')
#


# WEEKEND OR WORKING DAYS

# day = input()
# if day == 'Monday':
#     print("Working day")
# elif day == 'Tuesday':
#     print("Working day")
# elif day == 'Wednesday':
#     print("Working day")
# elif day == 'Thursday':
#     print("Working day")
# elif day == 'Friday':
#     print("Working day")
# elif day == 'Saturday':
#     print("Weekend")
# elif day == 'Sunday':
#     print("Weekend")
# else:
#     print("Error")
#


# # ANIMAL TYPE
# animal = input()
#
# if animal == 'dog':
#     print("04.10.02.01.Mammal")
# elif animal == 'crocodile' or 'tortoise' or 'snake ':
#     print("reptile")
# else:
#     print("unknown")
#


# # PERSONAL TITLES
# age = float(input())
# sex = input()
#
# if sex == 'f':
#     if age < 16:
#         print("Miss")
#     else:
#         print("Ms.")
# else:
#     if age < 16:
#         print("Master")
#     else:
#         print("Mr.")
#


# # SMALL SHOP - FIX THIS SHIT, IT AIN'T WORKING!!!!
# city = input()
# product = input()
# quantity = float(input())
# price = 0
#
# if city == 'Sofia':
#     if product == 'coffee':
#         price = quantity * 0.50
#     elif product == 'water':
#         price = quantity * 0.80
#     elif product == 'beer':
#         price = quantity * 1.20
#     elif product =='sweets':
#         price = quantity * 1.45
#     else:
#         price = quantity * 1.60
#
# elif city == 'Plovdiv':
#     if product == 'coffee':
#         price = quantity * 0.40
#     elif product == 'water':
#         price = quantity * 0.70
#     elif product == 'beer':
#         price = quantity * 1.15
#     elif product == 'sweets':
#         price = quantity * 1.30
#     else:
#         price = quantity * 1.50
#
#
# else:
#     if product == 'coffee':
#         price = quantity * 0.45
#     elif product == 'water':
#         price = quantity * 0.70
#     elif product == 'beer':
#         price = quantity * 1.10
#     elif product == 'sweets':
#         price = quantity * 1.35
#     else:
#         price = quantity * 1.55
#
# print(price)
#


# # NUMBERS IN RANGE
# number = int(input())
#
# if -100 <= number <= 100 and number != 0:
#     print("Yes")
# else:
#     print("No")
#


# # WORKING HOURS
# time = int(input())
# day = input()
#
# if 10 <= time <= 18 and day != 'Sunday':
#     print("open")
# else:
#     print("closed")
#


# # CINEMA TICKET
# day = input()
# price = 0
#
# if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
#     price = 12
# elif day == 'Wednesday' or day == 'Thursday':
#     price = 14
# elif day == 'Saturday' or day == 'Sunday':
#     price = 16
#
# print(price)
#


# # FRUIT OF VEGETABLE
# produce = input()
#
# if produce == 'banana' or \
#     produce == 'apple' or \
#     produce == 'kiwi' or \
#     produce == 'cherry' or \
#     produce == 'lemon ' or \
#     produce == 'grapes':
#     print("fruit")
#
# elif produce == 'tomato' or \
#     produce == 'cucumber' or \
#     produce == 'pepper ' or \
#     produce == 'carrot':
#     print("vegetable")
#
# else:
#     print("unknown")
#


# # INVALID NUMBERS
# number = int(input())
#
# if 100 <= number <= 200 or number == 0:
#     print()
# else:
#     print('invalid')
#


# # FRUIT SHOP
# fruit = input()
# day = input()
# quantity = float(input())
# price = 0
#
# if day == 'Saturday' or day == 'Sunday':
#     if fruit == 'banana':
#         price = quantity * 2.70
#     elif fruit == 'apple':
#         price = quantity * 1.25
#     elif fruit == 'orange':
#         price = quantity * 0.90
#     elif fruit == 'grapefruit':
#         price = quantity * 1.60
#     elif fruit == 'kiwi':
#         price = quantity * 3.00
#     elif fruit == 'pineapple':
#         price = quantity * 5.60
#     elif fruit == 'grapes':
#         price = quantity * 4.20
# elif day == 'Monday' or day == 'Tuesday' or \
#         day == 'Wednesday' or day == 'Thursday' or \
#         day == 'Friday':
#
#     if fruit == 'banana':
#         price = quantity * 2.50
#     elif fruit == 'apple':
#         price = quantity * 1.20
#     elif fruit == 'orange':
#         price = quantity * 0.85
#     elif fruit == 'grapefruit':
#         price = quantity * 1.45
#     elif fruit == 'kiwi':
#         price = quantity * 2.70
#     elif fruit == 'pineapple':
#         price = quantity * 5.50
#     elif fruit == 'grapes':
#         price = quantity * 3.85
#
# if price == 0:
#     print("error")
# else:
#     print(f"{price:.2f}")
#


# # TRADE COMMISSIONS
# city = input()
# sales = float(input())
#
# commission = 0
#
# is_invalid_input = False
#
# if city == 'Sofia':
#     if sales >= 0 and sales <= 500:
#         commission = sales * 0.05
#     elif sales > 500 and sales <= 1000:
#         commission = sales * 0.07
#     elif sales > 1000 and sales <= 10000:
#         commission = sales * 0.08
#     elif sales > 10000:
#         commission = sales * 0.12
#     else:
#         is_invalid_input = True
#
# elif city == 'Varna':
#     if sales >= 0 and sales <= 500:
#         commission = sales * 0.045
#     elif sales > 500 and sales <= 1000:
#         commission = sales * 0.075
#     elif sales > 1000 and sales <= 10000:
#         commission = sales * 0.10
#     elif sales > 10000:
#         commission = sales * 0.13
#     else:
#         is_invalid_input = True
#
# elif city == 'Plovdiv':
#     if sales >= 0 and sales <= 500:
#         commission = sales * 0.055
#     elif sales > 500 and sales <= 1000:
#         commission = sales * 0.08
#     elif sales > 1000 and sales <= 10000:
#         commission = sales * 0.12
#     elif sales > 10000:
#         commission = sales * 0.145
#     else:
#         is_invalid_input = True
#
# else:
#     is_invalid_input = True
#
# if is_invalid_input:
#     print("error")
# else:
#     print(f"{commission:.2f}")
#

