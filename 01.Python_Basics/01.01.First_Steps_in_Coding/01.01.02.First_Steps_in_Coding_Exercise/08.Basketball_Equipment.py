year_tax = int(input())

sneakers = year_tax - year_tax * 0.40
uniform = sneakers - sneakers * 0.20
ball = uniform / 4
accessories = ball / 5

money_total = year_tax + sneakers + uniform + ball + accessories

print(money_total)
