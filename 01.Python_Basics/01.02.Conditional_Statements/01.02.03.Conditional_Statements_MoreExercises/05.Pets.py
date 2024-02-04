import math

days = int(input())
food_kg = int(input())

food_dog_day = float(input())
food_cat_day = float(input())
food_turtle_day = float(input()) / 1000

food_eaten = (food_dog_day + food_cat_day + food_turtle_day) * days

if food_kg >= food_eaten:
    food_left = food_kg - food_eaten
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    food_needed = food_eaten - food_kg
    print(f"{math.ceil(food_needed)} more kilos of food are needed.")
