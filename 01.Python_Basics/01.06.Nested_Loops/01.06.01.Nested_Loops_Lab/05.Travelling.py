money = 0

while True:
    country = input()
    if country == "End":
        break

    budget = float(input())

    while money < budget:
        deposit = float(input())
        money += deposit

        if money >= budget:
            print(f"Going to {country}!")
            money = 0
            break
