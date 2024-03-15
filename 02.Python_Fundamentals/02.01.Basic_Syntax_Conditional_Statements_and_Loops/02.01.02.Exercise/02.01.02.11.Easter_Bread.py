import math

budget = float(input())             # Total Budget
flour_1_kg = float(input())         # Price 1kg of flour

eggs_1_pack = flour_1_kg * 0.75     # Price 1 Egg Carton
milk_1_l = flour_1_kg * 1.25        # Price 1L Milk

current_eggs = 0        # Eggs in possession

price_per_bread = flour_1_kg + eggs_1_pack + (milk_1_l * 0.25)      # Price per 1 bread

bread_count = math.floor(budget / price_per_bread)                  # Breads Produced

money_left = budget - (price_per_bread * bread_count)               # Money Left

for i in range(1, bread_count + 1):     # Counting Eggs
    if i % 3 != 0:          # +3 Eggs per Loaf
        current_eggs += 3
    else:                   # +3 Eggs per Loaf & (Current Loaf - 2) Eggs are Broken
        current_eggs += 3
        current_eggs -= (i - 2)

print(f"You made {bread_count} loaves of Easter bread! Now you have {current_eggs} eggs and {money_left:.2f}BGN left.")

