coupon = int(input())

tickets = 0
others = 0

product_price = 0

while True:
    command = input()

    if command == "End":
        print(tickets)
        print(others)
        break

    command_len = len(command)

    if command_len > 8:
        product_price = ord(command[0]) + ord(command[1])
        if product_price <= coupon and (product_price - coupon) < 0:
            coupon -= product_price
            tickets += 1
        else:
            print(tickets)
            print(others)
            break
    else:
        product_price = ord(command[0])
        if product_price <= coupon and (product_price - coupon) < 0:
            coupon -= product_price
            others += 1
        else:
            print(tickets)
            print(others)
            break
