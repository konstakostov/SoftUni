chicken_menu_price = int(input()) * 10.35
fish_menu_price = int(input()) * 12.40
vegetarian_menu_price = int(input()) * 8.15

meals_price = (chicken_menu_price + fish_menu_price + vegetarian_menu_price)
desert_price = (meals_price) * 0.20

delivery_price = 2.50

total_price = meals_price + desert_price + delivery_price

print(total_price)