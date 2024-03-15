import math

vineyard_area = int(input())
grapes_per_sq_m = float(input())
wine_liters_needed = int(input())
workers = int(input())

wine_area = vineyard_area * 0.40
grapes_produced_kg = wine_area * grapes_per_sq_m

wine_liters_produced = grapes_produced_kg / 2.5

if wine_liters_produced < wine_liters_needed:
    wine_liters_left = wine_liters_needed - wine_liters_produced
    print(f"It will be a tough winter! "
          f"More {math.floor(wine_liters_left)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine_liters_produced)} liters.")
    wine_liters_left = wine_liters_produced - wine_liters_needed
    wine_per_worker = wine_liters_left / workers
    print(f"{math.ceil(wine_liters_left)} liters left -> "
          f"{math.ceil(wine_per_worker)} liters per person.")
