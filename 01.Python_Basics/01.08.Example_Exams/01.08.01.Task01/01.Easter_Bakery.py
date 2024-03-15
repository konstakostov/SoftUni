flour_per_kg_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_cartons = int(input())
maya_packages = int(input())

sugar_kg_price = flour_per_kg_price * 0.75
egg_cartons_price = flour_per_kg_price * 1.10
maya_packages_price = sugar_kg_price * 0.20

flour_total = flour_kg * flour_per_kg_price
sugar_total = sugar_kg * sugar_kg_price
eggs_total = egg_cartons * egg_cartons_price
maya_total = maya_packages * maya_packages_price

total = flour_total + sugar_total + eggs_total + maya_total

print(f'{total:.2f}')
