import math

green_per_liter = 3.4
red_per_liter = 4.3

x = float(input())
y = float(input())
h = float(input())

front_back = (x * x) + (x * x) - (1.2 * 2)
sides = (x * y) + (x * y) - ((1.5 * 1.5) * 2)

roof_top = 2 * (x * y)
roof_sides = 2 * ((x * h) / 2)

green_needed = (front_back + sides) / green_per_liter
red_needed = (roof_top + roof_sides) / red_per_liter

print(f"{green_needed:.2f}")
print(f"{red_needed:.2f}")
