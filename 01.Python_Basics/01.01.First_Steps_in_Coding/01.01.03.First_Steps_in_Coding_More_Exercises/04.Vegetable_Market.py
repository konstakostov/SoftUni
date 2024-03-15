vegetables_price = float(input())
fruits_price = float(input())

vegetables_kg = int(input())
fruits_kg = int(input())

vegetables = vegetables_kg * vegetables_price
fruits = fruits_price * fruits_kg

price_eu = vegetables + fruits

price_bgn = price_eu / 1.94

print(f"{price_bgn:.2f}")
