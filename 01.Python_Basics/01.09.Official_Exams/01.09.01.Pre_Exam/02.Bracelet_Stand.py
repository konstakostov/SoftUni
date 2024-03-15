pocket_money = float(input()) * 5
sales_money = float(input()) * 5
costs = float(input())
gift_price = float(input())

money_total = (pocket_money + sales_money) - costs

if money_total >= gift_price:
    print(f"Profit: {money_total:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {(gift_price - money_total):.2f} BGN.")
    