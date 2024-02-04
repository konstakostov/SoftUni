food_bought = int(input()) * 1000

days_passed = 0

food_eaten = 0

while True:
    command = input()

    if command == "Adopted":
        if food_bought >= food_eaten:
            print(f"Food is enough! Leftovers: {food_bought - food_eaten} grams.")
        else:
            print(f"Food is not enough. You need {food_eaten - food_bought} grams more.")
        break

    food = int(command)
    food_eaten += food
