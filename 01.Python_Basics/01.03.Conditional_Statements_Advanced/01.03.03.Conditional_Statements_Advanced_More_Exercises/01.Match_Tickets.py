# Input Data
budget = float(input())
category = input()
people = int(input())

# Ticket Prices
ticket_vip_price = 499.99
ticket_normal_price = 249.99

# Money for Transport
money_transport = 0

if people >= 50:
    money_transport = budget * 0.25

elif 50 >= people >= 25:
    money_transport = budget * 0.40

elif 24 >= people >= 10:
    money_transport = budget * 0.50

elif 9 >= people >= 5:
    money_transport = budget * 0.60

elif 4 >= people >= 1:
    money_transport = budget * 0.75

else:
    print("Error")

# Money Left for Tickets
money_left = budget - money_transport

# Money Needed for Tickets
money_for_tickets = 0

if category == "VIP":
    money_for_tickets = ticket_vip_price * people
else:
    money_for_tickets = ticket_normal_price * people

# Calculations if Budget is Enough
money = 0

if money_left > money_for_tickets:
    money = money_left - money_for_tickets
    print(f"Yes! You have {money:.2f} leva left.")
else:
    money = money_for_tickets - money_left
    print(f"Not enough money! You need {money:.2f} leva.")
