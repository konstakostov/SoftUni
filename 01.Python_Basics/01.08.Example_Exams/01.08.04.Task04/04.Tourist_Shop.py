budget = float(input())

money_spent = 0

counter = 0

while money_spent <= budget:
    product = input()
    if product == "Stop":
        print(f"You bought {counter} products for {money_spent:.2f} leva.")
        break

    product_price = float(input())
    counter += 1

    if counter % 3 == 0:
        product_price *= 0.5

    money_spent += product_price

else:
    money_needed = abs(0 + (budget - money_spent))
    print(f"You don't have enough money!")
    print(f"You need {money_needed:.2f} leva!")
