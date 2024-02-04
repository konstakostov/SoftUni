import math

people = int(input())
entry_price = float(input())
chair_price = float(input())
umbrella_price = float(input())


chairs_used = math.ceil(people * 0.75)
umbrellas_used = math.ceil(people / 2)

entry_price_total = people * entry_price
chairs_price = chairs_used * chair_price
umbrellas_price = umbrellas_used * umbrella_price


total_money = entry_price_total + chairs_price + umbrellas_price
print(f"{total_money:.2f} lv.")
