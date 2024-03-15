contract = input()
contract_type = input()
mobile_data = input()
months = int(input())

basic_price = 0
data_price = 0
discount = 0

if contract == "one":
    if contract_type == "Small":
        basic_price = 9.98
    elif contract_type == "Middle":
        basic_price = 18.99
    elif contract_type == "Large":
        basic_price = 25.98
    elif contract_type == "ExtraLarge":
        basic_price = 35.99

elif contract == "two":
    if contract_type == "Small":
        basic_price = 8.58
    elif contract_type == "Middle":
        basic_price = 17.09
    elif contract_type == "Large":
        basic_price = 23.59
    elif contract_type == "ExtraLarge":
        basic_price = 31.79

    discount = 0.0375


if mobile_data == "yes":
    if basic_price <= 10:
        data_price = 5.50
    elif basic_price <= 30:
        data_price = 4.35
    elif basic_price > 30:
        data_price = 3.85
elif mobile_data == "no":
    basic_price = basic_price

price_per_month = basic_price + data_price
price_per_contract = (price_per_month * months)

total_price = price_per_contract - price_per_contract * discount

print(f"{total_price:.2f} lv.")
