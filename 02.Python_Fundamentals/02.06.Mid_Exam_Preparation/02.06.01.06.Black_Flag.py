days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

plundered = 0

for current_day in range(1, days + 1):
    plundered += daily_plunder

    if current_day % 3 == 0:
        plundered += (daily_plunder / 2)

    if current_day % 5 == 0:
        plundered *= 0.70

plunder_percentage = (plundered / expected_plunder) * 100

if plundered >= expected_plunder:
    print(f"Ahoy! {plundered:.2f} plunder gained.")
else:
    print(f"Collected only {plunder_percentage:.2f}% of the plunder.")
