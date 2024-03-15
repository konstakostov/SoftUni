drink = input()
sugar = input()
quantity = int(input())

price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = 0.90 * quantity
        price *= 0.65
    elif sugar == "Normal":
        price = 1 * quantity
    elif sugar == "Extra":
        price = 1.20 * quantity

    if quantity >= 5:
        price *= 0.75

elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1 * quantity
        price *= 0.65
    elif sugar == "Normal":
        price = 1.20 * quantity
    elif sugar == "Extra":
        price = 1.60 * quantity

elif drink == "Tea":
    if sugar == "Without":
        price = 0.50 * quantity
        price *= 0.65
    elif sugar == "Normal":
        price = 0.60 * quantity
    elif sugar == "Extra":
        price = 0.70 * quantity

if price > 15:
    price *= 0.80

print(f"You bought {quantity} cups of {drink} for {price:.2f} lv.")
