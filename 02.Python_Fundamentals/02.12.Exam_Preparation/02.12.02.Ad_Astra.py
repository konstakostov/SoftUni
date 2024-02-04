import re

text = input()
pattern = r"(\#|\|)([04.03.01.01.Food-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"

matches = re.findall(pattern, text)

food = []
expiration = []
calories = []
calories_total = 0

for match in matches:
    food.append(match[1])
    expiration.append(match[2])
    calories.append(match[3])
    calories_total += int(match[3])

days = int(calories_total / 2000)

print(f"You have food to last you for: {days} days!")

index = 0

for food_item in food:
    print(f"Item: {food_item}, Best before: {expiration[index]}, Nutrition: {calories[index]}")
    index += 1
