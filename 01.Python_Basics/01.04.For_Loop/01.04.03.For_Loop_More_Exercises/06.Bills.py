# Months to Pay Bills
months = int(input())

electricity_bill = 0        # Total Electricity Bill
water_bill = 0              # Total Water Bill
internet_bill = 0           # Total Internet Bill
others_bill = 0             # Total Others Bill

for _ in range(1, months + 1):
    electricity = float(input())

    electricity_bill += electricity
    water_bill += 20
    internet_bill += 15
    others_bill += (electricity + 20 + 15) + (electricity + 20 + 15) * 0.20

# Average Bills per Month
average_bill = (electricity_bill + internet_bill + water_bill + others_bill) / months

# Print Results
print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {others_bill:.2f} lv")
print(f"Average: {average_bill:.2f} lv")
