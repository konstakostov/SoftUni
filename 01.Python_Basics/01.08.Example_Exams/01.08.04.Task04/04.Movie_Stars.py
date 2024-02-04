budget = float(input())

money_left = budget
salary = 0

while True:
    command = input()

    if command == "ACTION":
        print(f"We are left with {money_left:.2f} leva.")
        break

    name_length = len(command)

    if name_length > 15:
        salary = money_left * 0.20
        if money_left - salary >= 0:
            money_left -= salary
        else:
            print(f"We need {(salary - money_left):.2f} leva for our actors.")
            raise SystemExit
    else:
        salary = float(input())
        if money_left - salary >= 0:
            money_left -= salary
        else:
            print(f"We need {(salary - money_left):.2f} leva for our actors.")
            raise SystemExit
