expected_sum = int(input())

payment = 0
card_sum = 0
cash_sum = 0
total_sum = 0
people_card = 0
people_cash = 0

while total_sum < expected_sum:
    command = input()

    if command == "End":
        print(f"Failed to collect required money for charity.")
        break

    money = int(command)
    payment += 1

    if payment % 2 == 0:
        if money < 10:
            print("Error in transaction!")
        else:
            card_sum += money
            print(f"Product sold!")
            people_card += 1
    else:
        if money > 100:
            print("Error in transaction!")
        else:
            cash_sum += money
            print(f"Product sold!")
            people_cash += 1

    total_sum = cash_sum + card_sum

else:
    average_card = card_sum / people_card
    average_cash = cash_sum / people_cash
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
