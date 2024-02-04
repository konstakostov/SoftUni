lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_repairs = 0

for current_loss in range(1, lost_fights + 1):
    if current_loss % 2 == 0:
        expenses += helmet_price

    if current_loss % 3 == 0:
        expenses += sword_price
        if current_loss % 2 == 0:
            expenses += shield_price
            shield_repairs += 1
            if shield_repairs % 2 == 0:
                expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
