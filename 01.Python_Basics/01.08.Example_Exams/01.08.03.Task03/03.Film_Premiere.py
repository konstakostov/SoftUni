movie = input()
package = input()
tickets = int(input())

final_price = 0

if movie == "John Wick":
    if package == "Drink":
        final_price = tickets * 12
    elif package == "Popcorn":
        final_price = tickets * 15
    elif package == "Menu":
        final_price = tickets * 19

elif movie == "Star Wars":
    if package == "Drink":
        final_price = tickets * 18
    elif package == "Popcorn":
        final_price = tickets * 25
    elif package == "Menu":
        final_price = tickets * 30

    if tickets >= 4:
        final_price *= 0.70

elif movie == "Jumanji":
    if package == "Drink":
        final_price = tickets * 9
    elif package == "Popcorn":
        final_price = tickets * 11
    elif package == "Menu":
        final_price = tickets * 14

    if tickets == 2:
        final_price *= 0.85

print(f"Your bill is {final_price:.2f} leva.")
