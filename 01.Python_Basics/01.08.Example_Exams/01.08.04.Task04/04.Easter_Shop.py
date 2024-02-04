starting_eggs = int(input())

eggs = starting_eggs
eggs_sold = 0

while True:
    command = input()

    if command == "Close":
        print(f"Store is closed!")
        print(f"{eggs_sold} eggs sold.")
        break

    if command == "Buy":
        bought_eggs = int(input())
        if bought_eggs > eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {eggs}.")
            break
        else:
            eggs -= bought_eggs
            eggs_sold += bought_eggs

    if command == "Fill":
        filled_eggs = int(input())
        eggs += filled_eggs


