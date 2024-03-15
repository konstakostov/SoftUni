days = int(input())

liters_total = 0
degrees_sum = 0
degrees_total = 0

for i in range(1, days + 1):
    liters = float(input())
    degrees = float(input())

    liters_total += liters
    degrees_sum += (liters * degrees)
    degrees_total = degrees_sum / liters_total

print(f"Liter: {liters_total:.2f}")
print(f"Degrees: {degrees_total:.2f}")

if degrees_total < 38:
    print(f"Not good, you should baking!")
elif 38 <= degrees_total <= 42:
    print(f"Super!")
elif degrees_total > 42:
    print(f"Dilution with distilled water!")
