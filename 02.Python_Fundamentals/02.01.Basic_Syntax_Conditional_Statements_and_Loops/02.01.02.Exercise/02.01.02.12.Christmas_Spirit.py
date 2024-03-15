quantity = int(input())     # Quantity of Decorations
days = int(input())         # Days to Christmas

ornament = 2            # Ornament Set Price
ornament_points = 5     # Ornament St Happiness

skirt = 5               # Tree Skirt Price
skirt_points = 3        # Tree Skirt Happiness

garland = 3             # Tree Garland Price
garland_points = 10     # Tree Garland Happiness

light = 15              # Tree Lights Price
light_points = 17       # Tree Lights Happiness

money = 0           # Total Money Spent on Decorations
spirit = 0           # TotalHappiness Level

for current_day in range(1, days + 1):
    if current_day % 11 == 0:          # Every 11th Day
        quantity += 2

    if current_day % 2 == 0:          # Every 2nd Day
        money += quantity * ornament
        spirit += ornament_points

    if current_day % 3 == 0:          # Every 3rd Day
        money += quantity * skirt
        money += quantity * garland
        spirit += skirt_points + garland_points

    if current_day % 5 == 0:          # Every 5th Day
        money += quantity * light
        spirit += light_points
        if current_day % 3 == 0:      # Are Skirts and Garlands Bought on the Same Say Too
            spirit += 30

    if current_day % 10 == 0:          # Every 10th Day
        spirit -= 20
        money += 1 * (skirt + light + garland)

if days % 10 == 0:   # Is Last Day 10th Day Too
    spirit -= 30

print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")
