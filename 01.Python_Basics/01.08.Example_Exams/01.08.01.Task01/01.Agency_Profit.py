company = input()
adult_tickets = int(input())
kid_tickets = int(input())
adult_price = float(input())
service_price = float(input())

kid_price = adult_price * 0.30

adults = ((adult_price + service_price) * adult_tickets)
kids = ((kid_price + service_price) * kid_tickets)
tickets_total = adults + kids

profit = tickets_total * 0.20

print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")
