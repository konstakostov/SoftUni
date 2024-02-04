money_goal = int(input())

money_earned = 0

while money_earned < money_goal:
    cocktail = input()

    if cocktail == "Party!":
        print(f"We need {(money_goal - money_earned):.2f} leva more.")
        print(f"Club income - {money_earned:.2f} leva.")
        break

    quantity = int(input())
    cocktail_price = len(cocktail) * quantity

    if cocktail_price % 2 == 0:
        money_earned += cocktail_price
    else:
        cocktail_price *= 0.75
        money_earned += cocktail_price

else:
    print(f"Target acquired.")
    print(f"Club income - {money_earned:.2f} leva.")
