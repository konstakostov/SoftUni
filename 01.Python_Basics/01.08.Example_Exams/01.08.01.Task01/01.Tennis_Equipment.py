import math

racket_price = float(input())
racket_quantity = int(input())
sneakers_quantity = int(input())

rackets = racket_quantity * racket_price
sneakers_price = racket_price / 6
sneakers = sneakers_price * sneakers_quantity

others = (rackets + sneakers) * 0.2

total_price = rackets + sneakers + others

price_dj = total_price / 8
price_sp = total_price * (7 / 8)

print(f"Price to be paid by Djokovic {math.floor(price_dj)}")
print(f"Price to be paid by sponsors {math.ceil(price_sp)}")
