# Number of Shipments
shipment_count = int(input())

# Pricing Per Ton
van_price = 200
truck_price = 175
train_price = 120

# Weight Information
van_weight = 0      # Van Weight in Tons
truck_weight = 0    # Truck Weight in Tons
train_weight = 0    # Train Weight in Tons

# Total Money Spent per Transport
costs_total = 0

for _ in range(1, shipment_count + 1):
    weight = int(input())

    if weight <= 3:
        costs_total += van_price * weight
        van_weight += weight
    elif weight <= 11:
        costs_total += truck_price * weight
        truck_weight += weight
    else:
        costs_total += train_price * weight
        train_weight += weight

# Total Weight in Tons
weight_total = van_weight + truck_weight + train_weight

# Average Shipping Price
average_price = costs_total / weight_total

# Print Results
print(f"{average_price:.2f}")                       # Average Price
print(f"{((van_weight / weight_total) * 100):.2f}%")        # Van Weight in Percentage
print(f"{((truck_weight / weight_total) * 100):.2f}%")      # Truck Weight in Percentage
print(f"{((train_weight / weight_total) * 100):.2f}%")      # Train Weight in Percentage
