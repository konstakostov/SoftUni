import math

bread = int(input())

sugar_package = 950
flour_package = 750

total_sugar = 0
total_flour = 0

max_sugar = 0
max_flour = 0

for i in range(bread):
    sugar_used = int(input())
    total_sugar += sugar_used

    if sugar_used > max_sugar:
        max_sugar = sugar_used

    flour_used = int(input())
    total_flour += flour_used

    if flour_used > max_flour:
        max_flour = flour_used

sugar_packages_needed = math.ceil(total_sugar / sugar_package)
flour_packages_needed = math.ceil(total_flour / flour_package)

print(f"Sugar: {sugar_packages_needed}")
print(f"Flour: {flour_packages_needed}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
