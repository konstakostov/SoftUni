eggs_size = input()
eggs_color = input()
batch_quantity = int(input())

price_per_batch = 0

if eggs_size == "Large":
    if eggs_color == "Red":
        price_per_batch = 16
    elif eggs_color == "Green":
        price_per_batch = 12
    elif eggs_color == "Yellow":
        price_per_batch = 9

elif eggs_size == "Medium":
    if eggs_color == "Red":
        price_per_batch = 13
    elif eggs_color == "Green":
        price_per_batch = 9
    elif eggs_color == "Yellow":
        price_per_batch = 7

elif eggs_size == "Small":
    if eggs_color == "Red":
        price_per_batch = 9
    elif eggs_color == "Green":
        price_per_batch = 8
    elif eggs_color == "Yellow":
        price_per_batch = 5

price = batch_quantity * price_per_batch
price *= 0.65

print(f"{price:.2f} leva.")
