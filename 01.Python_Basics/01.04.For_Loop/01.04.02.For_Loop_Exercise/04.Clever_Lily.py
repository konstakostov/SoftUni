age = int(input())
washer = float(input())
toy_price = int(input())

gifted_money = 10
b_day_money = 0

b_day_toys = 1

for years in range(1, age + 1):

    if years % 2 == 0:
        b_day_money += gifted_money - 1
        gifted_money += 10

    else:
        b_day_toys += 1

toys_price = b_day_toys * toy_price

budget = toys_price + b_day_money

if budget >= washer:
    print(f"Yes! {budget - washer}")

else:
    print(f"No! {washer - budget}")
























# age = int(input())
# washer_price = float(input())
# toy_price = int(input())
#
# money_given = 10
# gift_money = 0
#
# gift_toys = 0
#
# for years in range(1, age + 1):
#     if years % 2 == 0:
#         gift_money += (money_given - 1)
#         money_given += 10
#
#     else:
#         gift_toys += 1
#
# gift_money += toy_price * gift_toys
#
# if gift_money >= washer_price:
#     print(f"Yes! {(gift_money - washer_price):.2f}")
# else:
#     print(f"No! {(washer_price - gift_money):.2f}")



