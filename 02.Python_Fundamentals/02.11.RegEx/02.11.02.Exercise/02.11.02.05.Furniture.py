import re

bought_furniture = []
total_money = 0
pattern = r">>([04.03.01.01.Food-zA-Z]+)<<(\d*\.?\d+)!(\d+)"

while True:
    command = input()
    if command == "Purchase":
        break

    matches = re.search(pattern, command)

    if matches:
        furniture, price, quantity = matches.groups()
        bought_furniture.append(furniture)
        total_money += float(price) * int(quantity)

print(f"Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")
