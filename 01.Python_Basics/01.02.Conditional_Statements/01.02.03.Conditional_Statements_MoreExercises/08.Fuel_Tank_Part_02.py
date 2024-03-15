# Fuel Type, Liters of Fuel and Club Card
fuel_type = input()
fuel_liters = float(input())
club_card = input()

# Fuel Prices
gasoline_price_liter = 2.22
diesel_price_liter = 2.33
gas_price_liter = 0.93

# Club Card Discount
fuel_discount = 0
if club_card == "Yes":
    if fuel_type == "Gasoline":
        gasoline_price_liter = gasoline_price_liter - 0.18
    elif fuel_type == "Diesel":
        diesel_price_liter = diesel_price_liter - 0.12
    elif fuel_type == "Gas":
        gas_price_liter = gas_price_liter - 0.08

# Price to Pay
fuel_price = 0
if fuel_type == "Gasoline":
    fuel_price = fuel_liters * gasoline_price_liter
elif fuel_type == "Diesel":
    fuel_price = fuel_liters * diesel_price_liter
elif fuel_type == "Gas":
    fuel_price = fuel_liters * gas_price_liter

# Liters Discount
liter_discount = 0
if fuel_liters > 25:
    liter_discount = fuel_price * 0.10
elif 20 <= fuel_liters <= 25:
    liter_discount = fuel_price * 0.08
else:
    liter_discount = 0

# Final Price of Fuel
fuel_price_final = fuel_price - liter_discount
print(f"{fuel_price_final:.2f} lv.")
