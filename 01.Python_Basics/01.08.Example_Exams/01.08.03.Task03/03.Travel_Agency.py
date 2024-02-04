city = input()
package = input()
vip_status = input()
days = int(input())

price = 0
discount_vip = 0
discount_days = 0
total_price = 0

if city == "Bansko" or city == "Borovets":
    if package == "withEquipment":
        price = 100
        if vip_status == "yes":
            discount_vip = 0.10
            if days > 7:
                discount_days = price
    elif package == "noEquipment":
        price = 80
        if vip_status == "yes":
            discount_vip = 0.05
            if days > 7:
                discount_days = price
    if days < 1:
        print(f"Days must be positive number!")
        exit()
    total_price = (days * price) - (days * price * discount_vip) - discount_days
    print(f"The price is {total_price:.2f}lv! Have a nice time!")

elif city == "Varna" or city == "Burgas":
    if package == "withBreakfast":
        price = 130
        if vip_status == "yes":
            discount_vip = 0.12
            if days > 7:
                discount_days = price
    elif package == "noBreakfast":
        price = 100
        if vip_status == "yes":
            discount_vip = 0.07
            if days > 7:
                discount_days = price
    if days < 1:
        print(f"Days must be positive number!")
        exit()
    total_price = (days * price) - (days * price * discount_vip) - discount_days
    print(f"The price is {total_price:.2f}lv! Have a nice time!")

else:
    print("Invalid input!")
    if days < 1:
        print(f"Days must be positive number!")

