account = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        break
    money = float(command)

    if money < 0:
        print(f"Invalid operation!")
        break

    print(f"Increase: {money:.2f}")
    account += money

print(f"Total: {account:.2f}")
