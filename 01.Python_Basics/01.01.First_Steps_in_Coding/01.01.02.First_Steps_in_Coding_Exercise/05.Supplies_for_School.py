pens_price = int(input()) * 5.80
markers_price = int(input()) * 7.20
detergent_price = int(input()) * 1.20
discount = int(input()) / 100

products_price = (pens_price + markers_price + detergent_price)
discounted_price = products_price - (products_price * discount)

print(discounted_price)
