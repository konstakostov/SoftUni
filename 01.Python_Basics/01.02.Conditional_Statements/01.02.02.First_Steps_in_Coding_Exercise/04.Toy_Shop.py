excursion_price = float(input())

puzzle_quantity = int(input())
doll_quantity = int(input())
teddy_quantity = int(input())
minion_quantity = int(input())
truck_quantity = int(input())

quantity_total = puzzle_quantity + doll_quantity + teddy_quantity + minion_quantity + truck_quantity

puzzle_price = 2.60
doll_price = 3
teddy_price = 4.10
minion_price = 8.20
truck_price = 2

puzzle_total = puzzle_quantity * puzzle_price
doll_total = doll_quantity * doll_price
teddy_total = teddy_quantity * teddy_price
minion_total = minion_quantity * minion_price
truck_total = truck_quantity * truck_price

price_total = puzzle_total + doll_total + teddy_total + minion_total + truck_total

if quantity_total >= 50:
    price_total = price_total - (price_total * 0.25)
else:
    price_total = price_total

rent = price_total * 0.10

money_left = price_total - rent

if money_left >= excursion_price:
    print(f"Yes! {money_left - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - money_left:.2f} lv needed.")
