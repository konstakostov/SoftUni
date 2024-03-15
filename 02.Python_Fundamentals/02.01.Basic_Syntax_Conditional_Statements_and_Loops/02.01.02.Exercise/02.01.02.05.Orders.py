orders = int(input())   # Number of Orders

total_price = 0         # Total Price of All Orders

for i in range(orders):
    price_capsule = float(input())  # Price per Capsule
    days = int(input())             # Days
    capsules = int(input())         # Capsules per Day

    if price_capsule < 0.01 or price_capsule > 100.00:
        continue

    if days < 1 or days > 31:
        continue

    if capsules < 1 or capsules > 2000:
        continue

    price = (price_capsule * capsules) * days   # Price of Each Order
    total_price += price

    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")
