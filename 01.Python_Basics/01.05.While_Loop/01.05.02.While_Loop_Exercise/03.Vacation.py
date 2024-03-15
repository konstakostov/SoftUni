money_needed = float(input())
budget = float(input())

days_counter = 0
spending_counter = 0

while budget < money_needed and spending_counter < 5:
    command = input()
    sum_input = float(input())
    days_counter += 1

    if command == "spend":
        budget = budget - sum_input if budget - sum_input > 0 else 0
        spending_counter += 1

    if command == "save":
        budget += sum_input
        spending_counter = 0

    if budget >= money_needed:
        print(f"You saved the money for {days_counter} days.")
        break

else:
    print(f"You can't save the money.")
    print(f"{days_counter}")
