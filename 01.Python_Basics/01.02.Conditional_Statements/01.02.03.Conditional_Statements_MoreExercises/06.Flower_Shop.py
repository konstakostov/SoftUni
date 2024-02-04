# Flower that are bought
import math

magnolia = int(input())
hyacinth = int(input())
rose = int(input())
cactus = int(input())

# Money to spend
gift_money = float(input())

# Flower Prices
magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

# Money Made
magnolia_profit = magnolia * magnolia_price
hyacinth_profit = hyacinth * hyacinth_price
rose_profit = rose * rose_price
cactus_profit = cactus * cactus_price
total_profit = magnolia_profit + hyacinth_profit + rose_profit + cactus_profit

# Tax Deduction
tax = total_profit * 0.05

# Profit After Tax
final_profit = total_profit - tax

# Determining if the money are enough
if final_profit >= gift_money:
    money_left = final_profit - gift_money
    print(f"She is left with {math.floor(money_left)} leva.")
else:
    money_left = gift_money - final_profit
    print(f"She will have to borrow {math.ceil(money_left)} leva.")
