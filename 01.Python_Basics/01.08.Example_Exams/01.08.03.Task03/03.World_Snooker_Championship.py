stage = input()
ticket_type = input()
ticket_quantity = int(input())
picture = input()

ticket_price = 0
total_price = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
        total_price = ticket_quantity * ticket_price
    elif ticket_type == "Premium":
        ticket_price = 105.20
        total_price = ticket_quantity * ticket_price
    elif ticket_type == "VIP":
        ticket_price = 118.90
        total_price = ticket_quantity * ticket_price

elif stage == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
        total_price = ticket_quantity * ticket_price
    elif ticket_type == "Premium":
        ticket_price = 125.22
        total_price = ticket_quantity * ticket_price
    elif ticket_type == "VIP":
        ticket_price = 300.40
        total_price = ticket_quantity * ticket_price

elif stage == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
        total_price = ticket_quantity * ticket_price
    elif ticket_type == "Premium":
        ticket_price = 160.66
        total_price = ticket_quantity * ticket_price
    elif ticket_type == "VIP":
        ticket_price = 400
        total_price = ticket_quantity * ticket_price

if total_price > 4000:
    total_price *= 0.75
    if picture == "Y":
        total_price -= (40 * ticket_quantity)
elif total_price > 2500:
    total_price *= 0.90

if picture == "Y":
    total_price += (40 * ticket_quantity)

print(f"{total_price:.2f}")
