# Fuel and Left Over Fuel in Tank
fuel_type = input()
fuel_liters = float(input())

if fuel_type == "Diesel":
    fuel_type = "diesel"
    if fuel_liters >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")
elif fuel_type == "Gasoline":
    fuel_type = "gasoline"
    if fuel_liters >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")
elif fuel_type == "Gas":
    fuel_type = "gas"
    if fuel_liters >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")
else:
    fuel_type = "Invalid fuel!"
    print("Invalid fuel!")
