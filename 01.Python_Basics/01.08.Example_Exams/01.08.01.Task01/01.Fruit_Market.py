strawberries_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

raspberries_price = strawberries_price * 0.50
oranges_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20

bananas_total = bananas * bananas_price
oranges_total = oranges * oranges_price
raspberries_total = raspberries * raspberries_price
strawberries_total = strawberries * strawberries_price

print(f"{(bananas_total + oranges_total + raspberries_total + strawberries_total):.2f}")
