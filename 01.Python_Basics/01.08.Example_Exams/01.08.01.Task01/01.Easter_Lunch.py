bread_quantity = int(input())
egg_cartons_quantity = int(input())
cookies_kg = int(input())

bread_price = 3.20
egg_carton_price = 4.35
cookies_kg_price = 5.40
egg_paint_per_egg = 0.15

bread_money = (bread_price * bread_quantity)
egg_money = (egg_carton_price * egg_cartons_quantity)
cookie_money = (cookies_kg_price * cookies_kg)
egg_paint_money = (egg_cartons_quantity * 12 * egg_paint_per_egg)

total_money = bread_money + egg_money + cookie_money + egg_paint_money

print(f"{total_money:.2f}")
