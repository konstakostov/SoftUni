bitcoins = int(input())
yuans = float(input())
commision_percent = float(input()) / 100

bitcoins_to_leva = bitcoins * 1168

yuans_to_usd = yuans * 0.15
usd = yuans_to_usd

usd_to_leva = usd * 1.76

leva = bitcoins_to_leva + usd_to_leva

leva_to_eu = leva / 1.95

commision = leva_to_eu * commision_percent

total = leva_to_eu - commision

print(f"{total:.2f}")
