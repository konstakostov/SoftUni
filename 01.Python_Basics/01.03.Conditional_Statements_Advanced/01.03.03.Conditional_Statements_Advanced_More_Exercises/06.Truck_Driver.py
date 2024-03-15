season = input()
km_per_month = float(input())

lev_per_km = 0

if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        lev_per_km = 0.75
    elif 5000 < km_per_month <= 10000:
        lev_per_km = 0.95
    elif 10000 < km_per_month <= 20000:
        lev_per_km = 1.45

elif season == "Summer":
    if km_per_month <= 5000:
        lev_per_km = 0.90
    elif 5000 < km_per_month <= 10000:
        lev_per_km = 1.10
    elif 10000 < km_per_month <= 20000:
        lev_per_km = 1.45

elif season == "Winter":
    if km_per_month <= 5000:
        lev_per_km = 1.05
    elif 5000 < km_per_month <= 10000:
        lev_per_km = 1.25
    elif 10000 < km_per_month <= 20000:
        lev_per_km = 1.45

money_per_season = (km_per_month * lev_per_km) * 4
money_per_season *= 0.90

print(f"{money_per_season:.2f}")
