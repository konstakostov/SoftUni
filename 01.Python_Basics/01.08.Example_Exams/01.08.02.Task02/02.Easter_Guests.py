import math

guests = int(input())
budget = int(input())

bread_price = 4
egg_price = 0.45

eggs_needed = guests * 2
eggs = eggs_needed * egg_price

bread_needed = math.ceil(guests / 3)
bread = bread_needed * bread_price

total_costs = eggs + bread

if total_costs <= budget:
    print(f"Lyubo bought {bread_needed} Easter bread and {eggs_needed} eggs.")
    print(f"He has {(budget - total_costs):.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {(total_costs - budget):.2f} lv. more.")
