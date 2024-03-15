clients = int(input())

basket_price = 1.50
wreath_price = 3.80
bunny_price = 7

basket_counter = 0
wreath_counter = 0
bunny_counter = 0
product_counter = 0

money_spent_total = 0

for i in range(clients):
    while True:
        command = input()

        if command == "Finish":
            final_price = (basket_price * basket_counter) +\
                          (wreath_price * wreath_counter) + \
                          (bunny_price * bunny_counter)
            if product_counter % 2 == 0:
                final_price *= 0.80
            else:
                final_price *= 1
            money_spent_total += final_price
            print(f"You purchased {product_counter} items for {final_price:.2f} leva.")
            basket_counter = 0
            wreath_counter = 0
            bunny_counter = 0
            product_counter = 0
            break

        product_counter += 1
        if command == "basket":
            basket_counter += 1

        if command == "wreath":
            wreath_counter += 1

        if command == "chocolate bunny":
            bunny_counter += 1

print(f"Average bill per client is: {(money_spent_total / clients):.2f} leva.")
