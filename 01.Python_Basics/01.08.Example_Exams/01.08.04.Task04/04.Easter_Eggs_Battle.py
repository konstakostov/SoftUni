p1_eggs = int(input())
p2_eggs = int(input())

p1_counter = p1_eggs
p2_counter = p2_eggs

while True:
    command = input()

    if command == "End":
        print(f"Player one has {p1_counter} eggs left.")
        print(f"Player two has {p2_counter} eggs left.")
        break

    if command == "one":
        p2_counter -= 1
    elif command == "two":
        p1_counter -= 1

    if p1_counter < 1:
        print(f"Player one is out of eggs. Player two has {p2_counter} eggs left.")
        break

    if p2_counter < 1:
        print(f"Player two is out of eggs. Player one has {p1_counter} eggs left.")
        break
