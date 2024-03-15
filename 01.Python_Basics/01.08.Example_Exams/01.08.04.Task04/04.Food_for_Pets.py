days = int(input())
food_total = float(input())

days_passed = 0

food_dog_total = 0
food_cat_total = 0
food_both_total = 0

biscuit = 0

while days_passed < days:
    food_dog = int(input())
    food_cat = int(input())

    days_passed += 1

    food_dog_total += food_dog
    food_cat_total += food_cat

    if days_passed % 3 == 0:
        biscuit += (food_dog + food_cat) * 0.10

food_both_total = food_dog_total + food_cat_total

print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f"{((food_both_total / food_total) * 100):.2f}% of the food has been eaten.")
print(f"{((food_dog_total / food_both_total) * 100):.2f}% eaten from the dog.")
print(f"{((food_cat_total / food_both_total) * 100):.2f}% eaten from the cat.")

