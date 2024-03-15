yearly_price = int(input())

sneakers = yearly_price * 0.60
uniform = sneakers * 0.80
ball = uniform / 4
accessories = ball / 5

total = yearly_price + sneakers + uniform + ball + accessories

print(f"{total:.2f}")
